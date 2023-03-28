import xbmc
import xbmcvfs
import xbmcgui
import sys

units = [' Bytes', ' kB', ' MB', ' GB', ' TB']

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'toggleAddonStatus':
            '''
                toggles the addon status (enabled/disabled)
                argv[2]: Addon-Id
                argv[3]: Enabled (true/false)
            '''
            jsonrpc = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": {"addonid": "%s", "enabled": %s}, "id": 1}' % (sys.argv[2], sys.argv[3])
            xbmc.executeJSONRPC(jsonrpc)

        elif sys.argv[1] == 'getFileSize':
            '''
                get the file size of a file object
                [argv2]: the complete path and filename of the file object
                returns formatted file size (e.g. '12.05 GB') in property Window(Home).getProperty(size) 
            '''
            unit = 0
            fs = xbmcvfs.File(sys.argv[2]).size()
            fs = 0 if fs < 0 else fs

            while fs > 1024 and unit < 5:
                fs /= 1024
                unit += 1
            xbmcgui.Window(10000).setProperty('size', '%s%s' % ('{0:0.2f}'.format(fs), units[unit]))
            xbmc.log('set Property \'size\' to %s%s' % ('{0:0.2f}'.format(fs), units[unit]), xbmc.LOGINFO)

        else:
            xbmc.log('unknown parameter', xbmc.LOGERROR)

    except IndexError as e:
        xbmc.log(str(e), xbmc.LOGERROR)
