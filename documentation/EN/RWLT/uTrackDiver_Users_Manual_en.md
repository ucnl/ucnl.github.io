[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **uTrackDiver: User's manual**

> ℹ This document can be printed directly from your browser.
> For best results:
> - select the range of pages to print, excluding the first and last pages
> - in the advanced settings, disable headers and footers

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/ucnl/ucnl.github.io/assets/24439946/88cc0587-952c-4a67-9504-3bb63afc86f7) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uTrackDiver** - Application for tracking divers using the RWLT system <br/> User's manual |

# uTrackDiver <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
- [2. Application interface and functions](#2-application-interface-and-functions)
  - [2.1. Application settings](#21-application-settings)
  - [2.2. Main window](#22-main-window)
    - [2.2.2. Map toolbar](#222-map-toolbar)
    - [2.2.3. Map panel](#223-map-panel)
    - [2.2.4. Additional information field](#224-additional-information-field)
    - [2.2.5. Log field](#225-log-field)
    - [2.2.6. Diver list toolbar](#226-diver-list-toolbar)
    - [2.2.7. Diver list](#227-diver-list)
    - [2.2.8. Legend field](#228-legend-field)
    - [2.2.9. Scale bar](#229-scale-bar)
    - [2.2.10. Panel of switches for displayed diver parameters](#2210-panel-of-switches-for-displayed-diver-parameters)
    - [2.2.11. Status line](#2211-status-line)

<div style="page-break-after: always;"></div>

## 1. Introduction

To track the position of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diver stations, the [🤿 uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip) application must be installed on the operator's PC.

Download the necessary software in advance. No installation is required - just unpack the contents of the archive to any convenient location.

## 2. Application interface and functions

### 2.1. Application settings

We suggest starting with the application settings. The figure below shows an overview of the settings window. To open it, click the **'⚙ SETTINGS'** button on the main toolbar of the main application window.

| |
| :---: |
| ![1](/documentation/uTrackDiver_settingswindow_1.png)|
| Settings window controls |
| _1 - Checkbox for using an additional source of navigation data (GNSS receiver), 2 - Drop-down list for the port speed of the additional navigation data source, 3 - Checkbox for using the first buoy as an additional source of navigation data, 4 - List of map tile servers, 5 - Button for resetting the settings to their defaults, 6 - Checkbox for automatic salinity selection (from the database), 7 - Salinity input field, 8 - Checkbox for automatic speed of sound calculation, 9 - Speed of sound input field, 10 - Water temperature input field, 11 - Number of track points to display, 12 - Radial error threshold input field, 13 - Drop-down list for selecting the map tile size, 14 - Buttons for accepting settings and canceling_ |

The receiving radio modem connects to the PC via a USB port. The application automatically searches for the virtual serial port, so the user does not need to specify any settings.

- In some situations, it is convenient for the operator to see their own location on the map. This can be achieved in two ways. The first is to connect an additional GNSS receiver to the PC. To use this method, select checkbox 1 **Use AUX GNSS**. You also need to specify the serial port speed used by the external GNSS receiver. The port itself does not need to be specified; the application will detect it automatically.

- If there is no external GNSS receiver, but the operator would like to see their own location on the map, use the second method: buoy No. 1 can serve as the external GNSS source. This method has some limitations. For example, it is not always possible to position the operator next to the buoy, and the buoys provide a more limited set of navigation information than an external GNSS receiver. If this method is suitable for the current task, select checkbox 3 **Base 1 as AUX GNSS Source**. Checkbox 1 will be cleared automatically.

- The application can display tracks over a map whose tiles can be downloaded via HTTPS. The Open Street Maps service is currently supported. Field 4 **Tile servers** specifies the server addresses, and field 13 **Tile size** specifies the tile size in pixels. The application needs Internet access to download tiles.

- Button 5 **SET DEFAULTS** resets the settings to their default values.

- When checkbox 6 **Auto salinity** is selected, the application will try to determine the salinity from the database using the current geographic coordinates. The application contains a database of ocean surface salinity with a resolution of 1 degree in latitude and longitude. Use this setting only in large bodies of water: seas and oceans. If you work in small inland bodies of water, it is recommended to clear checkbox 6 and enter the appropriate water salinity in field 7 **Salinity, PSU**. In most cases, a value of 0 PSU is adequate for inland freshwater bodies. If you have accurate salinity data for the body of water, or the salinity can be measured directly, you can also enter it in field 7. The salinity is used to calculate the speed of sound.

- Clear checkbox 7 **Auto speed of sound** and use the corresponding field 9 **Speed of sound, m/s** to enter a known speed of sound if you have a direct measurement. Otherwise, it is recommended to select checkbox 7.

- Field 10 **Water temperature, °C** lets you enter the relevant water temperature. The water temperature is used to calculate the speed of sound when checkbox 9 **Auto speed of sound** is selected. If you measure the water temperature, it is recommended to take samples some distance from the surface.

- Field 11 **Track points to show** tells the application how many points (calculated positions) to display simultaneously for each track. This parameter affects the display only. The application also stores all received points, which can then be saved.

- Field 12 **Radial error threshold, m** specifies the radial error threshold (the value of the residual function at the end of solving the navigation problem), above which the calculated position is considered erroneous and discarded. It is recommended to set this value within 10 meters.

- Buttons 14 **OK** and **CANCEL** save the settings and cancel changes, respectively. After you change and save the settings, the application will request a restart for the settings to take effect.


### 2.2. Main window

An overview of the main application window, with its main controls labeled, is shown below.

| |
| :---: |
| ![1](/documentation/uTrackDiver_mainwindow_1.png)|
| Main elements of the main application window |
| _1 - Main toolbar, 2 - Map toolbar, 3 - Map field, 4 - Additional information field, 5 - Log field, 6 - Diver list toolbar, 7 - Diver list, 8 - Track designation field, 9 - Scale bar, 10 - Panel of switches for displayed diver parameters, 11 - Status line_ |

#### 2.2.1. Main toolbar

- 1 - The main toolbar is located at the top of the window and contains the following elements:
  - The **🔌 LINK** button controls the connection to the receiving radio modem and the external GNSS receiver.
  - The **⚙ SETTINGS** button opens the settings editor. This button is unavailable while the connection is active or a log file is being played back.
  - The **📖 LOG** menu contains functions for working with log files:
    - **👀 View current** opens the current log file in the application associated with the 'log' extension (usually Notepad).
    - **▶ Playback...** selects a log file for playback in real time. This function allows you to reconstruct almost the entire course of an operation and, for example, recover a track that was not saved.
    - **🧹 Remove empty entries** cleans up the LOG directory in the application folder: all log files smaller than 2 kilobytes and all empty folders will be deleted.
    - **🗜 Archive all entries...** packs the entire folder of log files into a Zip archive.
    - **🗑 Clear all** deletes all application log files. **Be careful! All files will be deleted without the possibility of recovery!!!**
    - **🧹+🗜+🗑 Do them all...** deletes all empty folders and log files smaller than 2 kilobytes, packs the remaining log files into a Zip archive, and deletes the originals from the application's LOG folder.
  - The **🛠 UTILS** menu contains additional functions:
    - The **🗺 TRACKS** submenu contains functions for working with tracks:
      - **💾 Export...** saves tracks in one of the supported formats through a system dialog.
      - **🗑 Clear** clears the tracks stored in the application's memory.
  - The input field and the **📝 ADD NOTE** button are used to enter comments into the log file. You can simply type a text comment and press **Enter** regardless of which control has focus. Comments are saved with a timestamp and are displayed at the corresponding time during log playback. This function allows you to quickly save text notes about the progress of an operation.
  - The **ℹ INFO** button opens a dialog with information about the application and links to additional information about the system.

#### 2.2.2. Map toolbar

- 2 - The map toolbar is located below the main toolbar on the left and contains the following elements:
  - The **⛯** button shows/hides the base points (buoys). Sometimes you may need to hide the buoy positions on the map to zoom in and view the divers' tracks in more detail. Changes to this button's state are automatically saved and reproduced during log playback.
  - The **📜** button shows/hides the log text field (5). Changes to this button's state are automatically saved and reproduced during log playback.
  - The **⋮** button shows/hides the legend - the list of track designations (8). Changes to this button's state are automatically saved and reproduced during log playback.
  - The **📑** button shows/hides the comments field (NOTES). Changes to this button's state are automatically saved and reproduced during log playback.
  - The **👽** button shows/hides the additional information field (4). Changes to this button's state are automatically saved and reproduced during log playback.
  - The **⎙** button saves a screenshot of the main application window. Screenshots are saved in the **SCREENSHOTS** directory in the application folder. The name of the last saved screenshot is displayed in the status line (11).
  - The **♻ RESET VIEW** button resets the current view and displayed tracks.
- 3 - The map field displays divers' tracks and buoy positions over the map background, as well as:
  - the vertical scale bar (9)
  - the application log (5). This field displays the last 4 lines of the application log from bottom to top.
  - the legend (8). The legend associates each track name with the color and size of its points.
  - comments. To create comments about the progress of an operation on the fly, simply type them on the keyboard. The text appears in the input field on the main toolbar. Pressing 'Enter' saves the text to the log and displays it on the right side of the map field (if the corresponding **'📑'** switch on the map toolbar is active).
  - additional navigation information (4).

#### 2.2.3. Map panel

- 3 - The map panel displays the map, buoy locations, calculated diver positions and some additional information.

#### 2.2.4. Additional information field

- 4 - The additional information field is located in the upper left part of the map panel and displays additional information. Its visibility can be toggled using the **👽** button on the map toolbar (2). Each parameter appears on a separate line, starting with a three-letter parameter ID and a colon, followed by the parameter value and units. The time in (MM:SS) format displayed next to a parameter shows how long ago its value was updated. The table below lists all possible IDs and their descriptions:

| ID | Description | Units | Range |
| :--- | :--- | :--- | :--- |
| CRS | Course from external GNSS data | ° | 0 .. 360 |
| SPD | Speed from external GNSS data | km/h (m/s) | >= 0 |
| LAT | Latitude from external GNSS data | ° | -90 .. 90 |
| LON | Longitude from external GNSS data | ° | -180 .. 180 |
| STY | Salinity value (from the settings or the database) | PSU | 0 .. 40 |
| WTM | Water temperature value (from the settings) | °C | -10 .. +40 |
| SOS | Speed of sound value (from the settings or calculated) | m/s | 1300 .. 1600 |
| B1V | Built-in battery voltage of buoy No. 1 | V | 10 .. 13 |
| B2V | Built-in battery voltage of buoy No. 2 | V | 10 .. 13 |
| B3V | Built-in battery voltage of buoy No. 3 | V | 10 .. 13 |
| B4V | Built-in battery voltage of buoy No. 4 | V | 10 .. 13 |
| B1M | Signal level at buoy No. 1 | dB | 14 .. 36 |
| B2M | Signal level at buoy No. 2 | dB | 14 .. 36 |
| B3M | Signal level at buoy No. 3 | dB | 14 .. 36 |
| B4M | Signal level at buoy No. 4 | dB | 14 .. 36 |

#### 2.2.5. Log field

- 5 - The log field is located at the bottom of the map panel and displays the last 4 lines of the application log. Its visibility is toggled using the **📜** button on the map toolbar (2).

#### 2.2.6. Diver list toolbar

- 6 - The **DIVERS** diver list toolbar is located above the diver list on the left side of the main application window. It contains the following elements:
  - The **🎢** button sorts the diver list by number.
  - The **▼** button collapses all list items.
  - The **▲** button expands all list items.

#### 2.2.7. Diver list

- 7 - The **DIVERS** diver list is located on the left side of the main application window. The list has a tree structure. Top-level nodes have the format **Diver #N**, where N is the diver's ID, set in the [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver communication station settings (**RWLT Diver's ID**; for more information, refer to the [RedPhone-DX diver station user's manual](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html)). Child nodes contain the information known to the system about that diver. Each parameter is represented by a line beginning with the parameter ID, followed by a colon and the parameter value. If the value was last updated more than 3 seconds ago, the elapsed time is shown in parentheses in (MM:SS) format. The possible parameters are listed below:

| ID | Description | Units | Range |
| :--- | :--- | :--- | :--- |
| LAT | Calculated latitude | ° | -90 .. 90 |
| LON | Calculated longitude | ° | -180 .. 180 |
| RER | Radial error | m | 0 .. 99 |
| DOP | Geometric dilution of precision | - | - |
| TBA | Quality of the relative position of the positioned object and reference points | - | - |
| DST | Distance to the diver from the position provided by external GNSS data | m | 0 .. 1500 |
| AZM | Direction (course) to the diver from the position provided by external GNSS data | ° | 0 .. 360 |
| RAZ | Reverse direction (course) from the diver to the position provided by external GNSS data | ° | 0 .. 360 |

The most important parameters here are **AZM**, **DST** and **RAZ**: the azimuth and distance tell the operator where a particular diver is located relative to them. The operator can relay the **RAZ** parameter to the diver via voice communication so that the diver can home in by following that course.

Use the buttons on panel (10) to toggle the display of individual parameters. Parameters describing the relative position of the diver and the surface point (range, forward and reverse course) can only be determined when an external navigation data source is available: either an external GNSS receiver provides the system with the position of the surface diver tracking point, or the **Base 1 as AUX GNSS Source** setting is enabled, in which case all parameters are determined relative to buoy No. 1.

#### 2.2.8. Legend field

- 8 - The legend field is displayed in the upper right corner of the map field. It lists the tracks with examples of their points.

#### 2.2.9. Scale bar

- 9 - The scale bar is displayed in the lower right corner of the map field and shows the map scale in meters.

#### 2.2.10. Panel of switches for displayed diver parameters

- 10 - The panel of switches for displayed diver parameters is located below the diver list and toggles the visibility of parameters in the list:
  - The **DST** button shows/hides the distance to the diver. Changes to this button's state are automatically saved and reproduced during log playback.
  - The **AZM** button shows/hides the direction **to** the diver. Changes to this button's state are automatically saved and reproduced during log playback.
  - The **RAZ** button shows/hides the direction **from** the diver to the position provided by the external GNSS receiver. Changes to this button's state are automatically saved and reproduced during log playback.
  - The **LOC** button shows/hides the diver's location (latitude and longitude). Changes to this button's state are automatically saved and reproduced during log playback.
  - The **RER** button shows/hides the radial error - the value of the residual function at the end of solving the diver positioning problem. Changes to this button's state are automatically saved and reproduced during log playback.
  - The **DOP** button shows/hides the **DOP** and **TBA** parameters.

#### 2.2.11. Status line

- 11 - The status line displays the status of the ports for the radio modem and the external navigation data source (external GNSS receiver), and the name of the last saved screenshot or Zip archive containing the log files.

<div style="page-break-after: always;"></div>

[Back to contents](#contents)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RWLT/uTrackDiver_Users_Manual_ru.md commit=9be58e1dd04a9dd18922aadc7ef61b7e4e52ef8e date=2024-04-18 -->
