import time
import xbmc
import xbmcgui
import xbmcaddon

if __name__ == '__main__':
    # init props
    trans_title = xbmc.getLocalizedString(369)
    monitor = xbmc.Monitor()
    xbmc.log("service.skin.viewswitcher - Start service", level=xbmc.LOGINFO)
    while not monitor.abortRequested():
        # Sleep/wait for abort for 0.5 seconds
        if monitor.waitForAbort(0.5):
            # Abort was requested while waiting. We should exit
            break
        # Check if forced view is enabled and do it's magic if yes
        if not xbmc.getCondVisibility("!Skin.HasSetting(ForcedViews.Enabled)") == 1:
            current_content = xbmc.getInfoLabel("Container.Content")
            path = xbmc.getInfoLabel("Container.FolderName")
            # Check if movie is part of a set
            if current_content == "movies":
                setname = xbmc.getInfoLabel("ListItem.Set")
                if (str(trans_title) != str(path) and (str(trans_title)+'s' != str(path))):
                    #dlg = xbmcgui.Dialog()
                    #dlg.notification("Compare",str(path) + " - " + str(trans_title),xbmcgui.NOTIFICATION_INFO,1000)
                    current_content = "setmovies"
            # Check if content is part of addon - if yes disable forced view and let addon select view
            plugin = xbmc.getInfoLabel("Container.PluginName")
            if plugin != "":
                current_content = ""
            # Check if conent type is part if defined views
            if current_content in "movies|sets|setmovies|tvshows|seasons|episodes|albums|artists|songs|musicvideos|pictures|videos|files" and not current_content == "":
                # Get labels and force ascii for compare to make rockstable for languages with special chars
                current_view_label = xbmc.getInfoLabel("Container.Viewmode").decode("utf-8").encode("ascii","ignore")
                dest_view_id = xbmc.getInfoLabel("Skin.String(SkinHelper.ForcedViews.%s)" % current_content).decode("utf-8").encode("ascii","ignore")
                dest_view_label = xbmc.getInfoLabel("Skin.String(SkinHelper.ForcedViews.%s.label)" % current_content).decode("utf-8").encode("ascii","ignore")
                # Set current view to forced one
                if (dest_view_id != ""):
                    if current_view_label != dest_view_label:
                        #dlg = xbmcgui.Dialog()
                        #dlg.notification("Set",str(path) + " - " + current_content,xbmcgui.NOTIFICATION_INFO,1000)
                        xbmc.executebuiltin("Container.SetViewMode(%s)" % dest_view_id)
                        xbmc.log("service.skin.viewswitcher - Cur label: " + current_view_label, level=xbmc.LOGINFO)
                        xbmc.log("service.skin.viewswitcher - Cur content: " + str(current_content), level=xbmc.LOGINFO)
                        xbmc.log("service.skin.viewswitcher - Switching to:", level=xbmc.LOGINFO)
                        xbmc.log("service.skin.viewswitcher - Dest label: " + str(dest_view_label), level=xbmc.LOGINFO)
                        xbmc.log("service.skin.viewswitcher - Dest id: " + str(dest_view_id), level=xbmc.LOGINFO)
                        # give kodi time to relax :-)
                        time.sleep(1)