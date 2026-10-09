[Main](/) ❯ [Underwater wireless voice systems](/underwater_wireless_voice_systems_en) ❯ **RedPhone-DX: Communication protocol specification**

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
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedPhone-DX** <br/> Communication protocol specification |

# RedPhone-DX <br/> Communication protocol specification

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. RPH command system](#2-rph-command-system)
  - [2.1. IC_D2H_ACK - device response](#21-ic_d2h_ack)
  - [2.2. IC_H2D_SETTINGS_WRITE - writing new settings](#22-ic_h2d_settings_write)
  - [2.3. IC_H2D_DINFO_GET - request for device information](#23-ic_h2d_dinfo_get)
  - [2.4. IC_D2H_DINFO - device information](#24-ic_d2h_dinfo)

<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol

**RedPhone-DX** devices support data interfacing via the RS-232 physical layer standard for an asynchronous interface (UART)
with a data line voltage of 3.3 V. The connection uses a four-wire cable with the wires Tx (transmitter), Rx (receiver), Vcc (power)
and GND (ground). Without additional repeaters or interface converters, the maximum length of the data bus for which correct operation
of the interface is guaranteed is no more than 2 m.

Default connection port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**CAUTION!**
>_The data line voltage is 3.3 V._


### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of dialog layer text (ASCII) sentences.  

Sentence example:  **`$RPH0,1,0*hh<CR><LF>`**  

The main elements of an NMEA0183 sentence (message):
* '$' - sentence start,
* 'P' - Proprietary code
* 'RPH' - three-letter ID
* '0' - sentence ID
* ',' - comma (parameter delimiter)  
* '*' - checksum delimiter
* 'hh' - checksum in hexadecimal format (e.g. FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)
________
<a name="footnote1"><sup>1</sup> The specified parameters can be changed on request</a>

<div style="page-break-after: always;"></div>

## 2. RPH command system
The **D2H** prefix in a sentence name means that the sentence is sent from the Device to the Host (control system).
The **H2D** prefix in a sentence name means that the sentence is sent from the Host (control system) to the Device.

### 2.1. IC_D2H_ACK
The IC_D2H_ACK sentence is the device's response to a request received from the control system.  

Sentence format: **`$RPH0,x,x*hh<CR><LF>`**  

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PRPH | RPH |
| 0 | Sentence ID |
| cmdID | ID of the command being processed (the one the device responded to) |
| errCode | Error code |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.2. IC_H2D_SETTINGS_WRITE
Writing new settings
 
Sentence format: **`$PRPH1,x,x,x,x*hh<CR><LF>`**                            

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PRPH | RPH |
| 1 | Sentence ID |
| chNumber | Receive and transmit channel ID |
| isRWLT | RWLT tracking system compatibility mode flag |
| RWLT_Diver_ID | Diver ID for operation with the RWLT system |
| RWLT_Channel_ID | Channel ID for operation with the RWLT system |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.3. IC_H2D_DINFO_GET
Get information about the device. The device responds to this sentence with the [IC_D2H_DINFO](#24-ic_d2h_dinfo) sentence.

Sentence format: **`$PRPH?,x*hh<CR><LF>`**

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PRPH | RPH |
| ? | Sentence ID |
Reserved | Reserved |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |

### 2.4. IC_D2H_DINFO
Device information  

Sentence format: **`$PRPH!,c--c,c--c,x,c--c,c--c,x,x,x,x*hh<CR><LF>`**                            

| Field/Parameter | Description |
| :--- | :--- |
| $ | Sentence start '$' |
| PRPH | RPH |
| ! | Sentence ID |
| Serial number | Device serial number |
| System moniker | System name |
| System version | Version |
| Core moniker | Communication subsystem |
| Core version | Communication subsystem version |
| acBaudrate | Data rate, baud |
| rxChID | Receive channel ID |
| txChID | Transmit channel ID |
| channelID | Receive/transmit channel ID |
| isRWLT | RWLT tracking system compatibility mode flag |
| RWLT_Diver_ID | Diver ID when operating with the RWLT system |
| RLWT_Channel_ID | RWLT system channel ID |
| * | NMEA checksum delimiter |
| hh | NMEA checksum |
| \<CR\>\<LF\> | End of sentence |



| Error | Value | Description |
| :--- | :--- | :--- |
| LOC_ERR_NO_ERROR | 0 | Request accepted |
| LOC_ERR_INVALID_SYNTAX | 1 | Syntax error |
| LOC_ERR_UNSUPPORTED | 2 | Request not supported |
| LOC_ERR_TRANSMITTER_BUSY | 3 | Transmitter is busy |
| LOC_ERR_ARGUMENT_OUT_OF_RANGE | 4 | The specified parameter is outside the valid range |
| LOC_ERR_INVALID_OPERATION | 5 | Invalid request |
| LOC_ERR_UNKNOWN_FIELD_ID | 6 | Unknown identifier |
| LOC_ERR_VALUE_UNAVAILIBLE | 7 | The requested parameter is not available at the moment |
| LOC_ERR_CHKSUM_ERR | 8 | Checksum error |


<div style="page-break-after: always;"></div>

[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RedPhone/RedPhone-DX_protocol_specification_ru.md commit=38f5908cb09601a036378a8faeaf6d389b8618fb date=2026-06-10 -->
