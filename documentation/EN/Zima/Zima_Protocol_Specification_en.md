[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima USBL: Communication protocol specification**

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

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima USBL** - underwater acoustic navigation system <br/> Communication protocol specification |

# Zima USBL <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)  
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. ZMA command system](#2-zma-command-system)  
   - [2.1. IC_D2H_ACK - device response](#21-ic_d2h_ack)
   - [2.2. IC_H2D_FLD_GET - field value request](#22-ic_h2d_fld_get)
   - [2.3. IC_H2D_FLD_SET - set field value](#23-ic_h2d_fld_set)
   - [2.4. IC_D2H_FLD_VAL - field value](#24-ic_d2h_fld_val)
   - [2.5. IC_H2D_LOC_DATA_GET - local parameter request](#25-ic_h2d_loc_data_get)
   - [2.6. IC_H2D_LOC_DATA_SET - set local parameter value](#26-ic_h2d_loc_data_set)
   - [2.7. IC_D2H_LOC_DATA_VAL - local parameter value](#27-ic_d2h_loc_data_val)
   - [2.8. IC_H2D_LOC_INVOKE - service function](#28-ic_h2d_loc_invoke)
   - [2.9. IC_D2H_LD - navigation data](#29-ic_d2h_ld)
   - [2.10. IC_D2H_BASE_REQ - base station request received](#210-ic_d2h_base_req)
   - [2.11. IC_H2D_REM_REQ - remote responder-beacon request](#211-ic_h2d_rem_req)
   - [2.12. IC_D2H_REM_TOUT - remote responder-beacon timeout](#212-ic_d2h_rem_tout)
   - [2.13. IC_D2H_REM_RESP - remote responder-beacon response](#213-ic_d2h_rem_resp)
   - [2.14. IC_D2H_SYS_STATE - system state](#214-ic_d2h_sys_state)
   - [2.15. IC_D2H_INC_DATA - built-in inclinometer readings](#215-ic_d2h_inc_data)
   - [2.16. IC_H2D_REM_REQ_EX - remote responder-beacon request](#216-ic_h2d_rem_req_ex)
   - [2.17. IC_D2H_DEV_INFO - device information](#217-ic_d2h_dev_info)
   - [2.18. IC_D2H_BASE_REQ - base station request received](#210-ic_d2h_base_req)   
- [3. Identifier tables](#3-identifier-tables)
   - [3.1. Device types](#31-device-types)
   - [3.2. Error codes](#32-error-codes)
   - [3.3. Local data identifiers](#33-local-data-identifiers)
   - [3.4. Service action identifiers](#34-service-action-identifiers)
   - [3.5. Remote command identifiers](#35-remote-command-identifiers)


<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol

Devices of the [Zima USBL](Zima_DataBrief_en.md) system exchange data via the RS-232 physical layer standard
for an asynchronous interface (UART) with a data line voltage of 3.3 V. The connection uses a four-wire cable with the wires Tx
(transmitter), Rx (receiver), Vcc (power) and GND (ground). Without additional repeaters or interface converters,
correct operation of the interface is guaranteed for a data bus length of up to 2 m.

Default connection port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**CAUTION!**
>_For devices without interface converters, the data line voltage is 3.3 V._

### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of dialog layer text (ASCII) sentences.  

Sentence example:  **`$PZMA0,0*hh<CR><LF>`**  

The main elements of an NMEA0183 sentence:
* '$' - sentence start,
* 'P' - Proprietary code
* 'ZMA' - three-letter manufacturer ID
* '0' - sentence ID
* ',' - comma (parameter delimiter)  
* '*' - checksum delimiter
* 'hh' - checksum in hexadecimal format (e.g. FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)
________
<a name="footnote1"><sup>1</sup> The specified parameters can be changed on request</a>

<div style="page-break-after: always;"></div>

## 2. ZMA command system
The **D2H** prefix in a sentence name means that the sentence is sent from the Device to the Host (control system).
The **H2D** prefix in a sentence name means that the sentence is sent from the Host (control system) to the Device.

### 2.1. IC_D2H_ACK
The IC_D2H_ACK sentence is the device's response to a request received from the control system.  

Sentence format: **`$PZMA0,xx*hh<CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 0 | Sentence ID |
| Error code | Error code \([see 3.2.](#32-error-codes)\) |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.2. IC_H2D_FLD_GET
Reads the value of a field. In response to this command, the device sends the sentence [IC_D2H_FLD_VAL](#24-ic_d2h_fld_val) containing the value of the requested field
if the assignment is successful, or the sentence [IC_D2H_ACK](#21-ic_d2h_ack) with an error code if an error occurs.  

Sentence format: **`$PZMA1,xx,00*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 1 | Sentence ID |
| Field ID | Field identifier |
| Reserved | Must always be '00', reserved |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.3 IC_H2D_FLD_SET
Sets the value of a field. In response to this command, the device sends the sentence [IC_D2H_FLD_VAL](#24-ic_d2h_fld_val) containing the value of the requested field
if the assignment is successful, or the sentence [IC_D2H_ACK](#21-ic_d2h_ack) with an error code if an error occurs.  

Sentence format: **`$PZMA2,x,x*hh<CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 2 | Sentence ID |
| Field ID | Field identifier |
| Field value | Field value (0..99) |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.4 IC_D2H_FLD_VAL
Value of the configuration field.  

Sentence format: **`$PZMA3,xx,xx,00*hh<CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 3 | Sentence ID |
| Requested field ID | Field identifier |
| Value | Field value |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.5 IC_H2D_LOC_DATA_GET
Reads the value of a local parameter.  

Sentence format: **`$PZMA4,xx,00*hh<CR><LF`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 4 | Sentence ID |
| LocDataID | Parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| Reserved | Reserved - '00' |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.6 IC_H2D_LOC_DATA_SET
Sets the value of a local parameter.  

Sentence format: **`$PZMA5,xx,x.x*hh<CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 5 | Sentence ID |
| LocDataID | Parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| LocDataValue | Parameter value |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.7 IC_D2H_LOC_DATA_VAL
Value of a local parameter.  

Sentence format: **`$PZMA6,xx,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 6 | Sentence ID |
| LocDataID | Parameter identifier \([see 3.3.](#33-local-data-identifiers)\) |
| LocDataValue | Parameter value |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.8 IC_H2D_LOC_INVOKE
Performs an operation.  

Sentence format: **`$PZMA7,xx,xx*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| 7 | Sentence ID |
| ActionID | Action identifier \([see 3.4.](#34-service-action-identifiers)\) |
| ActionParam | Parameter |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.9 IC_D2H_LD
Navigation data (responder-beacon).  

Sentence format: **`$PZMAA,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| A | Sentence ID |
| Azimuth | Azimuth to the base station, ° |
| Distance | Distance to the base station, m |
| SNR | Signal-to-noise ratio, dB |
| Dpl | Doppler frequency shift, Hz |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.10 IC_D2H_BASE_REQ
Base station request (responder-beacon).  

Sentence format: **`$PZMAB,x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| B | Sentence ID |
| CommandID | Command identifier \([see 3.5.](#35-remote-command-identifiers)\) |
| SNR | Signal-to-noise ratio, dB |
| Dpl | Doppler frequency shift, Hz |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.11 IC_H2D_REM_REQ
Remote responder-beacon request

Sentence format: **`$PZMAC,x,x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| C | Sentence ID |
| TargetID | Address of the requested responder-beacon |
| RequestID | Request identifier \([see 3.5.](#35-remote-command-identifiers)\) |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.12 IC_D2H_REM_TOUT
Remote responder-beacon timeout.  

Sentence format: **`$PZMAD,x, x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| D | Sentence ID |
| TargetID | Address of the requested responder-beacon |
| RequestID | Request identifier \([see 3.5.](#35-remote-command-identifiers)\) |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.13 IC_D2H_REM_RESP
Remote responder-beacon response.  

Sentence format: **`$PZMAE, x,x,x,x.x,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| E | Sentence ID |
| TargetID | Address of the requested responder-beacon |
| RequestID | Request identifier \([see 3.5.](#35-remote-command-identifiers)\) |
| dFlag | Reserved |
| Azimuth | Horizontal angle to the responder-beacon, ° |
| Distance | Distance to the responder-beacon, m |
| DataValue | Value of the requested parameter |
| SNR | Signal-to-noise ratio, dB |
| DPL | Doppler shift, Hz |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.14 IC_D2H_SYS_STATE
System state.  

Sentence format: **`$PZMAF, x.x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| F | Sentence ID |
| Temperature | Water temperature, °C |
| Depth | Depth of the base station below the surface, m |
| isAHRSEnabled | AHRS state |
| TRX_State | Transceiver state |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.15 IC_D2H_INC_DATA
Built-in inclinometer readings[<sup>*</sup>](#footnote_incdata)  

Sentence format: **`$PZMAG, x.x,x.x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| G | Sentence ID |
| Roll | Roll, °. 0 - vertical position, 0..+90 - tilt to starboard, 0..-90 - tilt to port |
| Pitch | Pitch, °. 0 - vertical position, 0..+90 - tilt toward the bow, 0..-90 - tilt toward the stern |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

____________
<a name="footnote_incdata"><sup>*</sup></a> For systems released after September 2019  

### 2.16 IC_H2D_REM_REQ_EX
Remote responder-beacon request with transmission of the reverse azimuth.  

Sentence format: **`$PZMAH,x,x,x*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| H | Sentence ID |
| TargetAddress | Address of the requested responder-beacon |
| RequestID | Command (must always be CDS_DPT_GET, \([see 3.5.](#35-remote-command-identifiers)\) |
| ReverseAzimuthToTheBase | Reverse azimuth[ The value of the reverse azimuth from the responder-beacon to the base station must be calculated in advance. When ZLibrary and the ZHost application are used, this is done automatically, provided that a system for determining the heading and position of the Zima-Base antenna is connected.] from the responder-beacon to the base station
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


### 2.17 IC_D2H_DEV_INFO
Device information.  

Sentence format: **`$PZMA!, c--c,x,c--c,x,x,c--c*hh <CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PZMA | ZMA command system |
| ! | Sentence ID |
| Sys_moniker | System name |
| Sys_version | System version |
| Device_Type | Device type |
| Core_moniker | Acoustic core name |
| Core_version | Core version |
| Serial number | Device serial number |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |


<div style="page-break-after: always;"></div>

## 3. Identifier tables

### 3.1 Device types

| Value | Name | Description |
| :---: | :---: | :--- |
| '0' | DEV_BASE | Base station |
| '1' | DEV_NODE | Responder-beacon |

### 3.2 Error codes

| Value | Name | Description |
| :---: | :---: | :--- |
| '0' | NO_ERROR | Request accepted | 
| '1' | INVALID_SYNTAX | Syntax error | 
| '2' | UNSUPPORTED | Command not supported | 
| '3' | TRANSMITTER_BUSY | Transmitter is busy | 
| '4' | ARGUMENT_OUT_OF_RANGE | Argument/parameter is outside the range of valid values | 
| '5' | INVALID_OPERATION | The operation cannot be performed at the moment | 
| '6' | UNKNOWN_FIELD_ID | Unknown/unsupported field | 
| '7' | VALUE_UNAVAILIBLE | The requested value is not available | 
| '8' | RECEIVER_BUSY | Receiver is busy | 
| '9' | WAKE_UP | Power-saving mode control. The responder-beacon sends an error message with this parameter immediately after waking up | 
| '10' | STAND_BY | Power-saving mode control. The responder-beacon sends an error message with this parameter before entering sleep mode | 

### 3.3 Local data identifiers

| Value | Name | Description |
| :---: | :---: | :--- |
| '0' | DEVICE_INFO | Device information |
| '1' | LOC_DATA_MAX_REMOTE_TIMEOUT | Maximum remote response waiting time, ms |
| '2' | LOC_DATA_MAX_SUBSCRIBERS | Maximum number of responder-beacons |
| '3' | LOC_DATA_PTS_PRESSURE | Built-in pressure sensor readings, mbar |
| '4' | LOC_DATA_PTS_TEMPERATURE | Built-in temperature sensor readings, °C |
| '5' | LOC_DATA_PTS_DEPTH | Depth of the antenna below the surface |
| '6' | LOC_DATA_CORE_TEMPERATURE | Processor core temperature, °C |
| '7' | LOC_DATA_BAT_CHARGE | Battery charge |
| '8' | LOC_DATA_PRESSURE_RATING | Maximum external pressure, bar |
| '9' | LOC_DATA_ZERO_PRESSURE | Pressure at the water surface, mbar |
| '10' | LOC_DATA_WATER_DENSITY | Water density, kg/m<sup>3</sup> |
| '11' | LOC_DATA_SALINITY | Water salinity, PSU |
| '12' | LOC_DATA_SOUNDSPEED | Speed of sound, m/s |
| '13' | LOC_DATA_GRAVITY_ACC | Acceleration due to gravity, m/s<sup>2</sup> |

### 3.4 Service action identifiers

| Value | Name | Description |
| :---: | :---: | :--- |
| '0' | LOC_INVOKE_FLASH_WRITE | Saving the configuration fields to the internal flash memory |
| '1' | LOC_INVOKE_DPT_ZERO_ADJUST | Take the current pressure sensor readings as the pressure at the water surface |
| '2' | LOC_INVOKE_SYSTEM_RESET | 'Warm' reboot of the device |
| '3' | LOC_INVOKE_STAND_BY | Switching the device to sleep mode |
| '4' | LOC_INVOKE_UART_OFF | Turning off the UART transceiver |

### 3.5 Remote command identifiers

| Value | Name | Description |
| :---: | :---: | :--- |
| CDS_PING | 361 | Ping request |
| CDS_DPT_GET | 362 | Depth of the remote responder-beacon |
| CDS_STY_SET_0 | 363 | Set salinity to 0 PSU |
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
| CDS_STY_SET_40 | 403 | Set salinity to 40 PSU |
| CDS_SLP_SET_59_60 | 404 | Set sleep mode: 59 out of 60 seconds |
| CDS_SLP_SET_58_60 | 405 | Set sleep mode: 58 out of 60 seconds |
| CDS_SLP_SET_56_60 | 406 | Set sleep mode: 56 out of 60 seconds |
| CDS_SLP_SET_52_60 | 407 | Set sleep mode: 52 out of 60 seconds |
| CDS_SLP_SET_50_60 | 408 | Set sleep mode: 50 out of 60 seconds |
| CDS_SLP_SET_40_60 | 409 | Set sleep mode: 40 out of 60 seconds |
| CDS_SLP_SET_30_60 | 410 | Set sleep mode: 30 out of 60 seconds |
| CDS_SLP_SET_20_60 | 411 | Set sleep mode: 20 out of 60 seconds |
| CDS_SLP_SET_10_60 | 412 | Set sleep mode: 10 out of 60 seconds |
| CDS_SLP_SET_NEVER | 413 | Set sleep mode: always on |
| CDS_BAT_CHG_GET | 414 | Battery charge |
| CDS_PTS_TMP_GET | 415 | Temperature |
| CDS_PTS_PRS_GET | 416 | Pressure |
| CDS_CRE_TMP_GET | 417 | Processor core temperature |
| CDS_SLP_GET | 418 | Sleep mode |
| CDS_STY_GET | 419 | Salinity |
| CDS_CMD_RSV_0 | 420 | Reserved |
| CDS_CMD_RSV_1 | 421 | Reserved |
| CDS_CMD_RSV_2 | 422 | Reserved |
| CDS_CMD_RSV_3 | 423 | Reserved |
| CDS_CMD_RSV_4 | 424 | Reserved |
| CDS_CMD_RSV_5 | 425 | Reserved |
| CDS_CMD_ZDPT_ADJ | 426 | Setting the depth zero for the responder-beacon |
| CDS_USR_CMD_0 | 427 | User command 0 |
| CDS_USR_CMD_1 | 428 | User command 1 |
| CDS_USR_CMD_2 | 429 | User command 2 |
| CDS_USR_CMD_3 | 430 | User command 3 |
| CDS_USR_CMD_4 | 431 | User command 4 |
| CDS_USR_CMD_5 | 432 | User command 5 |
| CDS_USR_CMD_6 | 433 | User command 6 |
| CDS_USR_CMD_7 | 434 | User command 7 |
| CDS_USR_CMD_8 | 435 | User command 8 |
| CDS_USR_CMD_9 | 436 | User command 9 |
| CDS_USR_CMD_10 | 437 | User command 10 |
| CDS_USR_CMD_11 | 438 | User command 11 |
| CDS_USR_CMD_12 | 439 | User command 12 |
| CDS_USR_CMD_13 | 440 | User command 13 |
| CDS_USR_CMD_14 | 441 | User command 14 |
| CDS_USR_CMD_15 | 442 | User command 15 |
| CDS_USR_CMD_16 | 443 | User command 16 |
| CDS_USR_CMD_17 | 444 | User command 17 |
| CDS_USR_CMD_18 | 445 | User command 18 |
| CDS_USR_CMD_19 | 446 | User command 19 |
| CDS_USR_CMD_20 | 447 | User command 20 |
| CDS_USR_CMD_21 | 448 | User command 21 |
| CDS_USR_CMD_22 | 449 | User command 22 |
| CDS_USR_CMD_23 | 450 | User command 23 |
| CDS_USR_CMD_24 | 451 | User command 24 |
| CDS_USR_CMD_25 | 452 | User command 25 |
| CDS_USR_CMD_26 | 453 | User command 26 |
| CDS_USR_CMD_27 | 454 | User command 27 |
| CDS_USR_CMD_28 | 455 | User command 28 |
| CDS_USR_CMD_29 | 456 | User command 29 |
| CDS_USR_CMD_30 | 457 | User command 30 |
| CDS_USR_CMD_31 | 458 | User command 31 |
| CDS_USR_CMD_32 | 459 | User command 32 |
| CDS_RESERVED_0 | 460 | Reserved |
| CDS_RESERVED_1 | 461 | Reserved |
| CDS_RESERVED_2 | 462 | Reserved |
| CDS_RESERVED_3 | 463 | Reserved |
| CDS_RESERVED_4 | 464 | Reserved |
| CDS_RESERVED_5 | 465 | Reserved |
| CDS_RESERVED_6 | 466 | Reserved |
| CDS_RESERVED_7 | 467 | Reserved |
| CDS_SET_ADDR_01 | 468 | Set address 1 |
| CDS_SET_ADDR_02 | 469 | Set address 2 |
| CDS_SET_ADDR_03 | 470 | Set address 3 |
| CDS_SET_ADDR_04 | 471 | Set address 4 |
| CDS_SET_ADDR_05 | 472 | Set address 5 |
| CDS_SET_ADDR_06 | 473 | Set address 6 |
| CDS_SET_ADDR_07 | 474 | Set address 7 |
| CDS_SET_ADDR_08 | 475 | Set address 8 |
| CDS_SET_ADDR_09 | 476 | Set address 9 |
| CDS_SET_ADDR_10 | 477 | Set address 10 |
| CDS_SET_ADDR_11 | 478 | Set address 11 |
| CDS_SET_ADDR_12 | 479 | Set address 12 |
| CDS_SET_ADDR_13 | 480 | Set address 13 |
| CDS_SET_ADDR_14 | 481 | Set address 14 |
| CDS_SET_ADDR_15 | 482 | Set address 15 |
| CDS_SET_ADDR_16 | 483 | Set address 16 |
| CDS_SET_ADDR_17 | 484 | Set address 17 |
| CDS_SET_ADDR_18 | 485 | Set address 18 |
| CDS_SET_ADDR_19 | 486 | Set address 19 |
| CDS_SET_ADDR_20 | 487 | Set address 20 |
| CDS_SET_ADDR_21 | 488 | Set address 21 |
| CDS_SET_ADDR_22 | 489 | Set address 22 |
| CDS_SET_ADDR_23 | 490 | Set address 23 |
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
| CDS_ERR_NAVAIL | 501 | Error - data is not available at the moment |
| CDS_ERR_RES_0 | 502 | Error - reserved |
| CDS_ERR_RES_1 | 503 | Error - reserved |
| CDS_ERR_RES_2 | 504 | Error - reserved |
| CDS_ERR_RES_3 | 505 | Error - reserved |
| CDS_ERR_RES_4 | 506 | Error - reserved |
| CDS_ERR_RES_5 | 507 | Error - reserved |
| CDS_ERR_RES_6 | 508 | Error - reserved |
| CDS_ERR_BAT_LOW | 509 | Battery charge is minimal |

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima_Protocol_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
