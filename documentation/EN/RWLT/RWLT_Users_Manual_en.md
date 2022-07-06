[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: User’s manual**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - Underwater acoustic tracking system <br/> User's manual |

# RWLT <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Purpose](#11-purpose)
  - [1.2. Peculiarities](#12-peculiarities)
  - [1.3. System Composition](#13-system-composition)
- [2. Working with the RWLT system](#2-working-with-the-rwlt-system)
  - [2.0. Before work](#20-before-work)
  - [2.1. Preparing for work and checking equipment](#21-preparing-for-work-and-checking-equipment)
    - [2.1.1. Choosing a location for the operator's place](#211-choosing-a-location-for-the-operators-place)
    - [2.1.2. Checking the set of buoys](#212-checking-the-set-of-buoys)
    - [2.1.3. Location of buoys on the surface of the water](#213-location-of-buoys-on-the-surface-of-the-water)
    - [2.1.4. Preparation of underwater equipment](#214-preparation-of-underwater-equipment)
  - [2.2. Working with the system](#22-working-with-the-system)
    - [2.2.1. Configuration for working with divers](#221-configuration-for-working-with-divers)
      - [2.2.1.1. Application interface and functions](#2211-application-interface-and-functions)
      - [2.2.1.2. Interaction with the system](#2212-interaction-with-the-system)
    - [2.2.2. Configuration for working with pinger beacon]()
  - [2.3. Upon completion of work](#23-upon-completion-of-work)
- [3. Liability and Disclaimer](#3-liability-and-disclaimer)
  - [3.1. Terms of replacement and free warranty service](#31-terms-of-replacement-and-free-warranty-service)
  - [3.2. Manufacturer disclaimer](#32-manufacturer-disclaimer)

<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1. Purpose

Underwater Acoustic Tracking System **RWLT** is designed for:

- determining the geographic location and depth of an underwater object (**AUV**, **ROV**, **ROU**, divers, etc.) equipped with an autonomous pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md). In this system configuration, it is possible to track the position of **one** object equipped with an autonomous pinger beacon.
- determining the geographic location of divers equipped with wireless voice diving transceivers [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html). In this system configuration, it is possible to track the position of 255 divers in one water area.

### 1.2. Peculiarities

The **RWLT** system uses state-of-the-art digital broadband noise-immune hydroacoustic communication, and the applied signal is specially designed for difficult hydrological conditions, including those found in shallow waters.

The **RWLT** System is the **Easiest to Use** yet Accurate Subsea Tracking Solution. The system **does not require any calibrations** and integration: it is enough to place an autonomous pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md) on an underwater object (ROV, AUV, diver, etc.), and four navigation buoys on the water surface [RWLT GIB](RWLT_GIB_Specification_en.md). This configuration allows you to monitor the movement of an underwater object in real time in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to work with wireless diver's telephones [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_EN_Specification_en.html) as a pinger, thus combining two-way voice communication and navigation.

### 1.3. System Composition

The minimum composition of the system includes:

- **Four sonobuoys** [RWLT GIB](RWLT_GIB_Specification_en.md):

| ![RWLT GIB](/documentation/RWLT_GIB.png) |
| :---: |
| [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> Navigation sonobuoy receiver |

- Radio modem [RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md), for receiving navigation information from buoys:

| ![RWLT RF Dongle](/documentation/RWLT_RF_Dongle.png) |
| :---: |
| [RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) <br/> Digital Radio |

And, depending on the user task:
* If it is required to determine the location of divers simultaneously with voice communication, then **up to 255** wireless diver's telephone stations [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) are used;

| ![RedPhone-DX](/documentation/redphone_dx.png) |
| :---: |
| [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) <br/> Wireless voice communication diver's station |

In this configuration, divers will be located at the moment they release the PTT button, i.e. completing the transmission of the voice message; the transmission of voice messages must take place in turn.

* If you want to determine the location of a remotely operated vehicle (ROV, ROV), or a diver without the need for voice communication, then **1** pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) is used. The pinger works autonomously and the geolocation of the object on which the pinger is attached will be updated every two seconds.

| ![RWLT Pinger](/documentation/RWLT_Pinger.png) |
| :---: |
| [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger beacon |


## 2. Working with the RWLT system

### 2.0. Before work
Depending on whether you are working with a pinger or tracking divers, you will need different versions of specialized software.

- To track an underwater object equipped with an autonomous pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md), the application [🐠 uTrack](https://github.com/ucnl/uTrack/releases/download/beta1/uTrack) must be installed on the operator's PC .zip)

- To track the position of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diving stations, the [🤿 uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip) application must be installed on the operator's PC 

Download the necessary software in advance. Installation is not required - just unzip the contents of the archive to a location convenient for you.

Whether you are using underwater equipment such as wireless voice communication diving stations or a stand-alone pinger beacon, make sure that all equipment is fully charged before entering the water and charge all devices if necessary.

Particular attention should be paid to wireless voice communication diving stations and pinger beacons: in view of the fact that these devices have built-in power supplies based on **LiFePO4**, they have a very flat discharge characteristic and it is difficult to determine the state of charge of the built-in power source. Therefore, it is recommended to charge all devices no earlier than 1-2 days before use.

We use **LiFePO4** based batteries as they are the most durable and withstand the maximum number of charge-discharge cycles compared to **Li-ion** and **Li-Po** batteries, and can also operate at low temperatures. temperatures.

### 2.1. Preparing for work and checking equipment

#### 2.1.1. Choosing a location for the operator's place 

Select the location where the system operator's station will be located. Since the receiving antenna of the radio modem is located in this place, there must be a direct line of sight to each of the buoys from this place. For normal operation of the system, the operator's console must be able to receive navigation data via radio from all four buoys.
Place the radio modem at the highest possible height away from any bulky objects that shield radio waves (metal, reinforced concrete, etc.).

Connect the radio modem to the USB port of the PC. Launch the application appropriate for your task and press the **🔌 LINK** button in the top toolbar - the application will start searching for a port for communication with the radio modem, which will be reflected in the status bar.

#### 2.1.2. Checking the set of buoys

- Check the integrity of the rubber caps of the toggle switches. If any defects are found that violate the moisture-proof functions of the caps, the use of buoys is **strictly prohibited**.
- Make sure that the charging port caps on all buoys are screwed on tightly.
- Turn on all buoys by moving the toggle switches on their cover to the **ON** position.
- Verify that all buoys are operational and that their built-in power supplies are sufficiently charged, as described in the warning lights below:

> _**WARNING!**_
> Almost all known buoy failures are due to the user using a buoy with an unscrewed cap of the charging connector!
> Operation of buoys with an unscrewed cap of the connector is prohibited and may result in water ingress into the device.
> Failure of buoys due to water ingress through an open charging port is _**out of warranty**_!

The location of the controls and indications on the buoy cover is shown below.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_cover_scheme.png)|
| Location of controls and indications on the cover of the buoy |
| _1 - power switch, 2 - light indication lamps, 3 - charging connector (Radio antenna not shown)_ |

The buoys in each set have different addresses from 1 to 4. When the buoy is turned on using toggle switch 1, the buoy reports its number in the set using indicator 2: the number of flashes corresponds to the buoy number.

After reporting its number, the buoy goes into operation mode. If the buoy's battery is charged, the indicator will remain lit until the built-in GNSS receiver detects signals from the satellites of the global navigation satellite system. After that, it will flash 1 time in 4 seconds. The number of flashes in this case also corresponds to the number of the buoy in the set.

If the battery of the buoy is in a state where the charge is less than 20%, the indicator will flash 1 time per second. The number of flashes in this case also corresponds to the number of the buoy in the set.

> If the user notices flashes 1 time per second, the buoy should be turned off and put on charge as soon as possible.
> Long-term operation with a discharged power supply is not permitted.

If the battery is in a state of critical discharge, then after reporting its number, the buoy will automatically turn off, in this case the indicator will also be off. The buoy must be immediately put on charge to avoid failure of the built-in power source.

If everything is done correctly, and the tops of the buoys have a good view of the celestial hemisphere, then after a while (usually no more than 1-2 minutes) you will be able to see the positions of the buoys in the main application window.

After that, you can place the buoys on the surface of the water.

If you need a significant amount of time to equip the buoys with anchor lines and place them on the surface of the water, you can turn off the buoys to save power and turn them on just before placing them on the water.

#### 2.1.3. Location of buoys on the surface of the water

The buoys are placed in the water area on the surface of the water, their position is fixed with the help of anchors.

> It is worth remembering that although the buoys have a slight positive buoyancy, they are not intended for direct attachment to an anchor line. To unload the buoy from the weight of the anchor rope, fenders (or floats) corresponding to the weight of the rope should be used.

The figure below<sup>[1](#footnote1)</sup> shows the recommended scheme for installing a buoy on a body of water.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_dep_scheme.png)|
| Recommended buoy installation scheme |
| _1 - sonobuoy, 2 - extra weight<sup>[2](#footnote2)</sup>, 3 - float, 4 - anchor line, 5 - anchor_ |

__________
<a name="footnote1"><sup>1</sup></a> Images may vary slightly from actual product,
as the manufacturer is constantly working to improve performance and make changes to the design.
<a name="footnote2"><sup>2</sup></a> The extra weight is only applied to the underloaded version.

The buoys should be located in a convex quadrilateral covering the entire proposed work area with a small margin. It is important to observe a few simple conditions for the effective operation of the system:

- buoys are located no closer than 40 and no further than 1500 meters from each to each
- from each buoy there must be direct visibility to the receiving radio modem of the operator's console
- from each sonoacoustic receiver of the buoy there must be a direct line of sight to the positioned underwater object
- it is not recommended to place buoys close to the shore, port infrastructure facilities, ships
- the size of the navigation base (the average size of the rectangle formed by buoys on the surface of the water) should not be less than the maximum depth of the positioned object
- the size of the navigation base should be slightly larger than the intended area of work

> _**WARNING!**_
> Buoys are not underwater devices and are designed to operate on the surface of the water. Although the protection class implies a short-term overlap of the device with a wave, it is worth remembering that the built-in radio equipment (GNSS module and radio modem) cannot work in such conditions!

It is not recommended to throw buoys overboard. It is necessary to carefully lower them to the surface of the water, at the same time making sure that the length of the anchor rope is sufficient and its weight is perceived by the unloading fender, and the buoy is located vertically on the surface of the water and does not experience any additional loads.

#### 2.1.4. Preparation of underwater equipment

Subsea equipment preparation varies for different system configurations:

- For location-tracking configuration of divers equipped with  wireless voice diving stations [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html), refer to the [RedPhone-DX diving stations instruction manual](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html);
It should be remembered that:
  - the **RWLT Pinger** mode must be enabled on the stations (setting **RWLT Pinger enabled**);
  - when using several voice communication stations in one body of water, they must be given **different** addresses (**RWLT Diver's ID**).

- To configure a system with a stand-alone pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md), no preliminary steps are required other than pre-charging the built-in power source (battery pack). For versions with a detachable connection between the pinger beacon and the battery pack, you must first make sure that the connector is tightly closed and serviced (for threaded connectors, make sure that the sealing rings are lubricated with silicone grease, for SUBCONN and similar connectors, make sure that both parts of the connector are grease recommended by the connector manufacturer).

The pinger beacon turns on automatically when it gets into the water (contacts for switching on from water are located on the battery pack). It should be remembered that immediately after switching on, the pinger beacon determines atmospheric pressure for **5** seconds for more accurate depth measurement. Therefore, it is recommended to submerge the battery pack first and wait 5 seconds before submerging the pinger beacon itself.

The pinger beacon must be fastened only to a special groove with a soft clamp in such a way as to exclude any uneven loading of the beacon body, excessive squeezing and shading/shielding of the beacon body. The figure below shows the basic requirements for mounting the acoustic part of the pinger beacon on the vessel:

| |
| :---: |
| ![0](/documentation/uWave_mounting_en.png)|
| Requirements for mounting the acoustic part of the pinger beacon on the vessel|
| _It is not allowed to shield the spatial hemisphere or parts of the antenna located above the mounting groove; the pressure in the area under the fastening must be balanced with the external pressure_ |

The performance of the pinger beacon is easy to check by lowering it into the water: when submerged more than 1 meter, it starts emitting a navigation signal with a period of 2 seconds.

## 2.2. Working with the system

### 2.2.1. Configuration for working with divers

#### 2.2.1.1. Application interface and functions

We propose to start acquaintance with the application with its settings. The figure below shows a general view of the settings window, it can be opened by pressing the **'⚙ SETTINGS'** button on the main toolbar of the main application window.

| |
| :---: |
| ![1](/documentation/uTrackDiver_settingswindow_1.png)|
| Settings window controls |
| _1 - Checkbox for using an additional source of navigation data (GNSS receiver), 2 - Combo box of port speed of an additional source of navigation data, 3 - Checkbox for using the first buoy as an additional source of navigation data, 4 - List of map tile source servers, 5 - Button for reset the settings to default settings, 6 - Checkbox of automatic salinity selection (from the database), 7 - Salinity input field, 8 - Sound speed auto calculation flag, 9 - Sound speed input field, 10 - Water temperature input field, 11 - Number of points track to display, 12 - Radial error threshold input field, 13 - Drop-down list for selecting the size of map tiles, 14 - Buttons for accepting settings and canceling_ |

The receiving radio modem is connected to the PC via the USB port. The application itself searches for the serial port and this does not require the user to set any settings.

- In some situations it is convenient for the operator to see his own location on the map, this can be achieved in two ways: the first is to connect an additional GNSS receiver to the PC. In this case, the application needs to indicate that this method is being used by checking the check box 1 **Use AUX GNSS**. Also in this case, you need to specify the serial port speed at which the external GNSS receiver operates. The port itself does not need to be specified, the application will detect it itself.

- If there is no external GNSS receiver, but the operator would like to see his own location on the map, you can use the second method: buoy #1 can be used as an external GNSS. This method has some limitations, for example, it is not always possible to locate the operator next to the buoy, the buoys provide a limited set of navigation information compared to an external GNSS receiver. If this method is applicable in the current task, then check the check box 3 **Base 1 as AUX GNSS Source**. In this case, the checkbox in box 1 will be automatically unchecked.

- The application allows you to display tracks on top of the map, the tiles of which can be downloaded via the HTTPS protocol (this needs the Internet connection). Currently, the Open Street Maps service is supported. Field 4 **Tile servers** specifies server addresses, and field 13 **Tile size** specifies the size of tiles in pixels. To download tiles, the application needs access to the Internet.

- Button 5 **SET DEFAULTS** allows you to reset the settings to the default state.

- Check box 6 **Auto salinity** means that the application will try to determine the salinity from the database using the current geographic coordinates. The application contains a base of salinity of the surface of the world's oceans with a step of 1 degree in latitude and longitude. Use this setting only in large bodies of water: seas and oceans. If you work in small inland waters, it is recommended to uncheck 6 and set the appropriate water salinity value in field 7 **Salinity, PSU**. In most cases, for inland fresh waters, a value of 0 PSU is adequate. If you have accurate data on the salinity of the body of water, or it can be measured directly, you can also enter it in field 7. The salinity value is used to calculate the speed of sound.

- With the check box 7 **Auto speed of sound** unchecked and the corresponding field 9 **Speed of sound, m/s** allows you to set a known sound speed value. Use this option if you have a direct measurement, otherwise it is recommended to check the check box 7.

- Field 10 **Water temperature, °C** allows to specify the relevant water temperature value. The water temperature is used in the calculation of the speed of sound, if the check box 9 **Auto speed of sound** is checked. If you are measuring water temperature, it is recommended to take samples some distance from the surface.

- Field 11 **Track points to show** tells the application how many points (calculated positions) for each track should be displayed at the same time. This setting only affects the display. The application additionally stores all received points, which can then be saved.

- Field 12 **Radial error threshold, m** specifies the radial error threshold (residual function values at the end of the navigation problem solution), above which the computed position is considered erroneous and discarded. It is recommended to set this value within 10 meters.

- Buttons 14 **OK** and **CANCEL** are responsible for saving the settings and canceling the changes, respectively. After changing and saving the settings, the application will request a restart for the settings to take effect.

Consider now the main window of the application. Its general view with indication of the main controls is shown in the figure below.

| |
| :---: |
| ![1](/documentation/uTrackDiver_mainwindow_1.png)|
| Basic elements of the main application window |
| _1 - Main toolbar, 2 - Map toolbar, 3 - Map panel, 4 - Additional information panel, 5 - Log panel, 6 - Divers list toolbar, 7 - Divers list, 8 - Track legend panel, 9 - Scale bar , 10 - Panel of switches for displayed parameters of divers, 11 - Status line_ |

- 1 - The main toolbar is located in the upper part of the window and contains the following elements:
  - **🔌 LINK** button - controls the connection to the receiving radio modem and external GNSS receiver (if the corresponding settings enabled).
  - Button **⚙ SETTINGS** - call the settings editor. This button is not available when the connection is active or when a log file is being playing.
  - Menu **📖 LOG** - contains functions for working with log files
    - Item **👀 View current** - opens the current log file in the application associated with the 'log' extension (usually Notepad)
    - Item **▶ Playback...** - selects a log file for real-time playback. This function allows you to almost completely restore the progress of the work done and, for example, restore a track that has not been saved from a log file.
    - Item **🧹 Remove empty entries** - cleaning the LOG directory in the application folder: all log files less than 2 kilobytes in size and all empty folders will be deleted
    - Item **🗜 Archive all entries...** - packing the entire folder with log files into a Zip archive.
    - Item **🗑 Clear all** - deletes all application log files. **Be careful! All files will be permanently deleted!!!**
    - Item **🧹+🗜+🗑 Do them all...** - Deleting all empty folders, log files less than 2 kilobytes, packing the rest of the log files into a Zip archive and deleting the originals in the LOG folder of the application.
  - Menu **🛠 UTILS** - contains additional functions
    - Submenu **🗺 TRACKS** - functions for working with tracks
      - Item **💾 Export...** - saving tracks in one of the supported formats through the system dialog
      - Item **🗑 Clear** - clearing the tracks contained in the application's memory
  - The input field and button **📝 ADD NOTE** are used to enter comments (notes) into the log file. You can simply type a text comment and press **Enter** regardless of which control has focus. The comments are saved with a timestamp, and in the future, when playing the log file, the comments will be displayed at the appropriate point in time. This function allows you to quickly save any text notes about the progress of work.
  - Button **ℹ INFO** - calls a dialog with information about the application and links to additional information on the system.

- 2 - The map toolbar is located under the main toolbar on the left and contains the following elements:
  - Button **⛯** - enable/disable the display of base points (buoys) positions. Sometimes it may be necessary to turn off the display of buoy positions on the chart in order to zoom in and be able to view diver tracks in more detail. Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **📜** - enable/disable the display of the log text panel (5). Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **⋮** - enable/disable the display of the 'legend' - the list of track designations (8). Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **📑** - enable/disable the display of the comments field (NOTES). Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **👽** - enable/disable the display of the additional (Extra-) information field (4). Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **⎙** - used to save a screenshot of the main application window. Screenshots are saved in the **SCREENSHOTS** directory in the application folder. The name of the last saved screenshot is displayed in the status bar (11).
  - The **♻ RESET VIEW** button allows you to reset the current view and displayed tracks. This does not affects tracks in the application memory.
- 3 - Map panel - serves to display divers' tracks, buoy positions on the map, as well as:
  - vertical scale bar (9)
  - application log (5). This field displays the last 4 lines of the application log from bottom to top.
  - legends (8). The legend matches the color and size of the points and the track name.
  - comments (notes). To create comments on the progress of work on the fly, the operator simply needs to type them on the keyboard, while the typed text will be displayed in the input field on the main toolbar. By pressing the 'Enter' key, the text will be saved to the log and will be displayed on the right in the map panel (if the corresponding switch **'📑'** on the map toolbar is in the active state).
  - additional navigational information (4).
- 3 - The map panel is for displaying the map, buoy positions, calculated diver positions and some additional information
- 4 - The additional information field is located in the upper left part of the map panel and serves to display additional information. The display of this field can be switched using the **👽** button on the map toolbar (2). Each parameter is displayed on a separate line, starting with a three-letter parameter identifier followed by a colon, followed by the parameter value and unit of measure. The time in the format (MM:SS) displayed next to the parameter indicates how long ago the parameter value was updated. The table below lists all possible identifiers and their descriptions:

| ID | Description | Units | Range |
| :--- | :--- | :--- | :--- |
| CRS | Heading according to external GNSS | ° | 0 .. 360 |
| SPD | Speed according to external GNSS | km/h (m/s) | >= 0 |
| LAT | Latitude according to external GNSS | ° | -90 .. 90 |
| lon | Longitude according to external GNSS | ° | -180 .. 180 |
| STY | Salinity (from settings or from database) | PSU | 0 .. 40 |
| WTM | Water temperature (from settings) | °C | -10 .. +40 |
| SOS | Sound speed (from settings or calculated) | m/s | 1300 .. 1600 |
| B1V | Built-in battery voltage of buoy 1 | v | 10 .. 13 |
| B2V | Built-in battery voltage of buoy 2 | v | 10 .. 13 |
| B3V | Built-in battery voltage of buoy 3 | v | 10 .. 13 |
| B4V | Built-in battery voltage of buoy 4 | v | 10 .. 13 |
| B1M | Signal level on buoy 1 | dB | 14 .. 36 |
| B2M | Signal level on buoy 2 | dB | 14 .. 36 |
| B3M | Signal level on buoy 3 | dB | 14 .. 36 |
| B4M | Signal level on buoy 4 | dB | 14 .. 36 |

- 5 - The log panel is located at the bottom of the map panel and displays the last 4 lines of the application's log. The visibility of this field is toggled with the **📜** button on the map toolbar (2).
- 6 - The **DIVERS** diver list toolbar is located above the diver list on the left side of the main application window. The toolbar contains the following elements:
  - Button **🎢** - sorting the list of divers by their ID.
  - Button **▼** - collapse all list items.
  - Button **▲** - expand all list items.
- 7 - The list of divers **DIVERS** is located on the left side of the main application window. The list has a tree structure, the top-level nodes are in the format **Diver #N**, where N is the diver ID, which is set in the settings of the diving communication station [RedPhone-DX](https://docs.unavlab.com/documentation /EN/RedPhone/RedPhone_DX_Specification_en.html) (setting **RWLT Diver's ID**, for more information, see [Operating Instructions for RedPhone-DX Diving Stations](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html)). Child nodes contain information about the diver known to the system. Each individual parameter is represented by a string that begins with the parameter identifier, followed by a colon followed by the value of the parameter. If the value of this parameter was updated more than 3 seconds ago, then the time elapsed since the parameter was updated in the format (MM:SS) is indicated in brackets. Below is a list of possible options:

| ID | Description | Units | Range |
| :--- | :--- | :--- | :--- |
| LAT | Computed latitude | ° | -90 .. 90 |
| LON | Computed longitude | ° | -180 .. 180 |
| RER | Radial error | m | 0 .. 99 |
| DOP | Geometric dilution of precision factor | - | - |
| TBA | The quality of the relative position of the positioned object and reference points | - | - |
| DST | Distance to diver from external GNSS position | m | 0 .. 1500 |
| AZM | Direction (course) to the diver from the position according to external GNSS | ° | 0 .. 360 |
| RAZ | Reverse direction (course) from diver to external GNSS position | ° | 0 .. 360 |

The most important parameters here are **AZM**, **DST** and **RAZ**: by azimuth and distance, the operator can always understand where this or that diver is located relative to him, and he can report the **RAZ** parameter to the diver via voice communication, so that he, adhering to this course, can perform homing task.

The display of various parameters is switched by the buttons on the panel (10). It should be understood that the parameters associated with the relative position of the diver and the surface point (range, forward and reverse course) can only be determined if there is an external source of navigation data - an external GNSS receiver that sets the system the location of the surface point of operator or when the setting is enabled **Base 1 as AUX GNSS** - when all parameters are determined relative to buoy #1.

- 8 - Legend panel. Displayed in the upper right corner of the map field. It displays a list of tracks with examples of track points.
- 9 - The scale bar is displayed in the lower right corner of the map field and shows the scale of the map in meters.
- 10 - The panel of switches for the displayed parameters of divers is located under the list of divers and switches the visibility of parameters in the list:
  - Button **DST** - turns on/off the display of the distance to a diver. Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **AZM** - turns on/off the display of the direction **to** a diver. Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **RAZ** - turns on/off the display of the direction **from** a diver to the position according to the external GNSS receiver. Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **LOC** - turns on/off the display of the diver's location (latitude and longitude). Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **RER** - turns on/off the display of the radial error - the value of the residual function, on which the solution of the problem of determining the location of the diver ended. Changes to the state of this button are automatically saved and replayed when playing log files.
  - Button **DOP** - enables/disables the display of parameters **DOP** and **TBA**.
- 11 - Status bar. The line displays the statuses of the ports of the radio modem and the external source of navigation data (external GNSS receiver), the name of the last saved screenshot or the Zip archive into which the log files were packed.


#### 2.2.1.2. Interaction with the system

Locating divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication stations is possible when the following conditions are met (assuming the stations are properly configured to work with the RWLT system, and navigation buoys are properly deployed):

- all buoys have GNSS reception, and the operator's console has radio reception from all buoys. Thus the application displays the positions of all four buoys;
- a special navigation signal transmitted by the diving station after the diver completes the voice transmission (releasing the **PTT** button), is received by all four buoys of the **RWLT** system;
- signals from different divers do not overlap each other, and there is a time interval of at least 2 seconds between signals from different divers;

It is necessary to remember the factors that reduce the efficiency of the system:
- hydrological conditions: natural and technogenic noise can worsen and completely exclude the normal operation of the system; unfavorable underwater landscape and benthic vegetation can contribute to acoustic shadowing, etc.
- divers leaving the navigation base (a figure formed by buoys on the water surface): the most stable operation of the system is achieved inside the navigation base. In some approximation, the relative position of the diver and the navigation base is estimated by the parameters **DOP** and **TBA**. Position in the immediate vicinity of one of the buoys or directly behind it is also unfavorable.
- large vessels, especially those with deep draft, may interfere with the passage of the acoustic signal.

### 2.2.2. Configuration for working with pinger beacon

**THIS SECTION IS UNDER DEVELOPMENT**

## 2.3. Upon completion of work

**Navigation buoys** must be:
- removed from anchors;
- turned off;
- cleaned of contaminants (silt, dirt, algae, etc.);
- desalinated without immersion of the upper part, if the work was not carried out in fresh water;
- wiped with a soft cloth from moisture before being placed in a transport case;

Not allowed:
- Storage in undesalinated form;
- Storage of buoys together with wet anchor lines;
- Hanging out buoys for drying by load-carrying eyes;

**Pinger-beacon** should be:
- dismantled from the vessel;
- washed from contaminants (silt, dirt, algae, etc.);
- desalinated, if the work was not carried out in fresh water;
- gently wiped with a soft cloth and air-dried for at least 30 minutes;

Not allowed:
- mechanical impact on the opening of the pressure sensor;
- storage with the presence of moisture (especially marine);
- freezing of water in the opening of the pressure sensor;

**Diving Wireless Voice Stations**
Upon completion of work, it does not require any additional manipulations and turns off automatically in the air. Before packing in a shipping container, it is necessary to rinse and/or desalinate in fresh water, followed by wiping with an absorbent cloth and air drying for at least 30 minutes.

For additional and up-to-date information, refer to the [Operating Instructions for RedPhone-DX Wireless Voice Diver Stations](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html).

<div style="page-break-after: always;"></div>

## 3. Liability and Disclaimer
### 3.1. Terms of replacement and free warranty service
The manufacturer's warranty covers only factory defects that appear during the operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a manufacturing defect.

The reasons for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** of the equipment from the delivery set, including violation of the insulation of wires and cables;
- any **damage caused by exposure to moisture and dirt** due to improper use of the equipment supplied;
- any **electrical damage** caused by **the use of incomplete accessories** (chargers), the use of low-quality and/or defective batteries; Incomplete accessories do not include accessories supplied by the manufacturer or its representative to replace faulty or lost ones;
- any **traces of self-repair and/or opening** of the equipment supplied.

<div style="page-break-after: always;"></div>

### 3.2. Manufacturer disclaimer

_____________

_**ANY OF THE PARTS OF THE DELIVERY SET, INDIVIDUALLY AND AS A PART OF THE SYSTEM (hereinafter referred to as the "EQUIPMENT SUPPLIED"):**_

_**- NOT DEVELOPED AS MEANS OF RESCUE**_
_**- NOT TESTED AS MEANS OF RESCUE**_
_**- IS NOT MEANS OF RESCUE**_
_**- THE MANUFACTURER DECLARES THAT THE EQUIPMENT SUPPLIED IS SAFE WHEN USE ACCORDING TO THESE INSTRUCTIONS AND IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF THE USE OF THE SUPPLIED EQUIPMENT**_

______________

_**THE MANUFACTURER GUARANTEE THAT THE RWLT HYDRO-ACOUSTIC TRACKING SYSTEM (hereinafter referred to as the SYSTEM):**_
_**- DESIGNED ONLY TO WORK WITH PINGER BEACONS OR DIVING COMMUNICATION STATIONS DESIGNED FOR JOINT OPERATION WITH THE SYSTEM**_
_**- STRUCTURALLY CANNOT BE USED FOR TRACKING OBJECTS NOT EQUIPPED WITH PINGER BEACONS OR DIVING COMMUNICATION STATIONS NOT DESIGNED FOR JOINT WORK WITH THE SYSTEM**_
_**- CONTAINS ONLY CIVIL AND UNLICENSED RADIO MODULES: GNSS RECEIVERS AND RADIOS**_
_**THE ABOVE LIMITATIONS CANNOT BE REMOVED BY ANY MANIPULATION WITH THE SETTINGS AND/OR CONTROLS OF THE SYSTEM DEVICES AND/OR THE SOFTWARE INTENDED TO WORK WITH THE SYSTEM**_

______________


[Back to contents](#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
