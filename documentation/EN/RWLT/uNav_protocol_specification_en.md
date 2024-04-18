[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **uNav: protocol specification**

> ℹ This document can be printed directly from your browser.
> For best results:
> - select the range of pages to print, excluding the first and last
> - in advanced settings, disable footers and headers

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/ucnl/ucnl.github.io/assets/24439946/074871c4-ccf6-4423-b90f-ec9b4383b879) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uNav** - navigation solver/radio modem for RWLT/WAYU systems <br/> Communication protocol |
  
# uNav <br/> Communication protocol

<div style="page-break-after: always;"></div>

## Contents
- [0. Version history](#0-version-history)
- [1. Introduction](#1-introduction)
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 Conversational Layer Protocol Standard](#12-nmea0183-conversational-layer-protocol-standard)
- [2. UNV command system](#2-unv-command-system)
  - [2.1. UNV0 - Settings](#21-unv0---settings)
  - [2.2. UNV1 - Reference point](#22-unv1---reference-point)
  - [2.3. UNV2 - Water depth and temperature](#23-unv2---water-depth-and-temperature)
  - [2.4. UNV4 - Parameters relative to the reference point](#24-unv4---parameters-relative-to-the-reference-point)
  - [2.5. UNV5 - Data from built-in GNSS receiver](#25-unv5---data-from-built-in-gnss-receiver)
  - [2.6. UNV6 - Data from RWLT pinger](#26-unv6---data-from-rwlt-pinger)
- [3. Other messages](#3-other-messages)
  - [3.1. GGA](#31-gga)
  - [3.2. RMC](#32-rmc)
  - [3.3. APLA - Data packet from WAYU navigation buoy](#33-apla---data-packet-from-wayu-navigation-buoy)
  - [3.4. RWLA - Data packet from RWLT navigation buoy](#34-rwla---data-packet-from-rwlt-navigation-buoy)

<div style="page-break-after: always;"></div>

## 0. Version history
[Version history](uNav_version_history_en.md)

<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol
   
uNav devices support data pairing using a serial interface.

Default connection port settings:
> _Baudrate: 38400 bit/s_
> _Data bits: 8_
> _Stop bits: 1_
>_Parity: No_
> _Hardware flow control: No_


### 1.2. NMEA0183 Conversational Layer Protocol Standard
The NMEA0183 standard describes the format of text (ASCII) dialog-level messages.

Example message:  **`$PUNA0,1,0*hh<СR><LF>`**  

Basic elements of a message (message, sentence) NMEA0183:
* '$' - start of message,
* 'P' - Proprietary, proprietary code
* 'UNV' is a three-letter identifier
* '0' - message identifier
* ',' - comma (parameter separator)
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example FF, 01). Calculated as a bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of message (line feed)


<div style="page-break-after: always;"></div>

## 2. UNV command system

The device and the system of commands for interacting with it are designed so that, once configured, it can be connected to various applications designed to work with GNSS receivers. For the most part, the device uses standard NMEA protocol messages: RMC and GGA.

### 2.1. UNV0 - Settings
The UNV0 message is used to specify settings for the device, request current settings, and transfer current settings from the device.

Message format: **`$PUNV0,x.x,x.x,x.x,x.x,x,x.x,x,x.x,x,x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 0 | Message ID |
| 1 | sty_PSU | Water salinity in PSU, 0 .. 40 PSU |
| 2 | wtmp_C | Water temperature in °C, -4 .. 46 °C |
| 3 | sos_mps | Speed of sound in water in m/s, 1300 .. 1600 m/s |
| 4 | max_tspd_mps | Maximum movement speed in m/s, 0.5 .. 5 m/s |
| 5 | sf_FIFO_size | Anti-aliasing filter buffer size, 2 .. 64 |
| 6 | sf_rthld_m | Smoothing filter reset threshold, 5 .. 1000 m |
| 7 | dhf_FIFO_size | Classifier buffer size, 2 .. 64 |
| 8 | dhf_rthld | Classifier buffer threshold, 5 .. 1000 m |
| 9 | ce_FIFO_size | Course estimator buffer size, 2 .. 64 |
| 10 | brate | Port speed (see...) |
| 11 | rwlt_mode | Operating mode (for RWLT system). Empty field or 0 - pinger, 1 - divers |
| 12 | rwlt_drating | Maximum pinger depth (for RWLT system). 0 - 300, 1 - 500, 2 - 1000 m |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

### 2.2. UNV1 - Reference point
The command is used to set a reference point, relative to which the device can calculate the course and distance to the positioned object.
 
Message format: **`$PUWV1,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 1 | Message ID |
| 1 | ref_point_type | 0 - AUX GNSS, 1-4 base points, empty - user defined |
| 2 | ref_point_lat | latitude, -90.0 .. 90.0° |
| 3 | ref_point_lon | longitude, -180.0 .. 180.0° |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

### 2.3. UNV2 - Water depth and temperature
The command is used to set the depth of the positioned object (WAYU only) and water temperature.

Message format: **`$PUWV2,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 2 | Message ID |
| 1 | tDpt_m | Depth of the positioned object, m |
| 2 | wTmp_С | Water temperature, -4 .. 46 °C |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

### 2.4. UNV4 - Parameters relative to the reference point
The message contains the calculated navigation parameters of the positioned object, relative to the configured reference point.

Message format: **`$PUWV4,x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 4 | Message ID |
| 1 | tID | Object ID. For all cases except RWLT operation in diver mode, the field remains empty |
| 2 | rpLt | Reference point latitude, -90.0 .. 90.0 ° |
| 3 | rpLn | Longitude of reference point, -180.0 .. 180.0 ° |
| 4 | dst2rp | Distance to the reference point on the plane, m |
| 5 | crs2rp | Course from object to reference point, 0 .. 360.0 ° |
| 6 | crs4rp | Course from the reference point to the object, 0 .. 360.0 ° |
| 7 | Age | Navigation data age, sec |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

### 2.5. UNV5 - Data from built-in GNSS receiver
The message contains navigation data from the built-in GNSS receiver.

Message format: **`$PUWV5,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 5 | Message ID |
| 1 | gnssLt | Geographic latitude, -90.0 .. 90.0 ° |
| 2 | gnssLn | Geographic longitude, -180.0 .. 180.0 ° |
| 3 | gnssCrs | Heading, 0 .. 360.0 ° |
| 4 | gnssSog | Speed, km/h |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

### 2.6. UNV6 - Data from RWLT pinger
The message contains data received from the RWLT pinger.

Message format: **`$PUWV6,x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PUNV | UNV |
| | 6 | Message ID |
| 1 | dataID | Data ID |
| 2 | dataValue | Data |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

<div style="page-break-after: always;"></div>

## 3. Other messages

### 3.1. GGA
Standard message NMEA0183 - Global positioning system fix data.

Message format: **`$GNGGA,hhmmss.sss,ddmm.mmm,N|S,yyymm.mmm,E|W,x,xx,x.x,x.x,M,x.x,M,xx,xxxx*hh<CR ><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | GN | Standard data source - Global navigation |
| | GGA | Standard Message ID - Globap positioning system fix data |
| 1 | UTC Time | UTC, hhmmss.sss (via built-in GNSS receiver) |
| 2 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 3 | N|S | Hemisphere identifier, N - northern, S - southern |
| 4 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 5 | E|W | Hemisphere identifier, E - eastern, W - western |
| 6 | Fix Type | Type of navigation solution |
| 7 | Satellites in view | Number of available satellites (always 4) |
| 8 | HDOP | Horizontal dilution of precision, meters. (this field conveys the radial error, the value of the residual function at the end of the solution) |
| 9 | Altitude | Altitude, meters. (this field conveys depth, i.e. height with a "-" sign) |
| 10 | M | M - meters |
| 11 | Geoidal separation | The field is not supported and remains empty |
| 12 | Age of data | The field is not supported and remains empty |
| 13 | Reference station ID | The field is not supported and remains empty |
| | * | NMEA checksum separator |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of message |

### 3.2. RMC
Standard message NMEA0183 - Recommended minimum, sentence 'C'.

Message format: **`$GNRMC,hhmmss.sss,A|V,ddmm.mmm,N|S,dddmm.mmm,E|W,x.x,x.x,ddmmyy,,,A|D|V*hh<CR ><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | GN | Standard data source - Global navigation |
| | RMC | Standard message identifier - Recommended minimum, sentence 'C' |
| 1 | UTC Time | UTC, hhmmss.ss |
| 2 | Data quality indicator | A - time data (based on built-in GNSS receiver) is correct |
| 3 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 4 | N|S | Hemisphere identifier, N - northern, S - southern |
| 5 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 6 | E|W | Hemisphere identifier, E - eastern, W - western |
| 7 | Speed | Field not supported |
| 8 | Course | Course of movement, degrees |
| 9 | Date | According to the built-in GNSS receiver |
| 10 | Magnetic variation | Field not supported |
| 11 | E|W | Field not supported |
| 12 | A | Mode, A - GNSS |
| | * | NMEA checksum separator |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of message |

### 3.3. APLA - Data packet from WAYU navigation buoy
Data received from the navigation buoy of the WAYU system (APostLe, message "A").

Message format: **`$PAPLA,x,x.x,x.x,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PAPLA | APL |
| | A | Message ID |
| 1 | bID | Buoy number (address), 1 .. 4 |
| 2 | bLt | Buoy latitude, -90.0 .. 90.0 ° |
| 3 | bLn | Buoy longitude, -180.0 .. 180.0 ° |
| 4 | bDpt_m | Acoustic antenna immersion depth, m |
| 5 | bBat | Supply voltage of the built-in buoy source, V |
| 6 | bTOA | Time of signal arrival at the buoy, sec, 0 .. 62 |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |


### 3.4. RWLA - Data packet from RWLT navigation buoy
Data received from an RWLT navigation buoy (RWLT message "A")

Message format: **`$PRWLA,x,x.x,x.x,x,x.x,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Message start '$' |
| | PRWLA | RWL |
| | A | Message ID |
| 1 | bID | Buoy number (address), 1 .. 4 |
| 2 | bLt | Buoy latitude, -90.0 .. 90.0 ° |
| 3 | bLn | Buoy longitude, -180.0 .. 180.0 ° |
| 4 | bDpt_m | Acoustic antenna immersion depth, m |
| 5 | bBat | Supply voltage of the built-in buoy source, V |
| 6 | pData | Data packet from positioned object |
| 7 | bTOA | Time of signal arrival at the buoy, sec, 0 .. 62 |
| 8 | bMSR | Main peak to side lobe ratio, dB |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of message |

<div style="page-break-after: always;"></div>
  
[Back to contents]()

<div style="page-break-after: always;"></div>
