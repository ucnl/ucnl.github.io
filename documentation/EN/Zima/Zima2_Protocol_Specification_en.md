[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 USBL: Communication protocol specification**

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
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2 USBL** - underwater acoustic navigation system <br/> Communication protocol specification |

# Zima2 USBL <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. AZM command system](#2-azm-command-system)
  - [2.1. D2H_ACK](#21-d2h_ack)
  - [2.2. D2D_STRSTP](#22-d2d_strstp)
  - [2.3. D2D_RSTS](#23-d2d_rsts)
  - [2.4. D2H_NDTA](#24-d2h_ndta)
  - [2.5. H2D_DPTOVR](#25-h2d_dptovr)
  - [2.6. D2H_RUCMD](#26-d2h_rucmd)
  - [2.7. D2H_RBCAST](#27-d2h_rbcast)
  - [2.8. H2D_DINFO_GET](#28-h2d_dinfo_get)
  - [2.9. D2H_DINFO](#29-d2h_dinfo)
  - [2.10. H2D_CREQ](#210-h2d_creq)
  - [2.11. H2D_CSET](#211-h2d_cset)
- [3. Identifier tables](#3-identifier-tables)
  - [3.1. Error codes](#31-error-codes)
  - [3.2. NDTA sentence status](#32-ndta-sentence-status)
  - [3.3. Addressed request identifiers](#33-addressed-request-identifiers)
  - [3.4. Broadcast command identifiers](#34-broadcast-command-identifiers)
  - [3.5. Response identifiers](#35-response-identifiers)
  - [3.6. Pressure sensor types](#36-pressure-sensor-types)

<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol

Devices of the [Zima2 USBL](Zima2_DataBrief_en.md) system exchange data via the RS-232 physical layer standard
for an asynchronous interface (UART) with a data line voltage of 3.3 V. The connection uses a four-wire cable with the wires Tx
(transmitter), Rx (receiver), Vcc (power) and GND (ground). Without additional repeaters or interface converters,
correct operation of the interface is guaranteed for a data bus length of up to 2 m.

Connection port settings:  

| Parameter | Value |
| :--- | :--- |
| Baudrate | 9600 bit/s |
| Data bits | 8 |
| Stop bits | 1 |  
| Parity | No |
| Hardware flow control | No |  

>**CAUTION!**
>_For devices without interface converters, the data line voltage is 3.3 V._

### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of dialog layer text (ASCII) sentences.  

Sentence example:  
**`
$PAZM0,,0*06<CR><LF>
`**  

The main elements of an NMEA0183 sentence:

| Element | Description |
| :--- | :--- |
| $ | Sentence start |
| P | Proprietary code |
| AZM | Three-letter ID |
| 0 | Sentence ID |
| | The first parameter is empty |
| , | Comma (parameter delimiter) |
| 0 | The second parameter has the value '0' |
| \* | Checksum delimiter |
| 06 | Checksum in hexadecimal format (e.g. FF, 01). [Calculated](https://docs.unavlab.com/online_utils/nmea0183_checksum_calculator.html) as the bitwise XOR of all bytes between '$' and '\*'. |
| <CR\><LF\> | End of sentence (line break) |

The format of the above sentence is described as follows:
**`
$PAZM0,[x],x*06<CR><LF>
`**

x means an integer parameter; square brackets '[]' indicate that the parameter can be empty.
The following is a list of possible parameter descriptors:

| Descriptor | Description |
| :--- | :--- |
| x | Integer value |
| xx | Integer value occupying exactly two characters: from 00 to 99 |
| x.x | Real (floating-point) value |
| c--c | Character string |
| hh | Hexadecimal value from 00 to FF |

<div style="page-break-after: always;"></div>

## 2. AZM command system
The **D2H** prefix in a sentence name means that the sentence is sent from the Device to the Host (control system).
The **H2D** prefix in a sentence name means that the sentence is sent from the Host (control system) to the Device.
The **D2D** prefix in a sentence name means that the sentence can be transmitted in both directions: from the device to the control system and vice versa.

### 2.1. D2H_ACK
The D2H_ACK sentence is the device's response to a request received from the control system.  

Sentence format: 
**`
$PAZM0,[x],x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 0 | Sentence ID |
| 1 | cmdID | ID of the command to which the device responded |
| 2 | result | Error code [See Table 3.1. Error codes](#31-error-codes) |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.2. D2D_STRSTP
The D2D_STRSTP sentence sets the polling parameters of responder-beacons.

Transmitted from the control system to the direction-finding station to:
- start polling the responder-beacons
- stop polling the responder-beacons
- change the polling parameters (address mask, maximum distance, water salinity)

Transmitted from the direction-finding station to the control system as an echo confirmation that the command has been accepted. If the command is not accepted by the device, the device reports this using the [2.1. D2H_ACK](#21-d2h_ack) command with the corresponding error code.

Sentence format: 
**`
$PAZM1,[x],[x.x],[x.x],[x]*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 1 | Sentence ID |
| 1 | addrMask | Address mask of the beacons to poll, 16-bit unsigned integer, each bit from 0 to 15 corresponds to one of the beacons, bit = 0 - the beacon does not participate in polling, bit = 1 - the beacon participates in polling. If the parameter is empty or equal to zero, polling stops. |
| 2 | sty_PSU | Water salinity in PSU in the range from 0 to 40. If the parameter is empty, the default value (0 PSU) is used |
| 3 | soundSpeed_mps | Speed of sound in water, in m/s, in the range from 1350 to 1600 m/s. If the parameter is empty, the speed of sound will be calculated automatically based on the salinity, temperature and pressure data |
| 4 | max_dist_m | Maximum range in meters, from 500 to 5500. This parameter is used to calculate the maximum beacon response waiting interval. |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.3. D2D_RSTS
The D2D_RSTS sentence sets the settings of responder-beacons.

Transmitted from the control system to a responder-beacon to set its address and the water salinity.
Transmitted from the responder-beacon to the control system as an echo confirmation that the command has been accepted and the parameters have been set.
If the command is not accepted by the device, the device reports this using the [2.1. D2H_ACK](#21-d2h_ack) command with the corresponding error code.

Sentence format: 
**`
$PAZM2,[x],[x.x]*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 2 | Sentence ID |
| 1 | addr | Beacon address in the range from 0 to 15. If the parameter is empty, the address is not changed. |
| 2 | sty_PSU | Water salinity in PSU in the range from 0 to 40. If the parameter is empty, the default value (0 PSU) is used |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.4. D2H_NDTA
The D2H_NDTA sentence reports the status of the direction-finding station.

This is the main sentence transmitted from the direction-finding station to the control system. The station uses it to report:
- values of local parameters: temperature, pressure, roll, pitch
- parameters of the response received from a responder-beacon: beacon address, signal propagation time, slant range and its projection, depth, horizontal and vertical angles, error code, communication quality
- that the beacon response waiting interval has been exceeded (timeout)

Sentence format: 
**`
$PAZM3,x,[x],[x],[x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x]*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 3 | Sentence ID |
| 1 | status | Sentence status, [See Table 3.2. NDTA sentence status](#32-ndta-sentence-status) |
| 2 | addr | Beacon address in the range from 0 to 15. The parameter is empty for sentences whose 'status' field contains '0' (local parameters only) |
| 3 | rq_code | ID of the parameter requested from the beacon, [See Table 3.3. Addressed request identifiers](#33-addressed-request-identifiers) |
| 4 | rs_code | Beacon response code, [See Table 3.5. Response identifiers](#35-response-identifiers) |
| 5 | msr_dB | Reception quality of the beacon response signal, in dB. 14 is the reception threshold; values above 20 dB indicate good communication conditions |
| 6 | p_time_s | Signal propagation time in seconds. Multiplied by the speed of sound, it gives the slant range |
| 7 | s_range_m | Slant range from the direction-finding antenna to the beacon in meters |
| 8 | p_range_m | Projection of the slant range from the direction-finding antenna to the beacon onto the water surface, in meters |
| 9 | r_dpt_m | Absolute depth value of the responder-beacon in meters |
| 10 | a_deg | Horizontal angle of arrival of the responder-beacon signal in degrees. Measured from the zero direction of the direction-finding antenna, clockwise as seen from the cable side |
| 11 | e_deg | Vertical angle of arrival of the responder-beacon signal in degrees. Measured from the horizontal plane passing through the antenna array |
| 12 | lprs_mBar | Absolute pressure in millibars, from the built-in sensor of the direction-finding antenna |
| 13 | ltmp_C | Temperature in °C, from the built-in sensor of the direction-finding antenna |
| 14 | lhdn_deg | The parameter is not used, reserved for future use |
| 15 | lptc_deg | Pitch angle of the direction-finding antenna. Measured from the vertical, positive values - tilt toward the bow (toward the zero direction of the antenna), negative values - tilt toward the stern |
| 16 | lrol_deg | Roll angle of the direction-finding antenna. Measured from the vertical, positive values - to starboard (relative to the zero direction of the antenna), negative values - to port |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.5. H2D_DPTOVR
The H2D_DPTOVR sentence sets the depth for responder-beacons that do not have a built-in depth sensor.
If the command is not accepted by the device, the device reports this using the [2.1. D2H_ACK](#21-d2h_ack) command with the corresponding error code.

Sentence format: 
**`
$PAZM4,x.x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 4 | Sentence ID |
| 1 | dpt_m | Depth value in meters |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.6. D2H_RUCMD
The D2H_RUCMD sentence is transmitted by the responder-beacon to the control system if a remote control command has been received.

Sentence format: 
**`
$PAZM5,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 5 | Sentence ID |
| 1 | cmdID | Command ID, [see Table 3.3. Addressed request identifiers](#33-addressed-request-identifiers) |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.7. D2H_RBCAST
The D2H_RBCAST sentence is transmitted by the responder-beacon to the control system if a broadcast command has been received.

Sentence format: 
**`
$PAZM6,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 6 | Sentence ID |
| 1 | cmdID | Command ID, [see Table 3.4. Broadcast command identifiers](#34-broadcast-command-identifiers) |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.8. H2D_DINFO_GET
The H2D_DINFO_GET sentence is used to request information about the device. 

Sentence format: 
**`
$PAZM?,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | ? | Sentence ID |
| 1 | 0 | Reserved |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.9. D2H_DINFO
The D2H_DINFO sentence contains information about the device. 

Sentence format: 
**`
$PAZM!,x,x,c--c,c--c,x,x,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | ! | Sentence ID |
| 1 | d_type | Device type (0 - direction-finding station, 1 - responder-beacon) |
| 2 | addressOrMask | Depending on the device type - a mask of responder-beacon addresses or the address of a responder-beacon |
| 3 | serialNumber | Device serial number |
| 4 | sys_info | Firmware information |
| 5 | sys_version | Firmware version |
| 6 | pts_type | Pressure sensor type [see Table 3.6. Pressure sensor types](#36-pressure-sensor-types) |
| 7 | ch_id | Communication channel ID |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.10. H2D_CREQ
> Supported since firmware version 1.33

The H2D_CREQ sentence is a request for user parameters. The command is supported only by the direction-finding station. The request is made once, after which the station continues to request the depth of the responder-beacons. 

Sentence format: 
**`
$PAZM7,x,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 7 | Sentence ID |
| 1 | addr | Responder-beacon address; if the field is empty, the specified parameter will be requested from all responder-beacons the station is currently working with |
| 2 | user_data_id | User parameter ID [see Table 3.3. Addressed request identifiers](#33-addressed-request-identifiers) in the range from CDS_REQ_USER_CMD_27 to CDS_REQ_USER_CMD_0 |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.11. H2D_CSET
> Supported since firmware version 1.33

The H2D_CSET sentence sets the value of a user parameter. The command is supported only by responder-beacons. 

Sentence format: 
**`
$PAZM8,x,x,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 8 | Sentence ID |
| 1 | user_data_id | User parameter ID [see Table 3.3. Addressed request identifiers](#33-addressed-request-identifiers) in the range from CDS_REQ_USER_CMD_27 to CDS_REQ_USER_CMD_0 |
| 2 | user_data_value | If the parameter is empty, the responder-beacon will transmit the value of this parameter, if it has been set. Values in the range from 0 to 499 are accepted |
| 3 | Leave the field empty. The parameter is reserved for future use | |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.12. IC_D2D_ISC

The IC_D2D_ISC sentence is a service command. 

Sentence format: 
**`
$PAZM9,x,x,x,x*hh<CR><LF>
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | 9 | Sentence ID |
| 1 | actID | reserved |
| 2 | param1 | reserved |
| 3 | param2 | reserved |
| 4 | param3 | reserved |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.13. IC_D2D_LBP_SETA

The IC_D2D_LBP_SETA sentence sets the LBL solver parameters. 

Sentence format: 
**`
$PAZMA,x,x,x.x,x.x,x,x,x.x,x,x.x,x.x,x.x,x,x.x,x.x,x,x.x,x.x,x,x.x,x.x,x,x.x,x.x
`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | PAZM | AZM command system |
| | A | Sentence ID |
| 1 | auto_output | 1 - on power-up, the device immediately starts transmitting data every 1 s, 0 - only after this sentence is received |
| 2 | autostart_on_poweron | 1 - when power is applied, the device immediately starts polling the beacons, if their parameters have been set previously, 0 - only after STRSTP is received |
| 3 | sty | salinity, 0 .. 40 PSU, default value 0 |
| 4 | sos | speed of sound, 1350 .. 1600 m/s, default value 1450 m/s |
| 5 | sos_auto | 1 - automatic calculation of the speed of sound, 0 - use the specified value | 
| 6 | smflt_size | smoothing filter window size, 2 .. 32, default value 4 | 
| 7 | smflt_thld | smoothing filter reset threshold, 1 .. 999 m, default value 100 m | 
| 8 | achod_size | ACHOD window size, 2 .. 32, default value 8 | 
| 9 | achod_mspd | maximum speed of the positioned object, 0.5 .. 10 m/s, default value 0.5 m/s | 
| 10 | achod_thld | ACHOD threshold, 0.5 .. 25 m, default value 5 m | 
| 11 | rerr_thld | radial error threshold, default value 25 m |
| 12 | a1 | Address of the first responder-beacon, 1 .. 16 | 
| 13 | ln1 | Geographic latitude of the first responder-beacon, -90.0 .. 90.0 | 
| 14 | lt1 | Geographic longitude of the first responder-beacon, -180 .. 180 |
| 15 | a2 | Address of the second responder-beacon, 1 .. 16 | 
| 16 | ln2 | Geographic latitude of the second responder-beacon, -90.0 .. 90.0 | 
| 17 | lt2 | Geographic longitude of the second responder-beacon, -180 .. 180 |
| 18 | a3 | Address of the third responder-beacon, 1 .. 16 | 
| 19 | ln3 | Geographic latitude of the third responder-beacon, -90.0 .. 90.0 | 
| 20 | lt3 | Geographic longitude of the third responder-beacon, -180 .. 180 |
| 21 | a4 | Address of the fourth responder-beacon, 1 .. 16 | 
| 22 | ln4 | Geographic latitude of the fourth responder-beacon, -90.0 .. 90.0 | 
| 23 | lt4 | Geographic longitude of the fourth responder-beacon, -180 .. 180 |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |



<div style="page-break-after: always;"></div>

## 3. Identifier tables

### 3.1. Error codes

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | IC_RES_OK | Command accepted without errors |
| 1 | IC_RES_INVALID_SYNTAX | Syntax error |
| 2 | IC_RES_UNSUPPORTED_CMD | Command not supported |
| 3 | IC_RES_ARGUMENT_OUT_OF_RANGE | The value of at least one argument is outside the range of valid values |
| 4 | IC_RES_INVALID_OPERATION | This command cannot be executed in the current state of the device |
| 5 | IC_RES_VALUE_UNAVAILABLE | The value of the requested parameter is not available at the moment |
| 6 | IC_RES_TX_BUSY | Transmitter is busy |
| 7 | IC_RES_RX_BUSY | Receiver is busy |

### 3.2. NDTA sentence status

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | NDTA_LOC_ONLY | The sentence contains only the local parameters of the direction-finding antenna |
| 1 | NDTA_REMR | The sentence contains the response data of the responder-beacon and the local parameters of the direction-finding antenna |
| 2 | NDTA_REMT | The sentence contains data on the responder-beacon response waiting interval being exceeded and the local parameters of the direction-finding antenna |

### 3.3. Addressed request identifiers

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | CDS_REQ_DPT | |
| 1 | CDS_REQ_TMP | |
| 2 | CDS_REQ_VCC | |
| 3 | CDS_REQ_USER_CMD_27 | |
| 4 | CDS_REQ_USER_CMD_26 | |
| 5 | CDS_REQ_USER_CMD_25 | |
| 6 | CDS_REQ_USER_CMD_24 | |
| 7 | CDS_REQ_USER_CMD_23 | |
| 8 | CDS_REQ_USER_CMD_22 | |
| 9 | CDS_REQ_USER_CMD_21 | |
| 10 | CDS_REQ_USER_CMD_20 | |
| 11 | CDS_REQ_USER_CMD_19 | |
| 12 | CDS_REQ_USER_CMD_18 | |
| 13 | CDS_REQ_USER_CMD_17 | |
| 14 | CDS_REQ_USER_CMD_16 | |
| 15 | CDS_REQ_USER_CMD_15 | |
| 16 | CDS_REQ_USER_CMD_14 | |
| 17 | CDS_REQ_USER_CMD_13 | |
| 18 | CDS_REQ_USER_CMD_12 | |
| 19 | CDS_REQ_USER_CMD_11 | |
| 20 | CDS_REQ_USER_CMD_10 | |
| 21 | CDS_REQ_USER_CMD_9 | |
| 22 | CDS_REQ_USER_CMD_8 | |
| 23 | CDS_REQ_USER_CMD_7 | |
| 24 | CDS_REQ_USER_CMD_6 | |
| 25 | CDS_REQ_USER_CMD_5 | |
| 26 | CDS_REQ_USER_CMD_4 | |
| 27 | CDS_REQ_USER_CMD_3 | |
| 28 | CDS_REQ_USER_CMD_2 | |
| 29 | CDS_REQ_USER_CMD_1 | |
| 30 | CDS_REQ_USER_CMD_0 | |

### 3.4. Broadcast command identifiers

| Code | Name | Description |
| :--- | :--- | :--- |
| 497 | CDS_BCAST_FUNC_0 | |
| 498 | CDS_BCAST_FUNC_1 | |
| 499 | CDS_BCAST_FUNC_2 | |
| 500 | CDS_BCAST_FUNC_3 | |
| 501 | CDS_BCAST_FUNC_4 | |
| 502 | CDS_BCAST_STY_SET_0 | |
| 503 | CDS_BCAST_STY_SET_5 | |
| 504 | CDS_BCAST_STY_SET_10 | |
| 505 | CDS_BCAST_STY_SET_15 | |
| 506 | CDS_BCAST_STY_SET_20 | |
| 507 | CDS_BCAST_STY_SET_25 | |
| 508 | CDS_BCAST_STY_SET_30 | |
| 509 | CDS_BCAST_STY_SET_35 | |
| 520 | CDS_BCAST_STY_SET_40 | |

### 3.5. Response identifiers

| Code | Name | Description |
| :--- | :--- | :--- |
| 500 | CDS_ERR_RES_0 | |
| 501 | CDS_ERR_RES_1 | |
| 502 | CDS_ERR_RES_2 | |
| 503 | CDS_ERR_RES_3 | |
| 504 | CDS_ERR_RES_4 | |
| 505 | CDS_ACK | |
| 506 | CDS_ERR_NAVAIL | |
| 507 | CDS_ERR_NSUPP | |
| 508 | CDS_ERR_BAT_LOW | |
| 509 | CDS_RSYS_STRT | |

### 3.6. Pressure sensor types

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | NO SENSOR | The device does not contain a built-in pressure sensor |
| 1 | 100 BAR | Closed-type sensor with a range of 0 .. 100 Bar |
| 2 | 30 BAR TYPE 1 | Open-type sensor with a range of 0 .. 30 Bar |
| 3 | 30 BAR TYPE 2 | Open-type sensor with a range of 0 .. 30 Bar |


<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima2_Protocol_Specification_ru.md commit=d22d67599503e61f5b55ca94e3b987b14e22709f date=2026-10-06 -->
