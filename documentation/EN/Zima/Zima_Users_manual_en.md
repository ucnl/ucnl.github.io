[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima USBL: User's manual**

<details>
  <summary><b>ℹ Recommendations for printing / saving as PDF</b></summary>
  <br>
  <ol>
    <li>Press <b>Ctrl+P</b> (macOS: <b>Cmd+P</b>)</li>
    <li>Select <b>"Save as PDF"</b> (Microsoft Print to PDF) as the printer</li>
    <li>In <b>"Pages"</b>, enter a range that excludes the first and the last page</li>
    <li>Disable <b>headers and footers</b> (title, URL, page numbers)</li>
    <li>In <b>Chrome/Edge</b>: More settings → "Margins" → <b>None</b> | in <b>Firefox</b>: "Margins & Header/Footer" → <b>None</b></li>
    <li>Click <b>Print</b> and choose where to save the PDF</li>
  </ol>
</details>

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima USBL** - underwater acoustic navigation system <br/> User's manual |

# Zima USBL <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
- [2. System composition](#2-system-composition)
  - [2.1. Zima-B: Underwater acoustic direction-finding station](#21-zima-b-underwater-acoustic-direction-finding-station)
    - [2.1.1. General information](#211-general-information)
    - [2.1.2. Technical specifications](#212-technical-specifications)
    - [2.1.3 Storage and maintenance](#213-storage-and-maintenance)
  - [2.2. Zima-R: responder-beacon](#22-zima-r-responder-beacon)
    - [2.2.1. General information](#221-general-information)
    - [2.2.2. Technical specifications](#222-technical-specifications)
    - [2.2.3. Configuration options](#223-configuration-options)
    - [2.2.4. Working with the device (standalone version)](#224-working-with-the-device-standalone-version)
    - [2.2.5. Working with the device (integrated version)](#225-working-with-the-device-integrated-version)
    - [2.2.6. Storage and maintenance](#226-storage-and-maintenance)
- [3. ZHost host software](#3-zhost-host-software)
  - [3.1. System requirements](#31-system-requirements)
  - [3.2. Description of the ZHost software interface](#32-description-of-the-zhost-software-interface)
    - [3.2.1 Toolbar](#321-toolbar)
      - [3.2.1.1. CONNECTION menu item](#3211-connection-menu-item)
      - [3.2.1.2. STATION menu item](#3212-station-menu-item)
      - [3.2.1.3. RESPONDER menu item](#3213-responder-menu-item)
      - [3.2.1.4. LOG menu item](#3214-log-menu-item)
      - [3.2.1.5. TRACK menu item](#3215-track-menu-item)
      - [3.2.1.6. SETTINGS menu item](#3216-settings-menu-item)
      - [3.2.1.7. AUTOQUERY menu item](#3217-autoquery-menu-item)
      - [3.2.1.8. AUTOSNAPSHOT menu item](#3218-autosnapshot-menu-item)
    - [3.2.2 PPI panel](#322-ppi-panel)
    - [3.2.3 RESPONDERS panel](#323-responders-panel)
    - [3.2.3 Status panel](#323-status-panel)
- [4. Effective use of the Zima USBL navigation system](#4-effective-use-of-the-zima-usbl-navigation-system)
- [5. Troubleshooting](#5-troubleshooting)
- [6. Obligations and disclaimer](#6-obligations-and-disclaimer)
  - [6.1. Terms of replacement and free warranty service](#61-terms-of-replacement-and-free-warranty-service)
  - [6.2. Limitation of the manufacturer's liability](#62-limitation-of-the-manufacturers-liability)

<div style="page-break-after: always;"></div>

## 1. Introduction
The underwater acoustic navigation system **Zima** is designed to determine, in real time, the horizontal angle and the distance
to underwater objects equipped with underwater acoustic responder-beacons [Zima-R](Zima_R_Specification_en.md). The responder-beacons
(hereinafter, beacons) can be installed on remotely operated underwater vehicles (ROVs), human-occupied vehicles (HOVs), autonomous
unmanned underwater vehicles (AUVs), as well as on recreational and technical divers (when the standalone version of the beacon is used).

The **Zima** navigation system is an ultra-short baseline (USBL) navigation system whose principle of operation is based
on the use of a phased antenna array to determine the horizontal angle of arrival of the signal and on determining the distance to the beacon by the "request-response" method.
A distinctive feature of this system is the so-called two-way navigation, a patented solution that makes it possible to determine
the distance mutually, both at the base station and at the beacon, and also to transmit to the beacon the azimuth angle to the base station.
The system also makes it possible to transmit remote control signals to the beacons and to receive telemetry data from the beacons.

<div style="page-break-after: always;"></div>

## 2. System composition
### 2.1. Zima-B: Underwater acoustic direction-finding station
#### 2.1.1. General information
The underwater acoustic direction-finding station [Zima-B](Zima_B_Specification_en.md) (hereinafter, the base station) is designed to transmit control acoustic signals to the beacons, to determine the signal propagation time to the beacons, to determine the horizontal angle of arrival of the beacons' response signals, to transmit remote control commands and to receive telemetry information from the beacons by means of specialized underwater acoustic signals.

| ![Zima-B](/documentation/def_zima_b_ant.png) |
| :---: |
| **Figure 1 - Base station [Zima-B](Zima_B_Specification_en.md)** | 
| _external view_ |

The base station is designed as a maintenance-free monoblock on a cable, potted in a high-strength polyurethane compound. The station has a phased antenna array, a transmitting antenna and a built-in depth/temperature sensor. As an additional option, the base station is supplied with a heading and position determination system. In the general case, the base station is mounted on a rigid vertical pole, taking into account the directivity of the antenna - the determined angles of arrival are given in the antenna coordinate system.

| ![Zima-B placement](/documentation/zima_boat_placement.png) |
| :---: |
| **Figure 2 - Installation diagram of the [Zima-B](Zima_B_Specification_en.md) antenna** |
| _1-pole, 2-vessel, 3-water surface, 4-cable, 5-antenna [Zima-B](Zima_B_Specification_en.md), 6-zero direction of the antenna_ |

Figure 3 shows the dimensional drawing of the base station [Zima-B](Zima_B_Specification_en.md).
The base station has a cable entry for the cable of the power and data interface and an opening for the pressure/temperature sensor. Structurally, the base station is divided into the following parts: the cable entry (in the upper part of the station) and a mounting groove for securing the station with a clamp. Below is the cylindrical surface of the transmitting piezoelectric element, under which the receiving phased antenna array is located. During installation, the surfaces of the transmitting element and of the receiving array must not be covered or shielded. 
For correct operation of the station, a direct line of sight is required between the working surfaces of the station and the transducer of the responder-beacon.

| ![Zima-B drawings](/documentation/Zima_B_drawings.png) |
| :---: |
| **Figure 3 - [Zima-B](Zima_B_Specification_en.md)** |
|  _dimensional drawing_ |

In the standard configuration, [Zima-B](Zima_B_Specification_en.md) is supplied with a UART<->RS-422 interface converter and a cable
10 meters long, which is connected to the power supply and switching unit [Bat&Link Box](Bat_n_link_box_Specification_en.md). Thus,
through the switching unit, the station is connected to the host PC via the USB interface (serial port).

#### 2.1.2. Technical specifications

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 128 mm |
| WEIGHT (dry)<sup>[1](#footnote2121)</sup> | 0.44 kg |
| MAXIMUM DEPTH | 40 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAXIMUM COMMUNICATION RANGE | 3000 m |
| NOMINAL HORIZONTAL ANGLE OF ARRIVAL ACCURACY<sup>[2](#footnote2122)</sup> | 1° |
| MAXIMUM DEVICE TILT RELATIVE TO THE VERTICAL COMPENSATED BY THE BUILT-IN INCLINOMETER (ROLL/PITCH) | +/- 30° |
| OPERATING CONE (RELATIVE TO THE HORIZONTAL)<sup>[2](#footnote2122)</sup> | +/-30° |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°C |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2122)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| BATTERY LIFE<sup>[3](#footnote2123)</sup> WHEN SUPPLIED FROM [BAT&LINK BOX](Bat_n_link_box_Specification_en.md) | 8 h |
| INTERFACE | USB (COM) 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote2124)</sup> | 10 m |
| MULTIPLE ACCESS SCHEME (COMMANDS/SUBSCRIBERS) | 32/23 |
  
________________
<a name="footnote2121"><sup>1</sup></a> Excluding the weight of the converter and cable.  
<a name="footnote2122"><sup>2</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
<a name="footnote2123"><sup>3</sup></a> With the station operating at 1 request per 3 seconds.  
<a name="footnote2124"><sup>4</sup></a> Including the interface converter and extension cable up to the [Bat&Link Box](Bat_n_link_box_Specification_en.md) device. Optionally, the length can be increased up to 20 m.  

#### 2.1.3 Storage and maintenance

There are no special storage and maintenance requirements for the base station, with the exception of the following:
- When used in salt and/or heavily polluted water, desalination (soaking and rinsing in fresh water) is necessary
- The use of any organic solvents, strong acids, alkalis and other aggressive substances is not allowed
- If necessary, washing in household soap solutions is possible, avoiding liquid getting on the connector
- Impact or significant static loads are not allowed
- Strong bending of the cable (with a radius of less than 5 cm) is not allowed


### 2.2. Zima-R: responder-beacon
#### 2.2.1. General information
The responder-beacon is designed as a maintenance-free monoblock on a cable, potted in a high-strength polyurethane compound. The appearance of the responder-beacon [Zima-R](Zima_R_Specification_en.md) is shown in Figure 4. Structurally, the beacon includes a cable entry, a mounting groove, a pressure sensor opening and a working surface. The pressure sensor opening and the working surfaces (the cylinder and the end face of the cylinder opposite the cable entry) must not be covered or shielded. For correct operation of acoustic communication, a direct line of sight is required between the base station and the responder-beacon.

| ![Zima-R](/documentation/zima_r.png) |
| :---: |
| **Figure 4 - [Zima-R](Zima_R_Specification_en.md)** |
|  _external view (standalone version)_ |

#### 2.2.2. Technical specifications

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry)<sup>[1](#footnote2221)</sup> | 0.3 kg |
| MAXIMUM DEPTH | 300 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAXIMUM COMMUNICATION RANGE | 3000 m |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°C |
| SUPPLY VOLTAGE | 5 .. 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2222)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[3](#footnote2223)</sup> | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[3](#footnote2223)</sup> | 0.5 m |
| MULTIPLE ACCESS SCHEME (COMMANDS/SUBSCRIBERS) | 32/23 |
| NOMINAL HORIZONTAL ANGLE DETERMINATION ACCURACY<sup>[4](#footnote2224)</sup> | 1° |
| NOMINAL DISTANCE DETERMINATION ACCURACY<sup>[4](#footnote2224)</sup> | 0.3 m |

##### Additional parameters of the battery canister<sup>[5](#footnote2225)</sup>

| PARAMETER | VALUE |
| :--- | :--- |
| BUILT-IN BATTERY TYPE | Ni-MH |
| ELECTRICAL CAPACITY | 2.9 A·h |
| NOMINAL VOLTAGE | 12 V |
| NUMBER OF CELLS IN THE PACK | 10 pcs |
| HOUSING MATERIAL | Delrin |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |

________________
<a name="footnote2221"><sup>1</sup></a> Excluding the weight of the battery pack. Standard battery pack Ø50x165 mm, 0.58 kg, 2.9 A·h 12 V. 
Operating time with the standard battery pack in standby mode - up to 70 hours, with 1 transmission every 3 seconds - up to 8 hours.  
<a name="footnote2222"><sup>2</sup></a> The value was obtained without taking into account the multipath propagation effect.  
<a name="footnote2223"><sup>3</sup></a> The value can be changed on request.  
<a name="footnote2224"><sup>4</sup></a> Obtained in laboratory conditions in a static experiment.  
<a name="footnote2225"><sup>5</sup></a> Standard delivery set, subject to change without notice.  

#### 2.2.3. Configuration options
The beacon [Zima-R](Zima_R_Specification_en.md) is a transceiver for underwater acoustic digital wideband communication and can be interfaced with the control system for both power and data. In this case, if the control system has a magnetic compass, it is possible to determine the distance and the relative bearing to the base station, as well as to receive remote control code commands from the base station.
In the standalone version, the beacon is supplied with a battery canister, as shown in Figure 4. In this case it is fully autonomous and does not need to be interfaced with the carrier.
In the [OEM](Zima_R_OEM_Specification_en.md) version, the beacon is supplied as a set of electronic boards to be installed by the user in the user's own 
one-atmosphere (normobaric) housing. The beacon is supplied with a deep-water underwater acoustic transducer. Routing the transducer cable into the one-atmosphere housing 
and connecting it to the beacon electronics is, in this case, done by the user.

#### 2.2.4. Working with the device (standalone version)
In the standalone version, the beacon is fully autonomous. For operation, it must be fixed on the carrier in such a way that the working surfaces of the monoblock (the cylindrical surface and the end face) are not covered by the mounting elements (the special groove must be used for mounting) and are not shielded by various structural elements of the carrier. To switch on the responder-beacon, connect it to the battery pack using the connector, as shown in Figure 5.

| ![Zima-R](/documentation/zima_r_bat_conn.png) |
| :---: |
| **Figure 5 - Connecting the responder-beacon to the battery pack** |

In this version, the beacon is supplied with a 10-cell nickel-metal hydride battery pack. 
The one-atmosphere (normobaric) housing (canister) has a lid with a double seal and a four-start thread, which allows the canister lid to be closed in 3/4 of a turn. Before immersion in water, make sure that the canister lid is screwed on tightly (by hand).
After the beacon connector is connected to the battery pack, the device calibrates the atmospheric pressure during the first ten seconds; therefore, do not apply any pressure (negative or positive) other than atmospheric to it during the first ten seconds after the device is switched on - this will result in incorrect depth measurement by the responder-beacon.
In the standalone version, the Tx and Rx wires of the beacon cable are shorted (see Figure 6). This automatically disables the UART module to save power.

> CAUTION! Zima-R devices in the standalone version manufactured after October 2020 indicate that they are operational by emitting a signal 1 second after power is applied.

| ![Zima-R](/documentation/ZimaR_drawings.png) |
| :---: |
| **Figure 6a - [Zima-R](Zima_R_Specification_en.md)** |
| _dimensional drawing_ |

| ![Zima-R](/documentation/ZimaR_wiring_diagram_en.png) |
| :---: |
| **Figure 6b - [Zima-R](Zima_R_Specification_en.md)** |
| _Cable wire assignment_ |

#### 2.2.5. Working with the device (integrated version)
When interfaced with the carrier for both power and data, the beacon transmits to the carrier the distance to the base station and the azimuth to the beacon (only when a magnetic compass is connected to the base station). In addition, in this case the base station can transmit up to 28 code commands, of which the responder-beacon notifies the carrier in accordance with the [communication protocol](Zima_Protocol_Specification_en.md).

#### 2.2.6. Storage and maintenance
The responder-beacon does not require any special maintenance procedures, except for desalination and rinsing in running fresh water after use in salt and/or contaminated water.
In this case, the use of any lubricants or solvents, aggressive detergents, etc. to remove contamination from the responder-beacon and its cable is not allowed.

If the beacon is used in the standalone version, additional requirements apply and maintenance measures are prescribed for the battery pack and the canister. In particular:
- long-term (more than one day) storage of the battery pack while it is connected to the beacon is not allowed;
- long-term storage of the battery pack without scheduled recharging (1 time per month) is not recommended;
- if contaminated, the O-rings and the thread of the battery canister must be cleaned with water, a soft brush and a soap solution, followed by rinsing in running fresh water and lubricating the O-rings with silicone grease;
- the canister is stored with the lid closed;
- when the device is used in salt and/or contaminated water, it must be desalinated in running fresh water after the work is finished.

<div style="page-break-after: always;"></div>

## 3. ZHost host software

### 3.1. System requirements
The specialized software [ZHost](https://github.com/ucnl/ZHost) (hereinafter, the software) runs under the MS Windows operating system, versions 7, 8 and 10. A monitor with a resolution of at least 1024x768 pixels and a mouse or touchpad are recommended.
The software is portable, is distributed as a [zip archive \(Download the latest version\)](https://github.com/ucnl/ZHost/releases/download/2.2/ZHost.zip) and does not require any installation other than unpacking it on the user's PC. 

The executable file ZHost.exe, the settings file ZHost.settings and the required libraries are located in the root directory of the application. Localization resources are located in subdirectories corresponding to the localization language (e.g. \ru, \ru-RU, etc.).
While running, the application keeps log files. The logs are stored in the \LOG subdirectory, which contains subdirectories named with the current date (for example, \LOG\2020-01-21), which contain .log files with names corresponding to the file creation time (HH-MM-SS). A new log file is created each time the application starts. The log files are in text format and contain all the information exchange of the host software with the devices connected to it, as well as all errors that occur during the operation of the software.

When the AUTOSNAPSHOT function is enabled, screenshots of the application window are saved in the \SNAPSHOTS directory, which also contains subdirectories named with the creation date; the window screenshot files are named with the current time (HH-MM-SS) and are in PNG (Portable Network Graphics) format.

> Since the connection to the base station is made through UART/RS-232/RS-422 to USB interface converters, additional drivers 
> for the specific converter may be required.

### 3.2. Description of the ZHost software interface
The general view of the application window is shown in Figure 7. It consists of a toolbar (menu) located at the top of the window and a status panel located at the bottom of the window; on the left is the screen that displays the relative position of the responder-beacons (PPI), and on the right is a tree structure containing the properties of the beacons in use (RESPONDERS).  
The toolbar consists of an upper subpanel (CONNECTION, STATION, etc.) and a lower subpanel (AUTOQUERY, AUTOSNAPSHOT).

| ![ZHost main window view](/documentation/zhost_screen_gnss_hdg.png) |
| :---: |
| **Figure 7 - [ZHost](https://github.com/ucnl/ZHost) host software** |
| _main window view during operation_ |

#### 3.2.1 Toolbar

##### 3.2.1.1. CONNECTION menu item
The **"CONNECTION"** menu item is used to open and close connections on the configured serial ports. These include the port through 
which information is exchanged with the base station, the AUX ports through which the software can receive (with the appropriate settings) navigation data from a GNSS + GNSS compass or a GNSS + magnetic compass, and also the GNSS emulation port for one of the responder-beacons.

When the **"CONNECTION"** menu item is clicked, the application tries to open connections on the serial ports according to the specified settings.
If no additional navigation data providers (GNSS, compass) are specified and the system operates in relative coordinates, an attempt is made to open the port for communication with the base station. If one or both AUX ports and the GNSS emulation output port are enabled in the settings, the software will try to open them as well.

If the ports are opened successfully, the **"CONNECTION"** menu item becomes highlighted, and clicking it again closes the connections.

##### 3.2.1.2. STATION menu item
The **"STATION"** menu item becomes active only after the connection to the base station is open and the device information has been successfully received from it. The item contains the following subitems:
- **"VIEW INFO"** to open a dialog box containing information about the connected base station (device serial number, firmware version, etc.). 
- **"DEPTH CALIBRATION"** to open the dialog box for setting the actual depth of the base station. 

##### 3.2.1.3. RESPONDER menu item
This menu item becomes active only after the connection to the base station is open and the device information has been successfully received from it, and the **"AUTOQUERY"** function is not active. The item contains the following subitems:
- **"SEND A COMMAND..."** to open the remote command dialog box, in which the user can select the address of the responder-beacon to which a user command is to be sent, and the command identifier.
- **"CHANGE ADDRESS..."** to open the dialog box for changing the address of a remote responder-beacon. In the dialog box, the user must specify the current address of the beacon whose address is to be changed, and the new address. *Be careful when using this function. It is intended only for setting beacon addresses before immersion.*
- **"SET CURRENT DEPTH AS ZERO"** to open the atmospheric pressure calibration dialog box. In the dialog box, the user must specify the address of the beacon. On receiving the command to calibrate the atmospheric pressure, the responder-beacon will take the current pressure readings of its built-in sensor as atmospheric. *Be careful when using this function. It is intended only for setting up beacons before immersion.*

##### 3.2.1.4. LOG menu item
The **"LOG"** menu item contains functions for working with the application log files and contains the following subitems:
- **"VIEW"**. Selecting this subitem opens the current application log file.
- **"ANALYZE..."**. Selecting this subitem displays the dialog for selecting the file to be analyzed. The log file analysis function makes it possible to quickly restore the course of the system's operation, for example, to restore the tracks of the vessel and/or of the responder-beacons in case of its loss.
- **"ANALYZE CURRENT"**. This function acts like the **"ANALYZE..."** function, except that the current log file is selected as the file to be analyzed.
- **"RESTART CURRENT"**. When this subitem is activated, the contents of the current log file are deleted and logging continues.
- **"CLEAR ALL"**. This menu subitem is intended to delete all application logs from the LOG\ directory. *Caution! The data from the log files will be lost irretrievably!*

##### 3.2.1.5. TRACK menu item
The **"TRACK"** menu item contains functions for working with the tracks generated by the software and contains the following subitems:
- **"SAVE AS..."** is used to open the dialog box for selecting the file name and format for saving the tracks. The function becomes active only if there is unsaved geographic data in the system. The software supports exporting tracks to the Keyhole Markup Language (KML) and Comma-separated values (CSV) formats. 
- **"CLEAR"**. This subitem is used to delete all geographic data accumulated by the software during the current session. *Use this function with caution!*

##### 3.2.1.6. SETTINGS menu item
The **"SETTINGS"** menu item is active only when the connection is closed and is used to open the dialog box for changing the software settings. 

The settings are saved in the root directory of the application. Keep in mind that, for the changed and saved settings to be used by the application, it must be restarted. If the settings are saved successfully, the software displays the corresponding prompt to the user.

For convenience, the settings in the dialog box are arranged in groups, each group on a separate tab.
The **"SET DEFAULTS"** button is used to restore the default settings.  
The **"OK"** button, used to accept the settings, is active only when the user has entered consistent data (for example, when the AUX ports are enabled, the names of all enabled ports must not coincide with each other).

The **"CONNECTION"** tab contains the settings of the connection ports. Its appearance is shown in Figure 8.

| ![ZHost settings window view](/documentation/zhost_setts_1.png) |
| :---: |
| **Figure 8 - Settings window** |
| _Tab "CONNECTION"_ |

The **"ZMA Port"** group is always active and is responsible for the settings of the connection to the base station [Zima-B](Zima_B_Specification_en.md). In commercially produced devices, only the speed of 9600 bit/s is supported. 

The other groups, **"AUX1 Port"**, **"AUX2 Port"** and **"Output Port"**, become active only if the corresponding checkbox is selected. 

- If the [Zima USBL](Zima_DataBrief_en.md) system is used with a GNSS receiver with an azimuth determination function, only one of the AUX ports must be used, through which the data from this receiver enter the system

- If the [Zima USBL](Zima_DataBrief_en.md) system is used with a standard GNSS receiver and the direction data are supplied by a magnetic compass, both AUX ports must be used: the GNSS receiver is connected to one of them and the magnetic compass to the other.

If the **"Save AUX input to log"** checkbox is not selected, the data coming from the AUX ports will not be saved to the log file.

If the system operates in absolute coordinates (i.e., it receives data on the geographic location of the base station and its orientation relative to the cardinal directions) and the absolute geographic coordinates of the responder-beacons are calculated, it becomes possible to emulate GNSS **RMC** and **GGA** sentences based on the geographic position of the beacon and transmit them to the output port. 

This can be, for example, a virtual COM port, to the other end of which mapping software (for example, SAS.Planet) can be connected to display the location of the beacon on the map in real time. To enable this function, select the **"Use output port"** checkbox, set the required port settings, and also specify the address of the beacon on the basis of whose coordinates the GNSS data will be emulated. 

If the **"Save separately"** checkbox is selected, the data transmitted to the output port will be saved in a separate log.


The **"COMMON"** tab contains the settings of the addresses of the beacons in use and some physical parameters. Its appearance is shown in Figure 9.

| ![ZHost settings window view](/documentation/zhost_setts_2.png) |
| :---: |
| **Figure 9 - Settings window** |
| _Tab "COMMON"_ |

The **"Responders in use"** group contains the list of all possible beacon addresses. The system will automatically poll the beacons whose addresses are checked in this list. 

The **"Timings"** group contains the settings:
- the data obsolescence threshold (in seconds). If a value has not been updated for longer than the specified time interval, the symbols OBS (Obsolete) are displayed in parentheses next to it, indicating to the operator that this particular parameter (for example, the water temperature or the beacon supply voltage) has not been updated for a long time
- Max distance. This parameter tells the system the maximum distance at which the responder-beacon may be located. This parameter determines how long the base station will wait for a beacon response. If for some reason the station does not receive the response signal of the beacon, it waits for it for a certain time, called the timeout time. It makes sense to set the minimum possible values based on the requirements of the task, in order to limit the idle time of the system while it waits for a missed beacon response.

The **"Salinity"** group makes it possible to set the water salinity value (in PSU) either directly or by selecting it from the world ocean salinity database (by opening the salinity selection dialog via the **". . ."** link). It is not recommended to take the salinity from the database for small inland water bodies: rivers, lakes, ponds, etc. In this case, if the exact value is not known, set the salinity to zero (fresh water).
The salinity value is used by the system for more accurate determination of the depth and of the speed of sound.

The **"Sound speed autocalculation"** checkbox and the corresponding group controlled by it determine where the system takes the speed of sound in water from. If this value is known directly from a measurement, it is worth disabling the automatic calculation function and specifying the value directly. In all other cases the checkbox must be selected. In this case, the system calculates the speed of sound from the pressure, temperature and salinity. As a rule, the calculated value is in good agreement with the actual one.

The **"Misc."** group contains:
- The **"Rough depth (faster)"** checkbox. If this function is enabled, the beacon transmits the depth with a lower resolution (~40 cm), but the depth is transmitted in a single "request-response" transaction, and the simultaneous navigation function (sending to the beacon the reverse azimuth to the base station and measuring by the beacon the distance to the base station) is unavailable. If the simultaneous navigation function is not required (for example, if the beacon is used in the standalone version) and an accuracy of 40 cm in depth is sufficient, select this checkbox.
- The **"Antenna heading is fixed"** checkbox is intended for the situation when the system operates in relative coordinates and the base station is fixed motionless (for example, on a pier or another stationary facility of the port infrastructure) so that its horizontal axis points to the north. In this mode, the reverse azimuth can be transmitted to the responder-beacons without the need for a GNSS receiver and a compass.

The **"MISC."** tab contains the settings of the orientation of the base station relative to the position reference point (the GNSS antenna) and the zero direction of the compass. Its appearance is shown in Figure 10.

| ![ZHost settings window view](/documentation/zhost_setts_3.png) |
| :---: |
| **Figure 10 - Settings window** |
| _Tab "MISC."_ |

- The **"&Delta;X"** and **"&Delta;Y"** parameters (in meters) define the location of the base station in a rectangular coordinate system associated with the antenna of the GNSS receiver (according to the figure)
- The **"&delta;"** parameter (in degrees) sets the rotation of the zero of the base station antenna relative to the zero of the magnetic or GNSS compass


##### 3.2.1.7. AUTOQUERY menu item
This menu item controls the **"AUTOQUERY"** mode. When this mode is enabled, the software automatically polls the responder-beacons at the highest possible rate according to the **"Responders in use"** list on the **"COMMON"** tab of the application settings window.
The **"AUTOQUERY"** mode is the main operating mode of the system and must be disabled only when navigation data is not required or when a user command must be sent to one or more beacons (this function is unavailable while the **"AUTOQUERY"** mode is enabled).

##### 3.2.1.8. AUTOSNAPSHOT menu item
If this function is enabled, the software automatically saves an image of the main window when the data is updated. The files are located in the **"\SNAPSHOTS\YYYY-DD-MM\"** directory, where **"YYYY-DD-MM"** is the current date. Each file is named according to the current time in the format **"HH-MM-SS"** and is in the Portable Network Graphics (\*.png) format.

#### 3.2.2 PPI panel
On this panel (see Fig. 7), the position of the base station is displayed in the center in the form of a yellow arrow, which points from bottom to top when working in relative coordinates and changes its orientation when heading data is available. In the latter case, the symbol **"N"** (North) is displayed at the top of the limb.
The **"PPI"** panel displays the position of the beacons relative to the base station. The beacons are displayed as circles with the beacon address inside. When a timeout occurs (the waiting interval for the beacon response is exceeded), the corresponding beacons are displayed with a dashed line.

The current state of the base station is displayed in the upper left corner:
- **TRX**: transceiver state (TX - transmitting, RX - waiting for a response, READY - ready for requests)
- **DPT**: depth (distance from the water surface) of the base station according to the readings of the built-in pressure sensor
- **TMP**: water temperature according to the readings of the built-in temperature sensor

Additional data received by the system via the AUX ports is displayed in the lower left corner:
- **LAT, LON**: geographic latitude and longitude (from **RMC** sentences)
- **AZM**: azimuth angle (from **HDG** or **HDT** sentences)
- **SPD**: speed (from **VTG** sentences)
- **VTG**: course (direction of motion) (from **VTG** sentences)

#### 3.2.3 RESPONDERS panel
Displays the data of the responder-beacons as a tree structure, where the first-level nodes denote the beacons (**"RESPONDER #XX"**), each of which has a set of nodes denoting various parameters and characteristics of the beacons in the form `Parameter identifier: Value`. Below is a list of possible parameter identifiers and their descriptions.

| Parameter identifier | Units | Description | Source |
| :--- | :--- | :--- | :--- |
| **MSR** | dB | Mean lobe-to-sidepeak ratio. Reception quality characteristic. Reception threshold 14, values above 20 - good reception | Determined by the base station when receiving a beacon response |
| **DPL** | Hz | Doppler shift of the carrier frequency | Determined by the base station when receiving a beacon response |
| **AZM** | ° | Azimuth to the beacon | Determined by the base station when receiving a beacon response |
| **DST** | m | Slant range to the beacon | Determined by the base station when receiving a beacon response |
| **STY** | PSU | Salinity value that was set for the beacon | From the beacon response confirming that the parameter was set |
| **LQR** | - | Result of the last service request | Determined by the logic of the ZHost software |
| **TMP** | °C | Ambient temperature (water temperature) | From the beacon response, according to the data of the built-in sensor of the beacon |
| **BAT** | V | Beacon supply voltage | From the beacon response, as the result of a direct measurement |
| **LAT** | ° | Geographic latitude of the beacon | Determined by the logic of the ZHost software |
| **LON** | ° | Geographic longitude of the beacon | Determined by the logic of the ZHost software |
| **DPT** | m | Depth (distance from the water surface) of the beacon | From the beacon response, according to the data of the built-in depth sensor of the beacon |
| **DSTP** | m | Projection of the slant range onto the water surface | Determined by the logic of the ZHost software |

To the right of each value, the age of the data is displayed - the time that has passed since the parameter value was last updated. The age is displayed only if it exceeds 7 seconds.

#### 3.2.3 Status panel
Located at the bottom of the window and displays the state of the corresponding devices:
- **ZMA**: base station
- **GNSS**: geographic position
- **HDG**: azimuth data source

<div style="page-break-after: always;"></div>

## 4. Effective use of the Zima USBL navigation system
The [Zima USBL](Zima_DataBrief_en.md) system is an underwater acoustic ultra-short baseline system that determines the relative location of the responder-beacons from the propagation time of the acoustic signal in water and the angle of arrival of the response signal of the responder-beacons.  
In this regard, its effective use is based on compliance with the following conditions:
- **ensuring a stable position of the base station during operation**; This condition is ensured by reliably securing the base station on a vertical pole, taking into account the direction of the zero of the direction-finding antenna. Angular deviations of the vertical axis of the station from the vertical, as well as deviations and oscillations of its zero, adversely affect the accuracy of determining the angle of arrival of the response signal;
- **ensuring a direct line of sight between the base station and the responder-beacon;** Since the distance to the responder-beacon is determined from the propagation time of the underwater acoustic signal in water, any obstacles in the signal path strongly distort the measured propagation time and, consequently, the determined distance to the responder-beacon; obstacles include both natural ones, associated with the bottom relief and/or the shore profile, and artificial ones - piers, quay walls, deep-draft vessels, bridge supports and other engineering structures;
- **the working surfaces must be free of various contaminants** (silt, dirt, algae, etc.);

Owing to the specifics of the propagation of sound vibrations in the aquatic environment, the base station should not be located at a depth of less than **2 - 3** meters and should be at least **1.5** meters from the lower part of the keel for small boats and not less than **2 - 3** meters for large boats. 

The antenna array of the base station is designed to determine the horizontal angle of arrival of the signal of the responder-beacons, so keep in mind that with such a mutual arrangement of the antenna and the responder-beacon in which they are located practically on the same vertical axis, the accuracy of determining the location of the responder will be minimal. A good mutual arrangement of the antenna and the responder-beacon is one in which the projection of the slant range onto the water surface significantly exceeds its projection onto the vertical axis.
The working vertical angles of the base station [Zima-B](Zima_B_Specification_en.md) are the angles of +/- 30° from the horizontal plane passing through the antenna array of the base station. This is illustrated in Figure 11:

| ![Zima-B angular zones](/documentation/zima_dir.png) |
| :---: |
| **Figure 11 - Geometric limitations of [Zima-B](Zima_B_Specification_en.md)** |
| _1 - working zone (+/- 30°), 2 - accuracy reduction zone (30 .. 45°), 3 - shadow zone ( > 45°), 4 - direction-finding antenna. The deviation is indicated from the horizontal plane passing through the center of the antenna array_ |

<div style="page-break-after: always;"></div>

## 5. Troubleshooting

| No. | Symptoms | Possible cause | Remedy |
| :---: | :--- | :--- | :--- |
| 1 | Unable to establish a connection between ZHost and Zima-B (error “COM port access denied”) | A peculiarity of the operation of the RS422-USB converter drivers in Win8-10 systems | 1. Disconnect power from the Zima-B station <br/> 2. Unplug the USB connector <br/> 3. Close the ZHost application <br/> 4. Plug in the USB connector <br/> 5. Launch the ZHost application <br/> 6. Click the **CONNECTION** button in ZHost <br/> 7. Apply power to the Zima-B station |
| 2 | The station emits a request signal, but the beacon does not respond | Hydrological conditions do not allow stable communication to be provided | Check the serviceability of the beacon at a short distance (0.5–10 meters) in line of sight |
|   |   | The power connector on the beacon is not connected | Plug in the connector | 
|   |   | The battery pack of the beacon is discharged	| Charge or replace the battery pack |
|   |   | The requested beacon address does not match its actual address | In the ZHost settings, select all available addresses; the station will go through all of them in turn, and thus the beacon address will be determined |
|   |    | The signal may not be emitted in full because the station does not have enough power | This is possible when the station is powered from power supplies that have a current limit. For normal operation in the transmit mode, the station needs about 3 A |
| 3 | There is no communication with the Zima-B station; the port is open, but the station does not transmit data | No power reaches the station | Check the power supply and the connecting cables |
|   |   | The station is faulty | Replace the station |
| 4 | The determined angle of arrival has a static error | The zero directions of the station and of the compass (or of the longitudinal axis of the vessel) are at an angle to each other - the station is rotated in the clamp | Align the zero direction of the station with the longitudinal axis of the vessel and/or the zero direction of the compass, and prevent accidental rotation of the antenna in the clamp |
| 5 | The system works, the beacon responds, but the absolute location of the beacon is not calculated (with an external GNSS receiver, compass or GNSS compass connected) | The data on the geographic position and heading of the vessel is not updated | Check that the GNSS receiver, the magnetic/GNSS compass, the connecting cables and the port settings are in working order |

<div style="page-break-after: always;"></div>

## 6. Obligations and disclaimer
### 6.1 Terms of replacement and free warranty service
The manufacturer's warranty covers only factory defects that become apparent during operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).  

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a factory defect.  

Grounds for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** to the equipment from the delivery set, including damage to the insulation of wires and cables;
- any **damage caused by exposure to moisture and contamination** as a result of improper operation of the equipment from the delivery set;
- any **electrical damage** caused by the **use of accessories not included in the delivery set**; accessories supplied by the manufacturer or its representative to replace faulty or lost ones are not considered to be outside the delivery set;
- any **signs of unauthorized repair and/or opening** of the equipment from the delivery set.

<div style="page-break-after: always;"></div>

### 6.2 Limitation of the manufacturer's liability

_____________

_**ANY OF THE PARTS OF THE DELIVERY SET, INDIVIDUALLY AND AS PART OF THE SYSTEM, HEREINAFTER REFERRED TO AS THE "SUPPLIED EQUIPMENT":**_

_**- WAS NOT DESIGNED AS RESCUE EQUIPMENT**_  
_**- WAS NOT TESTED AS RESCUE EQUIPMENT**_  
_**- IS NOT RESCUE EQUIPMENT**_  
_**- THE MANUFACTURER DECLARES THAT THE SUPPLIED EQUIPMENT IS SAFE WHEN OPERATED IN ACCORDANCE WITH THESE INSTRUCTIONS, AND THE MANUFACTURER IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF THE USE OF THE SUPPLIED EQUIPMENT**_

_____________

<div style="page-break-after: always;"></div>

[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/Zima/Zima_Users_manual_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
