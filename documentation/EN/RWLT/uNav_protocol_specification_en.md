[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **uNav: Communication protocol specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/ucnl/ucnl.github.io/assets/24439946/90cb2dba-5bac-46da-bcab-e4880fd4277a) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uNav** - navigation receiver for RWLT/WAYU tracking systems <br/> Communication protocol specification |
  
# uNav <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.0. Physical layer protocol](#10-physical-layer-protocol)
  - [1.1. NMEA0183 dialog layer protocol standard](#11-nmea0183-dialog-layer-protocol-standard)
- [2. UNV command system](#2-unv-command-system)
  - [2.0. UNV0 - Settings](#20-unv0---settings)
  - [2.1. UNV1 - Reference point](#21-unv1---reference-point)
  - [2.2. UNV2 - Water depth and temperature](#22-unv2---water-depth-and-temperature)
  - [2.3. UNV3 - Position of a numbered object](#23-unv3---position-of-a-numbered-object)
  - [2.5. UNV4 - Parameters relative to the reference point](#25-unv4---parameters-relative-to-the-reference-point)
  - [2.6. UNV5 - Data from the built-in GNSS receiver](#26-unv5---data-from-the-built-in-gnss-receiver)
  - [2.7. UNV6 - Data from the RWLT pinger](#27-unv6---data-from-the-rwlt-pinger)
- [3. Other sentences](#3-other-sentences)
  - [3.0. GGA](#30-gga)
  - [3.1. RMC](#31-rmc)
  - [3.2. APLA - Data packet from the WAYU navigation buoy](#32-apla---data-packet-from-the-wayu-navigation-buoy)
  - [3.3. RWLA - Data packet from the RWLT navigation buoy](#33-rwla---data-packet-from-the-rwlt-navigation-buoy)

<div style="page-break-after: always;"></div>

## 0. Version history & list of changes
[Version history & changes](uNav_version_history_en.md)

<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.0. Physical layer protocol

uNav devices support data interfacing via a serial interface.

Default connection port settings:  
> _Baudrate: 38400 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  


### 1.1. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of dialog layer text (ASCII) sentences.  

Sentence example:  **`$PUNA0,1,0*hh<CR><LF>`**  

The main elements of an NMEA0183 sentence (message):
* '$' - sentence start,
* 'P' - Proprietary code
* 'UNV' - three-letter ID
* '0' - sentence ID
* ',' - comma (parameter delimiter)  
* '*' - checksum delimiter
* 'hh' - checksum in hexadecimal format (e.g. FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)


<div style="page-break-after: always;"></div>

## 2. UNV command system

The device and the command system for interacting with it are designed so that, once configured, the device can be connected to various applications designed to work with GNSS receivers. For the most part, the device uses standard NMEA protocol sentences: RMC and GGA.

### 2.0. UNV0 - Settings
The UNV0 sentence is used to specify settings for the device, request the current settings, and transfer the current settings from the device.

Sentence format: **`$PUNV0,x.x,x.x,x.x,x.x,x,x.x,x,x.x,x,x*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 0 | Sentence ID |
| 1 | sty_PSU | Water salinity in PSU, 0 .. 40 PSU |
| 2 | wtmp_C | Water temperature in °C, -4 .. 46 °C |
| 3 | sos_mps | Speed of sound in water in m/s, 1300 .. 1600 m/s |
| 4 | max_tspd_mps | Maximum movement speed in m/s, 0.5 .. 5 m/s |
| 5 | sf_FIFO_size | Smoothing filter buffer size, 2 .. 64 |
| 6 | sf_rthld_m | Smoothing filter reset threshold, 5 .. 1000 m |
| 7 | dhf_FIFO_size | Classifier buffer size, 2 .. 64 |
| 8 | dhf_rthld | Classifier buffer threshold, 5 .. 1000 m |
| 9 | ce_FIFO_size | Course estimator buffer size, 2 .. 64 |
| 10 | brate | Port speed (see ..) |
| 11 | rwlt_mode | Operating mode (for the RWLT system). Empty field or 0 - pinger, 1 - divers |
| 12 | rwlt_drating | Maximum pinger depth (for the RWLT system). 0 - 300, 1 - 500, 2 - 1000 m |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.1. UNV1 - Reference point
The command is used to set a reference point, relative to which the device can calculate the course and distance to the positioned object.
 
Sentence format: **`$PUWV1,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 1 | Sentence ID |
| 1 | ref_point_type | 0 - AUX GNSS, 1-4 base points, empty - user defined |
| 2 | ref_point_lat | Latitude, -90.0 .. 90.0 ° |
| 3 | ref_point_lon | Longitude, -180.0 .. 180.0 ° |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.2. UNV2 - Water depth and temperature
The command is used to set the depth of the positioned object (WAYU only) and the water temperature.

Sentence format: **`$PUWV2,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 2 | Sentence ID |
| 1 | tDpt_m | Depth of the positioned object, m |
| 2 | wTmp_C | Water temperature, -4 .. 46 °C |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.3. UNV3 - Position of a numbered object
For the RWLT system only, when operating in the diver positioning mode. This sentence transmits the determined navigation data of a numbered target (for example, a diver equipped with a [RedPhone-DX](/documentation/EN/RedPhone/RedPhone_DX_Specification_en) wireless voice communication device). The object ID (address) is transmitted by the object itself and can take values from 0 to 999.

Sentence format: **`$PUWV3,x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 3 | Sentence ID |
| 1 | tID | Object ID (address) |
| 2 | tLat | Latitude, -90.0 .. 90.0 ° |
| 3 | tLon | Longitude, -180.0 .. 180.0 ° |
| 4 | tDpt | Depth, m |
| 5 | tCrs | Course, , 0 .. 360.0 ° |
| 6 | tRer | Radial error, m |
| 7 | Age | Navigation data age, s |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.5. UNV4 - Parameters relative to the reference point
The sentence contains the calculated navigation parameters of the positioned object, relative to the configured reference point.

Sentence format: **`$PUWV4,x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 4 | Sentence ID |
| 1 | tID | Object ID. In all cases except RWLT operating in diver mode, the field remains empty |
| 2 | rpLt | Reference point latitude, -90.0 .. 90.0 ° |
| 3 | rpLn | Reference point longitude, -180.0 .. 180.0 ° |
| 4 | dst2rp | Distance to the reference point on the plane, m |
| 5 | crs2rp | Course from the object to the reference point, 0 .. 360.0 ° |
| 6 | crs4rp | Course from the reference point to the object, 0 .. 360.0 ° |
| 7 | Age | Navigation data age, s |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.6. UNV5 - Data from the built-in GNSS receiver
The sentence contains navigation data from the built-in GNSS receiver.

Sentence format: **`$PUWV5,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 5 | Sentence ID |
| 1 | gnssLt | Geographic latitude, -90.0 .. 90.0 ° |
| 2 | gnssLn | Geographic longitude, -180.0 .. 180.0 ° |
| 3 | gnssCrs | Course, 0 .. 360.0 ° |
| 4 | gnssSog | Speed, km/h |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.7. UNV6 - Data from the RWLT pinger
The sentence contains data received from the RWLT pinger.

Sentence format: **`$PUWV6,x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PUNV | UNV |
| | 6 | Sentence ID |
| 1 | dataID | Data ID |
| 2 | dataValue | Data |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

<div style="page-break-after: always;"></div>

## 3. Other sentences

### 3.0. GGA
Standard NMEA0183 sentence - Global positioning system fix data.

Sentence format: **`$GNGGA,hhmmss.sss,ddmm.mmm,N|S,yyymm.mmm,E|W,x,xx,x.x,x.x,M,x.x,M,xx,xxxx*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | GN | Standard data source - Global navigation |
| | GGA | Standard sentence ID - Global positioning system fix data |
| 1 | UTC Time | UTC, hhmmss.sss (according to the built-in GNSS receiver) |
| 2 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 3 | N|S | Hemisphere identifier, N - northern, S - southern |
| 4 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 5 | E|W | Hemisphere identifier, E - eastern, W - western |
| 6 | Fix Type | Navigation solution type | 
| 7 | Satellites in view | Number of available satellites (always 4) |
| 8 | HDOP | Horizontal dilution of precision, meters. (this field conveys the radial error, the value of the residual function at the end of the solution) |
| 9 | Altitude | Altitude, meters. (this field conveys depth, i.e. height with a "-" sign) |
| 10 | M | M - meters |
| 11 | Geoidal separation | The field is not supported and remains empty |
| 12 | Age of data | The field is not supported and remains empty |
| 13 | Reference station ID | The field is not supported and remains empty |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 3.1. RMC
Standard NMEA0183 sentence - Recommended minimum, sentence 'C'.

Sentence format: **`$GNRMC,hhmmss.sss,A|V,ddmm.mmm,N|S,dddmm.mmm,E|W,x.x,x.x,ddmmyy,,,A|D|V*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | GN | Standard data source - Global navigation |
|  | RMC | Standard sentence ID - Recommended minimum, sentence 'C' |
| 1 | UTC Time | UTC, hhmmss.sss |
| 2 | Data quality indicator | A - the time data (according to the built-in GNSS receiver) are correct |
| 3 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 4 | N|S | Hemisphere identifier, N - northern, S - southern |
| 5 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 6 | E|W | Hemisphere identifier, E - eastern, W - western |
| 7 | Speed | The field is not supported |
| 8 | Course | Course (direction of motion), degrees |
| 9 | Date | According to the built-in GNSS receiver data |
| 10 | Magnetic variation | The field is not supported |
| 11 | E|W | The field is not supported |
| 12 | A | Mode, A - GNSS |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

### 3.2. APLA - Data packet from the WAYU navigation buoy
Data received from the navigation buoy of the WAYU system (APostLe, sentence "A").

Sentence format: **`$PAPLA,x,x.x,x.x,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAPLA | APL |
| | A | Sentence ID |
| 1 | bID | Buoy number (address), 0 .. 3 (corresponds to buoys 1 .. 4) |
| 2 | bLt | Buoy latitude, -90.0 .. 90.0 ° |
| 3 | bLn | Buoy longitude, -180.0 .. 180.0 ° |
| 4 | bDpt_m | Acoustic transducer immersion depth, m |
| 5 | bBat | Supply voltage of the buoy's built-in power source, V |
| 6 | bTOA | Time of signal arrival at the buoy, s, 0 .. 62 |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 3.3. RWLA - Data packet from the RWLT navigation buoy
Data received from the navigation buoy of the RWLT system (RWLT, sentence "A")

Sentence format: **`$PRWLA,x,x.x,x.x,x,x.x,x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PRWLA | RWL |
| | A | Sentence ID |
| 1 | bID | Buoy number (address), 0 .. 3 (corresponds to buoys 1 .. 4) |
| 2 | bLt | Buoy latitude, -90.0 .. 90.0 ° |
| 3 | bLn | Buoy longitude, -180.0 .. 180.0 ° |
| 4 | bDpt_m | Acoustic transducer immersion depth, m |
| 5 | bBat | Supply voltage of the buoy's built-in power source, V |
| 6 | pData | Data packet from the positioned object |
| 7 | bTOA | Time of signal arrival at the buoy, s, 0 .. 62 |
| 8 | bMSR | Main peak to side lobe ratio, dB |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


<div style="page-break-after: always;"></div>
  
[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RWLT/uNav_protocol_specification_ru.md commit=947d0ec42df103b451151d139305df42923177ee date=2026-03-11 -->
