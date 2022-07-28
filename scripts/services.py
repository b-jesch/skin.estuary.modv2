import xbmc

# view switcher

content_ids = list(['50', '55', '53', '54', '505', '500', '502', '503', '504', '506', '507', '508', '509', '510'])
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


if __name__ == '__main__':

    # properties for viewswitcher

    TRANS_TITLE = str(xbmc.getLocalizedString(369))
    content = ''
    mode = ''

    monitor = xbmc.Monitor()
    xbmc.log('Estuary MOD V2 Matrix Service handler started', level=xbmc.LOGINFO)

    while not monitor.abortRequested():
        if monitor.waitForAbort(0.5): break

        # call service viewswitcher

        if xbmc.getCondVisibility('Skin.HasSetting(ForcedViews.Enabled)'):
            content, mode = viewswitcher(content, mode)

    xbmc.log('Estuary MOD V2 Matrix Service handler finished')
