[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **RedLine: Communication protocol specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedLine** - family of underwater acoustic communication devices <br/> Communication protocol specification |
  
# RedLine <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)  
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. TNT command system for RedLine underwater acoustic modems](#2-tnt-command-system-for-redline-underwater-acoustic-modems)  
   - [2.1. IC_D2H_ACK - device response](#21-ic_d2h_ack)
   - [2.2. IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get)
   - [2.3. IC_D2H_LOC_DATA_VAL](#23-ic_d2h_loc_data_val)
   - [2.4. IC_H2D_SETTINGS_WRITE](#24-ic_h2d_settings_write)
   - [2.5. IC_H2D_SETTINGS_READ](#25-ic_h2d_settings_read)
   - [2.6. IC_D2H_SETTINGS](#26-ic_d2h_settings)
   - [2.7. IC_D2H_DEV_INFO](#27-ic_d2h_dev_info)
- [3. Service mode](#3-service-mode)
- [4. Identifier tables](#4-identifier-tables)
   - [4.1. Error codes](#41-error-codes)
   - [4.2. Local data identifiers](#42-local-data-identifiers)
  
   
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol
[RedLine](RedLine_Specification_en.md) underwater acoustic modems support data communication using the RS-232 physical layer standard for
an asynchronous interface (UART) with a 3.3 V data line voltage. The connection is made using a four-wire cable
with Tx (transmitter), Rx (receiver), Vcc (power) and GND (ground) wires. Without additional repeaters and interface converters,
the maximum data bus length for which correct interface operation is guaranteed is no more than 2 meters.  

Default port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**CAUTION!**
>_The modems are powered by a 12 V DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of text (ASCII) sentences at the dialog layer.  

Sentence example: **`$PTNT0,0*hh<CR><LF>`**  

Main elements of an NMEA0183 sentence:
* '$' - sentence start,
* 'P' - Proprietary, a proprietary code
* 'TNT' - three-letter manufacturer identifier
* '0' - sentence identifier
* ',' - comma (parameter separator)  
* '0' - parameter (in this case, an error code)
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)
________
<a name="footnote1"><sup>1</sup> The specified parameters can be changed on request</a>

<div style="page-break-after: always;"></div>

## 2. TNT command system for RedLine underwater acoustic modems
The **D2H** prefix in a sentence name means that it is transmitted from the device (Device) to the control system (Host).
The **H2D** prefix in a sentence name means that it is transmitted from the control system (Host) to the device (Device).

### 2.1. IC_D2H_ACK
The IC_D2H_ACK sentence is the device response to a request received from the control system.  

Sentence format: **`$PTNT0,x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT	| TNT |
| 0	| Sentence identifier |
| errCode	| Error code \([see 4.1](#41-error-codes)\) |
| *	| NMEA checksum separator |
| hh	| NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.2. IC_H2D_LOC_DATA_GET
Get the value of a local variable.

Sentence format: **`$PTNT4,xx,00*hh<CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| 4	| Sentence identifier |
| Requested data ID	| Data identifier \([see 4.2](#42-local-data-identifiers)\) |
| Reserved	| Reserved; must always be '00' |
| *	| NMEA checksum separator |
| hh	| NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.3. IC_D2H_LOC_DATA_VAL
Value of a local variable.

Sentence format: **`$PTNT5,x,x.x*hh<CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| 5	| Sentence identifier |
| Requested data ID	| Data identifier \([see 4.2](#42-local-data-identifiers)\) |
| Requested data value	| Value |
| *	| NMEA checksum separator |
| hh	| NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.4. IC_H2D_SETTINGS_WRITE
This command allows the user to configure the modem settings.  

Sentence format: **`$PTNT7,x,x,x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT |
| 7 | Sentence identifier
| rxChID | Receive channel identifier
| txChID | Transmit channel identifier
| isRTX | ‘1’ – relaying is enabled, ‘0’ – relaying is disabled
| isRVRS | ‘1’ – by default, when the modem receives data from the control system via UART, it transmits the data on the reverse channel, ‘0’ – on the forward channel |
| *	| NMEA checksum separator |
| hh	| NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.5. IC_H2D_SETTINGS_READ
This command allows the user to read the modem settings.  

Sentence format: **`$PTNT8,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT |
| 8	Sentence identifier |
| reserved | Reserved. Must be ‘0’ |
| *	| NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.6. IC_D2H_SETTINGS
The device uses this command to report its current settings to the control system.  

Sentence format: **`$PTNT9,x,x,x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT |
| 9 | Sentence identifier
| rxChID | Receive channel identifier
| txChID | Transmit channel identifier
| isRTX | ‘1’ – relaying is enabled, ‘0’ – relaying is disabled
| isRVRS | ‘1’ – by default, when the modem receives data from the control system via UART, it transmits the data on the reverse channel, ‘0’ – on the forward channel |
| *	| NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.7. IC_D2H_DEV_INFO
The device uses this sentence to report its data: device type, firmware version and serial number.  

Sentence format: **`$PTNT!,c--c,x,x,c--c,x,c--c*hh<CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT |
| ! | Sentence identifier |
| System moniker | System name string |
| System version | System version |
| Device type | Device type |
| Communication subsystem moniker | Communication subsystem name string with the release name in square brackets '[]' |
| Communication subsystem version | Communication subsystem version |
| Serial number	96-bit serial number (a string in hexadecimal format) |
| *	| NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


## 3. Service mode
[RedLine](RedLine_Specification_en.md) modems provide the user with a so-called "transparent channel": all data supplied to the device input is transmitted to the underwater acoustic channel without modification or analysis, then received by another modem and passed unchanged to the user at the receiving end.
For this reason, a service mode is provided to allow the modems to be configured.

The modems analyze input data only in service mode. To enter service mode, the **"service"** wire must be pulled to +3.3 V. Then, to exit service mode, the **"service"** wire must be pulled to ground.

> **CAUTION!**
> _The **"service"** wire must be pulled **ONLY** to 3-5 V or ground; connecting it to a higher voltage will cause **IRREPARABLE** damage to the device that is **NOT COVERED BY THE WARRANTY**._

> **CAUTION!**
> _Before switching on the device, the **"service"** wire must be pulled to ground; otherwise, the device will enter firmware update
> mode._

## 4. Identifier tables

### 4.1. Error codes

| Value | Name | Description |
| :--- | :--- | :--- |
| 0 | NO_ERROR | Request accepted |
| 1 | INVALID_SYNTAX | Syntax error |
| 2 | UNSUPPORTED | Command not supported |
| 3 | TRANSMITTER_BUSY | Transmitter is busy |
| 4 | ARGUMENT_OUT_OF_RANGE | Argument/parameter outside the range of permissible values |
| 5 | INVALID_OPERATION | The operation cannot be performed at this time |
| 6 | UNKNOWN_FIELD_ID | Unknown/unsupported field |
| 7 | VALUE_UNAVAILIBLE | Requested value is unavailable |
| 8 | RECEIVER_BUSY | Receiver is busy |

### 4.2. Local data identifiers

| Value | Name | Description |
| :--- | :--- | :--- |
| 0 | DEVICE_INFO | Device information |
| 2 | MAX_SUBSCRIBERS | Maximum possible number of subscribers |
| 6 | PRESSURE_RATING | Maximum operating external hydrostatic pressure in bar |

__________

<div style="page-break-after: always;"></div>

[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RedLINE/RedLINE_Protocol_Specifications_ru.md commit=129f625fb0d8a3b442d86d7311ecd559bd0e2e78 date=2022-04-13 -->
