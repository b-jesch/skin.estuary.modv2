import xbmc
import xbmcgui

pam = False
try:
    from pvrmetadata import PVRMetaData
    pmd = PVRMetaData()
    pam = True
except ImportError:
    xbmc.log('PVR artwork module not available', xbmc.LOGWARNING)

# view switcher

content_ids = list(['50', '55', '53', '54', '505', '500', '502', '503', '504', '506', '507', '508', '509'])
forced_views = list(['movies', 'sets', 'setmovies', 'tvshows', 'seasons', 'episodes', 'albums', 'artists', 'musicvideos'])


def get_view_id(content):

    for id in content_ids:
        if xbmc.getCondVisibility('Skin.HasSetting(%s.%s)' % (content, id)): return id
    return False


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


# PVR artwork

content_types = dict({'MyPVRChannels.xml': 'channels', 'MyPVRGuide.xml': 'tvguide', 'DialogPVRInfo.xml': 'info',
                      'MyPVRRecordings.xml': 'recordings', 'MyPVRTimers.xml': 'timers', 'MyPVRSearch.xml': 'search'})

win = xbmcgui.Window(10000)


def pvrartwork(current_item):

    prefix = 'PVR.Artwork'
    current_content = None

    if xbmc.getCondVisibility('Container(%s).Scrolling') % xbmcgui.getCurrentWindowId() or \
            win.getProperty('%s.Lookup' % prefix) == 'busy':
        xbmc.sleep(500)
        xbmc.log('Artwork module is busy or scrolling is active, return')
        return current_item

    # check if Live TV or PVR related window is active

    for pvr_content in content_types:
        if xbmc.getCondVisibility('Window.IsActive(%s)' % pvr_content):
            current_content = content_types.get(pvr_content, None)
            break

    if current_content is None and xbmc.getCondVisibility('VideoPlayer.Content(LiveTV)'): current_content = 'livetv'

    # if no pvr related window there, clear properties and return
    if current_content is None:
        if win.getProperty('%s.present' % prefix) == 'true': pmd.clear_properties(prefix)
        return ''

    label = 'VideoPlayer' if current_content == 'livetv' else 'ListItem'
    title = xbmc.getInfoLabel('%s.Title' % label)
    if label == 'ListItem' and not title: title = xbmc.getInfoLabel('%s.Label' % label)
    channel = xbmc.getInfoLabel('%s.ChannelName' % label)
    genre = xbmc.getInfoLabel('%s.Genre' % label)
    year = xbmc.getInfoLabel('%s.Year' % label)

    if not (title or channel): return ''

    if current_item != '%s-%s' % (title, channel) and win.getProperty('%s.Lookup' % prefix) != 'busy':
        try:
            pmd.get_pvr_artwork(prefix, title, channel, genre, year, manual_select=False, ignore_cache=False)
        except:
            xbmc.log('PVR Artwork module error', xbmcgui.NOTIFICATION_ERROR)

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
