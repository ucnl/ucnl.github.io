| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedWAVE** - underwater acoustic navigation system <br/> RedNODE interfacing protocol |
  
 
# RedWAVE <br/> RedNODE interfacing protocol

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Physical protocol](#11-physical-protocol)
  - [1.2. NMEA0183 Protocol standard NMEA0183](#12-nmea0183-protocol-standard)
- [2. TNT Command System and Standard Messages NMEA0183](#2-tnt-command-system-and-standard-messages-nmea0183)
  - [2.1. Commonly used messages](#21-commonly-used-messages)
    - [2.1.1. GGA](#211-gga)
    - [2.1.2. RMC](#212-rmc)
    - [2.1.3. MTW](#213-mtw)
    - [2.1.4. IC_D2H_NEW_PFIX_UPDATE](#214-ic_d2h_new_pfix_update)
    - [2.1.5. IC_D2H_DPTTMP_VAL](#215-ic_d2h_dpttmp_val)
    - [2.1.6. IC_D2H_BUOY_STATUS](#216-ic_d2h_buoy_status)
    - [2.1.7. IC_D2H_PRETMP_VAL](#217-ic_d2h_pretmp_val)
    - [2.1.8. IC_H2D_SET_VAL](#218-ic_h2d_set_val)
  - [2.2. Additional sentences](#22-additional-sentences)
    - [2.2.1. IC_D2H_ACK](#221-ic_d2h_ack)
    - [2.2.2. IC_H2D_LOC_DATA_GET](#222-ic_h2d_loc_data_get)
    - [2.2.3. IC_D2H_LOC_DATA_VAL](#223-ic_d2h_loc_data_val)
    - [2.2.4. IC_D2H_DEV_INFO_VAL](#224-ic_d2h_dev_info_val)
    - [2.2.5. IC_H2D_SNT_ENABLE](#225-ic_h2d_snt_enable)
    - [2.2.6. IC_H2D_ACT_INVOKE](#226-ic_h2d_act_invoke)
- [3. Tables of identifiers](#3-tables-of-identifiers)
  - [3.1. Device types](#31-device-types)
  - [3.2. Error codes](#32-error-codes)
  - [3.3. Local parameters identifiers](#33-local-parameters-identifiers)
  - [3.4. Service actions identifiers](#34-service-actions-identifiers)
  - [3.5. Fix types](#35-fix-types)
  - [3.6. Buoy status](#36-buoy-status)
   
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical protocol
Hydroacoustic navigation receivers **[RedNODE](RedNODE_Specification_en.md)** support pairing using **RS-232** physical layer standard 
for asynchronous interface (UART) with 3.3V data line voltage. The connection is made using a four-wire cable, with wires Tx 
(transmitter), Rx (receiver), Vcc (power) and GND (ground). Without the use of additional repeaters and interface converters, the 
maximum length of the data cable, for which the correct operation of the interface is guaranteed, is no more than 2 meters.

Default port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

> ** ATTENTION! **
> _Receivers are powered by a 12 V DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 Protocol standard
The NMEA0183 standard describes the format of text (ASCII) messages (sentences) of an interactive level.

Example sentence: **`$PTNT0,1*hh<CR><LF>`**

The main elements of the sending (message, sentence) NMEА0183:
* '$' - the beginning of the message,
* 'P' - Proprietary, proprietary code
* 'TNT' - three-letter manufacturer identifier
* '0' - message identifier
* ',' - comma (parameter separator)
* '1' - 1st parameter
* '*' - checksum separator
* 'hh' is the checksum in hexadecimal format (e.g. FF, 01). It is calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of message (line feed)
________
<a name="footnote1"> <sup> 1 </sup> The specified parameters can be changed upon request </a>

<div style="page-break-after: always;"></div>

## 2. TNT Command System and Standard Messages NMEA0183
The **D2H** prefix in the message name means that it is transmitted from the device (Device) to the host system (Host).
The **H2D** prefix in the message name means that it is transmitted from the host system to the device.

### 2.1. Commonly used messages

This group includes messages that the device sends by default (considering on its internal state).

#### 2.1.1. GGA
Standard NMEA0183 sentence - Global positioning system fix data.

Format: **`$GNGGA,hhmmss.sss,ddmm.mmm,N|S,yyymm.mmm,E|W,x,xx,x.x,x.x,M,x.x,M,xx,xxxx*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | GN | Standard talker - Global navigation |
| | GGA |	Standard sentence ID - Global positioning system fix data |
| 1 | UTC Time |	UTC, hhmmss.sss |
| 2 | Latitude |	Latitude, ddmm.mmmmmm |
| 3 | N|S | Hemisphere ID, N - north, S - south |
| 4 | Longitude |	Longitude, dddmm.mmmmmm |
| 5 | E|W | Hemisphere ID, E - east, W - west |
| 6 | Fix Type | Fix type | 
| 7 | Satellites in view | Number of satellites in view (always 4 in RedWAVE) |
| 8 | HDOP | Horizontal dilution of precision, метры. (in RedWAVE this field contains the radial error - residual function value in the end of navigational problem solution) |
| 9 | Altitude | Altitude, m. (in RedWAVE this field contains the depth of the receiver, "altitude" with "-") |
| 10 | M |	М - meters |
| 11 | Geoidal separation | Not supported |
| 12 | Age of data |  Not supported |
| 13 | Reference station ID | Not supported |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.2. RMC
Standard NMEA0183 sentence - Recommended minimum, sentence 'C'.

Format: **`$GNRMC,hhmmss.sss,A|V,ddmm.mmm,N|S,dddmm.mmm,E|W,x.x,x.x,ddmmyy,,,A|D|V*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | GN | Standard talker - Global navigation |
|  | RMC | Standard sentence ID - Recommended minimum, sentence 'C' |
| 1 | UTC Time |	UTC, hhmmss.sss |
| 2 | Data quality indicator |	A - data valid |
| 3 | Latitude |	Latitude, ddmm.mmmmmm |
| 4 | N|S | N|S | Hemisphere ID, N - north, S - south |
| 5 | Longitude |	Longitude, dddmm.mmmmmm |
| 6 | E|W | Hemisphere ID, E - east, W - west |
| 7 | Speed |	Not supported |
| 8 | Course | Not supported |
| 9 | Date | Not supported |
| 10 | Magnetic variation | Not supported |
| 11 | E|W | Not supported |
| 12 | A | Mode, A - GNSS |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.3. MTW
Standard NMEA0183 sentence - Mean water temperature (Температура воды).

Format: **`$GNMTW,x.x,C*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | GN | Standard talker - Global navigation |
|  | MTW | Standard - Mean temperature of water |
| 1 | Temperature	| Температура воды, ˚C
| 2 | C	| C - Celsius |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.4. IC_D2H_NEW_PFIX_UPDATE
Position fix and location of the buoys.

Format: **`$PTNTC,x,x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | C | Sentence identifier |
| 1 | Own location - latitude | Latitude, signed, ° |
| 2 | Own location - longitude | Longitude, signed, ° |
| 3 | Own location - depth | Depth, m |
| 4 | Radial error | Radial error (value of residual function in the end of solution, m |
| 5 | Buoy #1 latitude | RedBASE №1 Latitude, signed, ° |
| 6 | Buoy #1 longitude | RedBASE №1 Longitude, signed, ° |
| 7 | Buoy #2 latitude | RedBASE №2 Latitude, signed, ° |
| 8 | Buoy #2 longitude | RedBASE №2 Longitude, signed, ° |
| 9 | Buoy #3 latitude | RedBASE №3 Latitude, signed, ° |
| 10 | Buoy #3 longitude | RedBASE №3 Longitude, signed, ° |
| 11 | Buoy #4 latitude | RedBASE №4 Latitude, signed, ° |
| 12 | Buoy #4 longitude | RedBASE №4 Longitude, signed, ° |
| 13 | Temperature | Water temperature, ˚C |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.5. IC_D2H_DPTTMP_VAL
Depth and water temperature.

Format: **`PTNTN,x.x,x.x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | N | Sentence ID |
| 1 | Depth | Depth, m |
| 2 | Temperature | Water temperature, ˚C |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.6. IC_D2H_BUOY_STATUS
Statuses of buoys.

Format: **`$PTNTM,x.x,x.x,x.x,x,x.x,x.x,x.x,x,x.x,x.x,x.x,x,x.x,x.x,x.x,x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | M | Sentence identifier |
| 1 | Buoy #1 latitude | RedBASE №1 Latitude, signed, ° |
| 2 | Buoy #1 longitude | RedBASE №1 Longitude, signed, ° |
| 3 | Buoy #1 SNR | RedBASE №1 MSR<sup>[2](#footnote2)</sup>, dB |
| 4 | Buoy #1 status | RedBASE №1 Status<sup>[3](#footnote3)</sup> |
| 5 | Buoy #2 latitude | RedBASE №2 Latitude, signed, ° |
| 6 | Buoy #2 longitude | RedBASE №2 Longitude, signed, ° |
| 7 | Buoy #2 SNR | RedBASE №2 MSR<sup>[2](#footnote2)</sup>, dB |
| 8 | Buoy #2 status | RedBASE №2 Status<sup>[3](#footnote3)</sup> |
| 9 | Buoy #3 latitude | RedBASE №3 Latitude, signed, ° |
| 10 | Buoy #3 longitude | RedBASE №3 Longitude, signed, ° |
| 11 | Buoy #3 SNR | RedBASE №3 MSR<sup>[2](#footnote2)</sup>, dB |
| 12 | Buoy #3 status | RedBASE №3 Status<sup>[3](#footnote3)</sup> |
| 13 | Buoy #4 latitude | RedBASE №4 Latitude, signed, ° |
| 14 | Buoy #4 longitude | RedBASE №4 Longitude, signed, ° |
| 15 | Buoy #4 SNR | RedBASE №4 MSR<sup>[2](#footnote2)</sup>, dB |
| 16 | Buoy #4 status | RedBASE №4 Status<sup>[3](#footnote3)</sup> |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

________
<a name="footnote2"><sup>2</sup> MSR (_Main lobe to side peak ratio_) - signal reception quality characteristic. Good reception conditions with values >= 20 dB.  
<a name="footnote3"><sup>3</sup> Table of possible values \([see 3.6.](#36-buoy-status)\)

#### 2.1.7. IC_D2H_PRETMP_VAL
Hydrostatic pressure and temperature of water.

Format: **`$PTNTO,x.x,x.x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | O | Sentence ID |
| 1 | Pressure | External hydrostatic pressure, mBar |
| 2 | Temperature | Temperature of water, ˚C |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.1.8. IC_H2D_SET_VAL
Query for setting value of a local parameter.

Format: **`$PTNTP,x,x.x<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | P | Sentence ID |
| 1 | Value ID | Local parameter ID \([see. 3.3.](#33-local-parameters-identifiers)\) |
| 2 | Value | New value to set |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.2. Additional sentences

This group of messages includes requests to the device from the control system and device responses.

#### 2.2.1. IC_D2H_ACK
Device acknowledgement.

Format: **`$PTNT0,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 0	| Sentence ID |
| 1 | errCode	| Error code \([see 3.2.](#32-error-codes)\) |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


#### 2.2.2. IC_H2D_LOC_DATA_GET
Query for a local parameter value.

Format: **`$PTNT4,xx,00*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 4 | Sentence ID |
| 1 | dataID	| Parameter ID \([see 3.3.]()\) |
| 2 | reserved | should be '00' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.2.3. IC_D2H_LOC_DATA_VAL
Device's response to [IC_H2D_LOC_DATA_GET](#222-ic_h2d_loc_data_get) and [IC_H2D_SET_VAL](#218-ic_h2d_set_val) sentences.

Format: **`$PTNT5,x,x<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 5 | Sentence ID | 
| 1 | Requested data ID | Parameter ID \([see. 3.3.](#33-local-parameters-identifiers)\) | 
| 2 | Value | Queried value | 
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


#### 2.2.4. IC_D2H_DEV_INFO_VAL
Device's responce to [IC_D2H_LOC_DATA_GET](#222-ic_h2d_loc_data_get), if the queried parameter ID = [LOC_DATA_DEV_INFO](#33-local-parameters-identifiers).

Format: **`$PTNT!,c--c,x,x,c--c,x,c--c<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | ! | Sentence ID |
| 1 | System moniker | System name |
| 2 | System version | System version (BCD) |
| 3 | Communication subsystem moniker | Communication subsystem name |
| 4 | Communication subsystem version | Communication subsystem version (BCD) |
| 5 | Device type | Device type \([see 3.1.](#31-device-types)\) |
| 6 | Serial number | Serial number |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

#### 2.2.5. IC_H2D_SNT_ENABLE
Enablind and disabling sentences output.

Format: **`$PTNTQ,b,b,b,b,b,b,b*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | Q | Sentence ID |
| 1 | isMTW | [MTW](#213-mtw) (0 - disabled, 1 - enabled) |
| 2 | isGGA | [GGA](#211-gga) (0 - disabled, 1 - enabled) |
| 3 | isRMC | [RMC](#212-rmc) (0 - disabled, 1 - enabled) |
| 4 | isM | [TNTM](#216-ic_d2h_buoy_status) (0 - disabled, 1 - enabled) |
| 5 | isC | [TNTC](#214-ic_d2h_new_pfix_update) (0 - disabled, 1 - enabled) |
| 6 | isN | [TNTN](#215-ic_d2h_dpttmp_val) (0 - disabled, 1 - enabled) |
| 7 | isO | [TNTO](#217-ic_d2h_pretmp_val) (0 - disabled, 1 - enabled) |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


#### 2.2.6. IC_H2D_ACT_INVOKE
Query for a service operation.

Format: **`$PTNT6,xx,00*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 6 | Sentence ID |
| 1 | Action ID | Service operation ID \([see 3.4.](#34-service-actions-identifiers)\) |
| 2 | Reserved | Reserved, should be '00' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


## 3. Tables of identifiers
### 3.1. Device types

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | DEVICE_REDBASE | RedBASE |
| '1' | DEVICE_REDNODE | RedNODE |
| '2' | DEVICE_REDNAV | RedNAV |
| '3' | DEVICE_REDGTR | RedGTR |

### 3.2. Error codes

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | NO_ERROR | Query accepted |
| '1' | INVALID_SYNTAX | Syntax is invalid |
| '2' | UNSUPPORTED | Not supported query |
| '3' | TRANSMITTER_BUSY | Acoustic transmitter is busy |
| '4' | ARGUMENT_OUT_OF_RANGE | Specified argument is out of range |
| '5' | INVALID_OPERATION | Specified operation can not be performent at this moment |
| '6' | UNKNOWN_FIELD_ID | Specified field ID is unknown |
| '7' | VALUE_UNAVAILIBLE | Queried parameter value is not available at this moment |
| '8' | RECEIVER_BUSY | Acoustic receiver is busy |

### 3.3. Local parameters identifiers

| Value | Name | Description | RO/RW<sup>[4](#footnote4)</sup> |
| :--- | :--- | :--- | :--- |
| '0' | DEVICE_INFO | Information about the device, serial number and FW version | RO |
| '1' | MAX_REMOTE_TIMEOUT | Maximal timeout, msec | RO |
| '2' | MAX_SUBSCRIBERS | Not supported | RO |
| '3' | DEPTH | Depth, according to built-in depth sensor | RO |
| '4' | TEMPERATURE | Temperature, according to built-in temperature sensor | RO |
| '5' | BAT_CHARGE | Not supported | RO |
| '6' | PRESSURE_RATING | Maximal external hydrostatic pressure, bar | RO |
| '7' | ZERO_PRESSURE | Pressure on the water surface, mBar | RW |
| '8' | WATER_DENSITY | Water density, kg/m<sup>3</sup> | RO |
| '9' | SALINITY | Water salinity, PSU | RW |
| '10' | SOUND_SPEED | Speed of sound, m/s | RW |
| '11' | GRAVITY_ACC | Gravity acceleration, m/s<sup>2</sup> | RO |
| '12' | YEAR | Year | RW |
| '13' | MONTH | Month | RW |
| '14' | DATE | Day of month | RW |
| '15' | HOUR | Hour | RO |
| '16' | MINUTE | Minute | RO |
| '17' | SECOND | Second | RO |


________
<a name="footnote4"><sup>4</sup> **RO** - Read-Only; **RW** - read/write.  

### 3.4. Service actions identifiers 

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | LOC_INVOKE_FLASH_WRITE | Save settings to internal flash |
| '1' | LOC_INVOKE_CLEAR_WAYPOINTS | Not supported |
| '2' | LOC_INVOKE_CLEAR_TRACK | Not supported |
| '3' | LOC_INVOKE_CLEAR_NDTABLE | Not supported |
| '4' | LOC_INVOKE_DPT_ZERO_ADJUST | Set current pressure as a pressure on the water surface |

### 3.5. Fix types

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | NO_FIX | Location is not available |
| '1' | GNSS_FIX | Location is based on GNSS data |

### 3.6. Buoy status

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | BSTS_NO_DATA | State is unknown |
| '1' | BSTS_TIMEOUT | Timeout |
| '2' | BSTS_DISCHARGED | Buoy is alive and used in navigation, but its battery shall be charged as soon as possible |
| '3' | BSTS_OK | Buoy is alive and used in navigation |
| '4' | BSTS_ALIVE |  Bouy is alive, but the data about its battery charge has not updated yet |

### [Back to contents]()
