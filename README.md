# Skin Estuary MOD V2 for KODI 19 Matrix KN Edition #

## Installation Notes ##

It's strongly recommended to install the skin via the "Kodinerds Repo", as this is the only way to guarantee that additional 
required modules (e.g. the PVR Artwork Module) are also installed. Another advantage is that you get automatic updates when 
you install an addon from a repository and not from ZIP.

To install the Kodinerds repository visit the page "https://repo.kodinerds.net", download the repository zip (red button) 
and install it. After that you can install the skin directly from the repository under "Look & Feel", "Skins".


### 3.3.0+matrix ###

- .9
  * Missing mono font added (thanks dshoreman)
  * NL language updated (thanks freaktabnl)


- .8
  * Including PVR archive & reminder icons (thanks berkhornet)


- .7
  * Introducing SACD (DSD) audio flag
  * minor improvements


- .6
  * Parental controls removed (use profiles and lock mechanism instead)
  * Fix conditional behaviours on movie/tvshow widgets
  * minor adjustments in various dialogs and views


- .5
  * optional display of channel logo/number in epg grid implemented
  * Changes in picture widget reversed


- .4
  * Costum settings widgets views revised
  * Selection for default action on movie and TV show widgets implemented
  * smaller fixes and enhancements


- .3
  * Autoclose OSD Fix


- .2
  * Code cleanups and small fixes
  * Date Aired Flag added (Movies/TV Shows)


- .1
  * Fix some issues when starting movie trailers from Embuary Info


- .0  
  * Fix in Shutdown Menu: correct distribution logo was not shown
  * Full integration and customization of Embuary Info windows into the skin
  * Improvements on widget info visibility (PVR)
  * Video OSD with adjustable timing on auto close


### 3.2.0+matrix ###
- .8
  * Fix in Shutdown Menu: correct distribution logo was not shown


- .7
  * Fix in List View (Posters was not shown)


- .6
  * Introducing media flags for video color depths like HDR (10bit), HDR+ (12bit) and Dolby Vision        by identifying special parts within filenames (.hdr., .10bit., .hdrplus., .12bit., .dv.)
  * Better implementation of embuary info script in Video Info Window and OSD Info
 

- .5
  * Bugfix: MPAA rating not showing in movie collections
  * Minor bugfixes


- .4
  * Reimplementation of extended info button in video OSD and native call to embuary info script


- .3
  * Introducing MPAA/TV media flags
  * Bug fixed in music visualization (PVR radio)


- .2
  * Improved Addon settings window (thanks @realvito from kodinerds)


- .1
  * Revert some cleanups of includes
  * Texture updates, PVR category improvements part #2
  * Improvements/Bugfix in PVR artwork section


- .0
  * Extended Info (embuary helper) in tvshow and movie info window added
  * Implementation of PVR category widget improved (addon German Telecast Offers)
  * TV show widget next aired episodes implemented
  * conditional visibility of media flags in info windows fixed


### 3.1.0+matrix ###
- .7
  * Some more labels from PVR artwork module in PVR info window added
  * Reimplementation of studio icons in PVR info view (studio icons white required)
  * Some smaller fixes


- .6
  * Fix missing semitransparent backgrounds on some PVR related windows
  * Fix missing action of info button in PVR OSD menu


- .5
  * Busy spinner for PVR artwork in several PVR views added
  * NL language file updated


- .4
  * Selection between fanart/poster view in EPG preview window, busy spinner added
  * bigger preview picture in EPG timeline, timeline items reduced from 8 to 7 lines
  * NL language strings updated
  * Dependency of TV show next aired addon removed from addon list and code


- .3
  * Introduction and Bugfix of normal/extended Power Menu
  * further improvements of PVR artwork functions


- .2
  * Improvements/Bugfixes of PVR artwork functions and info window


- .1
  * show distribution/standard logo in top left corner
  * modification/rearranging of date/time info
  

- .0
  * Implementation and introduction of PVR artwork using the "PVR Artwork Module"
  * show date in top bar (optional)


### 3.0.9+matrix ###
- .0
  * PVR NextUp notification window improved
  * NL language strings updated
  * Rewrite and reimplementation of forced views


### 3.0.8+matrix ###
- .7  
  * Empty space on TV Widget removed if current/next recordings are deselected from widget menu but current and/or next schedules are present
  * Bool condition of visibility for option "Reboot from NAND" in shutdown menu removed
  * Addon-Id info added (Addon Information window)
  * PVR NextUp notification fixed
  

- .6
  * 'Kodi restart' button implemented (Power menu)
  * Shift View for pictures fixed
  

- .5  
  * Background images for power menu, settings menu and search menu reimplemented
  * Rules of background images redefined
  

- .4 
  * "Up Next" double strings notifications fixed, many thanks to hawkeyexp
  * viewswitcher script temporarily deactivated as this cause some issues  


- .3
  * Some language strings updated


- .2
  * Relaunch weather fanart on main screen and selected weather widget
  * Fanart view fixed
  * Several music and concert views fixed
  * Reboot to NAND option in shutdown menu added
  * Some conditions of selecting artworks on music visualization changed (experimental)
  * Minor fixes
  
  
- .1
  * Display of publication year of movies/videos/tv shows in titles is now switchable
  * Dutch translation added, thanks to "theghostnl" from Kodi forum
  

- .0
  * "Add" Button in Default Dialog Select Window reimplemented

  
Note: In my opinion, the adaptation to Kodi 19 is complete. Future changes will only be bug fixes, as far as I am able to do  it.

### 3.0.7+matrix ###
- .16 
  * Bugfix: missing settings window of skin shortcuts addon reimplemented
  * Addon dependencies updated

  
- .15 
  * Portuguese (Brazil) translation added, many thanks to Fábio Vieitas Marques
  * Visibility of border and border color of radio and stream covers now dependend to border settings in skin setup, this allows shaped station logos


- .14
  * Media selection for splash screen removed (causes crashes on startup sometimes)
  * Introducing addon "Sleepy Watchdog" as sleeptimer in shutdown menu
  * Fix of banner and artist clearart positions in music views if they both enabled at same time
  * Clearlogo on main music views removed (when overlapping other items)
  

- .13
  * Rewrite of function "Jump to letter"
  * Option for API key management in settings removed
  * Behavior of widelist animation fixed if online content was requested
  

- .12
  * last added episodes widget fixed if no thumbnail is available
  * Expression for easter theme updated (2.04 - 5.04), missing runtime values in info views added
  
  
- .11
  * Library editor changed against Metadata editor (settings window)
  * Backup/Restore items from settings removed (use Backup Tools instead)
  * Some graphics changed
    

- .10
  * Dependencies of script.artwork.helper removed
  * Rework of animated background (Fanart)

    
- .9
  * Clearlogo from home screen and several main views removed (when overlays other items)
  * Settings window updated (required and optional addons)
  * Artwork Dump instead of Artwork Helper (n.a. for Matrix) implemented


- .8
  * Triple list fixed


- .7        
  * Mosaic view fixed, next unseen episodes reimplemented, start implementation of embuary helper


- .5
  * Dependencies of script.skinhelper completely removed
