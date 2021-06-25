import xbmc

content_labels = list(['50', '55', '53', '54', '505', '500', '502', '503', '504', '506', '507', '508', '509'])
forced_views = list(['movies', 'sets', 'setmovies', 'tvshows', 'seasons', 'episodes', 'albums', 'artists', 'musicvideos'])


def get_view_id(content_type):
    for label in content_labels:
        if xbmc.getCondVisibility("Skin.HasSetting(%s.%s)" % (content_type, label)):
            xbmc.log("forced view for %s defined: %s" % (content_type, label), level=xbmc.LOGDEBUG)
            return label
    return False


if __name__ == '__main__':
    # init props
    trans_title = xbmc.getLocalizedString(369)
    monitor = xbmc.Monitor()
    xbmc.log("service.skin.viewswitcher - Start service", level=xbmc.LOGINFO)

    while not monitor.abortRequested():
        if monitor.waitForAbort(0.5): break

        # Check if forced view is enabled and do it's magic
        if xbmc.getCondVisibility("Skin.HasSetting(ForcedViews.Enabled)"):
            current_content = xbmc.getInfoLabel("Container.Content")
            if not current_content: continue

            path = xbmc.getInfoLabel("Container.FolderName")

            # Check if movie is part of a set
            if current_content == "movies":
                if str(trans_title) != str(path) and (str(trans_title) + 's' != str(path)):
                    current_content = "setmovies"

            # Check if content is part of addon - if yes disable forced view and let addon select view
            plugin = xbmc.getInfoLabel("Container.PluginName")
            if xbmc.getInfoLabel("Container.PluginName") != "": continue

            # Check if content type is part if defined views
            if current_content in forced_views:

                # Check if content type is forced
                forced_id = get_view_id(current_content)
                if not forced_id: continue

                current_label = xbmc.getInfoLabel('Container.Viewmode')
                if current_label != forced_id: xbmc.executebuiltin("Container.SetViewMode(%s)" % forced_id)

                # give kodi time to relax :-)
                xbmc.sleep(1000)
