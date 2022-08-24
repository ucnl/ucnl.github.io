[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 USBL: Protocol specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2 USBL** - Underwater tracking system <br/> Communication protocol specification |

# Zima2 USBL <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents


<div style="page-break-after: always;"></div>

## 1. Introducation
### 1.1. Physical layer

Devices of the [Zima2 USBL](Zima2_DataBrief_en.md) system support data interfacing using the RS-232 physical layer standard
for asynchronous interface (UART) with 3.3V data line voltage. The connection is made with a four-wire cable, with Tx cores.
(transmitter), Rx (receiver), Vcc (power) and GND (ground). Without the use of additional repeaters and interface converters
the maximum length of the data bus, for which the correct operation of the interface is guaranteed, is no more than 2 meters.

Connection port settings: 

| Parameter | Value |
| :--- | :--- |
| Baudrate | 9600 bit/s |
| Data bits | 8 |
| Stop bits | 1 |  
| Parity | No |
| Hardware flow control | No |  

>**WARNING!**
>_For devices without interface converters, the data line voltage is 3.3 V._

### 1.2. NMEA0183 Dialog Layer Protocol Standard
The NMEA0183 standard describes the format for text (ASCII) messages (sentences).

Sentence example:
**`
$PAZM0,,0*06<СR><LF>
`**  

The main parts of an NMEA 0183 sentence:

| Item | Description |
| :--- | :--- |
| $ | Sentence start |
| P | Proprietary |
| AZM | Protocol ID |
| 0 | Sentence ID |
| | The first parameter is empty |
| , | comma (parameter delimiter) |
| 0 | the second parameter has value '0' |
| \* | Checksum delimiter |
| 06 | Checksum in hex (e.g. FF, 01). [Calculates](https://docs.unavlab.com/online_utils/nmea0183_checksum_calculator.html) as byte by byte XOR for all bytes between '$' и '\*'. |
| <CR\><LF\> | End of sentence |

The format of the above sentence is described as follows:
**`
$PAZM0,[x],x*06<СR><LF>
`**

x - means an integer parameter, square brackets '[]' - indicate that the parameter can be empty.
The following is a list of possible parameter descriptors:

| Descriptors | Description |
| :--- | :--- |
| x | Integer value |
| xx | Integer value spanning exactly two characters: from 00 to 99 |
| x.x | Real value |
| c--c | Character string |
| hh | hex value from 00 to FF |

<div style="page-break-after: always;"></div>

## 2. AZM Protocol
The **D2H** prefix in the sentence name means that it is transmitted from the device (Device) to the host system (Host).
The **H2D** prefix in the sentence name means that it is transmitted from the control system (Host) to the device (Device).
The **D2D** prefix in the sentence name means that it can be transmitted in both directions: from the device to the control system, and vice versa.

### 2.1. D2H_ACK
Sentence D2H_ACK - response of the device to a request received from the control system.  

Sentence format: 
**`
$PAZM0,[x],x*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 0	| Sentence ID |
| 1 | cmdID | ID of the command to which the device responded |
| 2 | result | Error code [see Table 3.1. Error codes]() |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.2. D2D_STRSTP
The D2D_STRSTP message is a sentence for setting the autorequest (polling) parameters for beacons-responders.

Transmitted from the control system to the direction finding station for:
- start of interrogation of beacons-responders
- stop polling beacons-responders
- changes in polling parameters (address masks, maximum distance, water salinity)

Transmitted from the direction finding antenna to the control system as an echo confirmation of the acceptance of the command. If the command is not accepted by the device, then it reports this using the command [2.1. D2H_ACK](#21-d2h_ack) with the corresponding error code.

Sentence format: 
**`
$PAZM1,[x],[x.x],[x.x],[x]*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 1	| Sentence ID |
| 1 | addrMask | Address mask for polling, 16-bit unsigned integer, each bit from 0 to 15 corresponds to one of the responders, bit = 0 - the responder does not participate in the poll, bit = 1 - the responder participates in the poll. If the parameter is empty or equal to zero, then polling stops. |
| 2 | sty_PSU | Salinity of water in PSU in the range from 0 to 40. If the parameter is empty, the default value (0 PSU) is used. |
| 3 | soundSpeed_mps | The speed of sound in water in m/s in the range from 1350 to 1600 m/s. If the parameter is empty, the speed of sound will be calculated automatically based on salinity, temperature and pressure data |
| 4 | max_dist_m | Maximum range in meters in the range from 500 to 5500. This parameter is used to calculate the maximum interval for waiting for a responder response |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.3. D2D_RSTS
D2D_RSTS message - a message for setting the settings of responder beacons.

It is transmitted from the control system to the responding beacon to set its address and water salinity.
It is transmitted from the responder beacon to the control system as an echo confirmation that the command has been accepted and the parameters have been set.
If the command is not accepted by the device, then it reports this using the command [2.1. D2H_ACK](#21-d2h_ack) with the corresponding error code.

Sentence format: 
**`
$PAZM2,[x],[x.x]*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 2	| Sentence ID |
| 1 | addr | Responder address in the range from 0 to 15. If the parameter is empty, then the address does not change. |
| 2 | sty_PSU | Salinity of water in PSU in the range from 0 to 40. If the parameter is empty, the default value (0 PSU) is used. |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.4. D2H_NDTA
D2H_NDTA message - direction-finding antenna status.

This is the main message transmitted from the direction finding antenna to the control system. With it, the station reports:
- values of local parameters: temperature, pressure, roll, pitch
- parameters of the response received from the responder beacon: address, signal propagation time, slant range and its projection, depth, horizontal and vertical angles, error code, communication quality
- exceeding the responder beacon response waiting interval (timeout)

Sentence format: 
**`
$PAZM3,x,[x],[x],[x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x],[x.x]*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 3	| Sentence ID |
| 1 | status | Sentence status [see Table 3.2. NDTA sentence status]() |
| 2 | addr | Responder address from 0 to 15. Parameter empty for sentences with 'status' field containing '0' (Local parameters only) |
| 3 | rq_code |Identifier of the parameter requested from the responder beacon, [see Table 3.3. Addressed requests]() |
| 4 | rs_code | Response code, [see Table 3.5. Response identifiers]() |
| 5 | msr_dB | A parameter that determines the quality of receiving the beacon's response signal in dB. 14 - reception threshold, values above 20 dB indicate good communication conditions |
| 6 | p_time_s | Signal propagation time in seconds. Multiplied by the speed of sound gives the slant range |
| 7 | s_range_m | Slant range from DF antenna to responder in meters |
| 8 | p_range_m | Projection of the slant range from the direction finding antenna to the responder on the water surface in meters |
| 9 | r_dpt_m | The absolute value of the depth of the responder beacon in meters |
| 10 | a_deg | Horizontal angle of arrival of the responder signal in degrees. Counted from the zero direction of the direction finding antenna clockwise from the cable side |
| 11 | e_deg | Vertical angle of arrival of the responder signal in degrees. Counted down from a horizontal plane passing through the antenna array |
| 12 | lprs_mBar | Absolute pressure in millibars according to the built-in DF antenna sensor |
| 13 | ltmp_C | Temperature in °C according to the built-in sensor of the DF antenna |
| 14 | lhdn_deg | Parameter not used, reserved for future use |
| 15 | lptc_deg | DF antenna pitch angle. Counted from the vertical, positive values - pitch to the bow (towards the zero direction of the antenna), negative - pitch to the stern |
| 16 | lrol_deg | Angle of roll of the DF antenna. Measured from the vertical, positive values - to starboard (relative to the zero direction of the antenna), negative values - to port |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |


### 2.5. H2D_DPTOVR
The H2D_DPTOVR sentence is for setting the depth for responder beacons that do not have a built-in depth sensor.
If the command is not accepted by the device, then it reports this using the command [2.1. D2H_ACK](#21-d2h_ack) with the corresponding error code.

Sentence format: 
**`
$PAZM4,x.x*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 4	| Sentence ID |
| 1 | dpt_m | Depth in meters |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.6. D2H_RUCMD
Sentence D2H_RUCMD - transmitted by the responder beacon to the control system if a telecontrol command was received.

Sentence format: 
**`
$PAZM5,x*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 5	| Sentence ID |
| 1 | cmdID | Addressed request ID, [see Table 3.3. Addressed requests]() |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.7. D2H_RBCAST
D2H_RBCAST sentence - sent by the responder beacon to the control system if a broadcast command has been received.

Sentence format: 
**`
$PAZM6,x*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | 6	| Sentence ID |
| 1 | cmdID | Request ID, [see Table 3.4. Broadcast requests](#34-%D0%B8%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D1%8B-%D1%88%D0%B8%D1%80%D0%BE%D0%BA%D0%BE%D0%B2%D0%B5%D1%89%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4) |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.8. H2D_DINFO_GET
H2D_DINFO_GET sentence - is used to request information about the device.

Sentence format: 
**`
$PAZM?,x*hh<CR><LF>
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | ?	| Sentence ID |
| 1 | 0 | Reserved |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

### 2.9. D2H_DINFO
Sentence D2H_DINFO - device information. 

Sentence format: 
**`
$PAZM!,x,x,c--c,c--c,x,x,x*hh<CR><LF>
d_type,address,serialNumber,sys_info,sys_version,pts_type,ch_id
`**

| № | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $	| Sentence start '$' |
| | PAZM | AZM protocol |
| | !	| Sentence ID |
| 1 | d_type | Device type (0 - DF-antenna, 1 - responder beacon) |
| 2 | addressOrMask | Depending on the type of device - a mask of responder beacon addresses or an address of a responder beacon |
| 3 | serialNumber | Device serial number |
| 4 | sys_info | Firmware information |
| 5 | sys_version | Firmware version |
| 6 | pts_type | Pressure sensor type [see Table 3.6. Pressure sensors]() |
| 7 | ch_id | Code channel ID |
| | *	| NMEA Checksum delimiter |
| | hh | NMEA Checksum |
| | \<CR\>\<LF\> | End of sentence |

<div style="page-break-after: always;"></div>

## 3. Identifiers

### 3.1. Error codes

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | IC_RES_OK | Command accepted. No errors |
| 1 | IC_RES_INVALID_SYNTAX | Syntax error |
| 2 | IC_RES_UNSUPPORTED_CMD | Command not supported |
| 3 | IC_RES_ARGUMENT_OUT_OF_RANGE | The value of at least one argument is out of the range of valid values |
| 4 | IC_RES_INVALID_OPERATION | This command cannot be executed in the current state of the device |
| 5 | IC_RES_VALUE_UNAVAILABLE | The value of the requested parameter is not available at the moment |
| 6 | IC_RES_TX_BUSY | Transmitter is busy |
| 7 | IC_RES_RX_BUSY | Receiver is busy |

### 3.2. NDTA sentence status

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | NDTA_LOC_ONLY | The sentence contains only local parameters of the direction finding antenna |
| 1 | NDTA_REMR | The sentence contains the response data of the responding beacon and the local parameters of the direction-finding antenna |
| 2 | NDTA_REMT | The sentence contains data on exceeding the waiting interval of the response of the requested responder beacon and local parameters of the direction-finding antenna |

### 3.3. Addressed requests

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
| 11 |	CDS_REQ_USER_CMD_19 | |
| 12 |	CDS_REQ_USER_CMD_18 | |
| 13 |	CDS_REQ_USER_CMD_17 | |
| 14 |	CDS_REQ_USER_CMD_16 | |
| 15 |	CDS_REQ_USER_CMD_15 | |
| 16 |	CDS_REQ_USER_CMD_14 | |
| 17 |	CDS_REQ_USER_CMD_13 | |
| 18 |	CDS_REQ_USER_CMD_12 | |
| 19 |	CDS_REQ_USER_CMD_11 | |
| 20 |	CDS_REQ_USER_CMD_10 | |
| 21 |	CDS_REQ_USER_CMD_9 | |
| 22 |	CDS_REQ_USER_CMD_8 | |
| 23 |	CDS_REQ_USER_CMD_7 | |
| 24 |	CDS_REQ_USER_CMD_6 | |
| 25 |	CDS_REQ_USER_CMD_5 | |
| 26 |	CDS_REQ_USER_CMD_4 | |
| 27 |	CDS_REQ_USER_CMD_3 | |
| 28 |	CDS_REQ_USER_CMD_2 | |
| 29 |	CDS_REQ_USER_CMD_1 | |
| 30 |	CDS_REQ_USER_CMD_0 | |
  
### 3.4. Broadcast requests

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

### 3.6. Pressure sensors

| Code | Name | Description |
| :--- | :--- | :--- |
| 0 | NO SENSOR | The device does not contain a built-in pressure sensor |
| 1 | 100 BAR | Closed type sensor with range 0 .. 100 Bar |
| 2 | 30 BAR TYPE 1 | Open type sensor with range 0 .. 30 Bar |
| 3 | 30 BAR TYPE 2 | Open type sensor with range 0 .. 30 Bar |


<div style="page-break-after: always;"></div>
