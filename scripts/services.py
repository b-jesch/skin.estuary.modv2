import xbmc
import xbmcgui

pam = False
try:
    from pvrmetadata import PVRMetaData
    pmd = PVRMetaData()
    pam = True
except ImportError:
    xbmc.log('PVR artwork module not available', xbmc.LOGWARNING)

content_labels = list(['50', '55', '53', '54', '505', '500', '502', '503', '504', '506', '507', '508', '509'])
forced_views = list(['movies', 'sets', 'setmovies', 'tvshows', 'seasons', 'episodes', 'albums', 'artists', 'musicvideos'])

content_types = dict({'MyPVRChannels.xml': 'channels', 'MyPVRGuide.xml': 'channels',
                      'MyPVRRecordings.xml': 'recordings', 'MyPVRTimers.xml': 'timers', 'MyPVRSearch.xml': 'search'})

labels = list(['director', 'writer', 'genre', 'country', 'studio', 'premiered', 'mpaa', 'status',
               'rating', 'castandrole'])

# Todo: Rating

win = xbmcgui.Window(10000)


def get_view_id(content_type):

    for label in content_labels:
        if xbmc.getCondVisibility('Skin.HasSetting(%s.%s)' % (content_type, label)): return label
    return False


def clear_properties(prefix):

    for item in pmd.dict_arttypes:
        win.clearProperty('%s.%s' % (prefix, item))
        for i in range(1, 6): win.clearProperty('%s.fanart%s' % (prefix, i))

    for label in labels: win.clearProperty('%s.ListItem.%s' % (prefix, label))

    win.clearProperty('PVR.Artwork.present')
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
            xbmc.log('%s.ListItem.%s: %s' % (prefix, label, lvalue))


def viewswitcher(view_label, trans_title):

    # Check if forced view is enabled and do it's magic
    if not xbmc.getCondVisibility('Skin.HasSetting(ForcedViews.Enabled)'): return view_label

    current_content = xbmc.getInfoLabel('Container.Content')
    if not current_content: return view_label

    path = xbmc.getInfoLabel('Container.FolderName')

    # Check if movie is part of a set
    if current_content == 'movies':
        if str(trans_title) != str(path) and (str(trans_title) + 's' != str(path)):
            current_content = "setmovies"

    # Check if content is part of addon - if yes disable forced view and let addon select view
    if xbmc.getInfoLabel('Container.PluginName') != '': return view_label

    # Check if content type is part if defined views
    if current_content not in forced_views: return view_label

    # Check if content type is forced
    forced_id = get_view_id(current_content)
    if not forced_id: return view_label

    current_label = xbmc.getInfoLabel('Container.Viewmode')
    if current_label != view_label:
        xbmc.log('Forced view for %s defined: %s (but is %s), changing.' % (current_content, view_label,
                                                                            current_label), level=xbmc.LOGDEBUG)

        xbmc.executebuiltin('Container.SetViewMode(%s)' % forced_id)

        # give kodi time to relax :-)
        xbmc.sleep(1000)

    return xbmc.getInfoLabel('Container.Viewmode')


def pvrartwork(current_item):

    if xbmc.getCondVisibility('Container(%s).Scrolling') % xbmcgui.getCurrentWindowId() or \
            win.getProperty('PVR.Artwork.ManualLookup') == 'busy':
        xbmc.sleep(500)
        return current_item

    current_content = None

    # check if PVR related window is active
    for pvr_content in content_types:
        if xbmc.getCondVisibility('Window.IsActive(%s)' % pvr_content):
            current_content = content_types.get(pvr_content, None)
            break

    # if no pvr related window there, clear properties and return
    if not current_content:
        if win.getProperty('PVR.Artwork.present') == 'true': clear_properties('PVR.Artwork')
        return current_item

    title = xbmc.getInfoLabel("ListItem.Title")
    if not title:
        title = xbmc.getInfoLabel("ListItem.Label")

    channel = xbmc.getInfoLabel('ListItem.ChannelName')
    genre = xbmc.getInfoLabel('ListItem.Genre')
    year = xbmc.getInfoLabel('ListItem.Year')

    if current_item != '%s-%s' % (title, channel) or win.getProperty('PVR.Artwork.ManualLookup') == 'changed':
        win.setProperty("PVR.Artwork.ManualLookup", "busy")
        clear_properties('PVR.Artwork')

        details = pmd.get_pvr_artwork(title, channel, genre, year, manual_select=False, ignore_cache=False)
        if details is not None:
            if details['art']: set_properties('PVR.Artwork', details['art'])
            set_labels('PVR.Artwork', details)

    win.clearProperty("PVR.Artwork.ManualLookup")
    return '%s-%s' % (title, channel)


if __name__ == '__main__':

    # properties for viewswitcher
    trans_title = xbmc.getLocalizedString(369)
    view_label = ''

    # properties for pvrartwork
    current_item = ''

    monitor = xbmc.Monitor()
    xbmc.log('Estuary MOD V2 Matrix Service handler started', level=xbmc.LOGINFO)

    while not monitor.abortRequested():
        if monitor.waitForAbort(0.5): break

        # call services

        # view switcher
        if xbmc.getCondVisibility('Skin.HasSetting(ForcedViews.Enabled)'):
            view_label = viewswitcher(view_label, trans_title)

        # PVR artwork
        if pam and xbmc.getCondVisibility('Skin.HasSetting(Skin_enablePvrArtwork)'):
            current_item = pvrartwork(current_item)

    xbmc.log('Estuary MOD V2 Matrix Service handler finished')
