
[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **uNav application: User’s manual**

> ℹ This document can be printed directly from your browser.
> For best results:
> - select the range of pages to print, excluding the first and last
> - in advanced settings, disable footers and headers

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/ucnl/ucnl.github.io/assets/24439946/18be12da-eb07-440f-83cd-7f0a4c019fa8) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uNav application <br/> User's manual** |

# 💧 uNav application <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)
- [2. Application interface and functions](#2-application-interface-and-functions)
  - [2.1. Application Settings](#21-application-settings)
    - [2.1.1. Tab 🧪 PHYSICS](#211-tab--physics)
    - [2.1.2. ❗ CONNECTION tab](#212--connection-tab)
    - [2.1.3. Tab 🛸 EXTRA](#213-tab--extra)
- [2.2. Main application window](#22-main-application-window)
    - [2.2.1. Main toolbar](#221-main-toolbar)
    - [2.2.2. Map Toolbar](#222-map-toolbar)
    - [2.2.3. Map panel](#223-map-panel)
    - [2.2.4. Additional information panel](#224-additional-information-panel)
    - [2.2.5. Log panel](#225-log-panel)
    - [2.2.6. Additional panel No. 1](#226-additional-panel-no-1)
    - [2.2.7. Additional panel No. 2](#227-additional-panel-no-2)
    - [2.2.8. Status line](#228-status-line)
    - [2.2.9. Legend field](#229-legend-field)
    - [2.2.10. Scale bar](#2210-scale-bar)

<div style="page-break-after: always;"></div>

## 1. Introduction

The navigation solver [uNav RF Dongle](RWLT_RF_Dongle_Specification_en.md) transmits the calculated position of the pinger, including emulating standard (RMC, GGA) messages of the NMEA0183 protocol used in GNSS receivers. Therefore, after configuration, if necessary, the device can connect to any geoinformation system that supports connection via the serial port of a standard GNSS receiver: GoogleEarth, SAS.Planet, etc.

To configure the device using a [specialized protocol](uNav_protocol_specification_en.md) or to obtain an extended set of data, which includes, for example, buoy positions, pinger position relative to the reference point, data from the built-in GNSS solver, etc. you can use the application [💧 uNav](https://github.com/ucnl/uNav/releases/download/1.0/uNav.zip).

The application also allows the user to transfer data from the solver via a serial connection or via the UDP protocol.

To work, download the necessary software. No installation is required - just unzip the contents of the archive to a location convenient for you.

The application runs on the .NET Framework and is compatible with Windows OS versions 10 and higher.

## 2. Application interface and functions

### 2.1. Application Settings

The application settings editor is available via the **SETTINGS** button in the main application menu. Settings are grouped into tabs:

- **🧪 PHYSICS** - basic settings related to the physical parameters of the environment and algorithm settings in the navigation solver [uNav](RWLT_RF_Dongle_Specification_en.md)
- **❗ CONNECTION** - connection parameters settings
- **🛸 EXTRA** - additional settings related to the display of tracks, map background and specific system parameters

In addition to the tabs, the settings editor has three buttons:

- **SET DEFAULTS** - reset to default settings
- **OK** - Save changes and close the settings editor
- **CANCEL** - Close the settings editor without saving changes
- 
#### 2.1.1. Tab 🧪 PHYSICS

The appearance of the tab controls is shown in the figure below:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/f7f3f344-ae2d-4b7c-9520-1e7b3510fe60) |
| **🧪PHYSICS** tab of the settings editor |

- **Salinity, PSU** - field for entering water salinity. Salinity is required to accurately calculate the speed of sound, as well as to recalculate the pressure transmitted by the pinger to depth. When **Auto** is checked, the application will try to find salinity from the geographic location database. The auto salinity detection function is recommended to be used only for seas, oceans and large bodies of water. Do not use this function when working in small inland bodies of water such as rivers, lakes, ponds, etc. Salinity can also be found manually in the database by clicking on the appropriate link **🔎**.
- **Water temperature, °C** - field for entering water temperature. This parameter is used only when working with the [WAYU](documentation/EN/WAYU/WAYU_DataBrief_en.md) system, where the pinger does not have a built-in temperature sensor.
- **Speed of sound, m/s** - if you have a directly measured sound speed value, enter its value in this input field. In other cases, it is recommended to check the **Auto** checkbox on the right - the speed of sound will be calculated automatically based on data on salinity, depth and temperature.
- **Target max speed, m/s** - The maximum possible speed of movement of the positioned object. This parameter affects the operation of the device's internal filter. In most cases it is recommended to leave the default value: 1 m/s
- **S-Filter range threshold, m** - The distance between adjacent measurements of the location of the positioned object, at which the smoothing filter will be reset.
- **S-Filter FIFO size** - size of the smoothing filter queue. It is not recommended to change this value.
- **DH-Filter range threshold, m** - threshold of the classifier filter. It is not recommended to change this value.
- **DH-Filter FIFO size** - queue size of the classifier filter. It is not recommended to change this value.
- **Course estimation by, points** - The number of consecutive positions of the positioned object by which the course of its movement will be determined.

#### 2.1.2. ❗ CONNECTION tab

The figure below shows the tab view:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/07f5ed71-8b2c-41c8-a671-22d93d249325) |
| **❗CONNECTION** tab of the settings editor |

- **Input port baudrate** - connection speed to the device [uNav](RWLT_RF_Dongle_Specification_en.md).
- **Serial bypass port baudrate** - speed of the output port through which the application can transmit data received from the device.
  
#### 2.1.3. Tab 🛸 EXTRA

The appearance of the tab controls is shown in the figure below:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/fe2dcc3a-aa2b-47e2-a1fd-4614920745fc) |
| **🛸 EXTRA** tab of the settings editor |

- **Number if track points to show** - This input field specifies the maximum number of track points to display.
- **Tile size, px** - sets the size of map tiles in pixels. This parameter depends on the tile server.
- **Tile servers** - list of tile server addresses for downloading map tiles.
- **Enable tile download** - when checked, the application will try to download the necessary tiles from the specified servers.
- **RWLT Mode** - This parameter determines the operating mode of the system [RWLT](RWLT_DataBrief_en.md): working with a pinger or with diving telephone stations [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_EN_Specification_ru.html). It is not recommended to change this parameter without consulting the manufacturer.
- **RWLT Pinger depth rating** - Determines the maximum depth for which the pinger is designed. It is not recommended to change this parameter without consulting the manufacturer.
  
### 2.2. Main application window

The general view of the main application window is shown in the figure below:

| |
| :---: |
| ![uNavHost](https://github.com/ucnl/ucnl.github.io/assets/24439946/7afe4416-785e-42cf-9172-752c4e4e0b06) |
| Main application window |
| _1 - Main toolbar, 2 - Map toolbar, 3 - Map panel, 4 - Additional information panel 5 - Log panel, 6 - Additional panel No. 1, 7 - Additional panel No. 2, 8 - Status line, 9 - Legend field , 10 - Scale bar_ |

#### 2.2.1. Main toolbar

This part contains basic controls for the application's state, as well as commands for managing settings, log files, tracks, and device information.

##### **📡 LINK** (Ctrl + L)
Button to open/close connection with the device. If the connection is active, i.e. button is pressed, the application will try to establish a connection with the **uNav** device via the serial port, trying all the serial ports in the system. The connection status is displayed in the status bar.

##### **⚙ SETTINGS** (Ctrl + O)
Button for calling the settings editor. Inactive when connected or when playing a log file.

##### **📖 LOG**
Contains a set of functions for working with log files.
###### **👀 Open current...** (Ctrl + H)
Opens the current log in the application designated for working with files with the log extension (usually notepad)
###### **▶ Playback...**
This function is designed to play back a log file. During the playback process, the application will repeat all the work that was recorded in the log file, respecting the time intervals. If the log file is already playing, then this line looks like this: **⏹ Stop playback**
###### **🧹 Clear empty entries**
The procedure for deleting all log files that are less than 2 KB in size, as well as empty folders.
###### **🗜 Archive all entries...**
Archiving all log files. After creating the archive, a link to it will appear in [status line (8)](#228-status-line).
###### **🗑 Delete all entries**
Deletes all contents of the LOG folder.
###### **🧹+🗜+🗑 Do them all**
Consistently performs the previous three steps: deletes log files with a size of less than 2 kb, places the rest in an archive, deletes all the contents of the LOG folder.

##### **🛠 UTILS**
Contains additional features.
###### **🛈 View device info**
View information about the device: name, firmware version, serial number.

##### **ℹ INFO**
Button for opening a window with information about the application.

#### 2.2.2. Map Toolbar

##### ✔ (Ctrl + M) - Mark current location
Saves the last calculated position of an object into a separate track (Marked). This function allows you to mark the current point on the motion track.
##### 📌 - Show/Hide marked points
Enables/disables the display of marked points on the map.
##### 🚨 - Show/Hide base points
Enables/disables display of buoy tracks.
##### 📜 - Show/Hide log
Enables/disables display of the log panel (5)
##### ⁞ - Show/Hide legend
Enables/disables display of the legend field (9)
##### 📑 - Show/Hide notes
Enables/disables display of comments
##### 👽 - Show/Hide extra info
Enables/disables display of additional information field (4)
##### ❌ - Reset view
Clears the displayed tracks. This action will not affect the recorded tracks or the log file.
##### 🎯 - Accuracy measurement utils
Contains functions for statistically assessing the accuracy of the system. These functions can only be activated when the positioned object is stationary in the water column (for example, standing on the bottom). Otherwise it will lead to incorrect calculation.
As statistical parameters, the following values are calculated: CEP (Circular Error Probable) - the radius of the circle in which with **50%** probability the next measurement of the object's location should be expected, and DRMS (Distance Root Mean Square), 2DRMS, 3DRMS, corresponding to the radii of the circle, where to expect the next location measurement with 65%, 95% and 98% probability, respectively.

The calculation proceeds as follows. After activating the function, each new calculated location of the positioned object is placed in a buffer for which the standard deviations 𝜎<sub>x</sub> and 𝜎<sub>y</sub> are calculated along the X (longitude) and Y (latitude) axes, respectively .

CEP = 0.62 · 𝜎<sub>y</sub> + 0.56 · 𝜎<sub>x</sub>
DRMS = √(𝜎<sub>x</sub><sup>2</sup> + 𝜎<sub>y</sub><sup>2</sup>)

###### ⏺ Start/⏹ Stop - Start/Stop accuracy estimation
Start or stop the accumulation of statistical data (CEP, DRMS).
###### ⏪ Reset - Reset accuracy test
Clears the set of measurements for which CEP and DRMS are calculated.
##### 🧭 - Reference point
Drop-down list allowing you to select a reference point. The course to this point from the positioned object, the course from this point to the positioned object and the distance between them will be calculated. The GNSS built into the uNav solver, one of four buoys, or a user-defined point can be selected as a reference point.
##### 🡹 (Ctrl + F) - Enable/Disable following target
Enables/Disables centering the map relative to the current position of the positioned object.
##### 🗺 - Enable/Disable tiles
Enables/disables the display of map tiles. Tiles will only be displayed when available.
##### 🡻 (Ctrl + D) - Set target depth
Allows you to directly specify the depth of the positioned object, if it is known. The function is used for the WAYU system, where the pinger does not have a built-in depth sensor.
##### 🌡 (Ctrl + T) - Set water temperature
Allows you to set the water temperature without going to settings (and without restarting the application). This function is used for the [WAYU](documentation/EN/WAYU/WAYU_DataBrief_en.md) system, where the pinger does not have a built-in temperature sensor.

#### 2.2.3. Map panel
The map panel is used to display tracks of movement of objects:
- calculated position of the positioned object
- buoy positions
- GNSS receiver built into uNav
- saved (marked) positions

The length of the track of the positioned object, i.e. the maximum number of points that make up a track is set in the application settings, on the **🛸 EXTRA** tab in the **Number if track points to show** field.

The map panel also contains:
- additional information panel (4)
- journal panel (5)
- legend field (9)
- scale ruler (10)

#### 2.2.4. Additional information panel
The display of this element is switched by the **👽** button on the [map toolbar (2)](#222-map-toolbar). This panel displays various system parameters in text form. To the right of each value you can see how long ago that value was updated.
For clarity, all possible parameters are summarized in the tables below.

Title **TGT - TarGeT**

| ID | Description |
| :--- | :--- |
| LAT | Geographic latitude of the object in °, negative values for the southern hemisphere |
| LON | Geographical longitude of the object in °, negative values for the Western Hemisphere |
| RER | Radial error in m |
| CRS | Heading in °, ranging from 0 to 360, clockwise from north |
| DPT | Depth of the positioned object in m. |
| LEC | Last error code received from the positioned object |
| RTM | Temperature in °C, according to pinger (RWLT pinger only) |
| RPR | Pressure in mBar, according to pinger (RWLT pinger only) |
| RBT | Pinger supply voltage in V, according to pinger data (RWLT pinger only) |

Heading **REF - REFerence point**

| ID | Description |
| :--- | :--- |
| REF | Reference point type |
| DST | Distance between the positioned object and the reference point in m |
| AZM | Azimuth - direction from the positioned object to the reference point in °, in the range from 0 to 360, clockwise from the north direction |
| RAZ | Back azimuth - the direction of the reference point to the positioned object in °, in the range from 0 to 360, clockwise from the direction north |

Header **GNSS - data from built-in GNSS receiver**

| ID | Description |
| :--- | :--- |
| LAT | Geographic latitude of the object in °, negative values for the southern hemisphere |
| LON | Geographical longitude of the object in °, negative values for the Western Hemisphere |
| CRS | Heading in °, ranging from 0 to 360, clockwise from north |
| SPD | Travel speed, m/s and km/h |

#### 2.2.5. Log panel
The display of this element is switched by the **📜** button on the [map toolbar (2)](#222-map-toolbar). This element displays the last few lines of the application log: data exchange with the device, errors that occur, etc.

#### 2.2.6. Additional panel No. 1
The panel contains controls for output ports and buttons for zooming in and out of the map display.
The **Serial bypass** button enables or disables the connection via the serial port, selected from the drop-down list to the right of the button. All data received by the application from the device is transmitted to this port. The **🔄** button to the right of the drop-down list with port names is used to update the list of ports.
The **UDP bypass** button is used to enable or disable transmission via the UDP protocol to the address indicated to the right of the button.
In both cases, the entire data stream received by the application from the device is transmitted to the output ports.

The **🔍➖** (Ctrl -) and **🔍➕** (Ctrl +) buttons are designed to increase (zoom out) and decrease (zoom in) the map scale, respectively.

#### 2.2.7. Additional panel No. 2
The input field on the left side of the panel is intended for creating records while working: the user can quickly type explanatory text and press **Enter**, after which the comment will appear at the top of the map field and will be saved to the current log file. When playing the log, this comment will also be displayed at the appropriate time.

The **📸** button (Ctrl + P) allows you to take a snapshot of the application window and save it in the SNAPSHOTS subfolder in the application root folder. After saving the snapshot, a link to it will appear in [status line (8)](#228-status-line).

The **🎞** button is designed to start and stop automatic saving of snapshots of the main application window with a period of 1 second. The snapshots will be saved to the AUTOSNAPSHOTS subfolder in the application root folder.

#### 2.2.8. Status line
The left side of the status bar displays the connection status. The middle section displays links to the last screenshot you saved or the log archive you created.

#### 2.2.9. Legend field
A list of tracks with sample markers that correspond to them is displayed here. You can turn on or off the display of the legend field using the **⁞** button on the [map toolbar (2)](#222-map-toolbar).

#### 2.2.10. Scale bar
The vertical ruler is used to display the map scale. The upper part of it shows the level (Z) of the scale and the size of the ruler in meters on the map.

If necessary, the user can take measurements between arbitrary points on the map using the right mouse button: to mark the starting point, press and release the right mouse button. After this, the tape measure will be displayed with the specified starting point. Clicking the right mouse button again will set the end point of the measurement. A subsequent right-click will reset the measurement.

The measurement is also reset when the map center is moved, so before taking a measurement, you must disable automatic centering of the map relative to the current position of the positioned object, if it is enabled.
The **🡹** (Ctrl + F) button on the [map toolbar (2)](#222-map-toolbar) is used to turn on/off automatic map centering.

[Back to contents](#contents)

<div style="page-break-after: always;"></div>
