| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima USBL** - underwater acoustic tracking system <br/> User's manual |


# THIS DOCUMENT IS UNDER CONSTRUCTION

# Zima USBL <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

    
<div style="page-break-after: always;"></div>

## 1. Introduction
Underwater acoustic navigation and tracking system **Zima** is designed to determine in real-time the horizontal angle and distance
to underwater objects equipped with responder-beacons [Zima-R](Zima_R_Specification_en.md). Responder-beacons
 can be installed on remote-operated underwater vehicles (ROVs), inhabited underwater vehicles, autonomous
unmanned underwater vehicles (AUVs) as well as for divers and technical divers (in case of using an autonomous version of the responder-beacons).

Navigation system **Zima** is an ultra-short baseline navigation system (_USBL_), the principle of which is based
using a phased array antenna to determine the horizontal angle of arrival of the signal and determine the distance to the beacons using the "request-response" method.
A distinctive feature of this system is the so-called "two-way" navigation, a patented solution that allows mutually
determine the distance both at the base station and at responder-beacons, and also transmit to beacons the azimuth angle to the base station.
The system also allows transmitting telecontrol commands to beacons and receiving telemetry data from beacons.

<div style="page-break-after: always;"></div>

## 2. Composition of the system
### 2.1. Zima-B: Hydroacoustic direction-finding base station
#### 2.1.1. General information
Hydroacoustic direction-finding station [Zima-B](Zima_B_Specification_en.md) (hereinafter referred to as the base station) is designed to transmit control acoustic signals to beacons, determine the propagation time of the signal to the beacons, determine the horizontal angle of arrival of the response signals of the beacons, transmit telecommands and receive telemetry information from beacons through specialized acoustic signals.

| ![Zima-B](https://ucnl.github.io/documentation/def_zima_b_ant.png) |
| :---: |
| **Figure 1 - Base station [Zima-B](Zima_B_Specification_en.md)** | 
| _Main view_ |

The base station is designed as a maintenance-free candy bar on a cable, embedded in a high-strength polyurethane compound. The station has a phased array antenna, a transmitting antenna, and an integrated depth/temperature sensor. As an additional option, the base station is equipped with a system for determining the course and position. In the general case, the base station is mounted on a rigid vertical rod taking into account the directivity of the antenna - the determined arrival angles are transmitted in the antenna coordinate system.  

| ![Zima-B placement](https://ucnl.github.io/documentation/zima_boat_placement.png) |
| :---: |
| **Figure 2 - [Zima-B](Zima_B_Specification_en.md) Deployment scheme** |
| _1-rod, 2-boat, 3-water surface, 4-cable, 5-[Zima-B](Zima_B_Specification_en.md), 6-zero direction_ |

Figure 3 shows the outline drawing of the base station [Zima-B](Zima_B_Specification_en.md).
The base station has an input cable for energy and information pairing and an opening for the pressure/temperature sensor. Structurally, the base station is divided into the following parts: cable entry (in the upper part of the station) and a fixing groove for fixing the station with a clamp. Below is the cylindrical surface of the transmitting piezoelectric element, under which there is a receiving phased antenna array. The surface of the transmitting element and the receiving grille during installation should not be blocked or shielded.
For proper operation of the station, line-of-sight is required between the working surfaces of the station and the antenna of the responder-beacon.

| ![Zima-B drawings](https://ucnl.github.io/documentation/Zima_B_drawings.png) |
| :---: |
| **Figure 3 - [Zima-B](Zima_B_Specification_en.md)** |
|  _Outine drawing_ |

In the standard configuration, [Zima-B](Zima_B_Specification_en.md) is supplied with a UART <-> RS-422 interface converter and cable
10 meters long, which is connected to the power supply and switching unit [Bat & Link Box](Bat_n_link_box_Specification_en.md). Thus,
through the switching unit, the station is connected to the control PC via the USB interface (serial port).

#### 2.1.2. Technical specifications

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 х 128 mm |
| WEIGHT<sup>[1](#footnote2121)</sup> (dry) | 0.44 kg |
| DEPTH RATING | 300 m |
| MAX. OPERATING RANGE<sup>[2](#footnote2122)</sup> |	3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote2123)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY | 0.3 m |
| MAX. TILT COMPENSATED BY THE BUILT-IN INCLINOMETER RELATED TO VERTICAL AXIS (pitch/roll) | +/- 30° |
| WORKING VERTICAL ANGLES (RELATIVE TO HORIZONTAL PLANE)<sup>[3](#footnote2123)</sup> | +/-30° |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote2123)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| BATTERY LIFE<sup>[4](#footnote2124)</sup> (WHEN SUPPLIED FROM [BAT&LINK BOX](Bat_n_link_box_Specification_en.md)) | 8 hours |
| INTERFACE | USB(COM) 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[5](#footnote2125)</sup> | 10 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
  
________________
<a name="footnote2121"><sup>1</sup></a> Withoud cable and interface converter.  
<a name="footnote2122"><sup>2</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2123"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote2124"><sup>4</sup></a> Considering 1 request in 3 seconds.  
<a name="footnote2125"><sup>5</sup></a> With additional cable and interface converter [Bat&Link Box](Bat_n_link_box_Specification_en.md). Can be increased by a request up to 20 m.  

#### 2.1.3 Storage and maintenance
There are no special storage and maintenance requirements for the base station, with the exception of the following:
- When used in salt and/or heavily polluted water, desalination is necessary (flushing in freshwater)
- The use of any organic solvents, strong acids, alkalis and other aggressive substances is not allowed
- If necessary, washing in household soap solutions is possible, avoiding liquid getting on the connector
- Impact or significant static loads are not allowed.
- Strong (with a radius of less than 5 cm) cable bending is not allowed.

### 2.2. Zima-R: responder-beacon
#### 2.2.1. General information
The responder-beacon is designed as a maintenance-free monoblock on a cable, embedded in a high-strength polyurethane compound. The appearance of the responder beacon [Zima-R] (Zima_R_Specification_en.md) is shown in Figure 4. Structurally, the beacon contains a cable entry, a mounting groove, a pressure sensor hole and a working surface. The pressure sensor opening and working surfaces (cylinder and cylinder end opposite the cable entry) must not be blocked or shielded. For correct operation of acoustic communication, line-of-sight between the base station and the responder-beacon is required.

| ![Zima-R](https://ucnl.github.io/documentation/zima_r.png) |
| :---: |
| **Figure 4 - [Zima-R](Zima_R_Specification_en.md)** |
|  _General view (autonomous version)_ |

#### 2.2.2. Technical specifications

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 x 62 mm |
| WEIGHT<sup>[1](#footnote2221)</sup> (dry) | 0.3 kg |
| DEPTH RATING | 300 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAX. OPERATING RANGE<sup>[2](#footnote2222)</sup> |	3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote2223)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| SUPPLY VOLTAGE | 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | USB(COM) 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote2224)</sup> | 1 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote2223)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY<sup>[3](#footnote2223)</sup> | 0.3 m |

##### Additional parameters of standard battery pack<sup>[5](#footnote2225)</sup>

| PARAMETER | VALUE |
| :--- | :--- |
| BUIT-IN BATTERY TYPE | Ni-MH |
| ELECTRICAL CAPACITY | 2.9 A\*h |
| NOMINAL VOLTAGE | 12 V |
| NUMBER OF BATTERIES | 10 pcs. |
| CANISTER MATERIAL | Delrin |
| WORKING TEMPERATURE RANGE | -5 .. 50 °С |
  
________________
<a name="footnote2221"><sup>1</sup></a> Without a battery pack. Standard battery pack ф50х165 mm, 0.58 kg, 2.9 A\*h 12 V. Operating time from a standard battery pack in standby mode - up to 70 hours, with radiation 1 time in 3 seconds up to 8 hours.  
<a name="footnote2222"><sup>2</sup></a> Without the presence of a multipath effect. A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.   
Battery life with standard battery pack - up to 70 hours in receiving mode, up to 8 hours with 1 request in 3 seconds schedule.  
<a name="footnote2223"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote2224"><sup>4</sup></a> Can be changed by a special request.  
<a name="footnote2225"><sup>5</sup></a> Standard delivery set, subject to change without notice  

#### 2.2.3. Configuration options
The responder-beacon [Zima-R](Zima_R_Specification_ru.md) is a transceiver for underwater acoustic digital broadband communication and can be interfaced with the control system energetically and informationally. In this case, it is possible, if the control system has a magnetic compass, to determine the distance and heading angle to the base station, as well as receive telecontrol code commands from the base station.
When autonomous, the beacon is equipped with a battery canister, as shown in Figure 4. In this case, it is completely autonomous and does not require pairing with the carrier underwater vessel.
In [OEM](Zima_R_OEM_Specification_en.md) the beacon is delivered as a set of electronic boards for user installation in own normobaric housing. The responder-beacon is equipped with a deep-sea underwater acoustic antenna. Insertion of the antenna cable into the pressure-sensitive housing and switching with the beacon electronics, in this case, is provided by the user.

#### 2.2.4. Work with the device (stand-alone version)
In this case, the responder-beacon is fully autonomous. For operation, it must be fixed on the carrier vessel in such a way that the working surfaces of the monoblock (cylindrical surface and end face) are not blocked by fasteners (a special groove must be used for fastening) and are not shielded by various structural elements of the carrier. To turn on the responder-beacon, the user needs to connect it to the battery pack using the connector, as shown in Figure 5.

| ![Zima-R](https://ucnl.github.io/documentation/zima_r_bat_conn.png) |
| :---: |
| **Figure 5 - Connecting a responder-beacon to a battery pack** |

In this version, the responder-beacon is equipped with a 10-cell nickel-metal hydride battery.
The normobaric housing (canister) has a lid with a double seal and a four-thread, which allows the user to close the lid of the canister in 3/4 of a turn. Before immersion in water, make sure that the lid of the canister is tightly screwed (by hand).
After connecting the responder-beacon connector to the battery pack within the first ten seconds, the device calibrates the atmospheric pressure, therefore it is not allowed to apply any (negative or positive) pressure to it during the first ten seconds from the moment the device is turned on, this will lead to incorrect depth measurement by the responder-beacon.
With the autonomous version Tx and Rx, the wires of the beacon cable are closed (see Figure 6). This causes the UART module to automatically shut off in order to save energy.

| ![Zima-R](https://ucnl.github.io/documentation/zima_r_drawings.png) |
| :---: |
| **Figure 6 - [Zima-R](Zima_R_Specification_en.md)** |
| _Outline drawing_ |

#### 2.2.5. Work with the device (integrated version)
During energy and information pairing with the carrier vessel, the beacon transmits to the carrier the distance to the base station and the azimuth (only when the heading sensor is connected to the base station). In addition, in this case, the base station can transmit up to 28 code commands, about which the responder-beacon notifies the carrier in accordance with the [pairing protocol](Zima_Protocol_Specification_en.md).

#### 2.2.6. Storage and maintenance
The responder-beacon does not require any special maintenance procedures, except for desalination and washing in running fresh water, after use in salt and/or contaminated water.
In this case, the use of any lubricants or solvents, aggressive detergents, etc. are not allowed to remove contaminants from the responder-beacon and its cable.

In the case of using the responder-beacon in the stand-alone version, additional requirements are presented and measures are taken to service the battery pack and canister. In particular:
- long-term (more than one day) storage of the battery pack in the state connected to the beacon is not allowed;
- long-term storage of the battery pack without scheduled recharging (1 time per month) is not recommended;
- O-rings and the threads of the battery canister should be cleaned with water, a soft brush and a soap solution, followed by washing in running freshwater and greasing the o-rings with silicone grease;
- the canister is stored with the lid closed;
- when using the device in salt and/or contaminated water at the end of work, it is required to desalinate it in running fresh water.

<div style="page-break-after: always;"></div>

## 3. ZHost software
### 3.1. System requirements
Specialized software [ZHost](https://github.com/ucnl/ZHost) (hereinafter referred to as the software) runs under the **MS Windows** operating system versions 7, 8 and 10. A monitor with a resolution of at least **1024x768** pixels and a mouse or touchpad are recommended.
The software is portable, distributed as [zip-archive \(Download the latest version\)](https://api.github.com/repos/ucnl/ZHost/zipball) and does not require any installation other than Unpacking to the user's PC.

The executable file **ZHost.exe**, the settings file **ZHost.setting**s and the required libraries are located in the root directory of the application. Localization resources are located in subdirectories corresponding to the localization language (e.g. `\ru`, `\ru-RU`, etc.).
When running, the application maintains log files. Logs are stored in the \LOG subdirectory, which contains subdirectories with the name of the current date (for example, `\LOG\2020-01-21`), which contain **.log** files with names corresponding to the file creation time (**HH-MM-SS**). A new log file is created each time the application starts. Log files have a text format and contain all the information exchange of the console software with the devices connected to it, as well as all errors that occur during the operation of the software.

When the **AUTOSCRINSHOT** function is enabled, the screenshots of the application window are saved in the `\SNAPSHOTS` directory, which also contains subdirectories by the name of the creation date, the window snapshot files are named by the current time (**HH-MM-SS**) and are in **PNG** format (Portable Network Graphics).

> Since the connection with the base station is carried out by means of converters of the UART/RS-232/RS-422 interface to USB, additional drivers for a specific converter are required.

### 3.2. Description of the ZHost software interface
The general view of the application window is shown in Figure 7. It consists of a toolbar (menu) located at the top of the window, a status panel located at the bottom of the window; on the left is a screen for displaying the relative position of responder beacons (**PLAN**), and on the right is a tree structure containing the properties of the beacons used (**BEACONS**).
The toolbar consists of the upper (**CONNECTION**, **STATION**, etc.) and lower (**AUTO REQUEST**, **AUTOSCRINSHOT**) subpanels.

| ![ZHost main window view](https://ucnl.github.io/documentation/zhost_screen_gnss_hdg.png) |
| :---: |
| **Figure 7 - [ZHost](https://github.com/ucnl/ZHost) software** |
| _Main window view_ |

#### 3.2.1 Toolbar
##### 3.2.1.1 Menu item CONNECTION
The menu item **"CONNECTION"** serves to open and close the connection on the configured serial ports. These include the port, through which is exchanging information with the base station, AUX ports, through which navigation information from the **GNSS + GNSS compass** or **GNSS + magnetic compass** can be received (with appropriate settings), as well as a GNSS emulation port for one of the responder beacons.

When the user clicks on the menu item **"CONNECTION"** the application tries to open connections on the serial ports according to the settings.
If additional providers of navigation data (GNSS, compass) are not specified and the system operates in relative coordinates, an attempt will be made to open the port for communication with the base station. If one or both of the AUX ports and the GNSS emulation output port are enabled in the settings, the software will try to open them as well.

If the ports are opened successfully, the menu item **"CONNECTION"** becomes highlighted, and subsequent clicking on it will close the connections.

##### 3.2.1.2 Menu item STATION
The menu item **"STATION"** becomes active only after the connection with the base station is open and device information has been successfully received from it. The item contains the following subitems:
- **"INFORMATION"** to call up a dialogue box containing information about the connected base station (device serial number, firmware version, etc.).
- **"DEPTH CALIBRATION"** to call the dialogue box for setting the actual depth of the base station.

##### 3.2.1.2 Menu item BEACON
This menu item becomes active only after the connection with the base station is opened and information about the device is successfully received from it, and the function **"AUTO REQUEST"** is not active. The item contains the following subitems:
- **"SEND COMMAND"** to call the remote command sending dialogue box, in which the user can select the address of the responder-beacon to which the user command should be sent and the command identifier.
- **"CHANGE ADDRESS"** to call the dialogue box for changing the address of the remote beacon-responder. In the dialogue box, the user must specify the current address of the beacon, which needs to change the address and the new address. *The user should be careful when using this function. It is intended only for setting beacon addresses before submersion.*
- **"CALIBRATION OF ATMOSPHERIC PRESSURE"** to call up the atmospheric pressure calibration dialogue box. In the dialogue box, the user must specify the address of the beacon. Upon receipt of a command to calibrate atmospheric pressure, the responder-beacon will use the current pressure readings from the built-in sensor as atmospheric. *The user should be careful when using this function. It is intended only for configuring beacons before submersion.*

##### 3.2.1.3 Menu item LOG
Menu item **"LOG"** contains functions for working with application log files and contains the following sub-items:
- **"VIEW"**. Selecting this subitem will open the current application log file.
- **"ANALYZE"**. If the user selects this sub-item, the file selection dialogue for analysis will be displayed. The log file analysis function allows the user to quickly restore the system’s progress, for example, in order to restore the tracks of the vessel and/or responder-beacons in case of loss.
- **"ANALYZE CURRENT"**. The action of this sub-item is similar to the function of the **"ANALYZE"** sub-item, with the difference that the current one will be selected as the analyzed log file.
- **"RESTART CURRENT"**. When this sub-item is enabled, the contents of the current log file will be deleted and the log recording will continue.
- **"DELETE ALL LOGS"**. This menu sub-item is intended to delete all application logs from the LOG\ directory. *Attention! Data from the log files will be lost forever!*

##### 3.2.1.4 Menu item TRACK
The menu item **"TRACK"** contains functions for working with tracks generated by the software and contains sub-items:
- **"SAVE AS ..."** serves to open a dialogue box for selecting a name and file format, for saving tracks. The function becomes active only if the system has unsaved geographic data. The software supports exporting tracks to Keyhole Markup Language (KML) and Comma-separated values (CSV) formats.
- **"CLEAR"**. This sub-item is used to delete all geographic data accumulated by the software for the current session. *This function should be used with caution!*

##### 3.2.1.5 Menu item SETTINGS
The menu item **"SETTINGS"** is active only when the connection is closed and serves to call the dialogue box for changing software settings.

Settings are saved in the root directory of the application. It should be remembered that in order for the changed and saved settings to be used by the application, it must be restarted. If the settings are saved successfully, the software will display the corresponding prompt to the user.

The settings in the dialogue box are grouped for convenience, each group is located on a separate tab.
**RESET button** is used to restore default settings.
The **OK button**, which is used to accept the settings, is only active when the user has set consistent data (for example, with AUX ports enabled, the names for all the enabled ports must not coincide with each other).

The **CONNECTION** tab contains the settings for the connection ports. Its appearance is shown in Figure 8.

| ![ZHost settings window view](https://ucnl.github.io/documentation/zhost_setts_1.png) |
| :---: |
| **Figure 8 - Settings editor** |
| _Tab "CONNECTION"_ |

The group **"ZMA port"** is always active and is responsible for the settings for connecting to the base station [Zima-B](Zima_B_Specification_ru.md). On commercially available devices, only 9600 bps is supported.

Other groups **"AUX1 port"**, **"AUX2 port"** and **"Output port"** become active only if the corresponding checkbox is selected.

- If the system [Zima USBL](Zima_DataBrief_en.md) is used with a GNSS receiver with heading measurement function, then the user needs to use only one of the AUX ports through which data is received;

- If the system [Zima USBL](Zima_DataBrief_en.md) is used with a standard GNSS receiver, and heading information is supplied from a magnetic compass, then both AUX ports should be used, a GNSS receiver is connected to one of them and a magnetic compass to the other.

If **"Save AUX to Log"** is not checked, then the data coming from the AUX ports will not be saved to the log file.

If the system operates in absolute coordinates (i.e., it receives data on the geographic location of the base station and its orientation relative to the cardinal points) and the absolute geographic coordinates of the responder beacons are calculated, then it becomes possible to emulate GNSS **RMC** and **GGA** messages based on the geographic location of the beacon and transmit them to the output port.

This can be, for example, a virtual COM port, to the second end of which cartographic software (for example, SAS.Planet) can be connected to display the location of the beacon on the map in real-time. To enable this function, it is necessary to check the **Use Output Port** checkbox and set the required port settings, as well as specify the beacon address, based on the coordinates of which GNSS data will be emulated.

If the checkbox **"Save log separately"** is checked, the data transferred to the output port will be saved in a separate log.


The tab **"GENERAL"** contains the address settings of the used beacons and some physical parameters. Its appearance is shown in Figure 9.
| ![ZHost settings window view](https://ucnl.github.io/documentation/zhost_setts_2.png) |
| :---: |
| **Figure 9 - Settings editor** |
| _Tab "GENERAL"_ |

The **Used Beacons** group contains a list of all possible beacon addresses. The system will automatically poll beacons, opposite the addresses of which are checked in this list.

The group **"Time intervals"** contains the settings:
- the threshold for data obsolescence (in seconds). If the value has not been updated more than the specified time interval, OBS (Obsolete) symbols will be displayed next to it in parentheses, indicating to the operator that this particular parameter (for example, water temperature or beacon supply voltage) has not been updated for a long time;
- The maximum distance. This parameter tells the system the maximum distance that the responder-beacon can be located. This parameter is responsible for how long the base station will wait for a beacon response. If for some reason the station does not receive a beacon response, it waits for it for a certain time, called a timeout time. It makes sense to set the minimum possible values ​​based on the requirements of the task, in order to limit the downtime of the system when it expects a missed beacon response.

The **Salinity** group allows the user to set the salinity of the water (in PSU) either directly, or select from the world salinity database (by calling the salinity selection dialogue by the link **".."**). It is not recommended to take salinity from the base for small inland water bodies: rivers, lakes, ponds, etc. In this case, if the exact value is not known, set zero salinity (freshwater).
The salinity value is used by the system to more accurately determine the depth and speed of sound.

The checkbox **"Auto-calculation of the speed of sound"** and the corresponding group managed by it are responsible for where the system will take the speed of sound in water. If this value is known directly from the measurement, the user should disable the automatic calculation function and specify the value directly. In other cases, the checkbox should be checked. In this case, the system will calculate the speed of sound by pressure, temperature and salinity. As a rule, the calculated value is in good agreement with the actual value.

Group **"Advanced"** contains:
- Checkbox **"Less accurate depth estimate"**. If this function is enabled, the beacon will transmit depth with a lower resolution (~ 40 cm), but at the same time, the depth will be transmitted in one request-response transaction, and the function of simultaneous navigation (sending back azimuth to the base station and measuring the distance by the beacon to the base station) will be unavailable. If the simultaneous navigation function is not required (for example, if a beacon is used in stand-alone version) and an accuracy of 40 cm in depth is sufficient, select this checkbox.
- The checkbox **"Antenna is stationary"** is designed for the situation when the system operates in relative coordinates and the base station is fixed motionless (for example, on a pier or other stationary facility of port infrastructure) so that its horizontal axis is directed to the north. In this mode, it is possible to transmit the reverse azimuth to the transponder beacons without the need for a GNSS receiver and compass.

The tab **"OPTIONAL"** contains the settings for the orientation of the base station relative to the topographic position (GNSS antenna) and the zero direction of the compass. Its appearance is shown in Figure 10.

| ![ZHost settings window view](https://ucnl.github.io/documentation/zhost_setts_3.png) |
| :---: |
| **Figure 10 - Settings editor** |
| _Tab "ADVANCED"_ |

- Parameters **"&Delta;X"** and **"&Delta;Y"** (in meters) determine the location of the base station in a rectangular coordinate system associated with the antenna of the GNSS receiver (according to the figure)
- The parameter **"&delta;"** (in degrees) sets the zero rotation of the base station antenna relative to the zero of the magnetic or GNSS compass


##### 3.2.1.6 Пункт АВТОЗАПРОС
Данный пункт меню управляет режимом **"АВТОЗАПРОС"**. При включении этого режима ПО будет автоматически с максимально возможной скоростью опрашивать маяки-ответчики согласно списку **"Используемые маяки"** вкладки **"ОБЩИЕ"** окна настроек приложения.
Режим **"АВТОЗАПРОС"** является основным рабочим режимом системы и должен отключаться только в тех случая, когда навигационные данные не требуются или необходима передача пользовательской команды на один или несколько маяков (при включенном режиме **"АВТОЗАПРОС"** данная функция недоступна).

##### 3.2.1.7 Пункт АВТОСКРИНШОТ
Если данная функция включена, ПО будет автоматически сохранять изображение главного окна при обновлении данных. Файлы располагаются в каталоге **"\SNAPSHOTS\YYYY-DD-MM\"**, где **"YYYY-DD-MM"** - текущая дата. Каждый файл именуется согласно текущему времени в формате **"HH-MM-SS"** и имеет формат Portable Network Graphics (\*.png).

#### 3.2.2 Панель ПЛАН
На этой панели (см. рис. 7) в центре отображается положение базовой станции в виде желтой стрелки, которая ориентирована снизу вверх при работе в относительных координатах и изменяет свою ориентацию, при доступных данных курса. В последнем случае в верху лимба отображается символ **"N"** (North, Север).
Панель **"ПЛАН"** отображает положение маяков относительно базовой станции. Маяки отображаются в виде кружков с адресом маяка внутри. При возникновении таймаута (превышении интервала ожидания ответа маяка) соответствующие маяки отображаются пунктирной линией.

В левом верхнем углу отображается текущее состояние базовой станции:
- **TRX**: состояние приемопередатчика (TX - идет передача, RX - ожидание ответа, READY - готова к запросам)
- **DPT**: глубина (расстояние от поверхности воды) базовой станции по показаниям встроенного датчика давления
- **TMP**: температура воды по показаниям встроенного датчика температуры

В левом нижнем углу отображаются дополнительные данные, получаемые системой через порты AUX:
- **LAT, LON**: географичекие широта и долгота (из сообщений **RMC**)
- **AZM**: азимутальный угол (из сообщений **HDG** или **HDT**)
- **SPD**: скорость (из сообщений **VTG**)
- **VTG**: курс движения (из сообщений **VTG**)

#### 3.2.3 Панель МАЯКИ
Отображает данные маяков-ответчиков в виде древовидной структуры, где узлы первого уровня обозначают маяки (**"RESPONDER #ХХ"**), каждый из которых имеет набор узлов, обозначающих различные парметры и характеристики маяков в виде `Идентификатор параметра: Значение`. Ниже представлен список возможных идентификаторов параметров и их описания.

| Идентификатор параметра | Единицы измерения | Описание | Источник |
| :--- | :--- | :--- | :--- |
| **MSR** | дБ | Mean lobe-to-sidepeak ratio. Характеристика качества приема. Порог приема 14, значения выше 20 - хороший прием | Определяется базовой станцией при приеме ответа маяка |
| **DPL** | Гц | Доплеровский сдвиг несущей частоты | Определяетя базовой станцией при приема ответа маяка |
| **AZM** | ° | Азимут на маяк | Определяется базовой станцией при приеме ответа маяка |
| **DST** | м | Наклонная дальность до маяка | Определяется базовой станцией при приема ответа маяка |
| **STY** | PSU | Значение солености, которое было задано маяку | Из ответа маяка, который подтверждает задание параметра |
| **LQR** | - | Результат последнего сервисного запроса | Определяется логикой ПО ZHost |
| **TMP** | °C | Окружающая температура (температура воды) | Из ответа маяка, по данным встроенного датчика маяка |
| **BAT** | В | Напряжение питания маяка | Из ответа маяка, как результат прямого измерения |
| **LAT** | ° | Географическая широта маяка | Определяется логикой ПО ZHost |
| **LON** | ° | Географическая долгота маяка | Определяется логикой ПО ZHost |
| **DPT** | м | Глубина (расстояние от поверхности воды) маяка | Из ответа маяка, по данным встроенного датчика глубины |
| **DSTP** | м | Проекция наклонной дальности на поверхность воды | Определяется логикой ПО ZHost |

Справа от каждого значения отображется возраст данных - время, которое прошло с момента, когда значение параметра было обновлено. Возраст отображается только в том случае, если он превышает 7 секунд.

#### 3.2.3 Панель статуса
Располагается в нижней части окна и отображает состояние соответствующих устройств:
- **ZMA**: базовая станция
- **GNSS**: географическое положение
- **HDG**: источник данных об азимуте

<div style="page-break-after: always;"></div>

## 4. Эффективное применение навигационной системы Zima
Система  [Zima USBL](Zima_DataBrief_ru.md) является гидроакустической ультракороткобазисной системой, которая определяет относительное местоположение маяков-ответчиков по времени распространения акустического сигнала в воде и углу прихода ответного сигнала маяков-ответчиков.  
В связи с этим, эффективное ее применение основывается на соблюдении следующих условий:
- **обеспечение стабильного положения базовой станции во время работы**; Данное условие обеспечивается надежным закреплением базовой станции на вертикальной штанге, с учетом направления нуля антенны пеленгования. Угловые отклонения вертикальной оси станции от вертикали а также отклонения и колебания ее нуля негативно сказываются на точности определения угла прихода ответного сигнала;
- **обеспечение прямой видимости между базовой станцией и маяком-ответчиком;** Поскольку дистанция до маяка-ответчика определяется по времени распространения гидроакустического сигнала в воде, то любые препятствия на пути прохождения сигнала сильно искажают измеряемое время распространения, а следовательно и определяемую дистанцию до маяка-ответчика; к препятствиям можно отнести как естественные, связанные с рельефом дна и/или береговым профилем, так и искусственные - пирсы, причальные стенки, суда с глубокой осадкой, опоры мостов и иные технические сооружения;
- **рабочие поверхности должны быть свободны от различных загрязнений** (ил, грязь, водоросли и т. п.);

Ввиду специфики распространения звуковых колебаний в водной среде базовую станцию не следует располагать на глубине, меньшей, чем **2 - 3 ** метра и как минимум **1.5** метра от нижней части киля для малых лодок и не менее **2 - 3** метров для крупных лодок. 

Антенная решетка базовой станции предназначена для определения горизонтального угла прихода сигнала маяков-ответчиков, поэтому стоит помнить, что при таком взаимном расположении антенны и маяка-ответчика, когда они находятся практически на одной вертикальной оси, точность определения местоположения ответчика будет минимальной. Хорошим взаимным расположением антенны и маяка-ответчика считается такое, при котором проекция наклонной дальности на водную поверхность значительно превышает проекцию ее на вертикальную ось.
Рабочими вертикальными углами базовой станции [Zima-B](Zima_B_Specification_ru.md) являются углы +/- 30° от горизонтальной плоскости, проходящей через антенную решетку базовой станции. Данное положени проиллюстрировано на рисунке 11:

| ![Zima-B angular zones](https://ucnl.github.io/documentation/zima_dir.png) |
| :---: |
| **Рисунок 11 - Геометрические ограничения [Zima-B](Zima_B_Specification_ru.md)** |
| _1 - рабочая зона (+/- 30°), 2 - зона снижения точности (30 .. 45°), 3 - теневая зона ( > 45°), 4 - пеленгационная антенна. Отклонение указывается от горизонтальной плоскости, проходящей через центр антенной решетки_ |

<div style="page-break-after: always;"></div>

## 5. Возможные неисправности, их диагностика и устранение

| № | Симптомы | Возможная причина | Устранение |
| :---: | :--- | :--- | :--- |
| 1 | Не удается установить соединение ZHost и Zima-B (Ошибка “Нет доступа к COM-порту) | Особенность работы драйверов преобразователя RS422-USB в системах Win8-10 | 1. Отключить питание станции Zima-B <br/> 2. Отсоединить разъем USB <br/> 3. Закрыть приложение ZHost <br/> 4. Подсоединить разъем USB <br/> 5. Запустить приложение ZHost <br/> 6. Нажать кнопку **СОЕДИНЕНИЕ** в ZHost <br/> 7. Подать питание на станцию Zima-B |
| 2 | Станция излучает запросный сигнал, но маяк не отвечает | Гидрология не позволяет обеспечить устойчивую связь | Проверить исправность маяка на малой дистанции (0.5-10 метров) в прямой видимости |
|   |   | Не подключен разъем питания на маяке | Подключить разъем | 
|   |   | Разряжен АКБ батарейного блока маяка	| Зарядить или заменить батарейный блок |
|   |   | Запрашиваемый адрес маяка не соответствует его фактическому | В настройках ZHost выбрать все доступные адреса, станция переберет все поочередно и таким образом адрес маяка будет установлен |
|   |    | Возможно, сигнал излучается неполностью и станции не хватает питания | Такое возможно при питании станции от источников питания, имеющих ограничение по току. Для нормальной работы в режиме передачи станции необходимо порядка 3А |
| 3 | Нет связи со станцией Zima-B, порт открыт, но станция не передает данные | На станцию не приходит питание | Проверить источник питания и соединительные кабеля |
|   |   | Станция неисправна | Заменить станцию |
| 4 | Определяемый угол прихода имеет статическую ошибку | Нулевые направления станции и компаса (или продольной оси судна) расположены под углом - станция повернута в хомуте | Совместить нулевое направление станции с продольной осью судна и/или нулевым направлением компаса и исключить случайное проворачивание антенны в хомуте |
| 5 | Система работает, маяк отвечает но абсолютное местоположение маяка не вычисляется (при подключенном внешнем GNSS-приемнике, компасе или GNSS-компасе) | Не обновляются данные о географическом положении и курсе судна | Проверить исправность GNSS-приемника и магнитного/GNSS компаса а также соединительных кабелей и настроек портов |

<div style="page-break-after: always;"></div>

## 6. Обязательства и отказ от ответственности
### 6.1 Условия замены и бесплатного гарантийного обслуживания
Гарантия производителя распространяется только на заводские дефекты, выявивщиеся при эксплуатации устройства в соответствие с настоящим руководством в течении гарантийного срока (2 года с момента покупки).  

Производитель гарантирует бесплатный ремонт или замену неисправного оборудования из комплекта поставки, вышедшего из строя по причине заводского дефекта.  

К поводам для отказа от бесплатного гарантийного обслуживания, бесплатного ремонта и замены относятся:
- любые **механические повреждения** оборудования из комплекта поставки, в т.ч. нарушение изоляции проводов и кабелей;
- любые **повреждения, вызванные воздействием влаги и загрязнейний**, вследствие неправильной эксплуатации оборудования из комплекта поставки;
- любые **электрические повреждения**, вызванные **использованием некомплектных аксессуаров**; к некомплектным не отностятся аксессуары, поставленные производителем или его представителем в замен неисправных или утраченых;
- любые **следы самостоятельного ремонта и/или вскрытия** оборудования из комплекта поставки.

<div style="page-break-after: always;"></div>

### 6.2 Ограничение ответственности производителя

_____________

_**ЛЮБАЯ ИЗ ЧАСТЕЙ КОМПЛЕКТА ПОСТАВКИ В ОТДЕЛЬНОСТИ И В СОСТАВЕ СИСТЕМЫ, ИМЕНУЕМЫЕ ДАЛЕЕ "ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ":**_

_**- НЕ РАЗРАБАТЫВАЛОСЬ КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ТЕСТИРОВАЛОСЬ, КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ЯВЛЯЕТСЯ СРЕДСТВОМ СПАСЕНИЯ**_  
_**- ПРОИЗВОДИТЕЛЬ ЗАЯВЛЯЕТ, ЧТО ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ БЕЗОПАСНО ПРИ ЭКСПЛУАТАЦИИ СОГЛАСНО НАСТОЯЩЕЙ ИНСТРУКЦИИ И НЕ ОТВЕЧАЕТ ЗА ЛЮБЫЕ ПОСЛЕДСТВИЯ ИСПОЛЬЗОВАНИЯ ПОСТАВЛЯЕМОГО ОБОРУДОВАНИЯ**_


