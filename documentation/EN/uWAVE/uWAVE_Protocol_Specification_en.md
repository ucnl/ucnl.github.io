| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE** underwater communication system interfacing protocol specification |
  
  
  
# uWAVE <br/> interfacing protocol specification

<div style="page-break-after: always;"></div>

## Content
- [1. Introduction](#1-introduction)  
  - [1.1. Physical layer](#11-physical-layer)
  - [1.2. NMEA0183 Protocol standard](#12-nmea0183-protocol-standard)
- [2. UWV Sentences](#2-uwv-sentences)  
   - [2.1. IC_D2H_ACK - device reaction](#21-ic_d2h_ack)
   - [2.2. IC_H2D_SETTINGS_WRITE - writing new settings](#22-ic_h2d_settings_write)
   - [2.3. IC_H2D_RC_REQUEST - code request to a remote subscriber](#23-ic_h2d_rc_request)
   - [2.4. IC_D2H_RC_RESPONSE - answer of remote subscriber](#24-ic_d2h_rc_response)
   - [2.5. IC_D2H_RC_TIMEOUT - remote subscriber timeout](#25-ic_d2h_rc_timeout)
   - [2.6. IC_D2H_RC_ASYNC_IN - incoming message from a remote subscriber](#26-ic_d2h_rc_async_in)
   - [2.7. IC_H2D_AMB_DTA_CFG - ambient parameters and supply voltage configuration](#27-ic_h2d_amb_dta_cfg)
   - [2.8. IC_H2D_AMB_DTA - ambient parameters and supply voltage](#28-ic_h2d_amb_dta)
   - [2.9. IC_H2D_DINFO_GET - request device information](#29-ic_h2d_dinfo_get)
   - [2.10. IC_D2H_DINFO - device information](#210-ic_d2h_dinfo)
- [3. Command mode](#3-command-mode)
- [4. Identifiers](#4-identifiers)
   - [4.1. Error codes](#41-error-codes)
   - [4.2. Remote commands](#42-remote-commands)
- [5. Appendix](#5-appendix)
   - [5.1 Command mode interfacing examples](#51-command-mode-interfacing-examples)
   - [5.2 Example 1 - requesting device information](#52-example-1---requesting-device-information)
   - [5.3 Example 2 - requesting remote data from a remote subscriber](#53-example-2---requesting-remote-data-from-a-remote-subscribers)
   - [5.4 Example 3 - setting up the ambient data configuration](#54-example-3---setting-up-the-ambient-data-configuration)  
   
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer
   
**uWAVE** underwater acoustic modems support data pairing using the RS-232 physical layer standard for asynchronous interface (UART) 
with a 3.3V data line voltage. The connection is made using a four-wire cable with Tx (transmitter), Rx (receiver), Vcc (power) 
and GND (ground) wires. Without the use of additional repeaters and interface converters, the maximum cable length, for which 
the correct operation of the interface is guaranteed, is no more than 2 meters.

Default port settings<sup>[1](#footnote1)</sup>: 
_Baudrate: 9600 bit/s_  
_Data bits: 8_  
_Stop bits: 1_  
_Parity: No_  
_Hardware flow control: No_  

>**WARNING!**
>_The modems are powered by a 5 or 12 Volt DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 Protocol standard
The NMEA0183 standard describes the format of text (ASCII) messages at the interactive level.

Sentence example: **`$PUWV0,1,0*hh<СR><LF>`**  

Parts of a message (sentence) NMEА0183:
* '$' - sentence start,
* 'P' - Proprietary
* 'UVW' - manufacturer identifier
* '0' - sentence identifier
* ',' - parameters separator
* '*' - checksum separator
* 'hh' - checksum in hexadecimal format (for example FF, 01). Byte-by-byte XOR for all characters between '$' and '*'.
* \<CR\>\<LF\> - end of sentence
________
<a name="footnote1"><sup>1</sup> Specified parameters can be changed by a request</a>

<div style="page-break-after: always;"></div>

## 2. UWV Sentences
The prefix **D2H** in the name of the message means that it is transmitted from the device (D) to the host system (H).
The **H2D** prefix in the message name means that it is transmitted from the host system (H) to the device (D).

### 2.1. IC_D2H_ACK
Device reaction  

Sentence format: **`$PUWV0,x,x*hh<CR><LF>`**  

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV	| UWV |
| 0	| Sentence ID |
| cmdID	| Incoming sentence ID that caused ACK |
| errCode	| Error code \([see 4.1](#41-error-codes)\) |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.2. IC_H2D_SETTINGS_WRITE
 Witing new settings
 
Sentence format: **`$PUWV1,x,x,x.x*hh<CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
| 1 | Sentence ID |
| txChID | Tx code channel ID |
| rxChID | Rx code channel ID |
| STY | Salinity, PSU |
| isCmdMode | ‘0’ - command mode by pin, ‘1’ - command mode by default \(to switch back to transparent channel mode use ‘0’\) |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.3. IC_H2D_RC_REQUEST
Code request to a remote subscriber

Sentence format: **`$PUWV2,x,x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
| 2 | Sentence ID | 
| txChID | Tx code channel ID |
| rxChID | Rx code channel ID for the request |
| rcCmdID | Command ID \([see 4.2](#42-remote-commands)\) |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.4. IC_D2H_RC_RESPONSE
Answer of remote subscriber  

Sentence format: **`$PUWV3,x,x.x,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
3 | Sentence ID |
rcCmdID | Command ID \([see 4.2](#42-remote-commands)\) |
propTime | Signal propagation time, sec |
MSR | Mean main lobe to side-peak ratio, dB |
Value | Requested value | 
Azimuth | Horizontal angle of arrival[ For uWAVE USBL devices only, otherwise empty] |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.5. IC_D2H_RC_TIMEOUT
Remote subscriber timeout  

Sentence format: **`$PUWV4,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
4 | Sentence ID |
rcCmdID | Command ID \([see 4.2](#42-remote-commands)\) |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.6. IC_D2H_RC_ASYNC_IN
Incoming message from a remote subscriber  

Sentence format: **`$PUWV5,x,x.x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
| 5 | Sentence ID |
| rcCmdID | Command ID \([see 4.2](#42-remote-commands)\) |
| MSR | Mean main lobe to side-peak ratio, dB |
| Azimuth | Horizontal angle of arrival[ For uWAVE USBL devices only, otherwise empty] |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.7. IC_H2D_AMB_DTA_CFG
Ambient parameters and supply voltage configuration.  
This mesage configures the modem's output of the readings of the built-in pressure/temperature sensor and supply voltage. After configuration, the modem can transmit these readings using the IC_D2H_AMB_DTA message (Section 2.8)

Sentence format: **`$PUWV6,x,x,x,x,x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
| 6 | Sentence identifier |
| IsSaveToFlash | 1 - store settings in internal Flash, 0 - do not store |
| PeriodMs | IC_D2H_AMB_DTA period in msec., 0 - disabled, 1 - tandem (send immediately after any outcoming message to the host system), or value from 500 to 60000 (0.5 - 60 sec.)  |
| IsPressure | 1 - pressure output enabled, 0 - disabled |
| IsTemperature | 1 - temperature output enabled, 0 - disabled |
| IsDepth | 1 - depth output enabled, 0 - disabled |
| IsVCC | 1 - supply voltage output enabled, 0 - disabled |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.8. IC_H2D_AMB_DTA
Ambient parameters and supply voltage.  

Sentence format: **`$PUWV7,x.x,x.x,x.x,x.x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
7 | Sentence identifier |
Pressure_mBar | Pressure in mBar |
Temperature_C | Temperature in °C |
Depth_m | Depth in meters |
VCC_V | Supply voltage in Volts |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.9. IC_H2D_DINFO_GET
Request device information  

Sentence format: **`$PUWV?,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
? | Sentence ID |
Reserved | Reserved |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

### 2.10. IC_D2H_DINFO
Device information  

Sentence format: **`$PUWV!,c--c,с--с,x,c--c,x,x.x,x,x,x*hh <CR><LF>`**

| Field/Parameter |	Description |
| :--- | :--- |
| $	| Sentence start '$' |
| PUWV | UWV |
| ! | Sentence ID |
| Serial number | Device serial number |
| System moniker | System name |
| System version | System version |
| Core moniker | Communication subsystem |
| Core version | Communication subsystem version |
| acBaudrate | Data transmission speed, baud |
| rxChID | Rx code channel ID |
| txChID | Tx code channel ID |
| maxChannels | Total number of possible code channel IDs |
| styPSU | Water salinity, PSU (can be set by the user) |
| isPTS | ‘1’ - device has a pressure/temperature sensor, ‘0’ - otherwise |
| isCmdMode | ‘1’ - command mode by default, ‘0’ - command mode by command pin. |
| *	| Checksum separator NMEA |
| hh	| Checksum NMEA |
| \<CR\>\<LF\> | Sentence end |

<div style="page-break-after: always;"></div>

## 3. Command mode
**uWAVE** modems provide the user with a so-called "transparent channel" when all data supplied to the input without changes and 
analysis are transmitted to the hydroacoustic channel, after which they are received by another modem and in the unchanged form are 
given to the user at the receiving side. In this regard, to be able to configure modems, as well as to measure the propagation time 
to remote subscribers, there is a command mode. Modems analyze input data only in command mode. To switch to the command mode, the 
“service” core should be pulled to +3.3 V. After that, the “service” core should be pulled to the ground to exit the service mode.
Also, the command mode can be enabled by default using the [IC_H2D_SETTINGS_WRITE](#22-ic_h2d_settings_write) sentence, when isCmdMode parameter equals to 1. To return to control by “service” core, [IC_H2D_SETTINGS_WRITE](#22-ic_h2d_settings_write) sentence can be used with isCmdMode parameter equals to 0.

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
| LOC_ERR_RECEIVER_BUSY | 8 | Receiver is busy (waiting for a remote answer) |
| LOC_ERR_TX_BUFFER_OVERRUN | 9 | Transmitter buffer is full |
| LOC_ERR_CHKSUM_ERROR | 10 | Checksum error |

### 4.2 Remote commands   

| Command | Value | Description |
| :--- | :--- | :--- |
| RC_PING | 0 | Ping |
| RC_PONG | 1 | Pong |
| RC_DPT_GET | 2 | Request a depth value of a remote subscriber |
| RC_TMP_GET | 3 | Request a temp. Value of a remote subscriber |
| RC_BAT_V_GET | 4 | Request a battery voltage of a remote subscriber |
| RC_ERR_NSUP | 5 | Remote subscriber answered - request not supported |
| RC_ACK | 6 | Remote subscriber answered - request accepted |
| RC_USR_CMD_000 | 7 | User command |
| RC_USR_CMD_001 | 8 | User command |
| RC_USR_CMD_002 | 9 | User command |
| RC_USR_CMD_003 | 10 | User command |
| RC_USR_CMD_004 | 11 | User command |
| RC_USR_CMD_005 | 12 | User command |
| RC_USR_CMD_006 | 13 | User command |
| RC_USR_CMD_007 | 14 | User command |
| RC_USR_CMD_008 | 15 | User command |

<div style="page-break-after: always;"></div>

## 5. Appendix
### 5.1. Command mode interfacing examples
In the following examples, the messages that come __**to**__ a modem are prefixed with `<<`, and the messages that come __**from**__
the modem are prefixed with `>>`.     
It is assumed that the modem is connected to a host system, and the command mode is enabled.  

### 5.2. Example 1 - requesting device information
```
<< $PUWV?,0*27<CR><LF>
```
PUWV? = [IC_H2D_DINFO_GET](#29-ic_h2d_dinfo_get)
```
>> $PUWV!,3A001E000E51363437333330,STRONG,256,uWAVE [JULY],257,78.27,0,0,28,0.0,1,0*18<CR><LF>
```
PUWV! = [IC_D2H_DINFO](#210-ic_d2h_dinfo)  
3A001E000E51363437333330 = serial number,  
STRONG = system moniker  
256 = 0x0100 system version is 01.00  
uWAVE \[JULY\] = core moniker,  
257 = 0x0101 core version is 01.01  
78.27 = acoustic channel baudrate, bit/sec  
0 = Tx channel ID  
0 = Rx channel ID  
28 = total number of channels available  
0.0 = salinity, PSU  
1 = built-in pressure/temperature sensor is present  
0 = command mode by default is disabled  


### 5.3. Example 2 - requesting remote data from a remote subscriber
```
<< $PUWV2,0,0,2*28
```
PUWV2 = [IC_H2D_RC_REQUEST](#23-ic_h2d_rc_request)  
0 = Tx channel ID (target Rx channel ID)  
0 = Rx channel ID (target Tx channel ID)  
2 = Request ID = [RC_DPT_GET](#42-remote-commands)  
```
>> $PUWV0,2,0*36
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
2 = ACK is for PUWV2 request  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
```
>> $PUWV3,0,2,0.00020,22.75,0.000,*1B
```
PUWV3 = [IC_D2H_RC_RESPONSE](#24-ic_d2h_rc_response)  
0 = remote modem’s Rx channel ID  
2 = Request ID = [RC_DPT_GET](#42-remote-commands)  
0.00020 = Propagation time, sec  
22.75 = MSR (Main lobe to side-peak ratio), dB  
0.000 = received value (in this case remote modem’s depth in meters)  
```
<< $PUWV2,0,0,3*29
```
PUWV2 = [IC_H2D_RC_REQUEST](#23-ic_h2d_rc_request)  
0 = Tx channel ID (target Rx channel ID)  
0 = Rx channel ID (target Tx channel ID)   
3 = Request ID = [RC_TMP_GET](#42-remote-commands)  
```
>> $PUWV0,2,0*36
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
2 = ACK is for PUWV2 request  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
```
>> $PUWV3,0,3,0.00030,26.31,27.300,*29
```
PUWV3 = [IC_D2H_RC_RESPONSE](#24-ic_d2h_rc_response)  
0 = remote modem’s Rx channel ID   
2 = Request ID = [RC_TMP_GET](#42-remote-commands)  
0.00030 = Propagation time, sec  
26.31 = MSR (Main lobe to side-peak ratio), dB  
27.300 = received value (in this case remote modem’s temperature in °C)  

### 5.4. Example 3 - setting up the ambient data configuration
```
<< $PUWV6,0,1000,1,1,1,1*03<CR><LF>
```
PUWV6 = [IC_H2D_AMB_DTA_CFG](#27-ic_h2d_amb_dta_cfg)  
0 = isSaveToFlash = false  
1000 = transmit ambient data every 1000 msec  
1 = isPressure = true  
1 = isTemperature = true  
1 = isDepth = true  
1 = isVCC = true  
```
>> $PUWV0,6,0*32<CR><LF>
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
6 = ACK is for PUWV6 request  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
```
>> $PUWV7,1025.2,29.9,-0.014,5.0*18
. . .
>> $PUWV7,1026.3,29.9,-0.002,5.0*1D
```
PUWV7 = [IC_D2H_AMB_DTA](#28-ic_h2d_amb_dta)   
1026.3 = current pressure, mBar  
29.9 = current temperature, °C  
-0.002 = current depth, m  
5.0 = current supply voltage, V  
```
<< $PUWV6,0,0,0,0,0,0*32
```
PUWV6 = [IC_H2D_AMB_DTA_CFG](#27-ic_h2d_amb_dta_cfg)  
0 = isSaveToFlash = false  
0 = do not transmit ambient data  
0 = isPressure = false  
0 = isTemperature = false  
0 = isDepth = false  
0 = isVCC = false  
```
>> $PUWV0,6,0*32
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
6 = ACK is for PUWV6 request  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
  
________

[Back to content](#content)
