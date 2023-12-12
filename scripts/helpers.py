import xbmc
import xbmcvfs
import xbmcgui
import sys
import json

units = [' Bytes', ' kB', ' MB', ' GB', ' TB']


def jsonrpc(query):
    querystring = {"jsonrpc": "2.0", "id": 1}
    querystring.update(query)
    try:
        response = json.loads(xbmc.executeJSONRPC(json.dumps(querystring)))
        if 'result' in response: return response['result']
    except TypeError as e:
        xbmc.log('Error executing JSON RPC: {}'.format(e.args), xbmc.LOGERROR)
    return None


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'toggleAddonStatus':
            '''
                toggles the addon status (enabled/disabled)
                argv[2]: Addon-Id
                argv[3]: Enabled (true/false)
            '''
            result = jsonrpc({"method": "Addons.SetAddonEnabled",
                              "params": {"addonid": sys.argv[2], "enabled": bool(sys.argv[3])}})

        elif sys.argv[1] == "getKodiSetting":
            '''
                get Kodi setting
                [argv2]: setting e.g. "lookandfeel.skin" in guisettings.xml 
            '''
            result = jsonrpc({"method": "Settings.GetSettingValue", "params": {"setting": sys.argv[2]}})
            xbmcgui.Window(10000).setProperty(sys.argv[2], str(result['value']))
            xbmc.log('set Property \'%s\' to %s' % (sys.argv[2], str(result['value'])), xbmc.LOGINFO)

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
                operator = sys.argv[2]
                prop = sys.argv[5]

                if operator == 'add': xbmcgui.Window(10000).setProperty(prop, str(int(p1 + p2)))
                elif operator == 'sub': xbmcgui.Window(10000).setProperty(prop, str(int(p1 - p2)))
                elif operator == 'mul': xbmcgui.Window(10000).setProperty(prop, str(int(p1 * p2)))
                elif operator == 'div': xbmcgui.Window(10000).setProperty(prop, str(int(p1 / p2)))
                else: raise ValueError('Operator unknown')

                xbmc.log('Property \'%s\' calculated' % prop, xbmc.LOGINFO)

            except IndexError:
                xbmc.log('not all parameters provided for math operations', xbmc.LOGERROR)
            except ValueError as e:
                xbmc.log('Value error: %s' % str(e), xbmc.LOGERROR)
        else:
            xbmc.log('unknown parameter', xbmc.LOGERROR)

    except IndexError as e:
        xbmc.log(str(e), xbmc.LOGERROR)
