import os.path
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

if xbmc.getInfoLabel('ListItem.dbid'): dbid = int(xbmc.getInfoLabel('ListItem.dbid'))
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
    if simlist is None: simlist = list()
    for file in filelist.keys():
        match = round(difflib.SequenceMatcher(None, title.lower(), file).quick_ratio(), 2)
        if match < 0.8: continue
        simlist.append({'similarity': match, 'file': filelist[file]})
    return simlist


def main():
    dbtype = xbmc.getInfoLabel('ListItem.dbtype')
    if sys.argv[1] == 'add':

        if not xbmc.getCondVisibility('Skin.String(ap_source)'):
            xbmcgui.Dialog().ok(addon_name, xbmc.getLocalizedString(40399))
            return

        ap_dir = xbmc.getInfoLabel('Skin.String(ap_source)')
        art = dict()
        dirs, files = xbmcvfs.listdir(ap_dir)

        # walk through artwork folder
        for file in files: art.update({','.join(file.split('.')[0:-1]).replace('-', ' ').lower(): file})
        # walk through subfolders
        for dir in dirs:
            s, s_f = xbmcvfs.listdir(os.path.join(ap_dir, dir))
            for file in s_f: art.update({','.join(file.split('.')[0:-1]).replace('-', ' ').lower(): os.path.join(dir, file)})

        xbmc.log('Lookup for %s' % title)
        sim = walkthrough(title, art)
        if not sim:
            # no match, try replacing '-'
            xbmc.log('No animated art matched, remove \'-\' from title \'%s\'' % title)
            sim = walkthrough(title.replace('-', ''), art, sim)
            if not sim:
                # no match, try split title and use first part
                xbmc.log('No animated art matched, split title \'%s\'' % title)
                sim = walkthrough(re.split('[:-]+', title)[0], art, sim)
                if not sim:
                    # no matches, giving up
                    xbmc.log('No animated art matched, giving up')
                    xbmcgui.Dialog().notification(addon_name,
                                                  xbmc.getLocalizedString(40400),
                                                  xbmcgui.NOTIFICATION_WARNING, time=3000)
                    return

        liz = list()
        if len(sim) == 1 and 0.9 <= sim[0].get('similarity', 0) <= 1.0:
            # full match with one hit
            xbmc.log('Full match \'%s\': %s' % (title, sim[0].get('file')))
            listitem = xbmcgui.ListItem(label=sim[0].get('file'),
                                        label2=xbmc.getLocalizedString(40401) + str(sim[0].get('similarity')))
            listitem.setArt({'icon': ap_dir + sim[0].get('file')})
            liz.append(listitem)

        elif len(sim) > 1 or (len(sim) == 1 and sim[0].get('similarity', 0) < 0.9):
            xbmc.log('More then one or unsafe match for title \'%s\'' % title)
            similarity = sorted(sim, key=itemgetter('similarity'), reverse=True)

            # built a list with max 7 items and let user decide
            for item in similarity:
                listitem = xbmcgui.ListItem(label=item.get('file'),
                                            label2=xbmc.getLocalizedString(40401) + str(item.get('similarity')))
                listitem.setArt({'icon': ap_dir + item.get('file')})
                liz.append(listitem)
                if len(liz) > 7: break

        if len(liz) == 1:
            dialog = 0
        else:
            dialog = xbmcgui.Dialog().select(xbmc.getLocalizedString(40394), list=liz, useDetails=True)

        if dialog > -1:
            if dbtype == 'movie':
                rpc = {'method': 'VideoLibrary.SetMovieDetails',
                       'params': {'movieid': dbid, 'art': {'animatedposter': ap_dir + liz[dialog].getLabel()}}}
            elif dbtype == 'tvshow':
                rpc = {'method': 'VideoLibrary.SetTVShowDetails',
                       'params': {'tvshowid': dbid, 'art': {'animatedposter': ap_dir + liz[dialog].getLabel()}}}
            else:
                pass

            if jsonrpc(rpc):
                xbmcgui.Dialog().notification(addon_name,
                                              xbmc.getLocalizedString(40397),
                                              xbmcgui.NOTIFICATION_INFO, time=3000)
        else:
            xbmcgui.Dialog().notification(addon_name, xbmc.getLocalizedString(40400), xbmcgui.NOTIFICATION_WARNING)

    elif sys.argv[1] == 'remove':

        if dbtype == 'movie':
            rpc = {'method': 'VideoLibrary.SetMovieDetails',
                   'params': {'movieid': dbid, 'art': {'animatedposter': None}}}
        elif dbtype == 'tvshow':
            rpc = {'method': 'VideoLibrary.SetTVShowDetails',
                   'params': {'tvshowid': dbid, 'art': {'animatedposter': None}}}
        else:
            xbmc.log('Database type %s not supported' % dbtype)

        if jsonrpc(rpc):
            xbmcgui.Dialog().notification(addon_name, xbmc.getLocalizedString(40396),
                                          xbmcgui.NOTIFICATION_INFO, time=3000)

    else:
        xbmc.log('Script called with unknown parameter: %s' % sys.argv[1])


if __name__ == '__main__':
    main()
