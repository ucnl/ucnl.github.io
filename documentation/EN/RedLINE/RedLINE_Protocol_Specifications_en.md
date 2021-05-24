| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedLINE** - underwater acoustic modem <br/> Interfacing protocol specification |
  
  
  
# RedLINE <br/> Interfacing protocol specification

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)
  - [1.1. Physical layer](#11-physical-layer)
  - [1.2. NMEA0183 Protocol standard](#12-nmea0183-protocol-standard)
- [2. TNT Command System for RedLINE modems](#2-tnt-command-system-for-redline-modems)
  - [2.1. IC_D2H_ACK](#21-ic_d2h_ack)
  - [2.2. IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get)
  - [2.3. IC_D2H_LOC_DATA_VAL](#23-ic_d2h_loc_data_val)
  - [2.4. IC_H2D_SETTINGS_WRITE](#24-ic_h2d_settings_write)
  - [2.5. IC_H2D_SETTINGS_READ](#25-ic_h2d_settings_read)
  - [2.6. IC_D2H_SETTINGS](#26-ic_d2h_settings)
  - [2.7. IC_D2H_DEV_INFO](#27-ic_d2h_dev_info)
- [3. Service mode](#3-service-mode)
- [4. Identifiers](#4-identifiers)
  - [4.1. Error codes](#41-error-codes)
  - [4.2. Local data identifiers](#42-local-data-identifiers)
   
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer
   
[RedLINE](RedLine_Specification_en.md) underwater acoustic modems support data pairing using the RS-232 physical layer standard for asynchronous interface (UART) 
with a 3.3V data line voltage. The connection is made using a four-wire cable with Tx (transmitter), Rx (receiver), Vcc (power) 
and GND (ground) wires. Without the use of additional repeaters and interface converters, the maximum cable length, for which 
the correct operation of the interface is guaranteed, is no more than 2 meters.

Default port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**WARNING!**
>_The modems are powered by 12 Volt DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 Protocol standard
The NMEA0183 standard describes the format of text (ASCII) messages at the interactive level.

Sentence example: **`$PTNT0,1*hh<СR><LF>`**  

Parts of a message (sentence) NMEА0183:
* '$' - sentence start,
* 'P' - Proprietary
* 'TNT' - Manufacturer/protocol identifier
* '0' - sentence identifier
* ',' - parameters separator
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example FF, 01). Byte-by-byte XOR for all characters between '$' and '*'.
* \<CR\>\<LF\> - end of sentence
________
<a name="footnote1"><sup>1</sup> Specified parameters can be changed by a request</a>

<div style="page-break-after: always;"></div>

## 2. TNT Command System for RedLINE modems
The **D2H** prefix in the message name means that it is transmitted from the device (Device) to the host system (Host).
The **H2D** prefix in the message name means that it is transmitted from the host system to the device.

### 2.1. IC_D2H_ACK
Device acknowledgement.

Format: **`$PTNT0,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 0	| Sentence ID |
| 1 | errCode	| Error code \([see 4.1.](#41-error-codes)\) |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.2. IC_H2D_LOC_DATA_GET
Query for a local parameter value.

Format: **`$PTNT4,xx,00*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 4 | Sentence ID |
| 1 | dataID	| Parameter ID \([see 4.2.](#42-local-data-identifiers)\) |
| 2 | reserved | should be '00' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


### 2.3. IC_D2H_LOC_DATA_VAL
Device's response to [IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get) sentence.

Format: **`$PTNT5,x,x<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 5 | Sentence ID | 
| 1 | Requested data ID | Parameter ID \([see. 4.2.](#42-local-data-identifiers)\) | 
| 2 | Value | Queried value | 
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


### 2.4. IC_H2D_SETTINGS_WRITE
This sentence is used to change device's configuration.  

Format: **`$PTNT7,x,x,x,x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 7 | Sentence ID |
| 1 | rxChID | Rx channel identifier | 
| 2 | txChID | Tx channel identifier |
| 3 | isRTX | ‘1’ – relay mode is enabled, ‘0’ – relay mode is disabled |
| 4 | isRVRS | ‘1’ – by default, the inverse channel is used for transmission, ‘0’ – by default, the direct channel is used for transmission | 
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.5. IC_H2D_SETTINGS_READ
Read current device's settings.  

Format: **`$PTNT8,x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 8	Sentence ID |
| 1 | reserved | Should be always '0' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.6. IC_D2H_SETTINGS
Current device's settings.  

Format: **`$PTNT9,x,x,x,x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 9 | Идентификатор сообщения
| 1 | rxChID | Rx channel identifier | 
| 2 | txChID | Tx channel identifier |
| 3 | isRTX | ‘1’ – relay mode is enabled, ‘0’ – relay mode is disabled |
| 4 | isRVRS | ‘1’ – by default, the inverse channel is used for transmission, ‘0’ – by default, the direct channel is used for transmission |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.7. IC_D2H_DEV_INFO
Device's responce to [IC_D2H_LOC_DATA_GET](#22-ic_h2d_loc_data_get), if the queried parameter ID = [LOC_DATA_DEV_INFO](#42-local-data-identifiers).

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

<div style="page-break-after: always;"></div>

## 3. Service mode
[RedLINE](RedLine_Specification_en.md) modems provide the user with a so-called "transparent channel" when all data supplied to the input without changes and analysis are transmitted to the hydroacoustic channel, after which they are received by another modem and in the unchanged form are given to the user at the receiving side. In this regard, to be able to configure modems there is a command mode. Modems analyze input data only in command mode. To switch to the command mode, the “service” core should be pulled to +3.3 V. After that, the “service” core should be pulled to the ground to exit the service mode.

> **WARNING!** The core "service" is pulled **ONLY** to 3-5 V or ground, connecting it to a higher voltage will cause a **FATAL** and **NON-GUARANTEE** failure of the device.

> **WARNING!** Before switching on the device, the "service" core should be pulled to the ground, otherwise, the device will enter the software update mode.

<div style="page-break-after: always;"></div>

## 4. Identifiers
### 4.1. Error codes 

| Error | Value | Description |
| :--- | :--- | :--- |
| LOC_ERR_NO_ERROR | 0 | Request accepted |
| LOC_ERR_INVALID_SYNTAX | 1 | Syntax error |
| LOC_ERR_UNSUPPORTED | 2 | Request not supported |
| LOC_ERR_TRANSMITTER_BUSY | 3 | Transmitter is busy |
| LOC_ERR_ARGUMENT_OUT_OF_RANGE | 4 | Specified parameter out of range |
| LOC_ERR_INVALID_OPERATION | 5 | Invalid request |
| LOC_ERR_UNKNOWN_FIELD_ID | 6 | Unknown field identifier |
| LOC_ERR_VALUE_UNAVAILIBLE | 7 | Requested parameter is not available at the moment |
| LOC_ERR_RECEIVER_BUSY | 8 | Receiver is busy |


### 4.2. Local data identifiers

| Value | Identifier | Description |
| :--- | :--- | :--- |
| 0 | DEVICE_INFO | Device information |
| 2 | MAX_SUBSCRIBERS | Max. number of code channels available |
| 6 | PRESSURE_RATING | Max. external hydrostatic pressure in Bars |

__________

[Back to contents](#contents)
