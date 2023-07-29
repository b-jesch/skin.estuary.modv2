# Skin Estuary MOD V2 for KODI 20 Nexus KN Edition #

**Some screenshots You'll find at the end of this Readme**

## Installation Notes ##

It's strongly recommended to install the skin via the "Kodinerds Repo", as this is the only way to guarantee that additional 
required modules (e.g. the PVR Artwork Module) are also installed. Another advantage is that you get automatic updates when 
you install an addon from a repository and not from ZIP.

To install the Kodinerds repository visit the page "https://repo.kodinerds.net", download the repository zip (red button) 
and install it. After that you can install the skin directly from the repository under "Look & Feel", "Skins".

## Installation from Git ##

If you want to install the latest version from Git (before this has added to Kodinerds Repo) just download the Addon from here 
https://github.com/b-jesch/skin.estuary.modv2/tree/Nexus (green Code button), **rename the root folder inside the ZIP** 
from ```skin.estuary.modv2-Nexus``` to ```skin.estuary.modv2``` and choose 'install from zip' inside Kodi. **Renaming 
the root folder inside the ZIP needs unpacking/packing the zip in some cases.**

### File name flagging ###
If you want to use special flags like HDR or Dolby Vision or special 3D formats you have to name your files with proper tags, 
preferably before the file extension: 

| 3D with <br> stereoscopic detection |           MVC codec            |          Side by Side          |         Top and Bottom         |            HDR+ Files            |
|:-----------------------------------:|:------------------------------:|:------------------------------:|:------------------------------:|:--------------------------------:|
|     ![](resources/flags/3d.png)     | ![](resources/flags/3dmvc.png) | ![](resources/flags/3dsbs.png) | ![](resources/flags/3dtab.png) | ![](resources/flags/hdrplus.png) | 
|             no tagging              |             3d.mvc             |             3d.sbs             |             3d.tab             |         hdrplus., .12bit.        |


The HDR type recognition by filename for HDR/HLG/Dolby Vision has been removed.

### Animated Artwork ###

As the setup of animated artwork was done by skinhelper addon (which was removed from skin) the addon "Animated Artwork Module" has now taken 
the management of those artwork. Animated artwork has some limitations (see Kodi Wiki: https://kodi.wiki/view/Artwork_types#Animated_Artwork). 
To get this feature work properly, you have to assign a folder within the addon settings, which contains all the artwork. This 
folder **must** be a folder of your local filesystem. You can use network share, but this **must** be mounted to a local mountpoint.
Put all your artwork into this folder. Subfolders are allowed (without nesting).  

If you navigate in your movie library, you'll have a new entry now to (re)assign animated Artwork in the context menu. The skin
supports animated poster only.

![](resources/setup_ap.png)

### 4.1.2+nexus ###
- .5
  * add support for PreShow Experience


- .4
  * Update Player Process Info (again thanks to frodo19)
  * Move Chapter/Cutmarkers to seekbar
  * improved battery level graphics
  * Option "Hide notifications while Playback" removed
  * Fix missing video genre fanart even if fanart pack is installed
  * add runtime (duration) to PVR search results, minor improvements
  * add a resume button to video info (DialogVideoInfo.xml)


- .3
  * reverted image type back to multiimage for weather widget pt.2
  * Introducing battery level display/symbol on Top Bar in Home screen for mobile devices
  

- .2
  * fix wrong plot position on PVR Icon Wall when "show channel groups" on EPG grid is selected
  * adjustments on mosaic views
  * add animation to PVR NextUp
  * reverted image type back to multiimage for weather widget


- .1
  * minor adjustments
  * fix player plot display on info if small Video OSD is selected


- .0
  * introducing auto stop timer (stop player after an amount of time when player is paused, configurable)
  * fix condition (issue #123)
  * add season label to flix view items (tv show season view)
  * convert all home images to baseline JPEG format specification
  * fix pause bug on PVR related OSD Info, remove pause on info for LiveTV/Recordings


### 4.1.1+nexus ###
- .14
  * improving extended info views (Embuary)
  * smaller fixes and improvements
  * add season/episode label to flix view (tv show episode view)


- .13
  * fix missing font definitions
  * fix mistakenly displayed chaptercount in music player
  * smaller fixes


- .12
  * add support for Android Super Partition (issue #122)
  * add title info to Mosaic view


- .11
  * fix wrong startup behaviour (issue #120) if startup window and startup action is set (Interface, Startup)
  * add Embuary Helper to skin dependencies 
  * avoid showing PVR Nextup if EPG isn't available
  * fix overlapping labels in video OSD
  * more compact main menu

- .10
  * fix "switch to last channel" in video OSD
  * some icons added
  * enable flix view for tvshow seasons
  * music OSD settings menu optimized
  * introduce Radio RDS info screen
  * set opacity of music fanart similar to background opacity

 
- .9
  * fix display of PVR status icon (Record, Timer, Scheduler, Premiered, ...) on EPG grid
  * fix addon activation of lrclyrics in Music OSD settings
  * add a "Black Screen" button to music OSD: show a black screen while playing music
  * fix live TV video OSD flickering on channel/window changes
  * smaller improvements in PVR section


- .8
  * quick fix of helper script (cause kodi to crash when file path is a plugin call)


- .7
  * calculate/display size of a file object by helper script
  * remove horizontal EPG grid layout
  * add EPG navigation entry to side blade (PVR EPG only)
  * add progress indicator to recording widget (PVR) 
  * smaller modifications on several views
  
- .6
  * fix overlapping genre/plotline in Flix View
  * extend option play/info for home widgets to music video widgets
  * add dependencies for estuary helper/info to widget selection menu entries (tvshows)
  * smaller improvements and updates on several files
  * introducing 'Arial Unicode MS' as a new font style supporting more languages (mainly asian region)
  

- .5
  * fix missing thumb/icon on extended list view for some plugins
  * disable/enable addon 'CU LrcLyrics' (song text) via script
  * improved Music OSD settings
  * fix missing artists pictures on actors category for musicvideos
  * add artist pictures to video info dialog


- .4
  * improved music OSD
  * changed cond visibility of metadata editor (video/music info)  
  * improved Flix View for movie sets (bigger background for sets with < 5 items)
  * add option to switch between poster/fanart in Mosaic views (video plugins)
  * conditions for displaying background images optimized/simplified 
  * fix slightly wrong aspect ratio for posters in views/info/OSD
  * fix now unsupported background opacity (Nexus 20.1) by replacing multiimage controls with image controls


- .3
  * fix wrong behaviour of seekbar in music OSD
  

- .2
  * remove doubled episode title on PVR timer widget
  * remove overlapping between title and plot in list view
  * smaller fixes


- .1
  * improving + removing fanart/landscape from seek bar
  * fix display of long titles/filenames on list view (issue #114)


- .0
  * coloured flags updated (Thanks to Frodo19)
  * Introducing volume amplification button (DSP) to video OSD
  * add Audio DSP addon to required addons list
  * Home images changed
  * Improvements on Flix view (just one more...)
  * add transparency option to seekbar background
  * add missing list view to tvshow episodes
  * fix TV-14 rating (wrongly shown as MPAA-14)
  * fix bug on seasonal themes

### 4.1.0+nexus ###
- .3
  * Fix missing HDR flag
  * Move themes back from Textures.xbt to file system
  * Improved smart play list (last seen movies)
  * Add last played flag to flix view


- .2
  * Add option for customizing own splash background
  * Add title list to album view pt.1
  * Add additional info to album view pt.2
  * Add option "prefer album fanart over artist fanart" in music visualisation
  * Fix MPAA rating "Rated M"
  * Add background opacity values to splash background
  * Update NL language


- .1
  * Introducing Skin Timers as replacement for splash screen timers
  * extend power menu property "reboot from eMMC/NAND"
  * Applying special seasonal themes to splash screen, update textures
  * fixed wrong behaviour on startup/logout when profiles are used (Issue #65)
  

- .0
  * Introducing favourites browser
  * Bugfix Listview
  * Fix doubled label of 'in progress tv shows'
  * Distribution logos in context menu added
  * update screen calibration
  * avoid flickering in settings window when video sources are shown and icon view is set


### 4.0.2+nexus ###
- .18
  * hungarian language updated
  * flix view improvements (background for sets, movie sets poster)
  * run condition of pvr artwork module for pvr nextup fixed
 

- .17
  * fix race condition in PVR next up that kodi causes to crash (issue #104)
  * add season/episode labels to pvr widget

 
- .16
  * add missing preview for musicvideos on view selection window (1131) 
  * add selection for default action on PVR widgets
  * prepare dates for special themes 2023
  * add PVR recording expiration date info
 

- .15
  * another behaviour of video info window fixed when fullscreen info is set and PVR is playing live TV


- .14
  * fixes on video info window


- .13
  * smaller fixes and textures updates
  * fix cond visibility for label 'Jump to letter'
  * fix incorrectly resolved condition while showing seekbar, when 'use small OSD' was not set
  * add Flix view to music videos
  * set info dialog metadata to invisible if trailer is playing
  * set power/settings/search/fullscreen menu buttons to vertical orientation if smaller main menu is set
  * add missing video info window if fullscreen video info is not set


- .12
  * Textures.xbt updated (av1 flag added)
  * coloured flags updated (thanks to frodo19) 
  * fix missing channel logo in Guide and Video OSD
  * link subtitles/audio OSD buttons to subtitles/audio settings for more flexibility (simplified OSD)
  * new more uniformed resolution flags (thanks again to frodo19)
  * modify cond visibility for 'Jump to Letter'
  * fix playing Live TV while (fullscreen) video info becomes active  
  * avoid stuttering if skin setting 'Play video in background' isn't set
  * modifications on 'telecast offers' info window 


- .11
  * update playlist view
  * extend setting 'Show Fanart' to all video views (affected earlier only to home widgets)
  * fix missing channel logo in PVR info views
  * fix wrong used mediaflag of endtime and endtime resume with appendix AM/PM
  * fix wrong position of channel group infolabel in PVR channel OSD

  
- .10
  * Widget header for TV timer in Home menu modified
  * include 'Jump to Letter' in Flix view
  * make 'Play Trailer' in context menu customizable
  * show next timer and available disk space in tv timers window
  * remove skin setting 'use poster view for music videos'
  * add title labels to poster view widgets


- .9
  * add "play trailer" to contextmenu
  * fix unmatched parentheses in Home.xml
  * fix doubled background in flex view
  * fix position and size of context menu in flix view
  * last seen movie template added (reset/modify main menu required)
  * seek bar components modified


- .8
  * Hungarian language update
  * Font fix of Economica font family
  * Revert mistakenly changes on DialogSeekBar
  * PVR OSD: Introducing last five channel switch (optional)
  * smaller fixes
  * add missing studio logos on several widget layouts


- .7
  * make simplified seek bar optional (skin settings)
  * improved skin settings
  * Bugfixes


- .6
  * Refinements on PVR EPG view
  * show seek bar only (without OSD parts) while seeking
  * Replace GUIBool Player.DisplayAfterSeek with Player.HasPerformedSeek()
  * close power menu on Poweroff (RPM) before rpm addon starts
  * Introducing audio samplerate flag for lossless audio codecs


- .5
  * improved PVR image preview
  * improved EPG timeline (8 rows)
  * improved PVR event icons
  * improved skin settings for textual selections (independend from language settings)


- .4
  * update translations for all languages (thanks for the bunch of work to C4Wiz)


- .3
  * Fix wrong viewtype labels
  * some more improvements on tvshow widgets
  * Improvements on Player OSD:
    * exclude actors list from autoclose
    * custom info on small OSD
    * global record flag (independent of actual channel recording)


- .2
  * Fix unchanged label IDs in shortcuts
  * Fix wrong *elec labels (thanks C4Wiz)
  * Add missing search button on video/audio side blade
  * Add missing previews in view selection window
  * Flix view improvements
  * skin script for animated artwork removed (obsolete, use animated artwork addon instead)
  * improved PVR status display in channel views
  * improved tvshow widgets (home menu)


- .1
  * Transparency of label background of widgets (Flix view) customizable
  * semitransparent Background for plot in video info added
  * Overlay texture in Flix view changed 
  * fix wrong behaviour on info button if a movie is paused
  * reorder language ids above 40xxx to 31xxx and usages to fit within the recommended range for skins


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
![improved PVR event icons](resources/screenshots/screenshot_13.png)
![various color...](resources/screenshots/screenshot_14.png)
![...and font schemes](resources/screenshots/screenshot_15.png)
![Audio DSP](resources/screenshots/screenshot_16.png)
![Flix Landscape](resources/screenshots/screenshot_17.png)
