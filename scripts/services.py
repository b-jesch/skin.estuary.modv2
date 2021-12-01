import xbmc
import xbmcgui

pam = False
try:
    from pvrmetadata import PVRMetaData
    pmd = PVRMetaData()
    pam = True
except ImportError:
    xbmc.log('PVR artwork module not available', xbmc.LOGWARNING)

content_ids = list(['50', '55', '53', '54', '505', '500', '502', '503', '504', '506', '507', '508', '509'])
forced_views = list(['movies', 'sets', 'setmovies', 'tvshows', 'seasons', 'episodes', 'albums', 'artists', 'musicvideos'])

content_types = dict({'MyPVRChannels.xml': 'channels', 'MyPVRGuide.xml': 'channels', 'DialogPVRInfo.xml': 'info',
                      'MyPVRRecordings.xml': 'recordings', 'MyPVRTimers.xml': 'timers', 'MyPVRSearch.xml': 'search'})

labels = list(['director', 'writer', 'genre', 'country', 'studio', 'studiologo', 'premiered', 'mpaa', 'status',
               'rating', 'castandrole', 'description'])

# Todo: Rating

win = xbmcgui.Window(10000)


def get_view_id(content):

    for id in content_ids:
        if xbmc.getCondVisibility('Skin.HasSetting(%s.%s)' % (content, id)): return id
    return False


def clear_properties(prefix):

    for item in pmd.dict_arttypes:
        win.clearProperty('%s.%s' % (prefix, item))
        for i in range(1, 6): win.clearProperty('%s.fanart%s' % (prefix, i))

    for label in labels: win.clearProperty('%s.ListItem.%s' % (prefix, label))

    win.clearProperty('%s.present' % prefix)
    xbmc.log('Properties of %s cleared' % prefix)


def set_properties(prefix, artwork):

    # set artwork properties
    for item in artwork:
        if item in pmd.dict_arttypes: win.setProperty('%s.%s' % (prefix, item), artwork[item])

    # Lookup for fanarts/posters list
    fanarts = artwork.get('fanarts', False)
    posters = artwork.get('posters', False)
    cf = 0
    if fanarts:
        for cf, fanart in enumerate(fanarts):
            if cf > 5: break
            win.setProperty('%s.fanart%s' % (prefix, str(cf + 1)), fanart)
        cf += 1
    if posters and cf < 2:
        for count, fanart in enumerate(posters):
            if count > 5: break
            win.setProperty('%s.fanart%s' % (prefix, str(cf + count + 1)), fanart)

    win.setProperty('%s.present' % prefix, 'true')


def set_labels(prefix, data):
    # set PVR related list items
    for label in labels:
        if data.get(label, False) and data[label]:
            lvalue = str(data[label])
            if isinstance(data[label], list): lvalue = ', '.join(data[label])
            win.setProperty('%s.ListItem.%s' % (prefix, label), lvalue)


def viewswitcher(content, view_mode):

    current_content = xbmc.getInfoLabel('Container.Content')
    if not current_content: return content, view_mode

    path = xbmc.getInfoLabel('Container.FolderName')

    # Check if movie is part of a set
    if current_content == 'movies':
        if TRANS_TITLE != str(path) and TRANS_TITLE + 's' != str(path):
            current_content = "setmovies"

    # Check if content type is part of forced content
    if current_content not in forced_views: return current_content, view_mode

    # Check if content is part of addon - if yes let addon select view
    if xbmc.getInfoLabel('Container.PluginName') != '': return current_content, view_mode

    # Check if content id is forced
    forced_id = get_view_id(current_content)
    if not forced_id: return current_content, view_mode

    current_mode = xbmc.getInfoLabel('Container.Viewmode')
    if current_content != content or view_mode != current_mode:
        xbmc.executebuiltin('Container.SetViewMode(%s)' % forced_id)

        # give kodi time to relax :-)
        xbmc.sleep(1000)
        view_mode = xbmc.getInfoLabel('Container.Viewmode')
        xbmc.log('changed viewmode for %s from %s to %s' % (current_content, current_mode, view_mode))

    return current_content, view_mode


def pvrartwork(current_item):

    prefix = 'PVR.Artwork'
    current_content = None

    if xbmc.getCondVisibility('Container(%s).Scrolling') % xbmcgui.getCurrentWindowId() or \
            win.getProperty('%s.Lookup' % prefix) == 'busy':
        xbmc.sleep(500)
        return current_item

    # check if PVR related window is active
    for pvr_content in content_types:
        if xbmc.getCondVisibility('Window.IsActive(%s)' % pvr_content):
            current_content = content_types.get(pvr_content, None)
            break

    # if no pvr related window there, clear properties and return
    if not (current_content or xbmc.getCondVisibility('VideoPlayer.Content(LiveTV)')):
        if win.getProperty('PVR.Artwork.present') == 'true': clear_properties(prefix)
        return current_item

    if xbmc.getCondVisibility('VideoPlayer.Content(LiveTV)') and not current_content:
        title = xbmc.getInfoLabel('VideoPlayer.Title')
        channel = xbmc.getInfoLabel('VideoPlayer.ChannelName')
        genre = xbmc.getInfoLabel('VideoPlayer.Genre')
        year = xbmc.getInfoLabel('VideoPlayer.Year')
    else:
        title = xbmc.getInfoLabel("ListItem.Title")
        if not title: title = xbmc.getInfoLabel("ListItem.Label")
        channel = xbmc.getInfoLabel('ListItem.ChannelName')
        genre = xbmc.getInfoLabel('ListItem.Genre')
        year = xbmc.getInfoLabel('ListItem.Year')

    if not (title or channel): return current_item

    if (current_item != '%s-%s' % (title, channel) and win.getProperty('%s.Lookup' % prefix) != 'busy') or win.getProperty('%s.Lookup' % prefix) == 'changed':
        win.setProperty("%s.Lookup" % prefix, "busy")
        details = pmd.get_pvr_artwork(title, channel, genre, year, manual_select=False, ignore_cache=False)
        # win.setProperty("%s.Lookup" % prefix, "changed")
        clear_properties(prefix)
        if details:
            if details.get('art', False): set_properties(prefix, details['art'])
            set_labels(prefix, details)

        win.clearProperty("%s.Lookup" % prefix)

    return '%s-%s' % (title, channel)


if __name__ == '__main__':

    # properties for viewswitcher
    TRANS_TITLE = str(xbmc.getLocalizedString(369))
    content = ''
    mode = ''

    # properties for pvrartwork
    current_item = ''

    monitor = xbmc.Monitor()
    xbmc.log('Estuary MOD V2 Matrix Service handler started', level=xbmc.LOGINFO)

    while not monitor.abortRequested():
        if monitor.waitForAbort(0.5): break

        # call services

        # view switcher
        if xbmc.getCondVisibility('Skin.HasSetting(ForcedViews.Enabled)'):
            content, mode = viewswitcher(content, mode)

        # PVR artwork
        if pam and xbmc.getCondVisibility('Skin.HasSetting(Skin_enablePvrArtwork)'):
            current_item = pvrartwork(current_item)

    xbmc.log('Estuary MOD V2 Matrix Service handler finished')
