"""
    Contextmenu for Pvr art applied from script.skinhelper.service
    thanks to Marcel van der Veldt and contributors
"""

import xbmc
import xbmcgui
import sys

try:
    from pvrmetadata import PVRMetaData
except ImportError:
    sys.exit()

if __name__ == '__main__':

    title = xbmc.getInfoLabel("ListItem.Title")
    if not title:
        title = xbmc.getInfoLabel("ListItem.Label")

    channel = xbmc.getInfoLabel("ListItem.ChannelName")
    genre = xbmc.getInfoLabel("ListItem.Genre")
    year = xbmc.getInfoLabel("ListItem.Year")

    pmd = PVRMetaData()
    pmd.pvr_artwork_options('PVR.Artwork', title, channel, genre, year)
