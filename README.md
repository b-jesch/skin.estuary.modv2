# Skin Estuary MOD V2 for KODI 19 Matrix KN Edition #

## Installation Notes ##

It's strongly recommended to install the skin via the "Kodinerds Repo", as this is the only way to guarantee that additional 
required modules (e.g. the PVR Artwork Module) are also installed. Another advantage is that you get automatic updates when 
you install an addon from a repository and not from ZIP.

To install the Kodinerds repository visit the page "https://repo.kodinerds.net", download the repository zip (red button) 
and install it. After that you can install the skin directly from the repository under "Look & Feel", "Skins".

### File name flagging ###
If you want to use special flags like HDR or Dolby Vision or special 3D formats you have to name your files with proper tags, 
preferably before the file extension: 

| 3D with <br> stereoscopic detection |           MVC codec            |          Side by Side          |         Top and Bottom         |            HDR+ Files            |
|:-----------------------------------:|:------------------------------:|:------------------------------:|:------------------------------:|:--------------------------------:|
|     ![](resources/flags/3d.png)     | ![](resources/flags/3dmvc.png) | ![](resources/flags/3dsbs.png) | ![](resources/flags/3dtab.png) | ![](resources/flags/hdrplus.png) | 
|             no tagging              |             3d.mvc             |             3d.sbs             |             3d.tab             |         hdrplus., .12bit.        |


The HDR type recognition by filename for HDR/HLG/Dolby Vision has been removed.

### Animated Artwork ###

As the setup of animated artwork was done by skinhelper addon (which was removed from skin) the skin itself has now taken 
the management of those artwork. Animated artwork has some limitations (see Kodi Wiki: https://kodi.wiki/view/Artwork_types#Animated_Artwork). 
To get this feature work properly, you have to assign a folder within the skin settings, which contains all the artwork. This 
folder **must** be a folder of your local filesystem. Also you can use network share, which  **must** be mounted to a local mountpoint.
Put all your artwork into this folder. Subfolders are allowed (without nesting). 

If you navigate in your movie library, you'll have a new entry now to (re)assign animated Artwork in the context menu. The skin
supports animated poster only.

![](resources/setup_ap.png)
### 4.0.2+nexus ###
- .1
  * Transparency of label background of widgets (Flix view) customizable


- .0 
  * Introducing Flix Landscape View
  

### 4.0.1+nexus ###
- .8
  * fix text adjustment in settings
  * fix incorrect shown clearlogo
  * set "show cast list" as general option in video info
  * introducing ISO flag as source flag
  * fix color overlay in settings.xml


- .7
  * Dutch + Hungarian language updated (many thanks to Klojum and frodo19)
  * some adjustments
  * introducing Font Economica 


- .6
  * Fix cast aspect ratio for 21:9 displays
  * Improved Next Popup for TV-Shows


- .5
  * Bugfix in Video OSD
  * Radio Channel Groups in Home Menu added 
  * settings button from music info removed
  * special settings for artists, extra fanart and discography removed 


- .4
  * Textures update
  * Movie set Info fixed  
  * Category 'PVR & Live TV' in skin settings added
  * changeable list height for channel and program OSD implemented


- .3
  * PVR widgets 'Timers' and 'Saved search results' added
  * smaller Bugfixes


- .2
  * Improved OSD animations (reduce flickering slides)
  * Icon Powerdown/Timer added (active addon "Recording & Power Manager - RPM")
  * OSD PVR flag added if broadcast is available in local file system
  * Background for PVR channel icons added


- .1
  * use sort order of upcoming next episodes from embuary skinhelper addon
  * move decorator into background (epg guide)
  * Fix bug on skin settings is unchangeable if a setting met no language string when language has changed.


- .0
  * improved Channel Guide OSD, Channel OSD
  * missing HDR label on Live-TV (PVR) added
  
### 4.0.0+nexus ###
- .4
  * add missing hdr type flag in video OSD
  * Settings option for displaying current time/total time and time remaining in small video OSD
  * changing fanart, many thanks to samfisher (Team-Kodi)
  * File view in video widgets added (movie, tvshow)
  * moving hdr+ detection priority above hdr detection 
  

- .3
  * add missing color scheme 'chicken.xml'
  

- .2
  * Partially reverted changes on Video/Audio OSD
  * UK:15 rating added


- .1
  * HDR type by filename recognition removed from fullscreeninfo
  * Revert removing of Autohide OSD setting from skin settings (disable setting in Interface/OSD)
  * some Fixes on PVR Radio OSD
  

- .0
  * Player.Cutlist (deprecated) changed to Player.Editlist
  * Cut & Scene Markers added
  * update player processinfo (video scan type progressiv/interlaced)
  * Show/hide button for passwords in keyboard added
  * Default color picker dialog added
  * Introducing DefaultColorSettingsButton
  * Skinhelper Colorpicker from optional addons list removed
  * Autohide OSD from skin settings removed 
  

### 3.4.0+nexus ###
- .12
  * fixed incorrect poster overlays in episode view
  * some icons added
  * Media flag gap closed if video codec is missing
  * Background pattern added
  * fixed missing content path for movie genres

  
### Screenshots ###

![PVR Info](resources/screenshots/screenshot_1.png)![Embuary Info](resources/screenshots/screenshot_2.png)
![Music Visualization](resources/screenshots/screenshot_3.png)![PVR OSD](resources/screenshots/screenshot_4.png)
![TV Widget](resources/screenshots/screenshot_5.png)![Video OSD](resources/screenshots/screenshot_6.png)
![Embuary localized Infos](resources/screenshots/screenshot_7.png)
![New channel View](resources/screenshots/screenshot_8.png)
![Improved OSD](resources/screenshots/screenshot_9.png)
![simplified OSD](resources/screenshots/screenshot_10.png)
![colored flags](resources/screenshots/screenshot_11.png)
![improved nextup info](resources/screenshots/screenshot_12.png)