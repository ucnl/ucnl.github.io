[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **uGPSHub: User's manual**

> ℹ This document can be printed directly from your browser. 
> For best results:
> - select the range of pages to print, excluding the first and the last
> - in the advanced settings, disable the footers and headers

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/632ccb76-3d24-48f0-adad-b53ccf7d6d7e) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **⚓ uGPSHub** <br/> Application for working with RedNode navigation receivers <br/> User's manual |

# ⚓ uGPSHub <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
- [2. Application interface and functions](#2-application-interface-and-functions)
  - [2.1. Application settings](#21-application-settings)
    - [2.1.1. Connection tab](#211-connection-tab)
    - [2.1.2. Physics tab](#212-physics-tab)
    - [2.1.3. Misc tab](#213-misc-tab)
  - [2.2. Main application window](#22-main-application-window)
    - [2.2.1. Main toolbar](#221-main-toolbar)
    - [2.2.2. Map toolbar](#222-map-toolbar)
    - [2.2.3. Map panel](#223-map-panel)
    - [2.2.4. Additional information panel](#224-additional-information-panel)
    - [2.2.5. Legend field](#225-legend-field)
    - [2.2.6. Scale bar](#226-scale-bar)
    - [2.2.7. Additional panel](#227-additional-panel)
    - [2.2.8. Status line](#228-status-line)
    - [2.2.9. Log panel](#229-log-panel)

<div style="page-break-after: always;"></div>

## 1. Introduction

The [RedNode](/documentation/EN/RedWAVE/RedNODE_Specification_en.html) navigation receivers of the **"underwater GPS"** system [RedWave](https://docs.unavlab.com/navigation_and_tracking_systems_en#redwave) transmit their own calculated geographical position, including by emulating the standard (**RMC, GGA**) sentences of the **NMEA0183** protocol used in GNSS receivers. Therefore, after configuration, if one is required, the device can be connected to any geographic information system that supports connecting a standard GNSS receiver via a serial port: **GoogleEarth**, **SAS.Planet**, etc.

This application can be used to obtain an extended set of data that includes, for example, the buoy positions, the state of their built-in power supplies, etc.
The application also allows the data from the navigation receiver to be passed through unchanged via a serial connection or via the UDP protocol.

To work with the application, download the required software. No installation is required - just unpack the contents of the archive to a location convenient for you.

The application runs on the **.NET Framework** and is compatible with Windows OS version 10 and higher.

## 2. Application interface and functions

### 2.1. Application settings

The application settings editor is available via the **SETTINGS** button in the main menu of the application. The settings are grouped into tabs:  

- **Connection** - connection parameter settings 
- **Physics** - basic settings related to the physical parameters of the environment and to the algorithm settings
- **Misc** - additional settings related to the display of tracks, the map background and system-specific parameters

In addition to the tabs, the settings editor has three buttons:

- **RESET** - reset to the default settings
- **OK** - Save the changes and close the settings editor
- **CANCEL** - Close the settings editor without saving the changes

#### 2.1.1. Connection tab

The appearance of the tab controls is shown in the figure below:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/0f1d417f-e093-45aa-a87a-83cad4ae88bc) |
| **CONNECTION** tab of the settings editor |

The tab is organized as a table in which the following parameters can be set:

- **UGPS Receiver baudrate** - port speed for connecting to the [RedNode](/documentation/EN/RedWAVE/RedNODE_Specification_en.html) navigation receiver
- **Serial AUX GNSS baudrate** - port speed for connecting to an additional external GNSS receiver. The element is active only when the "Enable" checkbox next to it is checked.
- **Serial output baudrate** and **Serial output port name** - active only when the **Enable** checkbox next to them is checked; they allow setting the speed and the name of the port for data output.
- **UDP output IP Address** and **Port number** - active only when the **Enable** checkbox next to them is checked; they allow setting the UDP connection parameters for data output.

#### 2.1.2. Physics tab

The figure below shows the appearance of the tab:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/44e8c956-4c16-4f83-ae49-69c95a1a550e) |
| **Physics** tab of the settings editor |

- **Salinity, PSU** - field for entering the water salinity. The salinity is required for accurate calculation of the speed of sound, as well as for converting the pressure transmitted by the pinger into depth. When the **Auto** checkbox is checked, the application will try to find the salinity in a database by the geographic position. It is recommended to use the salinity auto-detection function only for seas, oceans and large bodies of water. Do not use this function when working in small inland bodies of water such as rivers, lakes, ponds, etc. The salinity can also be looked up in the database manually by clicking the corresponding link **🔎**.
- **Speed of sound, m/s** - if you have a directly measured value of the speed of sound, enter it in this input field. In other cases it is recommended to check the **Auto** checkbox on the right - the speed of sound will be calculated automatically from the salinity, depth and temperature data.
- **Radial error threshold, m** - The maximum value of the residual function at which the calculated position is considered valid.
- **Course estimator FIFO size** - The number of consecutive positions of the positioned object from which the course of its movement will be determined. 
- **Track filter distance threshold, m** - The distance between adjacent location measurements of the positioned object at which the smoothing filter will be reset.
- **Track filter FIFO size** - size of the smoothing filter queue. It is not recommended to change this value.


#### 2.1.3. Misc tab

The appearance of the tab controls is shown in the figure below:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/1d3599af-9610-4895-8937-dcb35e90e87f) |
| **Misc** tab of the settings editor |

- **Number of track points to show** - This input field sets the maximum number of track points to display.
- **Screenshots names by time** - if the checkbox is checked, screenshots are named after the current system time, otherwise by an incrementing number.
- **Enable tile download** - when the checkbox is checked, the application will try to download the necessary tiles from the specified servers. 
- **Tile size, px** - sets the size of the map tiles in pixels. This parameter depends on the tile server.
- **Tile servers** - list of tile server addresses for downloading the map tiles.

### 2.2. Main application window

The general view of the main application window is shown in the figure below:

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/ca5bdc34-5481-4ee0-b6ff-eb53200afde0) |
| Main application window |
| _1 - Main toolbar, 2 - Map toolbar, 3 - Map panel, 4 - Additional information panel, 5 - Legend field, 6 - Scale bar, 7 - Additional panel, 8 - Status line, 9 - Log panel_ |

#### 2.2.1. Main toolbar

This part contains the main controls of the application state, as well as the commands for managing the settings, log files, tracks and device information.

#### **🔌 LINK** (Ctrl + L) 
Button for opening/closing the connection with the device. If the connection is active, i.e. the button is pressed, the application will try to establish a connection with the **RedNode** device via a serial port, trying all the serial ports in the system. The connection state is displayed in the status line.

#### **⚙ SETTINGS** (Ctrl + O) 
Button for opening the settings editor. Inactive when the connection is established or while a log file is being played back.

#### **📖 LOG**
Contains a set of functions for working with log files.
##### **👀 View current...** (Ctrl + H)
Opens the current log in the application assigned to files with the log extension (usually Notepad)
##### **▶ Playback...**
This function is intended for playing back a log file. During playback, the application repeats all the work that was recorded in the log file, observing the time intervals. If a log file is already being played back, this item looks like this: **⏹ Stop playback**
##### **🧹 Remove empty entries**
The procedure of deleting all log files smaller than 2 KB, as well as empty folders.
##### **🗜 Archive all**
Placing all log files into an archive. After the archive is created, a link to it will appear in the [status line (8)](#228-status-line).
##### **🗑 Delete all**
Deleting all contents of the LOG folder.
##### **🧹+🗜+🗑 Do them all**
Sequentially performs the previous three items: deletes the log files smaller than 2 KB, places the remainder into an archive, deletes all contents of the LOG folder.

#### **🛠 UTILS**
Contains additional functions.

##### **🗺 TRACKS**
Contains tools for working with tracks.

###### **💾 Export...** (Ctrl + S)
Opens a dialog for saving the tracks to a file, with a choice of format: KML or CSV
###### **🗑 Clear**
Clears all track data. This action cannot be undone.
###### **🥤 Smooth a track...**
Opens a dialog for selecting the file that contains the tracks to be smoothed.

##### **🤖 DEVICE**
Contains tools for working with the device - additional settings or device information.
###### **View device info** (Ctrl + D)
View the device information: serial number, version, firmware version.
###### **Zero depth adjust**
Atmospheric pressure calibration function. The current pressure reading will be taken as zero and, when the depth is calculated from the hydrostatic pressure, will be subtracted from the readings.

#### **ℹ INFO**
Button for opening the window with information about the application.

#### 2.2.2. Map toolbar

#### ✔ (Ctrl + M) - Mark current location
Saves the last calculated position of the object to a separate track (Marked). This function allows marking the current point on the movement track.
#### 📌 - Show/Hide marked points
Enables/disables the display of the marked points on the map.
#### ⛯ - Show/Hide base points
Enables/disables the display of the buoy tracks.
#### 📜 - Show/Hide log
Enables/disables the display of the log panel (9)
#### ⁞ - Show/Hide legend
Enables/disables the display of the legend field (5)
#### 📑 - Show/Hide notes
Enables/disables the display of comments
#### 👽 - Show/Hide extra info
Enables/disables the display of the additional information field (4)
#### ❌ - Reset view
Clears the displayed tracks. This action does not affect the tracks being recorded or the log file.
#### 🎯 - Accuracy measurement utils
Contains functions for the statistical estimation of the system accuracy. These functions can be used only when the positioned object is stationary in the water column (for example, standing on the bottom). Otherwise this will lead to an incorrect calculation.
The calculated statistical parameters are CEP (Circular Error Probable) - the radius of the circle within which the next measurement of the object's location is to be expected with **50%** probability, and DRMS (Distance Root Mean Square), 2DRMS, 3DRMS, which correspond to the radii of the circle within which the next measurement of the location is to be expected with 65%, 95% and 98% probability, respectively.

The calculation proceeds as follows. After the function is activated, each newly calculated location of the positioned object is placed into a buffer, for which the standard deviations 𝜎<sub>x</sub> and 𝜎<sub>y</sub> along the X (longitude) and Y (latitude) axes, respectively, are calculated.

CEP = 0.62 · 𝜎<sub>y</sub> + 0.56 · 𝜎<sub>x</sub>  
DRMS = √(𝜎<sub>x</sub><sup>2</sup> + 𝜎<sub>y</sub><sup>2</sup>)

##### ⏺ Start/⏹ Stop - Start/Stop accuracy estimation
Start or stop the accumulation of statistical data (CEP, DRMS).
##### 🧹 Clear data - Reset accuracy test
Clears the set of measurements for which CEP and DRMS are calculated.

##### 🧭 - Reference point
A drop-down list for selecting the reference point. The course to this point from the positioned object, the course from this point to the positioned object and the distance between them will be calculated. One of the four buoys, a user-defined point, or the position from an externally connected GNSS receiver can be selected as the reference point.
##### 🡹 - Enable/Disable following target 
Enables/disables centering the map on the current position of the positioned object.
##### 🗺 - Enable/Disable tiles
Enables/disables the display of the map tiles. Tiles are displayed only if they are available.


#### 2.2.3. Map panel
The map panel is used to display the movement tracks of objects: 
- the calculated position of the positioned object
- the positions of the buoys
- the position of the external (AUX) GNSS receiver
- saved (marked) positions

The length of the track of the positioned object, i.e. the maximum number of points that make up the track, is set in the application settings, on the **Misc** tab, in the **Number of track points to show** field.

The map panel also contains:
- the additional information panel (4)
- the log panel (9)
- the legend field (5)
- the scale bar (6)

Each track point is displayed as a square marker; the course, if it is known for the given track, is displayed as a line of the same color as the track points.
The scale of the map panel can be changed with the mouse wheel, with the **🔍➖** and **🔍➕** buttons on the additional panel (7), as well as with the hot keys **Ctrl+** and **Ctrl-**.

The map panel is scrolled in the standard way: press the left mouse button and move the mouse without releasing the button. However, if the **🡹** (Follow target) function on the map toolbar (2) is activated, the scrolling is done automatically - the application will automatically place the most recent track point at the center. 

To measure a distance on the map, mark the starting point with the right mouse button, move the pointer to the end point and press the right mouse button once more. Pressing the right mouse button again will reset the measurement. The measurement is also reset when the scale is changed.


#### 2.2.4. Additional information panel
The display of this element is toggled by the **👽** button on the [map toolbar (2)](#222-map-toolbar). This panel displays various system parameters in text form. To the right of each value, the time elapsed since this value was last updated may be displayed.
For clarity, all possible parameters are summarized in the tables below. 

| ID | Description |
| :--- | :--- |
| LAT | Geographic latitude of the object in °, negative values for the southern hemisphere |
| LON | Geographic longitude of the object in °, negative values for the western hemisphere |
| RER | Radial error in m |
| CRS | Course in °, in the range from 0 to 360, clockwise from the north direction |
| DPT | Depth of the positioned object in m. |
|     |      |
| PRS | Pressure in mbar, according to the navigation receiver data |
| TMP | Temperature in °C, according to the navigation receiver data |
|     |      |
| BPN | Reference point type |
| AZM | Azimuth - direction from the positioned object to the reference point in °, in the range from 0 to 360, clockwise from the north direction |
| REV | Back azimuth - direction from the reference point to the positioned object in °, in the range from 0 to 360, clockwise from the north direction |
| DST | Distance between the positioned object and the reference point in m |
|     |      |
| B#1 | Reception quality and state of buoy No. 1 |
| B#2 | Reception quality and state of buoy No. 2 |
| B#3 | Reception quality and state of buoy No. 3 |
| B#4 | Reception quality and state of buoy No. 4 |
|     |      |
| DOP | Dilution Of Precision |
| TBA | Target to base arrangement - the quality of the mutual arrangement of the positioned object and the navigation base |

#### 2.2.5. Legend field
The list of tracks is displayed here, together with the marker samples that correspond to them. The display of the legend field can be switched on or off with the **⁞** button on the [map toolbar (2)](#222-map-toolbar).

#### 2.2.6. Scale bar
The vertical ruler is used to display the map scale. In its upper part it shows the scale level (Z) and the size of the ruler on the map in meters.

If necessary, the user can measure the distance between arbitrary points on the map using the right mouse button: to mark the starting point, press and release the right mouse button. After that, a ruler with the specified starting point will be displayed. Pressing the right mouse button again will set the end point of the measurement. The next press of the right mouse button will reset the measurement.

The measurement is also reset when the center of the map is moved, so before taking a measurement, turn off the automatic centering of the map on the current position of the positioned object, if it is turned on. The automatic centering of the map is turned on/off with the **🡹** (Ctrl + F) button on the [map toolbar (2)](#222-map-toolbar).

#### 2.2.7. Additional panel
The input field in the left part of the panel is intended for creating entries during operation: the user can quickly type an explanatory text and press **Enter**, after which the comment will appear in the upper part of the map field and will be saved to the current log file. When the log is played back, this comment is also displayed at the corresponding time.

The **📸** (Ctrl + P) button allows taking a snapshot of the application window and saving it in the SNAPSHOTS subfolder in the root folder of the application. After the snapshot is saved, a link to it will appear in the [status line (8)](#228-status-line).
The **🔍➖** (Ctrl -) and **🔍➕** (Ctrl +) buttons are intended for increasing (zooming out) and decreasing (zooming in) the map scale, respectively.

#### 2.2.8. Status line
The left part of the status line displays the connection state. The middle part displays the links to the last saved screenshot or to the created log archive.

#### 2.2.9. Log panel
The display of this element is toggled by the **📜** button on the [map toolbar (2)](#222-map-toolbar). This element displays the last few lines of the application log: the data exchange with the device, the errors that occur, etc.

[Back to contents](#contents)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RedWAVE/uGPSHub_Users_manual_ru.md commit=a8bd606b867ae74213b65961d9e138e8b7605e33 date=2025-07-01 -->
