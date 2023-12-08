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
                [argv2]: the complete path and filename of the file object, plugin path is excluded by script
                returns formatted file size (e.g. '12.05 GB') in property Window(Home).getProperty(size) 
            '''
            unit = 0
            fs = 0 if sys.argv[2][0:9] == 'plugin://' else xbmcvfs.File(sys.argv[2]).size()
            fs = 0 if fs < 0 else fs

            while fs > 1024 and unit < 5:
                fs /= 1024
                unit += 1
            xbmcgui.Window(10000).setProperty('size', '%s%s' % ('{0:0.2f}'.format(fs), units[unit]))
            xbmc.log('set Property \'size\' to %s%s' % ('{0:0.2f}'.format(fs), units[unit]), xbmc.LOGINFO)

        elif sys.argv[1] == 'calculate':
            '''
                calculates two parameters, use integer operations
                [argv2]: operator (add, sub, div, mul)
                [argv3]: first operand (float)
                [argv4]: second operand (float)
                [argv5]: property
                returns result (int) in property Window(Home).getProperty(property)
            '''
            try:
                p1 = float(sys.argv[3])
                p2 = float(sys.argv[4])
                operation = sys.argv[2]
                prop = sys.argv[5]

                if operation == 'add':
                    xbmcgui.Window(10000).setProperty(prop, str(int(p1 + p2)))
                elif operation == 'sub':
                    xbmcgui.Window(10000).setProperty(prop, str(int(p1 - p2)))
                elif operation == 'mul':
                    xbmcgui.Window(10000).setProperty(prop, str(int(p1 * p2)))
                elif operation == 'div':
                    xbmcgui.Window(10000).setProperty(prop, str(int(p1 / p2)))
                else:
                    raise ValueError
            except IndexError:
                xbmc.log('not all parameters provided for math operations', xbmc.LOGERROR)
            except ValueError:
                xbmc.log('operand not permitted', xbmc.LOGERROR)
            xbmc.log('Property \'%s\' calculated' % prop, xbmc.LOGINFO)
        else:
            xbmc.log('unknown parameter', xbmc.LOGERROR)

    except IndexError as e:
        xbmc.log(str(e), xbmc.LOGERROR)
