import xbmc
import sys

jsonrpc = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": {"addonid": "%s", "enabled": %s}, "id": 1}' % (sys.argv[1], sys.argv[2])
xbmc.executeJSONRPC(jsonrpc)
