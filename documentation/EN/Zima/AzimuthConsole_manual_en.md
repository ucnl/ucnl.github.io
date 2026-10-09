[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **AzimuthConsole: User's manual**

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

| ![logo](/documentation/sm_logo.png) | [![AzimuthConsole: User's manual](https://github.com/user-attachments/assets/2a70ad5c-db4d-4dee-8c26-5c8cf04a91b6)](/documentation/EN/Zima/AzimuthConsole_manual_en)  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **AzimuthConsole** - Cross-platform application for the Zima2 USBL system <br/> User's manual |

# AzimuthConsole <br/> User's manual

> **Applies to version 2.2.0** (2026-09-25).
> Full change history: [changelog.md](https://github.com/ucnl/AzimuthConsole/blob/main/src/changelog.md).

<div style="page-break-after: always;"></div>

<div id="toc"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Supported platforms](#11-supported-platforms)
  - [1.2. Hotkeys](#12-hotkeys)
  - [1.3. Supported devices](#13-supported-devices)
  - [1.4. Recording and storing information](#14-recording-and-storing-information)
- [2. AzimuthConsole command system](#2-azimuthconsole-command-system)
  - [2.1. Characteristics](#21-characteristics)
  - [2.2. Examples](#22-examples)
  - [2.3. Command descriptions](#23-command-descriptions)
    - [2.3.1. Connection](#231-connection)
    - [2.3.2. Ports](#232-ports)
    - [2.3.3. Beacon interrogation](#233-beacon-interrogation)
    - [2.3.4. Transceiver](#234-transceiver)
      - [2.3.4.1. Determining the address mask from beacon addresses](#2341-determining-the-address-mask-from-beacon-addresses)
    - [2.3.5. Position](#235-position)
    - [2.3.6. Beacon configuration](#236-beacon-configuration)
    - [2.3.7. Service](#237-service)
    - [2.3.8. Log file management](#238-log-file-management)
    - [2.3.9. Output data configuration](#239-output-data-configuration)
    - [2.3.10. Calibrations](#2310-calibrations)
    - [2.3.11. Reference beacon mode](#2311-reference-beacon-mode)
- [3. Web interface](#3-web-interface)
  - [3.1. Connection](#31-connection)
  - [3.2. Main interface elements](#32-main-interface-elements)
    - [3.2.1. Map](#321-map)
    - [3.2.2. Command line](#322-command-line)
    - [3.2.3. Side panel](#323-side-panel)
    - [3.2.4. Information panels on the map](#324-information-panels-on-the-map)
    - [3.2.5. Calibration panels](#325-calibration-panels)
  - [3.3. Settings window](#33-settings-window)
  - [3.4. Mobile version](#34-mobile-version)
  - [3.5. Language support](#35-language-support)
- [4. Output data](#4-output-data)
  - [4.1. AZMLOC - local parameters](#41-azmloc---local-parameters)
  - [4.2. AZMREM - responder-beacon data](#42-azmrem---responder-beacon-data)
- [5. Auxiliary utilities](#5-auxiliary-utilities)
  - [5.1. AzimuthUDPRemote - UDP terminal](#51-azimuthudpremote---udp-terminal)
  - [5.2. AzimuthUDPListener - UDP receiver](#52-azimuthudplistener---udp-receiver)
- [6. Application deployment scenarios](#6-application-deployment-scenarios)
  - [6.1. Configuring access from the local network](#61-configuring-access-from-the-local-network)
- [7. Setting up a Raspberry Pi with application autostart](#7-setting-up-a-raspberry-pi-with-application-autostart)
  - [7.1. What you will need](#71-what-you-will-need)
  - [7.2. System preparation](#72-system-preparation)
    - [7.2.1. Writing the image to an SD card](#721-writing-the-image-to-an-sd-card)
    - [7.2.2 First boot and basic setup](#722-first-boot-and-basic-setup)
    - [7.2.3 Updating packages](#723-updating-packages)
  - [7.3. Installing the application](#73-installing-the-application)
    - [7.3.1 Creating the directory](#731-creating-the-directory)
    - [7.3.2 Copying files from a USB flash drive](#732-copying-files-from-a-usb-flash-drive)
    - [7.3.3 Alternative: copying via SCP from a computer](#733-alternative-copying-via-scp-from-a-computer)
  - [7.4. Creating startup scripts](#74-creating-startup-scripts)
    - [7.4.1 Script for manual start `start.sh`](#741-script-for-manual-start-startsh)
    - [7.4.2. Script for the daemon `dstart.sh`](#742-script-for-the-daemon-dstartsh)
    - [7.4.3. Execute permissions](#743-execute-permissions)
  - [7.5. Configuring autostart (systemd)](#75-configuring-autostart-systemd)
    - [7.5.1. Creating the service](#751-creating-the-service)
    - [7.5.2. Activating the service](#752-activating-the-service)
  - [7.6. Checking operation](#76-checking-operation)
    - [7.6.1. Service status](#761-service-status)
    - [7.6.2. Viewing logs](#762-viewing-logs)
    - [7.6.3. Finding the IP address](#763-finding-the-ip-address)
    - [7.6.4. Access from a browser](#764-access-from-a-browser)
  - [7.7. Managing the application](#77-managing-the-application)
  - [7.8. Updating the application](#78-updating-the-application)
  - [7.9. Useful commands](#79-useful-commands)
  - [7.10. Possible problems and solutions](#710-possible-problems-and-solutions)
- [8. Running as a Windows service](#8-running-as-a-windows-service)
  - [8.1. Step-by-step instructions](#81-step-by-step-instructions)
  - [8.2. Alternative option via a bat file](#82-alternative-option-via-a-bat-file)
  - [8.3. Management and verification](#83-management-and-verification)
- [9. Scripts](#9-scripts)
  - [9.1. Script examples](#91-script-examples)
  - [9.2. Tips for writing scripts](#92-tips-for-writing-scripts)

- [AzimuthConsole v1.x command system](/documentation/EN/Zima/AzimuthConsole_v1x_en.md)

<div style="page-break-after: always;"></div>

## 1. Introduction

The application is designed to work with [Zima2](/documentation/EN/Zima/Zima2_DataBrief_en.md) systems: 
- configuring the devices of the system 
- processing the information received from them and transmitting the results via
  - a serial connection
  - a UDP connection
  - the web interface

### 1.1. Supported platforms

- Windows x64
- Linux x64
- Linux arm64
- Linux arm

[Repository](https://github.com/ucnl/AzimuthConsole)  
[Full list of releases](https://github.com/ucnl/AzimuthConsole/releases).

### 1.2. Hotkeys
For convenience, the application supports the following hotkeys for the most frequently used commands:

| Key combination | Action |
| :--- | :--- |
| F1  | Display the supported commands |
| F12 | Cycle through the terminal output modes: Error messages only, output disabled, output enabled |
| Ctrl+N | **N**etwork: Open the connection (OCON) |
| Ctrl+Shift+N | **N**etwork: Close the connection (CCON) |
| Ctrl+I | **I**nterrogation: Resume interrogation of the responder-beacons |
| Ctrl+Shift+I | **I**nterrogation: Pause interrogation of the responder-beacons |
| Ctrl+L | C**l**ear screen: clear the screen |
| Ctrl+E | **E**xit: Close the application |


### 1.3. Supported devices

- Direction-finding antennas (USBL transceivers)
  - [Zima2B](/documentation/EN/Zima/Zima2B_Specification_en.md)
  - [Zima2B-35](/documentation/EN/Zima/Zima2B35_Specification_en.md)
  - [Zima2BK](/documentation/EN/Zima/Zima2BK_Specification_en.md)
- Responder-beacons
  - [Zima2R](/documentation/EN/Zima/Zima2R_Specification_en.md)
  - [Zima2R-35](/documentation/EN/Zima/Zima2R35_Specification_en.md)
  - [Zima2RK](/documentation/EN/Zima/Zima2RK_Specification_en.md) 
  - [Zima2uR](/documentation/EN/Zima/Zima2uR_Specification_en.md)
- LBL transceivers
  - [Zima2L]()
  - [Zima2L-35]()
  - [Zima2LK]()
  - [Zima2uL]()
 
### 1.4. Recording and storing information

The application does not use any encryption, obfuscation, or hidden storage or transmission of information.
The application keeps a log of the information exchange over all communication channels, which means that location information may be contained in these logs in clear text.
By default, logging of the exchange with the web interface is disabled to save space; the command `weblog,on=TRUE|FALSE` is used to enable/disable logging of the information exchange with the web interface.
At startup, the application calculates the disk space occupied by all log files, and if it exceeds 100 MB, the logs are deleted, starting from the oldest ones, until the occupied space falls below the specified limit.
A new log is created automatically at application startup, named after the current system date and time: `appPath\log\YYYY-MM-DD\hh-mm-ss.log`.


## 2. AzimuthConsole command system

The application is controlled with a **text protocol with named parameters**. This approach provides the following advantages:
- A single protocol for all control channels
- Human readability (commands can be entered manually in the terminal)
- Machine parsability (fixed structure with delimiters)
- Self-documentation (the keys carry semantics)
- Extensibility (new keys do not break old clients)
- Idempotence of get commands (an empty request returns the current value)


### 2.1. Characteristics

| Property | Description |
|----------|----------|
| **Transport** | Local (console), UDP (RCTRL), WebSocket (web interface) |
| **Encoding** | ASCII, UTF-8 |
| **Request format** | `CMD_ID[,key=value,...]` |
| **Response format** | `CMD_ID,OK[,key=value,...]` or `CMD_ID,ERR,msg=...` |
| **Delimiter** | Comma (`,`) |
| **Parameter types** | Integers, real numbers (decimal point), strings, IP:port |
| **Case sensitivity** | Commands are case-insensitive, keys are case-insensitive, values preserve case |
| **Mnemonic** | 3-5 characters, upper case |
| **Feedback** | The response always contains `CMD_ID`, which makes it possible to match requests to responses during asynchronous operation |
| **Empty parameters** | Mean "request the current value" (for get commands) or "do not change" (for set commands) |


### 2.2. Examples

```
→ STAT
← STAT,OK,azm_status=Detected,interrogation=True,position_valid=False

→ LHOV,lat=44.5,lon=39.3,hdg=180
← LHOV,OK

→ AUX1,proto=NMEA,port=COM3,baud=115200
← AUX1,OK

→ PORTS
← PORTS,OK,port0=azm|COM4|Detected,port1=aux1|COM3|Detected
```

### 2.3. Command descriptions

#### 2.3.1. Connection

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| CCON | T,R,W | - | CCON,OK | Close all connections |
| CNA? | T,R,W | - | CNA?,OK,active=TRUE/FALSE | Get the connection status |
| DET? | T,R,W | id=AZM/AUX1/AUX2/RDT | DET?,OK,detected=TRUE/FALSE | Get the status of whether the device has been detected |
| OCON | T,R,W | - | OCON,OK | Open all connections (chain AZM >> AUX1 >> AUX2 >> RDT) |

#### 2.3.2. Ports

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| AUX1 | T,R,W | proto=NMEA/BP,<br/>port=COMx/AUTO/OFF,<br/>baud=N | AUX1,OK | Configuration of the AUX1 port (GNSS/GNSS compass) |
| AUX2 | T,R,W | port=COMx/AUTO/OFF,<br/>baud=N | AUX2,OK | Configuration of the AUX2 port (magnetic compass) |
| AZM | T,R,W | port=COMx/AUTO,<br/>baud=N | AZM,OK | Configuration of the AZM port (transceiver) |
| OUTS | T,R,W | port=COMx/OFF,<br/>baud=N | OUTS,OK | Configuration of the serial output port |
| OUTU | T,R,W | addr=ip:port/OFF | OUTU,OK | Configuration of the UDP output channel |
| PORTS | T,R,W | - | PORTS,OK,<br/>port0=id\|port\|status,... | Get the status of all connections |
| RCTRL | T,R,W | in=port,out=ip:port | RCTRL,OK | Configuration of the remote UDP terminal |
| RDT | T,R,W | port=COMx/AUTO/OFF,<br/>baud=N | RDT,OK | Configuration of the serial port of the Radant rotator |
| SIOC | T,R,W | addr=N,ep=ip:port/OFF | SIOC,OK | Configuration of individual UDP channels for beacons |

#### 2.3.3. Beacon interrogation

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| ITG? | T,R,W | - | ITG?,OK,<br/>active=TRUE/FALSE | Get the interrogation status |
| PITG | T,R,W | - | PITG,OK | Pause beacon interrogation |
| RITG | T,R,W | - | RITG,OK | Resume beacon interrogation |

#### 2.3.4. Transceiver

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| CREQ | T,R,W | addr=N,<br/>code=N | CREQ,OK | Request user values from a beacon (addr=1-16, code=3-30) |
| MDST | T,R,W | val=N | MDST,OK,val=N | Set/get the maximum range, m |
| MSK | T,R,W | mask=N | MSK,OK,mask=N | Set/get the beacon address mask* |
| SLN | T,R,W | val=N | SLN,OK,val=N | Set/get the salinity, PSU |
| SOS | T,R,W | val=N | SOS,OK,val=N | Set/get the speed of sound (m/s). Empty value/NaN = automatic calculation |

##### 2.3.4.1. Determining the address mask from beacon addresses

The system supports operation with 16 beacons whose addresses correspond to the numbers from 1 to 16. The mask is specified as a 16-bit number; for example, if the beacon with address 1 is interrogated, only the least significant bit is set in the mask and its value is 1.

Each beacon with address N can be assigned a number equal to 2^(N-1):

| Beacon address |	Number	| Beacon address |	Number	|
| :--- | :--- | :--- | :--- |
| 1	| 1	| 9 | 256 |
| 2	| 2	| 10 | 512 |
| 3	| 4	| 11 | 1024 |
| 4	| 8	| 12 | 2048 |
| 5	| 16 | 13 | 4096 |
| 6	| 32 | 14 | 8192 |
| 7	| 64 | 15 | 16384 |
| 8	| 128 | 16 | 32768 |

To calculate the address mask:
1. Select from the table above the numbers corresponding to the required beacons:
3. Add these numbers; their sum is the address mask.

For example, if you plan to work with beacons 1 and 2:
The address mask will be: 1 + 2 = 3

If you need to work with beacons 2, 7 and 9:
The address mask will be: 2 + 64 + 256 = 322

#### 2.3.5. Position

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| LHO? | T,R,W | - | LHO?,OK,<br/>active=TRUE/FALSE | Get the status of the manual setting of position and orientation |
| LHOV | T,R,W | hdg=N[,lat=N][,lon=N] | LHOV,OK | Set the heading (mandatory) and, optionally, the antenna coordinates manually. Empty parameters disable the mode |
| OFS | T,R,W | x=N,y=N,phi=N | OFS,OK,<br/>x=N,y=N,phi=N | Get/set the offset of the antenna from the position reference point and the angular offset of the antenna zero from the compass zero (X,Y in m, Phi in degrees) |
| SRC3 | T,R,W | mode=0/1/2,c0..c5=N | SRC3,OK | Set the coordinates of the reference beacons for the LBL mode (0=discard,1=cartesian,2=geographic) |

#### 2.3.6. Beacon configuration

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| RRA? | T,R,W | - | RRA?,OK | Get the current beacon address |
| SRRA | T,R,W | addr=N | SRRA,OK | Set the beacon address |

#### 2.3.7. Service

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| EXIT | T,R,W | - | EXIT,OK | Terminate the application |
| EXPCR | T,R,W | file=path | EXPCR,OK | Export the description of the application commands in Markdown format |
| HELP | T,R,W | cmd=? | HELP,OK,commands=... | Show help for all commands or for the specified command |
| HKEYS | T,R,W | - | HKEYS,OK,hotkeys=... | Get the hotkeys hint |
| PLAY | T,R,W | speed=0\|1,file=path | PLAY,OK | Play back a log file (speed=0 — instantly, speed=1 — real time (default), without `file` — stop) |
| RESETINIT | T,R,W | - | RESETINIT,OK | Delete init.cmd - reset the settings to default |
| SAVE | T,R,W | file=path | SAVE,OK | Save the current settings to a script |
| SAVEINIT | T,R,W | - | SAVEINIT,OK | Save the current settings to the initialization script (init.cmd) |
| SCRIPT | T | file=path | SCRIPT,OK | Execute the script from the specified file |
| STAT | T,R,W | - | STAT,OK,azm_status=...,<br/>interrogation=...,... | Get a brief system status |
| VER | T,R,W | - | VER,OK,version=... | Get the application version information |
| WAIT | T | for=ACAL\|CAL\|OCON\|DETECTED\|N,<br/>timeout=N,port=id | WAIT,OK | Wait for an event: ACAL=angular calibration completed, CAL=rotator calibration completed, OCON=connection established, DETECTED=port detected, N=timeout in ms |

#### 2.3.8. Log file management

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| DELGS | T,R,W | - | DELGS,OK | Delete all log files and folders except the current one |
| WEBLOG | T,R,W | on=TRUE/FALSE | WEBLOG,OK | Control logging of the exchange with the web interface (OFF by default) |

#### 2.3.9. Output data configuration

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| OFMT? | T,R,W | - | OFMT?,OK,format=... | Get the description of the output message format |
| PSIMSSB | T,R,W | on=TRUE/FALSE,mode=H\|NE | PSIMSSB,OK | Enable/disable emulation of the PSIMSSB protocol (Simrad/HiPAP) |

#### 2.3.10. Calibrations

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| ACAL | T,R,W | start=N,<br/>end=N,step=N,<br/>n=N,addr=N | ACAL,OK | Start the calibration of the angular offset between the zero direction of the antenna and the compass |
| CAL? | T,R,W | - | CAL?,OK,state=...,<br/>points=N,total=N,<br/>angle=N,<br/>acal_state=...,<br/>acal_collected=N,<br/>acal_total=N,<br/>[acal_phi=N] | Get the status of the rotator (SCAL) and angular (ACAL) calibrations |
| FCAL | T,R,W | - | FCAL,OK | Abort the calibration |
| SCAL | T,R,W | start=N,step=N,n=N | SCAL,OK | Start the antenna calibration on the rotator (default: start=0,step=15,n=20) |

#### 2.3.11. Reference beacon mode

| Command | Channels | Parameters | Response | Description |
| :--- | :--- | :--- | :--- | :--- |
| AMODE | T,R,W | mode=geographic\|cartesian_fixed\|beacon_referenced | AMODE,OK,mode=... | System operating mode |
| RBADD | T,R,W | addr=N,lat=N,lon=N,[depth=N] | RBADD,OK | Add/change a reference beacon (addr=1-16, lat/lon in degrees) |
| RBCLR | T,R,W | - | RBCLR,OK | Delete all reference beacons |
| RBDEL | T,R,W | addr=N | RBDEL,OK | Delete a reference beacon by address (1-16) |
| RBLST | T,R,W | - | RBLST,OK,count=N,beacons=addr:lat:lon:depth;... | Get the list of reference beacons |
| SHPZ | T,R,W | maxspeed=N[,threshold=N][,fifo=N][,maxage=N][,maxspread=N] | SHPZ,OK,maxspeed=...,threshold=...,fifo=...,maxage=...,maxspread=... | Get/Set the filtering parameters for the vessel position in the reference beacon mode |

The `beacon_referenced` mode makes it possible to determine the vessel's coordinates **without external navigation sources** (GNSS, compass) — from responder-beacons with **known coordinates** (reference beacons).

**Principle of operation:**
- The user specifies one or more reference beacons with known coordinates (`RBADD`)
- Each response received from a reference beacon gives a **separate estimate** of the vessel's coordinates
- The estimates are filtered by the DH filter and accumulated in a buffer
- The final vessel position is calculated as the **median** of the valid measurements with spread control
- The coordinates of the target (non-reference) beacons are calculated relative to the current vessel position

**System operating modes** (the `AMODE` command):

| Mode | Description |
| :--- | :--- |
| `geographic` | Normal USBL mode — the vessel coordinates are taken from GNSS (AUX1) |
| `cartesian_fixed` | Cartesian coordinate system with a stationary antenna at point (0,0,0). X — to the right (East), Y — forward (North), Z — down (depth) |
| `beacon_referenced` | The vessel coordinates are determined from the reference beacons with known coordinates |

**Parameters of the vessel DH filter and buffer** (the `SHPZ` command):

| Parameter | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| `maxspeed` | 2.0 | 0.5 .. 50 | Maximum vessel speed, m/s |
| `threshold` | 8.0 | 0.5 .. 500 | DH filter threshold, m |
| `fifo` | 8 | 2 .. 32 | DH filter FIFO size |
| `maxage` | 20000 | 1000 .. 600000 | Buffer entry lifetime, ms |
| `maxspread` | 50.0 | 1 .. 5000 | Maximum spread between estimates, m |

**Configuration example:**
```
AMODE,mode=beacon_referenced
SHPZ,maxspeed=2.0,threshold=8,fifo=8,maxage=20000,maxspread=50
RBADD,addr=1,lat=46.6200135,lon=142.703034,depth=22.8
RBADD,addr=2,lat=46.6210000,lon=142.705000,depth=25.0
RITG
```

---
*Channels: T=Terminal, R=RCTRL (UDP), W=Web*


## 3. Web interface

The **AzimuthConsole** application includes a built-in web server that provides a graphical interface for monitoring and controlling the Zima2 system. The web interface is available through any modern browser and does not require installing additional software on the client device.

### 3.1. Connection

After the application is started, the web interface is available at the address:

The IP address can be found with the command:
- **Windows:** `ipconfig`
- **Linux/Raspberry Pi:** `hostname -I` or `ip a`

If the application is running on the same computer from which the browser is opened, use `http://localhost:8080`.

If the web interface cannot be accessed from the local network, you may need to open the port in the firewall of the Windows machine (see the section [Configuring access from the local network](#61-configuring-access-from-the-local-network)).

### 3.2. Main interface elements

The web interface consists of two main areas: the **map** (on the left) and the **side panel** (on the right).

#### 3.2.1. Map

The map displays:

- **Antenna/station position** — a diamond at the center (or at the point with coordinates X,Y in LBL mode). Color: light blue (USBL) or blue (LBL). The depth and speed are displayed next to it.
- **Direction (heading)** — a red arrow from the antenna. It is displayed when data from a GNSS compass or a magnetic compass is available, or when the direction is set manually (LHOV).
- **Direction of motion (course)** — a green arrow. It is displayed when GNSS data is available.
- **Responder-beacons** — circles with numbers. They are connected to the antenna by lines. The color depends on the age of the data:
  - Normal — the data is fresh (up to 5 s)
  - Yellow — the data is getting stale (5–10 s)
  - Red — timeout (more than 10 s)
- **Scale bar** — in the lower right corner of the map

**Map controls** (upper right corner):

| Button | Action |
| :---: | :--- |
| **+** | Zoom In |
| **−** | Zoom Out |
| **Reset** | Reset the scale and position |
| **A** | Auto Scale (on/off) — adjusts the scale so that all beacons are visible |
| **⚙** | Open the settings window |

**Interacting with the map:**
- Dragging with the mouse — panning
- Mouse wheel / pinch (on touch screens) — changing the scale
- When auto scaling is enabled, the map adjusts automatically when new beacons appear

#### 3.2.2. Command line

Located above the map, in the center. It lets you send any AzimuthConsole protocol command directly.

- **Input field** — supports autocompletion of commands and parameters based on the schema received from the server
- **Command history** — stored in the browser's local storage (up to 100 commands). Navigation: arrow keys ↑↓
- **Send** button — sends the command

Command line hotkeys:
- **Enter** — send the command
- **↑/↓** — navigate through the history
- **Tab** — accept the active autocompletion suggestion
- **Esc** — close the autocompletion drop-down list

The command execution status is displayed under the control buttons in the side panel.

#### 3.2.3. Side panel

The side panel (on the right) contains:

**📡 Beacons** — a list of the detected responder-beacons with detailed information for each:
- Azimuth and distance (relative and absolute, if GNSS is available)
- Depth, temperature, supply voltage
- Signal level (MSR), propagation time
- Computed coordinates (latitude, longitude)
- Timeout flag

Beacons are grouped by address; for each one the status (active/warning/timeout) and the age of the data are displayed.

**🎮 Control** — control buttons:
- **Open/Close** — open/close the connection to the devices
- **Interrogate/Pause** — start/pause beacon interrogation
- Status line — the result of the last executed command

**📋 Log** — a log of the latest messages (up to 8 entries). Download links are available:
- 📄 — download the current log
- 📦 — download an archive of all logs (ZIP)

At the bottom of the side panel there are links to GitHub, the documentation and the license.

#### 3.2.4. Information panels on the map

**Connection status panel** (upper left corner):
- 🟢 CONNECTED / 🔴 DISCONNECTED

**System information panel** (upper left corner, under the status):
- Operating mode (USBL/LBL/beacon_referenced)
- Device serial number
- Age of the antenna data (color indicator: green < 5 s, yellow 5–10 s, red > 10 s)
- Connection (🟢/🔴) and interrogation (🔵/⚪) status
- Antenna immersion depth

On mobile devices the panel is collapsed; when tapped, it expands with detailed information in three sections:

- **POSITION** — the vessel coordinates (`Lat`/`Lon` to 6 decimal places). In LBL mode the Cartesian coordinates `X`/`Y`/`Z` are additionally displayed
- **ORIENTATION** — course (`course`, green), heading (`heading`, red), speed, roll (`pitch`), pitch (`roll`)
- **ENVIRONMENT** — water temperature, external pressure, antenna immersion depth

**Port status panel** — displays the state of all configured ports (AZM, AUX1, AUX2, RDT) with the following indicators:
- ✓ — the port is detected (Detected)
- ↻ — the port is active (Active)
- ○ — the port is inactive

#### 3.2.5. Calibration panels

**📡 Calibration** — the panel for calibration on the rotator (SCAL). It is displayed only when the RDT device (Radant rotator) is connected. It contains:
- Start/Stop buttons
- Status (Idle/Moving/Measuring/Completed/Failed)
- Progress (points/total)
- Current angle of the rotator

**🔄 Angular Calibration** — the angular calibration panel (ACAL). It is displayed when there is activity (the state differs from idle, or after completion). It contains:
- Status (Idle/Collecting/Completed)
- Number of accumulated measurements
- Result: the computed angular correction φ

### 3.3. Settings window

Opened with the **⚙** button on the map. It contains the tabs:

**🔌 Ports:**
- AZM — port and baud rate for the direction-finding antenna
- AUX1 — protocol (NMEA/BP), port and baud rate for the external GNSS/GNSS compass
- AUX2 — port and baud rate for the magnetic compass
- RDT — port and baud rate for the rotator

**📤 Output:**
- Serial port for outputting navigation data
- UDP address for broadcasting
- Enabling/disabling the PSIMSSB format (Simrad/HiPAP)

**📍 Position:**
- Antenna offsets (X, Y, angle φ)
- Manual setting of coordinates and heading (Location Override)

**📡 Transceiver:**
- Beacon address mask (with a visual editor — a checkbox for each address)
- Water salinity
- Maximum distance
- Speed of sound (or auto-detection)

The **Apply & Restart** button applies the transceiver settings and restarts beacon interrogation. The **Apply All** button applies all settings and closes the window.

Service buttons:
- **💾 Save as default settings** — saves the current settings as init.cmd (loaded at startup)
- **🗑 Reset default settings** — deletes init.cmd (the next start will be with the factory settings)

### 3.4. Mobile version

The web interface is adapted for mobile devices. When the screen width is less than 768 px:

- The map and the side panel are arranged vertically
- The panel divider is hidden
- The side panel is displayed under the map
- The map controls are enlarged for convenient touch input
- The control buttons (Open/Close, Interrogate/Pause) are enlarged
- The command line moves to the upper left corner
- The information panels are scaled

### 3.5. Language support

The interface supports Russian and English. The language is determined automatically from the browser settings.



## 4. Output data

### 4.1. AZMLOC - local parameters
The message is transmitted about once per second (1 Hz) when a connection to the direction-finding antenna or an LBL transceiver is open.

Message format:
```
@AZMLOC,stPressure_mBar,stDepth_m,waterTemp_C,stPitch_deg,stRoll_deg,age,lat_deg,lon_deg,course_deg,speed_mps,age,heading_deg,age,x_m,y_m,z_m,rerr_m,age,
```

| No. | Parameter name | Type | Units | Value range | Description | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | stPressure_mBar | f32 | mbar | 0 .. 30 | External pressure | Built-in sensor |
| 2 | stDepth_m | f32 | m | 0 .. 300 | Immersion depth of the device | Built-in sensor |
| 3 | waterTemp_C | f32 | °C | -4 .. 40 | Ambient temperature | Built-in sensor |
| 4 | stPitch_deg | f32 | ° | -180 .. 180 | Roll | Built-in sensor |
| 5 | stRoll_deg | f32 | ° | -180 .. 180 | Pitch | Built-in sensor |
| 6 | age | f32 | s | 0 .. | Age of the previous values | System clock |
| 7 | lat_deg | f32 | ° | -90 .. 90 | Geographic latitude | External source **AUX1** or the value set by the LHOV command |
| 8 | lon_deg | f32 | ° | -180 .. 180 | Geographic longitude | External source **AUX1** or the value set by the LHOV command |
| 9 | course_deg | f32 | ° | 0 .. 360 | Course (direction of motion) | External source **AUX1** |
| 10 | speed_mps | f32 | m/s | 0 .. | Speed | External source **AUX1** |
| 11 | age | f32 | s | 0 ..  | Age of the previous values | System clock |
| 12 | heading_deg | f32 | ° | 0 .. 360 | Azimuth angle | External source **AUX1** or **AUX2** or the value set by the LHOV command |
| 13 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 14 | x_m | f32 | m | | Calculated position: X coordinate (LBL mode) | Calculated value |
| 15 | y_m | f32 | m | | Calculated position: Y coordinate (LBL mode) | Calculated value |
| 16 | z_m | f32 | m | 0 .. 300 | Immersion depth of the device (same value as field No. 2) | Built-in sensor |
| 17 | rerr_m | f32 | m | | Radial position error (LBL mode) | Calculated value |
| 18 | age | f32 | s | 0 .. | Age of the previous values | System clock |

> **Important regarding the `age` fields:**
> 
> The `age` field applies to **all preceding fields**, starting from the last `age` field (or from the beginning of the message). This avoids duplicating the age for a group of fields that are updated simultaneously.
> 
> Example for `@AZMLOC`: `age` field No. 6 applies **both to `stPitch_deg` (4) and to `stRoll_deg` (5)** — both of these sensors are updated simultaneously.
> 
> Fields whose age is **not output** (for example, `lat_deg`, `lon_deg`, `course_deg` in `@AZMLOC`) are called **IgnoreAge** — they always come without their own `age`. If the value of such a field is not initialized (there is no data from the source), the message will contain an **empty field** in its place (between two commas).


### 4.2. AZMREM - responder-beacon data
The message is transmitted separately for each of the beacons when the information is updated - when a beacon response is received or when a timeout occurs.

Message format:
```
@AZMREM,rem_addr,SRange_m,Azimuth_deg,PTime_s,MSR_dB,age,Depth_m,age,SRangeProjection_m,age,ADistance_m,age,AAzimuth_deg,age,Elevation_deg,age,VCC_V,age,WaterTemp_C,age,Lat_deg,Lon_deg,age,RAzimuth_deg,age,Message,age,X_m,Y_m,Z_m,IsTimeout
```

| No. | Parameter name | Type | Units | Value range | Description | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | rem_addr | u8 | - | 0 .. 15 | Address of the responder-beacon | - |
| 2 | SRange_m | f32 | m | 0 .. | Slant range between the antenna and the beacon. Negative values are allowed | Measurement |
| 3 | Azimuth_deg | f32 | ° | 0 .. 360 | Horizontal angle of arrival of the responder-beacon signal relative to the zero direction of the antenna | Measurement |
| 4 | PTime_s | f32 | s | 0 .. | Signal propagation time from the beacon to the antenna. Negative values are allowed | Measurement |
| 5 | MSR_dB | f32 | dB | 14 ..  | Quality of reception of the responder-beacon signal. Values below 20 dB indicate poor conditions | Measurement |
| 6 | age | f32 | s | 0 .. | Age of the previous values | System clock |
| 7 | Depth_m | f32 | m | 0 .. 300/350/500/1000 | Depth of the responder-beacon | Built-in sensor of the responder-beacon |
| 8 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 9 | SRangeProjection_m | f32 | m | 0 .. | Projection of the slant range onto the surface | Calculated value |
| 10 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 11 | ADistance_m | f32 | m | 0 .. | Distance from the position reference point to the responder-beacon along the water surface | Calculated value |
| 12 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 13 | AAzimuth_deg | f32 | ° | 0 .. 360 | Absolute azimuth to the responder-beacon from the position reference point | Calculated value |
| 14 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 15 | Elevation_deg | f32 | ° | 0 .. 360 | Elevation angle of the responder-beacon | Calculated value |
| 16 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 17 | VCC_V | f32 | V | 4 .. 16 | Supply voltage of the responder-beacon | Built-in sensor of the responder-beacon |
| 18 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 19 | WaterTemp_C | f32 | °C | -4 .. 46 | Ambient temperature | Built-in sensor of the responder-beacon |
| 20 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 21 | Lat_deg | f32 | ° | -90 .. 90 | Geographic latitude of the responder-beacon | Calculated value |
| 22 | Lon_deg | f32 | ° | -180 .. 180 | Geographic longitude of the responder-beacon | Calculated value |
| 23 | age | f32 | s | 0 .. | Age of the previous values | System clock |
| 24 | RAzimuth_deg | f32 | ° | 0 .. 360 | Absolute azimuth to the station from the responder-beacon | Calculated value |
| 25 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 26 | Message | string | - | - | The last message from the responder-beacon (error, diagnostics, response to a request). Empty if there were no messages | - |
| 27 | age | f32 | s | 0 .. | Age of the previous value | System clock |
| 28 | X_m | f32 | m | - | Position in the local Cartesian coordinate system: X coordinate (LBL mode) | Set by the user |
| 29 | Y_m | f32 | m | - | Position in the local Cartesian coordinate system: Y coordinate (LBL mode) | Set by the user |
| 30 | Z_m | f32 | m | 0 .. 300/350/500/1000 | Depth of the responder-beacon | Built-in sensor of the responder-beacon |
| 31 | IsTimeout | bool/string |  | true/false | Timeout flag - the responder-beacon response waiting interval has been exceeded | - |

> **Important regarding the `age` fields:**
> 
> The grouping logic is the same as in `@AZMLOC`: the `age` field applies to **all preceding fields** since the previous `age` (or since the beginning of the message).
> 
> Examples for `@AZMREM`:
> 
> - `age` field No. 6 applies to `MSR_dB` (5) — one sensor, one age.
> - The `Lat_deg` (21) and `Lon_deg` (22) fields have a **common** `age` — field No. 23. This makes sense: the beacon coordinates are calculated simultaneously, and they have a single age.
> - `age` field No. 27 (after `Message`) applies only to `Message` (26).
> 
> **IgnoreAge fields in `@AZMREM`** (`SRange_m`, `Azimuth_deg`, `PTime_s`, `Lat_deg`, `Lon_deg`, `X_m`, `Y_m`, `Z_m`) **do not have** their own `age` — their age is determined by the nearest following `age` field in the message.
> 
> **Empty fields.** If the value of a field is not initialized (for example, `WaterTemp_C` for a beacon without a temperature sensor), the message will contain an **empty field** in its place, and its `age` will also be empty. This is a normal situation, not an error.
> 
> **The `Message` field.** Contains a **text** message from the responder-beacon (error, diagnostics, response to a user request). If there are no messages, the field is empty. Do not confuse it with the numeric fields — `Message` is not a number.

## 5. Auxiliary utilities

### 5.1. AzimuthUDPRemote - UDP terminal
This demo utility provides a quick way to try out remote control of AzimuthConsole over UDP, if this option is enabled.
After the application starts, the user can enter commands that will be passed to AzimuthConsole; the results of execution will be displayed in the application window.

By default, the application listens on port 28129 and transmits data to the address 255.255.255.255:28127. To use other values, they must be specified as command line parameters. The command line format is as follows:

```
AzimuthUDPRemote [in_port] [out_address:port]
```

Since all user commands are transmitted over UDP, two additional commands are provided for controlling the application itself:

- xcls - clear the screen
- xexit - exit the application

### 5.2. AzimuthUDPListener - UDP receiver
This demo utility provides a quick way to try out the transmission of output data (see [3. Output data](#4-output-data)) over UDP.

By default, the application listens on port 28128 and outputs the received data to the console window.
To specify a different port for receiving data from AzimuthConsole, specify the port number as a command line parameter when starting the application. Command line format:

```
AzimuthUDPListener [in_port]
```

To close the application, press the **Enter** key.

## 6. Application deployment scenarios

### 6.1. Configuring access from the local network

- Run the application as administrator
- Determine the IP address of the machine:
  - Win: `cmd > ipconfig, in the line with IPv4 Address`
  - Linux: `ip a or hostname -I`
- Check the availability of the machine: `ping <ip-address>`
- Open `http://<ip-address>:8080` in a browser

If the application is running on a Windows machine and the server cannot be accessed from the local network, do the following:
- Run a terminal as administrator and execute:
   `New-NetFirewallRule -DisplayName "WebServer 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow`

## 7. Setting up a Raspberry Pi with application autostart

### 7.1. What you will need

- Raspberry Pi (any model)
- MicroSD card (8 GB or larger, Class 10)
- Power supply
- Internet access (Wi-Fi or Ethernet)
- A compiled self-contained .NET application for ARM32 (`linux-arm`) or ARM64 (`linux-arm64`)

### 7.2. System preparation

#### 7.2.1. Writing the image to an SD card

1. Download **Raspberry Pi Imager** from the [official website](https://www.raspberrypi.com/software/)
2. Select: **Raspberry Pi OS Lite** — without a desktop, lighter and faster
3. In the settings (the gear icon) you can set the following right away:
   - Hostname: `myapp-server`
   - Enable SSH
   - Login/password
   - Wi-Fi network
4. Write the image to the card

#### 7.2.2 First boot and basic setup

```bash
# Connect via SSH or directly and run
sudo raspi-config
```

**What to configure:**
- `System Options` → `Password` — change the password
- `System Options` → `Hostname` — set a convenient name on the network
- `System Options` → `Boot / Auto Login` → `Console Autologin`
- `Localisation Options` → `Timezone` — set the time zone
- `Interface Options` → `SSH` — enable if not enabled

After exiting, reboot the system.

#### 7.2.3 Updating packages

```bash
sudo apt update && sudo apt upgrade -y
```


### 7.3. Installing the application

#### 7.3.1 Creating the directory

```bash
sudo mkdir -p /opt/ac
sudo chown $USER:$USER /opt/ac
```

#### 7.3.2 Copying files from a USB flash drive

```bash
# List the devices
lsblk

# Mount the flash drive (usually /dev/sda1)
sudo mkdir -p /mnt/usb
sudo mount /dev/sda1 /mnt/usb

# Copy the contents
cp -r /mnt/usb/* /opt/ac/

# Grant execute permission to the executable file
chmod +x /opt/ac/AzimuthConsole

# Unmount the flash drive
sudo umount /mnt/usb
```

#### 7.3.3 Alternative: copying via SCP from a computer

```bash
# Run ON THE COMPUTER, not on the Raspberry Pi
scp -r ./publish/* pi@192.168.1.XXX:/opt/ac/
```

### 7.4. Creating startup scripts

#### 7.4.1 Script for manual start `start.sh`

```bash
nano /opt/ac/start.sh
```

```bash
#!/bin/bash
cd /opt/ac
./AzimuthConsole 
```

#### 7.4.2. Script for the daemon `dstart.sh`

```bash
nano /opt/ac/dstart.sh
```

```bash
#!/bin/bash
cd /opt/ac
./AzimuthConsole "daemon"
```

#### 7.4.3. Execute permissions

```bash
chmod +x /opt/ac/start.sh
chmod +x /opt/ac/dstart.sh
```


### 7.5. Configuring autostart (systemd)

#### 7.5.1. Creating the service

```bash
sudo nano /etc/systemd/system/ac.service
```

```ini
[Unit]
Description=AzimuthConsole
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/ac
ExecStart=/opt/ac/dstart.sh
Restart=on-failure
RestartSec=10
TimeoutStopSec=30
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

#### 7.5.2. Activating the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable ac.service
sudo systemctl start ac.service
```

### 7.6. Checking operation

#### 7.6.1. Service status

```bash
sudo systemctl status ac.service
```

Expected status: `Active: active (running)`

#### 7.6.2. Viewing logs

```bash
# The last 50 lines
sudo journalctl -u ac.service -n 50 --no-pager

# In real time
sudo journalctl -u ac.service -f
```

#### 7.6.3. Finding the IP address

```bash
hostname -I
```

#### 7.6.4. Access from a browser

From any device on the network: `http://IP_ADDRESS:8080`


### 7.7. Managing the application

| Action | Command |
|----------|---------|
| Start | `sudo systemctl start ac.service` |
| Stop | `sudo systemctl stop ac.service` |
| Restart | `sudo systemctl restart ac.service` |
| Status | `sudo systemctl status ac.service` |
| Enable autostart | `sudo systemctl enable ac.service` |
| Disable autostart | `sudo systemctl disable ac.service` |
| Logs | `sudo journalctl -u ac.service -f` |


### 7.8. Updating the application

```bash
# 1. Stop the service
sudo systemctl stop ac.service

# 2. Copy the new files (from a flash drive or via SCP) to /opt/ac/

# 3. Update the permissions
chmod +x /opt/ac/AzimuthConsole

# 4. Start the service
sudo systemctl start ac.service

# 5. Check the status
sudo systemctl status ac.service
```


### 7.9. Useful commands

```bash
# Reboot the Raspberry Pi
sudo reboot

# Shut down
sudo shutdown -h now

# System information
uname -a
cat /etc/os-release

# Free space
df -h

# Processes
htop  # if installed, otherwise top
```


### 7.10. Possible problems and solutions

| Problem | Solution |
|----------|---------|
| The service crashes with `exited` | Check the logs: `journalctl -u ac.service -n 50` |
| `failed to determine user credentials` | Set `User=root` in `/etc/systemd/system/ac.service` |
| The application does not start manually | Check the permissions: `chmod +x /opt/ac/AzimuthConsole` |
| Wrong architecture | Build for `linux-arm`: `dotnet publish -r linux-arm` |


Additional information:
- **Server IP:** `hostname -I`
- **Application directory:** `/opt/ac/`
- **Service file:** `/etc/systemd/system/ac.service`

*This guide is up to date as of 2026, for Raspberry Pi OS Lite*



## 8. Running as a Windows service

### 8.1. Step-by-step instructions

1.  **Open the command prompt as administrator**:
    Press `Win`, type `cmd`, right-click and select "Run as administrator".

2.  **Create the service (replace the paths with your own)**:
    Run the following command. Here `binPath=` is the path to the `.exe` file, and `start= auto` means automatic start at system startup.
    ```cmd
    sc create "AzimuthConsoleService" binPath= "\"C:\opt\ac\AzimuthConsole.exe\" daemon start= auto
    ```
    *Important:* The space after `=` in the `binPath=` and `start=` parameters is mandatory.

3.  **Configure the service**:
    To make the service restart after failures (like `Restart=on-failure` in a systemd unit):
    ```cmd
    sc failure "AzimuthConsoleService" reset= 86400 actions= restart/60000/restart/60000/restart/60000
    ```
    *   `reset= 86400` — resets the failure counter after one day.
    *   `actions= restart/60000` — restarts the service 60 seconds after a crash (and so on, up to three times).

4.  **Start the service**:
    ```cmd
    sc start "AzimuthConsoleService"
    ```

### 8.2. Alternative option via a bat file

1. Create the file `C:\opt\ac\dstart.bat`

```
C:\opt\ac\AzimuthConsole.exe daemon
```

2. Command to initialize the service
```
sc create "AzimuthConsoleService" binPath= "C:\opt\ac\dstart.bat" start= auto
```

### 8.3. Management and verification

*   **View the service status**:
    ```cmd
    sc query "AzimuthConsoleService"
    ```
*   **Graphical interface**: Press `Win + R`, type `services.msc` and press Enter. In the window that opens, find the service "MyAppService", where you can start, stop or change its properties manually.

**Key difference from Linux**:
If the application has a graphical interface (GUI), there is no need to create a service — Windows services are not designed to interact with the desktop. In this case it is enough to add a shortcut to the application to the startup folder (`shell:startup`), and it will be launched when the user logs in to the system.

## 9. Scripts

To be able to specify the required set of settings at startup or to perform any repetitive actions, the application supports processing scripts and saving the current settings as a script - a sequence of commands that set the required settings.
Essentially, scripts are files in which each line represents one control command.

At startup, the application tries to execute an initialization script with the fixed name `init.cmd`.
If there is no such file, the default settings are used. 
The `RESETINIT` command deletes the initialization script, and the `SAVEINIT` command saves the current settings to it.

An arbitrary script is executed with the `SCRIPT,file=path` command. 
Thus, to set all the settings there is no need to specify them on the command line; it is enough to specify a single `SCRIPT` command with the corresponding file as the `file` parameter.

This is convenient, for example, when you need to run different scenarios with different system configurations - with or without external navigation data providers, with or without a manually set antenna position and orientation relative to north, for operation in USBL or LBL mode, for different sets of responder-beacons, etc.

A script can contain comments - lines starting with the `#` character - and empty lines; both are ignored during execution.

For scripts to work properly, in particular to implement the event waiting mechanism, the WAIT command is used.
The following can be used as an event:
- `ACAL` - completion of the angular calibration
- `CAL` - completion of the calibration on the rotator
- `OCON` - opening of the connection
- `DETECTED` - detection of the specified device
The command supports specifying the maximum waiting interval - a timeout, after which the event is considered to have occurred.

The full description of the command format is given in the table [2.3.7. Service](#237-service).

Another important command for automation is `SAVE,file=path` - it saves the current application settings as a script, which can then be used to start the application with these settings. The `SAVEINIT` command is equivalent to `SAVE,file=init.cmd`.

### 9.1. Script examples

**Example 1. USBL with an external GNSS (`geographic` mode)**

```
#Port configuration
AZM,port=AUTO,baud=9600
AUX1,proto=NMEA,port=AUTO,baud=115200
AUX2,port=OFF

#Transceiver
MSK,mask=1
SLN,val=0.0
MDST,val=1000
SOS,val=1452

#Output
OUTS,port=OFF
OUTU,addr=255.255.255.255:28128

#Start
OCON
WAIT,for=OCON,timeout=30000
RITG
```

**Example 2. Reference beacon mode (`beacon_referenced`)**

```
#AZM only, no external navigation sources
AZM,port=AUTO,baud=9600
AUX1,port=OFF
AUX2,port=OFF

#Transceiver
MSK,mask=3
SLN,val=0.0
MDST,val=1000
SOS,val=1452

#Reference beacon mode
AMODE,mode=beacon_referenced
SHPZ,maxspeed=2.0,threshold=8,fifo=8,maxage=20000,maxspread=50

#Reference beacons (1-based addresses)
RBADD,addr=1,lat=46.6200135,lon=142.703034,depth=22.8
RBADD,addr=2,lat=46.6210000,lon=142.7050000,depth=25.0

#Start
OCON
WAIT,for=OCON,timeout=30000
RITG
```

**Example 3. USBL with manual setting of coordinates (`LHOV`)**

```
#AZM only, the coordinates are set manually
AZM,port=AUTO,baud=9600
AUX1,port=OFF
AUX2,port=OFF

#Transceiver
MSK,mask=1
SLN,val=0.0
MDST,val=1000
SOS,val=1452

#Manual setting of coordinates and heading
LHOV,lat=46.6200135,lon=142.703034,hdg=0.0

#Start
OCON
WAIT,for=OCON,timeout=30000
RITG
```


**Example 4. LBL with three beacons (geographic coordinates)**

```
AZM,port=AUTO,baud=9600
AUX1,proto=NMEA,port=AUTO,baud=115200

MSK,mask=7
SLN,val=0.0
MDST,val=1000

Coordinates of the three reference beacons (mode=2 — geographic)
SRC3,mode=2,c0=142.703034,c1=46.6200135,c2=142.705000,c3=46.621000,c4=142.700000,c5=46.619000

OCON
WAIT,for=OCON,timeout=30000
RITG
```

**Example 5. Antenna calibration on the rotator**

```
AZM,port=AUTO,baud=9600
RDT,port=AUTO,baud=9600

MSK,mask=1
SLN,val=0.0
MDST,val=1000

#Open the connection and wait for AZM and RDT to be detected
OCON
WAIT,for=DETECTED,port=azm,timeout=30000
WAIT,for=DETECTED,port=rdt,timeout=30000

#Start the calibration: start 0°, step 15°, 20 points
SCAL,start=0,step=15,n=20
WAIT,for=CAL,timeout=600000

#Save the result
SAVE,file=calibration.cmd
```


### 9.2. Tips for writing scripts

- **The order of commands matters.** First the ports are configured (`AZM`, `AUX1`, `AUX2`), then the transceiver parameters (`MSK`, `SLN`, `MDST`, `SOS`), then the mode (`AMODE`), and at the end `OCON` and `RITG`.
- **Use `WAIT` for synchronization.** If the next command depends on the result of the previous one (for example, `RBADD` after `AMODE`), add `WAIT`.
- **Comments.** Lines starting with `#` are ignored. So are empty lines.
- **`SAVEINIT` vs `SAVE`.** `SAVEINIT` saves to `init.cmd` — this script is executed automatically at application startup. `SAVE,file=path` saves to an arbitrary file, which can then be executed with the `SCRIPT,file=path` command.
- **Check after startup.** After the script has been executed, it is useful to run `STAT` — it will show the current state of the system.





<div style="page-break-after: always;"></div>

[Back to contents](#toc)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/AzimuthConsole_manual_ru.md commit=064c8b236490d2cebf08087f779ba144e3307c2b date=2026-09-25 -->
