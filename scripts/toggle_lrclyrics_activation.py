import xbmc
import sys

jsonrpc = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": {"addonid": "script.cu.lrclyrics", "enabled": %s}, "id": 1}' % sys.argv[1]
xbmc.executeJSONRPC(jsonrpc)
