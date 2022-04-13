<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedGTR** - code communication underwater acoustic modem <br/> Communication protocol specification |
 
  
# RedGTR <br/> communication protocol specification

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Physical layer](#11-physical-layer)
  - [1.2. NMEA0183 Protocol standard](#12-nmea0183-protocol-standard)
- [2. TNT Command System for RedGTR modems](#2-tnt-command-system-for-redline-modems)
  - [2.1. IC_D2H_ACK](#21-ic_d2h_ack)
  - [2.2. IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get)
  - [2.3. IC_H2D_LOC_DATA_SET](#23-ic_h2d_loc_data_set)
  - [2.4. IC_D2H_LOC_DATA_VAL](#24-ic_d2h_loc_data_val)
  - [2.5. IC_D2H_DEV_INFO](#25-ic_d2h_dev_info)
  - [2.6. IC_H2D_ACT_INVOKE](#26-ic_h2d_act_invoke)
  - [2.7. IC_H2D_REM_SEND](#27-ic_h2d_rem_send)
  - [2.8. IC_H2D_REM_PING](#28-ic_h2d_rem_ping)
  - [2.9. IC_H2D_REM_PINGEX](#29-ic_h2d_rem_pingex)
  - [2.10. IC_D2H_REM_RECEIVED](#210-ic_d2h_rem_received)
  - [2.11. IC_D2H_REM_TOUT](#211-ic_d2h_rem_tout)
  - [2.12. IC_D2H_REM_PONG](#212-ic_d2h_rem_pong)
  - [2.13. IC_D2H_REM_PONGEX](#213-ic_d2h_rem_pongex)
- [3. Identifiers](#3-identifiers)
  - [3.1. Device type identifiers](#31-device-type-identifiers)
  - [3.2. Error messages](#32-error-messages)
  - [3.3. Local data identifier](#33-local-data-identifier)
  - [3.4. Service actions identifiers](#34-service-actions-identifiers)
  - [3.5. Remote requests identifiers](#35-remote-requests-identifiers)

<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer
[RedGTR](RedGTR_Specification_ru.md) underwater acoustic modems support data pairing using the RS-232 physical layer standard for asynchronous interface (UART) with a 3.3V data line voltage. The connection is made using a four-wire cable with Tx (transmitter), Rx (receiver), Vcc (power) and GND (ground) wires. Without the use of additional repeaters and interface converters, the maximum cable length, for which the correct operation of the interface is guaranteed, is no more than 2 meters.

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

## 2. TNT Command System for RedGTR modems
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
| 1 | errCode	| Error code \([see 3.2.](#32-error-messages)\) |
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
| 1 | dataID	| Parameter ID \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | reserved | should be '00' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.3. IC_H2D_LOC_DATA_SET
Setting a value of a local parameter \([see 3.3.](#33-local-data-identifiers)\).  

Format:  **`$PTNT7,xx,00*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
| | 7 | Sentence ID |
| 1 | Requested data ID | Local parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | Reserved | Reserved, should always be '00' |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |


### 2.4. IC_D2H_LOC_DATA_VAL
Device's response to [IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get) sentence.

Format: **`$PTNT5,x,x<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 5 | Sentence ID | 
| 1 | Requested data ID | Parameter ID \([see 3.3.](#33-local-data-identifiers)\) | 
| 2 | Value | Queried value | 
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.5. IC_D2H_DEV_INFO
Device's responce to [IC_D2H_LOC_DATA_GET](#22-ic_h2d_loc_data_get), if the queried parameter ID = [LOC_DATA_DEV_INFO](#33-local-data-identifiers).

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
| 5 | Device type | Device type \([see 3.1.](#31-device-type-identifiers)\) |
| 6 | Serial number | Serial number |
| | *	| NMEA checksum separator |
| | hh	| NMEA checksum |
| | \<CR\>\<LF\> | end of sentence |

### 2.6. IC_H2D_ACT_INVOKE
Service action request.   

Format:  **`$PTNT6,xx,00*hh<CR><LF>`** 

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 6 | Идентификатор сообщения |
| 1 | Action ID | Service action ID \([see 3.4.](#34-service-actions-identifiers)\) |
| 2 | Reserved | Reserved, should always be '00' |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |

### 2.7. IC_H2D_REM_SEND
Send a code message to a remote device.  

Format: **`$PTNT8,x,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|  | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
| 8 | Sentence ID |
| 1 | Subscriber ID | Remote device ID (from 0 to 25. 25 is broadcast address) |
| 2 | Message ID | Code message ID \([see 3.5.](#35-remote-requests-identifiers)\) |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |

### 2.8. IC_H2D_REM_PING
Send a ping to a remote device.  

Format: **`$PTNTA,x,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | A | Sentence ID |
| 1 | Subscriber ID | Remote device address from 0 to 24 | 
| 2 | Timeout | Max. timeout in msec (integer value) |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |

### 2.9. IC_H2D_REM_PINGEX
Send a ping to a remote device (extended version).  

Format: **`$PTNTE,x,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | E | Sentence ID | 
| 1 | Subscriber ID | Remote device address from 0 to 24 |
| 2 | Message ID | Requested parameter identifier \([see 3.5.](#35-remote-requests-identifiers)\) |
| 3 | Timeout | Max. timeout in msec (integer value) |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |

### 2.10. IC_D2H_REM_RECEIVED
Received a code message from a remote subscriber.  

Format: **`$PTNT9,x,x.x,x.x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | 9 | Sentence ID |
| 1 | Message ID | Received message ID \([see 3.5.](#35-remote-requests-identifiers)\) |
| 2 | MSR | Signal quality (Main lobe to side-peak ratio, dB |
| 3 | Dpl | Doppler shift, Hz |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |



### 2.11. IC_D2H_REM_TOUT
Remote device timeout exceeded.  

Format: **`$PTNTB,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | B | Sentence ID |
| 1 | Subscriber ID | Remote device identifier |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |


### 2.12. IC_D2H_REM_PONG
Remote device response received for request [REM_PING](#28-ic_h2d_rem_ping).  

Format: **`$PTNTC,x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | C | Sentence ID |
| 1 | Subscriber ID | Remote device ID |
| 2 | MSR | Signal quality (Main lobe to side-peak ratio), dB |
| 3 | Dpl | Doppler shift, Hz |
| 4 | pTime | Signal propagation time to the requested device, sec |
| 5 | Dist | Distance to the requested device, m (only for devices with built-in depth sensor) |
| 6 | Dpt | Own depth, m (only for devices with built-in depth sensor) |
| 7 | Tmp | Water temperature, °С (only for devices with built-in depth sensor) |
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |


### 2.13. IC_D2H_REM_PONGEX
Remote device response received for request [REM_PINGEX](#29-ic_h2d_rem_pingex).  

Format: **`$PTNTD,x,x,x.x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | TNT | Proprietery code ID |
|  | D	| Sentence ID |
| 1 | Subscriber ID | Remote device ID |
| 2 | Requested data ID	| Requested parameter ID \([see 3.5.](#35-remote-requests-identifiers)\) |
| 3 | Requested data | Received value |
| 4 | MSR	| Signal quality (Main lobe to side-peak ratio), dB	| 
| 5 | Dpl	| Doppler shift, Hz	| 
| 6 | pTime	| Signal propagation time to the requested device, sec	| 
| 7 | Dist	| Distance to the requested device, m (only for devices with built-in depth sensor)	| 
| 8 | Dpt	| Own depth, m (only for devices with built-in depth sensor)	| 
| 9 | Tmp	| Water temperature, °С (only for devices with built-in depth sensor)	| 
|  | * | NMEA checksum separator |
|  | hh	| NMEA checksum |
|  | \<CR\>\<LF\> | end of sentence |


## 3. Identifiers 
### 3.1. Device type identifiers

| Value | Device type | Description |
| :--- | :--- | :--- | 
| 0 | DEVICE_REDBASE | RedWave GIB |
| 1 | DEVICE_REDNODE | RedWave navigation receiver |
| 2 | DEVICE_REDNAV | RedWave diver's navigation receiver |
| 3 | DEVICE_REDGTR | RedGTR code modem |
| 10 | DEVICE_REDLINE | RedLine modem |

### 3.2. Error messages

| Value | Name | Description |
| :--- | :--- | :--- | 
| 0 | NO_ERROR | Request accepted |
| 1 | INVALID_SYNTAX | Syntax error in incoming sentence |
| 2 | UNSUPPORTED | Command is not supported |
| 3 | TRANSMITTER_BUSY | Transmitter is busy |
| 4 | ARGUMENT_OUT_OF_RANGE | One or more arguments in the sentence is out of range |
| 5 | INVALID_OPERATION | Operation cannot be performed at the moment |
| 6 | UNKNOWN_FIELD_ID | Unknown/unsupported field ID |
| 7 | VALUE_UNAVAILIBLE | Requested value is not available at the moment |
| 8 | RECEIVER_BUSY | Receiver if busy (waiting for a response of a remote device) |
    
### 3.3. Local data identifiers

| Value | Name | Description |
| :--- | :--- | :--- | 
| 0 | DEVICE_INFO | Device information |
| 1 | MAX_REM_TOUT | Max. timeout value for remote requests, msec |
| 2 | MAX_SUBS | Max. number of addresses (device IDs) |
| 3 | PTS_PRESSURE | External hydrostatic pressure, mBar |
| 4 | PTS_TEMP | Water temperature, °С |
| 5 | PTS_DEPTH | Depth, m |
| 6 | CORE_TEMP | CPU core temperature, °С |
| 7 | BAT_VOLTAGE | Supply voltage, V |
| 8 | PRESSURE_RATING | Max. allowed external hydrostatic pressure, Bar |
| 9 | SURFACE_PRESSURE | Pressure at the water surface, mBar |
| 10 | WATER_DENSITY | Water density, kg/m<sup>3</sup> |
| 11 | SALINITY | Water salinity, PSU |
| 12 | SOUND_SPEED | Speed of sound, m/s |
| 13 | GRAVITY_ACC | Gravity acceleration, m/s<sup>2</sup> |
| 14 | Reserved |  |
| 15 | Reserved |  |
| 16 | Reserved |  |
| 17 | Reserved |  |
| 18 | Reserved |  |
| 19 | Reserved |  |
| 20 | SUB_ID | Device ID (address) |

### 3.4. Service actions identifiers

| Value | Name | Description |
| :--- | :--- | :--- | 
| 0 | LOC_INVOKE_FLASH_WRITE | Save current settings in flash |
| 1 | LOC_INVOKE_DPT_ZERO_ADJUST | Set current pressure as the pressure at the water surface |
| 2 | LOC_INVOKE_RESTART | Hot system restart |

### 3.5. Remote requests identifiers

| Name | Value | Description |
| :--- | :--- | :--- | 
| CDS_CMD_PING | 0 | Ping |
| CDS_CMD_PONG | 1 | Pong |
| CDS_CMD_DPT | 2 | Depth |
| CDS_CMD_TMP | 3 | Temperature |
| CDS_CMD_BAT | 4 | Supply voltage |
| CDS_CMD_USR_0 | 5 | User command |
| CDS_CMD_USR_1 | 6 | User command |
| CDS_CMD_USR_2 | 7 | User command |
| CDS_CMD_USR_3 | 8 | User command |
| CDS_CMD_USR_4 | 9 | User command |
| CDS_CMD_USR_5 | 10 | User command |
| CDS_CMD_USR_6 | 11 | User command |
| CDS_CMD_USR_7 | 12 | User command |
| CDS_CMD_USR_8 | 13 | User command |
| CDS_CMD_USR_9 | 14 | User command |
| CDS_CMD_USR_10 | 15 | User command |
| CDS_CMD_USR_11 | 16 | User command |
| CDS_CMD_USR_12 | 17 | User command |
| CDS_CMD_USR_13 | 18 | User command |
| CDS_CMD_USR_14 | 19 | User command |
| CDS_CMD_USR_15 | 20 | User command |
| CDS_CMD_USR_16 | 21 | User command |
| CDS_CMD_USR_17 | 22 | User command |
| CDS_CMD_USR_18 | 23 | User command |
| CDS_CMD_USR_19 | 24 | User command |
| CDS_CMD_USR_20 | 25 | User command |
| CDS_CMD_USR_21 | 26 | User command |
| CDS_CMD_USR_22 | 27 | User command |
| CDS_CMD_USR_23 | 28 | User command |
| CDS_CMD_USR_24 | 29 | User command |
| CDS_CMD_USR_25 | 30 | User command |
| CDS_CMD_USR_26 | 31 | User command |
| CDS_CMD_USR_27 | 32 | User command |
| CDS_CMD_USR_28 | 33 | User command |
| CDS_CMD_USR_29 | 34 | User command |
| CDS_CMD_USR_30 | 35 | User command |
| CDS_CMD_USR_31 | 36 | User command |
| CDS_CMD_USR_32 | 37 | User command |
| CDS_CMD_USR_33 | 38 | User command |
| CDS_CMD_USR_34 | 39 | User command |

<div style="page-break-after: always;"></div>

____________
[Back to contents](#contents)


