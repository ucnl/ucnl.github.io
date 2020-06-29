| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima USBL** <br/> Communication protocol specification |


  
# Zima USBL <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents
- [1. Introducation](#1-introduction)  
  - [1.1. Physical layer](#11-physical-layer)
  - [1.2. NMEA0183 Protocol standard](#12-nmea0183-protocol-standard)
- [2. ZMA command system for Zima USBL system](#2-zma-command-system-for-zima-usbl-system)  
   - [2.1. IC_D2H_ACK](#21-ic_d2h_ack)
   - [2.2. IC_H2D_FLD_GET](#22-ic_h2d_fld_get)
   - [2.3. IC_H2D_FLD_SET](#23-ic_h2d_fld_set)
   - [2.4. IC_D2H_FLD_VAL](#24-ic_d2h_fld_val)
   - [2.5. IC_H2D_LOC_DATA_GET](#25-ic_h2d_loc_data_get)
   - [2.6. IC_H2D_LOC_DATA_SET](#26-ic_h2d_loc_data_set)
   - [2.7. IC_D2H_LOC_DATA_VAL](#27-ic_d2h_loc_data_val)
   - [2.8. IC_H2D_LOC_INVOKE](#28-ic_h2d_loc_invoke)
   - [2.9. IC_D2H_LD](#29-ic_d2h_ld)
   - [2.10. IC_D2H_BASE_REQ](#210-ic_d2h_base_req)
   - [2.11. IC_H2D_REM_REQ](#211-ic_h2d_rem_req)
   - [2.12. IC_D2H_REM_TOUT](#212-ic_d2h_rem_tout)
   - [2.13. IC_D2H_REM_RESP](#213-ic_d2h_rem_resp)
   - [2.14. IC_D2H_SYS_STATE](#214-ic_d2h_sys_state)
   - [2.15. IC_D2H_INC_DATA](#215-ic_d2h_inc_data)
   - [2.16. IC_H2D_REM_REQ_EX](#216-ic_h2d_rem_req_ex)
   - [2.17. IC_D2H_DEV_INFO](#217-ic_d2h_dev_info)
   - [2.18. IC_D2H_BASE_REQ](#210-ic_d2h_base_req)   
- [3. Identifiers](#3-identifiers)
   - [3.1. Device types](#31-device-types)
   - [3.2. Error codes](#32-error-codes)
   - [3.3. Local data identifiers](#33-local-data-identifiers)
   - [3.4. Service action identifiers](#34-service-action-identifiers)
   - [3.5. Remote request identifiers](#35-remote-request-identifiers)


<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer
Devices of [Zima USBL](Zima_DataBrief_en.md) underwater acoustic tracking system support data pairing using the **RS-232** physical layer standard for asynchronous interface **(UART)** with a **3.3V** data line voltage. The connection is made using a four-wire cable with Tx (transmitter), Rx (receiver), Vcc (power) and GND (ground) wires. Without the use of additional repeaters and interface converters, the maximum cable length, for which the correct operation of the interface is guaranteed, is no more than 2 meters.

Default port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**WARNING!**
>_Devices are powered by 12 Volt DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 Protocol standard
The NMEA0183 standard describes the format of text (ASCII) messages at the interactive level.

Sentence example: **`$PZMA0,0*hh<СR><LF>`**  

Parts of a message (sentence) NMEА0183:
* '$' - sentence start,
* 'P' - Proprietary
* 'ZMA' - Manufacturer/protocol identifier
* '0' - sentence identifier
* ',' - parameters separator
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example FF, 01). Byte-by-byte XOR for all characters between '$' and '*'.
* \<CR\>\<LF\> - end of sentence
________
<a name="footnote1"><sup>1</sup> Specified parameters can be changed by a request</a>

<div style="page-break-after: always;"></div>

## 2. ZMA command system for Zima USBL system
The **D2H** prefix in the message name means that it is transmitted from the device (Device) to the host system (Host).
The **H2D** prefix in the message name means that it is transmitted from the host system to the device.

### 2.1. IC_D2H_ACK
Device acknowledgement.

Format: **`$PTNT0,x*hh<CR><LF>`**  

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 0	| Sentence ID |
| 1 | errCode	| Error code \([see 3.2.](#32-error-codes)\) |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.2. IC_H2D_FLD_GET
Reads the value of the field. In response to this command, the device sends a message [IC_D2H_FLD_VAL](#24-ic_d2h_fld_val) containing the value of the requested field
in case of successful assignment and message [IC_D2H_ACK](#21-ic_d2h_ack) with an error code, in case of an error. 

Format: **`$PZMA1,xx,00*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|  | $	| Sentence start '$' |
|  | P | Proprietary sentence |
|  | ZMA | Proprietery code ID |
|   | 1 | Sentence ID |
| 1 | Field ID | Field identifier |
| 2 | Reserved | Shall be '00' |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.3. IC_H2D_FLD_SET
Sets the value of the field. In response to this command, the device sends a message [IC_D2H_FLD_VAL](#24-ic_d2h_fld_val) containing the value of the requested field in
in case of successful assignment and message [IC_D2H_ACK](#21-ic_d2h_ack) with an error code, in case of an error.

Format: **`$PZMA2,x,x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 2 | Sentence ID |
| 1 | Field ID | Field identifier |
| 2 | Field value | Field value (0..99) |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.4 IC_D2H_FLD_VAL
Requested field value.  

Format: **`$PZMA3,xx,xx,00*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 3 | Sentence ID |
| 1 | Requested field ID | Field identifier |
| 2 | Value | Requested value |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |



### 2.5 IC_H2D_LOC_DATA_GET
Reads the value of local parameter.  

Format: **`$PZMA4,xx,00*hh<CR><LF`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 4	| Sentence ID |
| 1 | LocDataID	| Local parameter ID \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | Reserved	| Reserved, shall be '00' |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.6 IC_H2D_LOC_DATA_SET
Sets the value of a local parameter.  

Format: **`$PZMA5,xx,x.x*hh<CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 5	| Sentence ID |
| 1 | LocDataID	| Local parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | LocDataValue	| New value to be set |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.7 IC_D2H_LOC_DATA_VAL
Value of the requested local parameter.  

Format: **`$PZMA6,xx,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 6 | Sentence ID |
| 1 | LocDataID | Local parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | LocDataValue | Actual parameter value |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |

### 2.8 IC_H2D_LOC_INVOKE
Service operation invokation.  

Format: **`$PZMA7,xx,xx*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | 7 | Sentence ID |
| 1 | ActionID | Service operation identifier \([see 3.4.](#34-service-action-identifiers)\) |
| 2 | ActionParam | Service operation parameter |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.9 IC_D2H_LD
Navigation data (responder-beacon).  

Format: **`$PZMAA,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | A	| Sentence ID |
| 1 | Azimuth	| Azimuth to the base station, ° |
| 2 | Distance	| Slant range to the base station, m |
| 3 | MSR	| Main lobe to side-peak ratio, dB |
| 4 | Dpl	| Doppler shift, Hz |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |

### 2.10 IC_D2H_BASE_REQ
A request from the base station is received (responder-beacon).  

Format: **`$PZMAB,x,x.x,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | B | Sentence ID |
| 1 | CommandID | Request ID \([see 3.5.](#35-remote-request-identifiers)\) |
| 2 | MSR	| Main lobe to side-peak ratio, dB |
| 3 | Dpl	| Doppler shift, Hz |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.11 IC_H2D_REM_REQ
Request to a remote responder-beacon.

Format: **`$PZMAС,x,x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | C | Sentence ID |
| 1 | TargetID | Address of a remote responder-beacon |
| 2 | RequestID | Request ID \([see 3.5.](#35-remote-request-identifiers)\) |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.12 IC_D2H_REM_TOUT
Requested responder-beacon timeout exceeded.  

Format: **`$PZMAD,x, x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | D | Идентификатор сообщения |
| 1 | TargetID | Address of the requested remote responder-beacon |
| 2 | RequestID | Request identifier \([see 3.5.](#35-remote-request-identifiers)\) |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.13 IC_D2H_REM_RESP
Station has received a response of a requested responder-beacon.  

Format: **`$PZMAE, x,x,x,x.x,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | E | Sentence ID |
| 1 | TargetID | Address of the requested remote responder-beacon |
| 2 | RequestID | Request identifier \([see 3.5.](#35-remote-request-identifiers)\) |
| 2 | dFlag | reserved |
| 4 | Azimuth | Horizontal angle to the responder-beacon, °. |
| 5 | Distance | Slant range to the responder-beacon, m |
| 6 | DataValue | Value of the requested parameter |
| 7 | MSR | Main lobe to side-peak ratio, dB |
| 8 | Dpl | Doppler shift, Hz |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.14 IC_D2H_SYS_STATE
Station state.  

Format: **`$PZMAF, x.x,x.x,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | F | Sentence ID |
| 1 | Temperature | Water temperature, °С |
| 2 | Depth | Depth of the base station, m |
| 3 | isAHRSEnabled | reserved |
| 4 | TRX_State | Transmitter/Receiver state |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


### 2.15 IC_D2H_INC_DATA
Built-in inclinometer data[<sup>*</sup>](#footnote_incdata).  

Format: **`$PZMAG, x.x,x.x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | G | Sentence ID |
| 1 | Roll | Roll, °. 0 - vertical, 0 .. +90 - to the right side, 0 .. -90 - to the left side |
| 2 | Pitch | Pitch, °. 0 - vertical, 0 .. +90 - to bow, 0 .. -90 - to stern |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |

____________
<a name="footnote_incdata"><sup>*</sup></a> For devices released after 09.2019  

### 2.16 IC_H2D_REM_REQ_EX
Request of a remote responder-beacon with transmission of a reverse azimiuth.  

Format: **`$PZMAH,x,x,x*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | H	| Sentence ID |
| 1 | TargetAddress	| Address of a remote responder-beacon to request |
| 2 | RequestID | Command (should be always **CDS_DPT_GET** \([see 3.5.](#35-remote-request-identifiers)\) |
| 3 | ReverseAzimuthToTheBase | Reverse azimuth[<sup>*</sup>](#footnote_revaz) from the responder-beacon to the base station |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |

____________
<a name="footnote_revaz"><sup>*</sup></a> The azimuth value from the responder-beacon to the base station must be pre-calculated. When using the [ZHost](https://api.github.com/repos/ucnl/ZHost/zipball) application, it happens automatically, if there is a connected system for determining the heading and position of the [Zima-B](Zima_B_Specification_en.md) antenna.  


### 2.17 IC_D2H_DEV_INFO
Device information.  

Format: **`$PZMA!, c--c,x,c--c,x,x,c--c*hh <CR><LF>`**

| № | Field/Parameter |	Description |
| :--- | :--- | :--- |
|   | $	| Sentence start '$' |
|   | P | Proprietary sentence |
|   | ZMA | Proprietery code ID |
|   | ! | Sentence ID |
| 1 | Sys_moniker | System name |
| 2 | Sys_version | System version |
| 3 | Device_Type | Device type \(see [3.1.](#31-device-types)\) |
| 4 | Core_moniker | Acoustic subsystem name |
| 5 | Core_version | Acoustic subsystem version |
| 6 |Serial number | Device serial number |
|   | *	| NMEA checksum separator |
|   | hh	| NMEA checksum |
|   | \<CR\>\<LF\> | end of sentence |


<div style="page-break-after: always;"></div>

## 3. Identifiers

### 3.1 Device types 

| Value | Name | Description |
| :---: | :--- | :--- |
| 0 |	DEV_BASE | Zima-B base station |
| 1 | DEV_BCN | Zima-R responder-beacon |

### 3.2 Error codes

| Value | Name | Description |
| :---: | :--- | :--- |
| 0 | NO_ERROR | Request accepted | 
| 1 | INVALID_SYNTAX | Syntax error | 
| 2 | UNSUPPORTED | Request is not supported | 
| 3 | TRANSMITTER_BUSY | Transmitter is busy | 
| 4 | ARGUMENT_OUT_OF_RANGE | One or more arguments is out of range | 
| 5 | INVALID_OPERATION | Requested operation can not be performed at the moment | 
| 6 | UNKNOWN_FIELD_ID | Unknown/unsupported field ID | 
| 7 | VALUE_UNAVAILIBLE | Requested value is not available at the moment | 
| 8 | RECEIVER_BUSY | Receiver is busy | 
| 9 | WAKE_UP | Energy Saving Management. The responder-beacon sends an error message with this parameter immediately after waking up | 
| 10 | STAND_BY | Energy Saving Management. The responder-beacon an error message with this parameter before going to sleep | 

### 3.3 Local data identifiers

| Value | Name | Description |
| :---: | :--- | :--- |
| 0 | DEVICE_INFO | Device information |
| 1 | LOC_DATA_MAX_REMOTE_TIMEOUT | Remote response timeout, msec |
| 2 | LOC_DATA_MAX_SUBSCRIBERS | Max. number of responder-beacons (addresses) |
| 3 | LOC_DATA_PTS_PRESSURE | Indications of the built-in pressure sensor, mBar |
| 4 | LOC_DATA_PTS_TEMPERATURE | Indications of the built-in temperature sensor,˚С |
| 5 | LOC_DATA_PTS_DEPTH | Depth of the device, m |
| 6 | LOC_DATA_CORE_TEMPERATURE | CPU core temperature, ˚С |
| 7 | LOC_DATA_BAT_CHARGE | Battery voltage, V |
| 8 | LOC_DATA_PRESSURE_RATING | Max. allowed external hydrostatic pressure, Bar |
| 9 | LOC_DATA_ZERO_PRESSURE | Pressure at the water surface, mBar |
| 10 | LOC_DATA_WATER_DENSITY | Water density, kg/m<sup>3</sup> |
| 11 | LOC_DATA_SALINITY | Water salinity, PSU |
| 12 | LOC_DATA_SOUNDSPEED | Speed of sound, m/s |
| 13 | LOC_DATA_GRAVITY_ACC | Gravity acceleration, m/s<sup>2</sup> |

### 3.4 Service action identifiers

| Value | Name | Description |
| :---: | :--- | :--- |
| 0 | LOC_INVOKE_FLASH_WRITE | Save all settings in built-in flash memory |
| 1 | LOC_INVOKE_DPT_ZERO_ADJUST | Set current pressure readings as a pressure at the water surface |
| 2 | LOC_INVOKE_SYSTEM_RESET | Warm system reset |
| 3 | LOC_INVOKE_STAND_BY | Go to sleep mode |
| 4 | LOC_INVOKE_UART_OFF | Turn off the UART unit |

### 3.5 Remote request identifiers
| Name | Value | Description |
| :---: | :--- | :--- |
| CDS_PING | 361 | Ping |
| CDS_DPT_GET | 362 | Remote responder-beacon depth |
| CDS_STY_SET_0 | 363 | Set salinity 0 PSU |
| CDS_STY_SET_1 | 364 | ... |
| CDS_STY_SET_2 | 365 | ... |
| CDS_STY_SET_3 | 366 | ... |
| CDS_STY_SET_4 | 367 | ... |
| CDS_STY_SET_5 | 368 | ... |
| CDS_STY_SET_6 | 369 | ... |
| CDS_STY_SET_7 | 370 | ... |
| CDS_STY_SET_8 | 371 | ... |
| CDS_STY_SET_9 | 372 | ... |
| CDS_STY_SET_10 | 373 | ... |
| CDS_STY_SET_11 | 374 | ... |
| CDS_STY_SET_12 | 375 | ... |
| CDS_STY_SET_13 | 376 | ... |
| CDS_STY_SET_14 | 377 | ... |
| CDS_STY_SET_15 | 378 | ... |
| CDS_STY_SET_16 | 379 | ... |
| CDS_STY_SET_17 | 380 | ... |
| CDS_STY_SET_18 | 381 | ... |
| CDS_STY_SET_19 | 382 | ... |
| CDS_STY_SET_20 | 383 | ... |
| CDS_STY_SET_21 | 384 | ... |
| CDS_STY_SET_22 | 385 | ... |
| CDS_STY_SET_23 | 386 | ... |
| CDS_STY_SET_24 | 387 | ... |
| CDS_STY_SET_25 | 388 | ... |
| CDS_STY_SET_26 | 389 | ... |
| CDS_STY_SET_27 | 390 | ... |
| CDS_STY_SET_28 | 391 | ... |
| CDS_STY_SET_29 | 392 | ... |
| CDS_STY_SET_30 | 393 | ... |
| CDS_STY_SET_31 | 394 | ... |
| CDS_STY_SET_32 | 395 | ... |
| CDS_STY_SET_33 | 396 | ... |
| CDS_STY_SET_34 | 397 | ... |
| CDS_STY_SET_35 | 398 | ... |
| CDS_STY_SET_36 | 399 | ... |
| CDS_STY_SET_37 | 400 | ... |
| CDS_STY_SET_38 | 401 | ... |
| CDS_STY_SET_39 | 402 | ... |
| CDS_STY_SET_40 | 403 | Set salinity 40 PSU |
| CDS_SLP_SET_59_60 | 404 | Set sleep mode: sleep 59 from 60 seconds |
| CDS_SLP_SET_58_60 | 405 | Set sleep mode: sleep 58 from 60 seconds |
| CDS_SLP_SET_56_60 | 406 | Set sleep mode: sleep 56 from 60 seconds |
| CDS_SLP_SET_52_60 | 407 | Set sleep mode: sleep 52 from 60 seconds |
| CDS_SLP_SET_50_60 | 408 | Set sleep mode: sleep 50 from 60 seconds |
| CDS_SLP_SET_40_60 | 409 | Set sleep mode: sleep 40 from 60 seconds |
| CDS_SLP_SET_30_60 | 410 | Set sleep mode: sleep 30 from 60 seconds |
| CDS_SLP_SET_20_60 | 411 | Set sleep mode: sleep 20 from 60 seconds |
| CDS_SLP_SET_10_60 | 412 | Set sleep mode: sleep 10 from 60 seconds |
| CDS_SLP_SET_NEVER | 413 | Set sleep mode - always on |
| CDS_BAT_CHG_GET | 414 | Battery voltage |
| CDS_PTS_TMP_GET | 415 | Water temperature | 
| CDS_PTS_PRS_GET | 416 | External pressure |
| CDS_CRE_TMP_GET | 417 | CPU core temperature |
| CDS_SLP_GET | 418 | Sleep mode |
| CDS_STY_GET | 419 | Salinity |
| CDS_CMD_RSV_0 | 420 | Reserved |
| CDS_CMD_RSV_1 | 421 | Reserved |
| CDS_CMD_RSV_2 | 422 | Reserved |
| CDS_CMD_RSV_3 | 423 | Reserved |
| CDS_CMD_RSV_4 | 424 | Reserved |
| CDS_CMD_RSV_5 | 425 | Reserved |
| CDS_CMD_ZDPT_ADJ | 426 | Set current pressure readings as pressure at the water surface |
| CDS_USR_CMD_0 | 427 | User command 0 |
| CDS_USR_CMD_1 | 428 | User command 1 |
| CDS_USR_CMD_2 | 429 | User command 2 |
| CDS_USR_CMD_3 | 430 | User command  3 |
| CDS_USR_CMD_4 | 431 | User command  4 |
| CDS_USR_CMD_5 | 432 | User command  5 |
| CDS_USR_CMD_6 | 433 | User command  6 |
| CDS_USR_CMD_7 | 434 | User command  7 |
| CDS_USR_CMD_8 | 435 | User command  8 |
| CDS_USR_CMD_9 | 436 | User command  9 |
| CDS_USR_CMD_10 | 437 | User command  10 |
| CDS_USR_CMD_11 | 438 | User command  11 |
| CDS_USR_CMD_12 | 439 | User command  12 |
| CDS_USR_CMD_13 | 440 | User command  13 |
| CDS_USR_CMD_14 | 441 | User command  14 |
| CDS_USR_CMD_15 | 442 | User command  15 |
| CDS_USR_CMD_16 | 443 | User command  16 |
| CDS_USR_CMD_17 | 444 | User command  17 |
| CDS_USR_CMD_18 | 445 | User command  18 |
| CDS_USR_CMD_19 | 446 | User command  19 |
| CDS_USR_CMD_20 | 447 | User command  20 |
| CDS_USR_CMD_21 | 448 | User command  21 |
| CDS_USR_CMD_22 | 449 | User command  22 |
| CDS_USR_CMD_23 | 450 | User command  23 |
| CDS_USR_CMD_24 | 451 | User command  24 |
| CDS_USR_CMD_25 | 452 | User command  25 |
| CDS_USR_CMD_26 | 453 | User command  26 |
| CDS_USR_CMD_27 | 454 | User command  27 |
| CDS_USR_CMD_28 | 455 | User command  28 |
| CDS_USR_CMD_29 | 456 | User command  29 |
| CDS_USR_CMD_30 | 457 | User command  30 |
| CDS_USR_CMD_31 | 458 | User command  31 |
| CDS_USR_CMD_32 | 459 | User command  32 |
| CDS_RESERVED_0 | 460 | Reserved |
| CDS_RESERVED_1 | 461 | Reserved |
| CDS_RESERVED_2 | 462 | Reserved |
| CDS_RESERVED_3 | 463 | Reserved |
| CDS_RESERVED_4 | 464 | Reserved |
| CDS_RESERVED_5 | 465 | Reserved |
| CDS_RESERVED_6 | 466 | Reserved |
| CDS_RESERVED_7 | 467 | Reserved |
| CDS_SET_ADDR_01 | 468 | Set address 1 |
| CDS_SET_ADDR_02 | 469 | Set address  2 |
| CDS_SET_ADDR_03 | 470 | Set address  3 |
| CDS_SET_ADDR_04 | 471 | Set address  4 |
| CDS_SET_ADDR_05 | 472 | Set address  5 |
| CDS_SET_ADDR_06 | 473 | Set address  6 |
| CDS_SET_ADDR_07 | 474 | Set address  7 |
| CDS_SET_ADDR_08 | 475 | Set address  8 |
| CDS_SET_ADDR_09 | 476 | Set address  9 |
| CDS_SET_ADDR_10 | 477 | Set address  10 |
| CDS_SET_ADDR_11 | 478 | Set address  11 |
| CDS_SET_ADDR_12 | 479 | Set address  12 |
| CDS_SET_ADDR_13 | 480 | Set address  13 |
| CDS_SET_ADDR_14 | 481 | Set address  14 |
| CDS_SET_ADDR_15 | 482 | Set address  15 |
| CDS_SET_ADDR_16 | 483 | Set address  16 |
| CDS_SET_ADDR_17 | 484 | Set address  17 |
| CDS_SET_ADDR_18 | 485 | Set address  18 |
| CDS_SET_ADDR_19 | 486 | Set address  19 |
| CDS_SET_ADDR_20 | 487 | Set address  20 |
| CDS_SET_ADDR_21 | 488 | Set address  21 |
| CDS_SET_ADDR_22 | 489 | Set address  22 |
| CDS_SET_ADDR_23 | 490 | Set address  23 |
| CDS___________0 | 491 | Reserved |
| CDS___________1 | 492 | Reserved |
| CDS___________2 | 493 | Reserved |
| CDS___________3 | 494 | Reserved |
| CDS___________4 | 495 | Reserved |
| CDS___________5 | 496 | Reserved |
| CDS___________6 | 497 | Reserved |
| CDS___________7 | 498 | Reserved |
| CDS___________8 | 499 | Reserved |
| CDS_ERR_NSUPP | 500 | Error - request is not supported |
| CDS_ERR_NAVAIL | 501 | Error - requested data is not available at the moment |
| CDS_ERR_RES_0 | 502 | Error - reserved |
| CDS_ERR_RES_1 | 503 | Error - reserved |
| CDS_ERR_RES_2 | 504 | Error - reserved |
| CDS_ERR_RES_3 | 505 | Error - reserved |
| CDS_ERR_RES_4 | 506 | Error - reserved |
| CDS_ERR_RES_5 | 507 | Error - reserved |
| CDS_ERR_RES_6 | 508 | Error - reserved |
| CDS_ERR_BAT_LOW | 509 | Low battery voltage |




