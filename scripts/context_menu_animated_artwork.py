import sys
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import json
import difflib
import re
from operator import itemgetter

addon_name = xbmcaddon.Addon(xbmc.getInfoLabel('Window(home).Property(CurrentSkin)')).getAddonInfo('name')
dbid = int(xbmc.getInfoLabel('ListItem.DBid'))
title = xbmc.getInfoLabel('ListItem.title')


def jsonrpc(query):
    querystring = {"jsonrpc": "2.0", "id": 1}
    querystring.update(query)
    try:
        response = json.loads(xbmc.executeJSONRPC(json.dumps(querystring)))
        if 'result' in response:
            return response['result']
    except TypeError as e:
        xbmc.log('Error executing JSON RPC: %s' % e, xbmc.LOGERROR)
    return False


def walkthrough(title, filelist, simlist=None):
    if simlist is None:
        simlist = list()
    for file in filelist:
        match = round(difflib.SequenceMatcher(None, title, '.'.join(file.split('.')[0:-1]).replace('-', ' ')).quick_ratio(), 2)
        if match < 0.8: continue
        simlist.append({'similarity': match, 'file': file})
    return simlist


if sys.argv[1] == 'add':

    if not xbmc.getCondVisibility('Skin.String(ap_source)'):
        xbmcgui.Dialog().ok(addon_name, xbmc.getLocalizedString(40399))
        exit(0)

    ap_dir = xbmc.getInfoLabel('Skin.String(ap_source)')
    dirs, files = xbmcvfs.listdir(ap_dir)
    xbmc.log('Lookup for %s' % title)
    sim = walkthrough(title, files)
    if not sim:
        # no match, try replacing '-'
        xbmc.log('No animated art matched, remove \'-\' from title \'%s\'' % title)
        sim = walkthrough(title.replace('-', ''), files, sim)
        if not sim:
            # no match, try split title and use first part
            xbmc.log('No animated art matched, split title \'%s\'' % title)
            sim = walkthrough(re.split('[:-]+', title)[0], files, sim)
            if not sim:
                # no matches, giving up
                xbmc.log('No animated art matched, giving up')
                xbmcgui.Dialog().notification(addon_name,
                                              xbmc.getLocalizedString(40400),
                                              xbmcgui.NOTIFICATION_WARNING, time=3000)

    if len(sim) == 1 and 0.9 <= sim[0].get('similarity', 0) <= 1.0:
        # full match with one hit
        xbmc.log('Full match for title \'%s\': %s' % (title, sim[0].get('file')))
        rpc = {'method': 'VideoLibrary.SetMovieDetails',
               'params': {'movieid': dbid, 'art': {'animatedposter': ap_dir + sim[0].get('file')}}}
        if jsonrpc(rpc):
            xbmcgui.Dialog().notification(addon_name,
                                          xbmc.getLocalizedString(40397),
                                          xbmcgui.NOTIFICATION_INFO, time=3000)

    elif len(sim) > 1 or (len(sim) == 1 and sim[0].get('similarity', 0) < 0.9):
        xbmc.log('More then one or unsafe match for title \'%s\'' % title)
        similarity = sorted(sim, key=itemgetter('similarity'), reverse=True)

        # built a list with max 7 items and let user decide
        liz = list()
        for item in similarity:
            listitem = xbmcgui.ListItem(label=item.get('file'),
                                        label2=xbmc.getLocalizedString(40401) + str(item.get('similarity')))
            listitem.setArt({'icon': ap_dir + item.get('file')})
            liz.append(listitem)
            if len(liz) > 7: break

        dialog = xbmcgui.Dialog().select(xbmc.getLocalizedString(40394), list=liz, useDetails=True)
        if dialog > -1:
            rpc = {'method': 'VideoLibrary.SetMovieDetails',
                   'params': {'movieid': dbid, 'art': {'animatedposter': ap_dir + liz[dialog].getLabel()}}}
            if jsonrpc(rpc):
                xbmcgui.Dialog().notification(addon_name,
                                              xbmc.getLocalizedString(40397),
                                              xbmcgui.NOTIFICATION_INFO, time=3000)
        else:
            xbmcgui.Dialog().notification(addon_name, xbmc.getLocalizedString(40400), xbmcgui.NOTIFICATION_WARNING)

elif sys.argv[1] == 'remove':

    rpc = {'method': 'VideoLibrary.SetMovieDetails', 'params': {'movieid': dbid, 'art': {'animatedposter': None}}}
    if jsonrpc(rpc):
        xbmcgui.Dialog().notification(addon_name, xbmc.getLocalizedString(40396),
                                      xbmcgui.NOTIFICATION_INFO, time=3000)

else:
    xbmc.log('Script called with unknown parameter: %s' % sys.argv[1])
