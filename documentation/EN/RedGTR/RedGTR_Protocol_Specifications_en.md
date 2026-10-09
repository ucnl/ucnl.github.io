[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **RedGTR: Communication protocol specification**

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedGTR** - underwater acoustic code communication modem <br/> Communication protocol specification |
  
  
  
# RedGTR <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)  
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. TNT command system for RedGTR underwater acoustic modems](#2-tnt-command-system-for-redgtr-underwater-acoustic-modems)  
  - [2.1. IC_D2H_ACK - Device response](#21-ic_d2h_ack)
  - [2.2. IC_H2D_LOC_DATA_GET - Request a local parameter](#22-ic_h2d_loc_data_get)
  - [2.3. IC_H2D_LOC_DATA_SET - Set a local parameter value](#23-ic_h2d_loc_data_set)
  - [2.4. IC_D2H_LOC_DATA_VAL - Local parameter value](#24-ic_d2h_loc_data_val)
  - [2.5. IC_D2H_DEV_INFO - Device information](#25-ic_d2h_dev_info)
  - [2.6. IC_H2D_ACT_INVOKE - Request to perform an action](#26-ic_h2d_act_invoke)
  - [2.7. IC_H2D_REM_SEND - Send a command to a remote device](#27-ic_h2d_rem_send)
  - [2.8. IC_H2D_REM_PING - Request to a remote device](#28-ic_h2d_rem_ping)
  - [2.9. IC_H2D_REM_PINGEX - Request to a remote device (extended version)](#29-ic_h2d_rem_pingex)
  - [2.10. IC_D2H_REM_RECEIVED - Message received from a remote device](#210-ic_d2h_rem_received)
  - [2.11. IC_D2H_REM_TOUT - Remote device response timeout exceeded](#211-ic_d2h_rem_tout)
  - [2.12. IC_D2H_REM_PONG - Response to a remote device request](#212-ic_d2h_rem_pong)
  - [2.13. IC_D2H_REM_PONGEX - Response to a remote device request (extended version)](#213-ic_d2h_rem_pongex)
- [3. Identifier tables](#3-identifier-tables)
  - [3.1. Device type identifiers](#31-device-type-identifiers)
  - [3.2. Error codes](#32-error-codes)
  - [3.3. Local data identifiers](#33-local-data-identifiers)
  - [3.4. Service action identifiers](#34-service-action-identifiers)
  - [3.5. Remote request identifiers (code commands)](#35-remote-request-identifiers-code-commands)
     
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol
   
[RedGTR](RedGTR_Specifications_en.md) underwater acoustic modems support data interfacing using the RS-232 physical layer standard for
an asynchronous interface (UART) with a data line voltage of 3.3 V. The connection uses a four-wire cable
with Tx (transmitter), Rx (receiver), Vcc (power) and GND (ground) wires. Without additional repeaters and interface
converters, the maximum data bus length for which correct interface operation is guaranteed is no more than 2 meters.  

Default connection port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**CAUTION!**
>_The modems are powered by a 12 V DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of text (ASCII) sentences at the dialog layer.  

Sentence example:  **`$PTNT0,0*hh<CR><LF>`**  

Main elements of an NMEA0183 sentence:
* '$' - sentence start,
* 'P' - Proprietary, a proprietary code
* 'TNT' - three-letter manufacturer identifier
* '0' - sentence identifier
* ',' - comma (parameter separator)  
* '0' - parameter (in this case, an error code)
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example, FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)
________
<a name="footnote1"><sup>1</sup> The specified parameters can be changed on request</a>

<div style="page-break-after: always;"></div>

## 2. TNT command system for RedGTR underwater acoustic modems
The **D2H** prefix in a sentence name means that it is transmitted from the device (Device) to the control system (Host).
The **H2D** prefix in a sentence name means that it is transmitted from the control system (Host) to the device (Device).

### 2.1. IC_D2H_ACK
With this sentence, the device indicates that a command has been accepted or that an error has occurred (depending on the value of the errorCode parameter,
see [section 3.2](#32-error-codes)).

Sentence format:  **`$PTNT0,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 0| Sentence identifier |
| errorCode | Error code \(see [section 3.2](#32-error-codes)\) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.2. IC_H2D_LOC_DATA_GET
Request the value of a local parameter. With this sentence, the control system can request the value of a local parameter
\(see [section 3.3](#33-local-data-identifiers)\).  

Sentence format: **`$PTNT4,xx,00*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 4 | Sentence identifier |
| Requested data ID | Data identifier \(see [section 3.3](#33-local-data-identifiers)\) |
| Reserved | Reserved, must always be '00' |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.3. IC_H2D_LOC_DATA_SET
Set the value of a local parameter. With this sentence, the control system can request that a local parameter value be set \(see [section 3.3](#33-local-data-identifiers)\).  

Sentence format: **`$PTNT7,xx,00*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 7 | Sentence identifier |
| Requested data ID | Data identifier \(see [section 3.3](#33-local-data-identifiers)\) |
| Reserved | Reserved, must always be '00' |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.4. IC_D2H_LOC_DATA_VAL
Local parameter value. With this sentence, the modem returns the value of a local parameter requested
by the control system \(using the [IC_H2D_LOC_DATA_GET](#22-ic_h2d_loc_data_get) sentence\).  

Sentence format: **`$PTNT5,x,x.x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 5 | Sentence identifier |
| Requested data ID | Data identifier \(see [section 3.3](#33-local-data-identifiers)\) |
| Requested data value | Value |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.5. IC_D2H_DEV_INFO
Device information. With this sentence, the device reports its data: device type, firmware version and serial number.  

Sentence format: **`$PTNT!,c--c,x,x,c--c,x,c--c*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| !	| Sentence identifier
| System moniker | System name string |
| System version | System version |
| Device type | Device type \([see section 3.1](#31-device-type-identifiers)\) |
| Communication subsystem moniker | Communication subsystem name string with the release name in square brackets '\[\]' |
| Communication subsystem version | Communication subsystem version |
| Serial number | 96-bit serial number (a string in hexadecimal format) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.6. IC_H2D_ACT_INVOKE
Request to perform a service action.   

Sentence format: **`$PTNT6,xx,00*hh<CR><LF>`** 

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 6 | Sentence identifier |
| Action ID | Service action identifier \([see section 3.4](#34-service-action-identifiers)\) |
| Reserved | Reserved '00' |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.7. IC_H2D_REM_SEND
Transmit a code message to a remote subscriber.  

Sentence format: **`$PTNT8,x,ч*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 8 | Sentence identifier |
| Subscriber ID | Subscriber address from 0 to 25 (25 - broadcast message) |
| Message ID | Message identifier, \([see section 3.5](#35-remote-request-identifiers-code-commands)\) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.8. IC_H2D_REM_PING
Ping a remote subscriber.  

Sentence format: **`$PTNTA,x,x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| A | Sentence identifier |
| Subscriber ID | Subscriber address from 0 to 24 | 
| Timeout | Maximum response waiting time in ms (integer) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.9. IC_H2D_REM_PINGEX
Ping a remote subscriber (extended version).  

Sentence format: **`$PTNTE,x,x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| E | Sentence identifier | 
| Subscriber ID | Subscriber address from 0 to 24 |
| Message ID | Identifier of the requested parameter of the remote subscriber \([see section 3.5](#35-remote-request-identifiers-code-commands)\) |
| Timeout | Maximum response waiting time in ms (integer) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.10. IC_D2H_REM_RECEIVED
A message has been received.  

Sentence format: **`$PTNT9,x,x.x,x.x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| 9 | Sentence identifier |
| Message ID | Identifier of the received message \([see section 3.5](#35-remote-request-identifiers-code-commands)\) |
| SNR | Signal-to-interference ratio on reception, dB |
| Dpl | Doppler shift, Hz |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.11. IC_D2H_REM_TOUT
The remote subscriber response timeout has been exceeded.  

Sentence format: **`$PTNTB,x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| B | Sentence identifier |
| Subscriber ID | Identifier of the queried subscriber |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.12. IC_D2H_REM_PONG
A response to the [REM_PING](#28-ic_h2d_rem_ping) request has been received from a remote subscriber.  

Sentence format: **`$PTNTC,x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| C | Sentence identifier |
| Subscriber ID | Identifier of the queried subscriber |
| MSR | Signal-to-interference ratio on reception, dB |
| Dpl | Doppler shift, Hz |
| pTime | Signal propagation time to the queried subscriber, s |
| Dist | Distance to the queried subscriber, m (only for the version with a built-in depth sensor) |
| Dpt | Local depth, m (only for the version with a built-in depth sensor) |
| Tmp | Local temperature, °C (only for the version with a built-in depth sensor) |
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.13. IC_D2H_REM_PONGEX
A response to the [REM_PINGEX](#29-ic_h2d_rem_pingex) request has been received from a remote subscriber.  

Sentence format: **`$PTNTD,x,x,x.x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PTNT | TNT command system |
| D	| Sentence identifier
| Subscriber ID	| Identifier of the queried subscriber |
| Requested data ID	| Identifier of the requested value \([see section 3.5](#35-remote-request-identifiers-code-commands)\) |
| Requested data	| Requested value |
| MSR	| Signal-to-interference ratio on reception, dB	| 
| Dpl	| Doppler shift, Hz	| 
| pTime	| Signal propagation time to the queried subscriber, s	| 
| Dist	| Distance to the queried subscriber, m (only for the version with a built-in depth sensor)	| 
| Dpt	| Local depth, m (only for the version with a built-in depth sensor)	| 
| Tmp	| Local temperature, °C (only for the version with a built-in depth sensor)	| 
| * | NMEA checksum separator |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


## 3. Identifier tables
 
### 3.1. Device type identifiers

| Value | Device type | Description |
| :--- | :--- | :--- | 
| '0' | DEVICE_REDBASE | RedWave relay sonobuoy |
| '1' | DEVICE_REDNODE | RedWave navigation receiver |
| '2' | DEVICE_REDNAV | RedWave diver's navigator |
| '3' | DEVICE_REDGTR | RedWave code modem |
| '10' | DEVICE_REDLINE | RedLine underwater acoustic modem |
| '11' | DEVICE_NATRIX | Natrix underwater acoustic modem |

### 3.2. Error codes

| Value | Name | Description |
| :--- | :--- | :--- | 
| '0' | NO_ERROR | Request accepted |
| '1' | INVALID_SYNTAX | Syntax error |
| '2' | UNSUPPORTED | Command not supported |
| '3' | TRANSMITTER_BUSY | Transmitter busy |
| '4' | ARGUMENT_OUT_OF_RANGE | Argument/parameter outside the range of permissible values |
| '5' | INVALID_OPERATION | The operation cannot be performed at this time |
| '6' | UNKNOWN_FIELD_ID | Unknown/unsupported field |
| '7' | VALUE_UNAVAILIBLE | The requested value is not available |
| '8' | RECEIVER_BUSY | Receiver busy |
    
### 3.3. Local data identifiers

| Value | Name | Description |
| :--- | :--- | :--- | 
| ‘0’ | DEVICE_INFO | Device information |
| ‘1’ | MAX_REM_TOUT | Maximum remote response timeout, ms |
| ‘2’ | MAX_SUBS | Maximum possible number of subscriber addresses |
| ‘3’ | PTS_PRESSURE | Pressure value from the built-in sensor (if present), mbar |
| ‘4’ | PTS_TEMP | Water temperature value from the built-in sensor (if present), °C |
| ‘5’ | PTS_DEPTH | Depth (distance from the water surface) from the built-in sensor (if present) |
| ‘6’ | CORE_TEMP | Processor core temperature, °C |
| ‘7’ | BAT_VOLTAGE | Supply voltage, V |
| ‘8’ | PRESSURE_RATING | Maximum permissible external pressure, bar |
| ‘9’ | SURFACE_PRESSURE | Pressure at the water surface, mbar |
| ‘10’ | WATER_DENSITY | Water density, kg/m3 |
| ‘11’ | SALINITY | Water salinity, PSU |
| ‘12’ | SOUND_SPEED | Speed of sound in water, m/s |
| ‘13’ | GRAVITY_ACC | Gravitational acceleration, m/s2 |
| ‘14’ | Reserved |  |
| ‘15’ | Reserved |  |
| ‘16’ | Reserved |  |
| ‘17’ | Reserved |  |
| ‘18’ | Reserved |  |
| ‘19’ | Reserved |  |
| ‘20’ | SUB_ID | Subscriber address |

### 3.4. Service action identifiers

| Value | Name | Description |
| :--- | :--- | :--- | 
| '0' | LOC_INVOKE_FLASH_WRITE | Save configuration fields to internal flash memory
| '1' | LOC_INVOKE_DPT_ZERO_ADJUST | Use the current pressure reading as the pressure at the water surface
| '2' | LOC_INVOKE_RESTART | 'Warm' reboot of the device

### 3.5. Remote request identifiers (code commands)

| Name | Code | Description |
| :--- | :--- | :--- | 
| CDS_CMD_PING | 0 | Ping request |
| CDS_CMD_PONG | 1 | Response to a ping |
| CDS_CMD_DPT | 2 | Depth |
| CDS_CMD_TMP | 3 | Temperature |
| CDS_CMD_BAT | 4 | Battery voltage |
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

[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RedGTR/RedGTR_Protocol_Specifications_ru.md commit=da243547f2f274e0a5466efa98455e7a2c6fda29 date=2021-04-21 -->
