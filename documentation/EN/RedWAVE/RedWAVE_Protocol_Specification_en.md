[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RedNode: Communication protocol specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedWave** - underwater acoustic navigation system <br/> Communication protocol specification for the RedNode navigation receiver |  

# RedWave <br/> Communication protocol specification for RedNode navigation receivers

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Physical layer protocol](#11-physical-layer-protocol)
  - [1.2. NMEA0183 dialog layer protocol standard](#12-nmea0183-dialog-layer-protocol-standard)
- [2. TNT command system and standard NMEA0183 sentences](#2-tnt-command-system-and-standard-nmea0183-sentences)
  - [2.1. Main and frequently used sentences](#21-main-and-frequently-used-sentences)
    - [2.1.1. GGA](#211-gga)
    - [2.1.2. RMC](#212-rmc)
    - [2.1.3. MTW](#213-mtw)
    - [2.1.4. IC_D2H_NEW_PFIX_UPDATE](#214-ic_d2h_new_pfix_update)
    - [2.1.5. IC_D2H_DPTTMP_VAL](#215-ic_d2h_dpttmp_val)
    - [2.1.6. IC_D2H_BUOY_STATUS](#216-ic_d2h_buoy_status)
    - [2.1.7. IC_D2H_PRETMP_VAL](#217-ic_d2h_pretmp_val)
    - [2.1.8. IC_H2D_SET_VAL](#218-ic_h2d_set_val)
  - [2.2. Additional sentences](#22-additional-sentences)
    - [2.2.1. IC_D2H_ACK](#221-ic_d2h_ack)
    - [2.2.2. IC_H2D_LOC_DATA_GET](#222-ic_h2d_loc_data_get)
    - [2.2.3. IC_D2H_LOC_DATA_VAL](#223-ic_d2h_loc_data_val)
    - [2.2.4. IC_D2H_DEV_INFO_VAL](#224-ic_d2h_dev_info_val)
    - [2.2.5. IC_H2D_SNT_ENABLE](#225-ic_h2d_snt_enable)
    - [2.2.6. IC_H2D_ACT_INVOKE](#226-ic_h2d_act_invoke)
- [3. Identifier tables](#3-identifier-tables)
  - [3.1. Device types](#31-device-types)
  - [3.2. Error codes](#32-error-codes)
  - [3.3. Local data identifiers](#33-local-data-identifiers)
  - [3.4. Service action identifiers](#34-service-action-identifiers)
  - [3.5. Fix types](#35-fix-types)
  - [3.6. Buoy status identifiers](#36-buoy-status-identifiers)
   
<div style="page-break-after: always;"></div>

## 1. Introduction
### 1.1. Physical layer protocol
**[RedNode](RedNODE_Specification_en.md)** underwater acoustic navigation receivers exchange data via the RS-232 physical layer standard 
for an asynchronous interface (UART) with a data line voltage of 3.3 V. The connection uses a four-wire cable with the wires Tx (transmitter), 
Rx (receiver), Vcc (power) and GND (ground). Without additional repeaters or interface converters, correct operation of the interface 
is guaranteed for a data bus length of up to 2 m.  

Default connection port settings<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  

>**CAUTION!**
>_The modems are powered by a 12 V DC source, while the data line voltage is 3.3 V._

### 1.2. NMEA0183 dialog layer protocol standard
The NMEA0183 standard describes the format of dialog layer text (ASCII) sentences.  

Sentence example:  **`$PTNT0,1,0*hh<CR><LF>`**  

The main elements of an NMEA0183 sentence (message):
* '$' - sentence start,
* 'P' - Proprietary code
* 'TNT' - three-letter manufacturer identifier
* '0' - sentence ID
* ',' - comma (parameter delimiter)  
* '*' - checksum delimiter
* 'hh' - checksum in hexadecimal format (e.g. FF, 01). Calculated as the bitwise XOR of all bytes between '$' and '*'.
* \<CR\>\<LF\> - end of sentence (line break)  
________
<a name="footnote1"><sup>1</sup> The specified parameters can be changed on request</a>

<div style="page-break-after: always;"></div>

## 2. TNT command system and standard NMEA0183 sentences
The **D2H** prefix in a sentence name means that the sentence is sent from the Device to the Host (control system).
The **H2D** prefix in a sentence name means that the sentence is sent from the Host (control system) to the Device.

### 2.1. Main and frequently used sentences

This group includes the sentences that the device transmits by default (depending on its internal state).

#### 2.1.1. GGA
Standard NMEA0183 sentence - Global positioning system fix data.

Sentence format: **`$GNGGA,hhmmss.sss,ddmm.mmm,N|S,yyymm.mmm,E|W,x,xx,x.x,x.x,M,x.x,M,xx,xxxx*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
| | $ | Sentence start '$' |
| | GN | Standard data source - Global navigation |
| | GGA | Standard sentence ID - Global positioning system fix data |
| 1 | UTC Time | UTC, hhmmss.sss |
| 2 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 3 | N|S | Hemisphere identifier, N - northern, S - southern |
| 4 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 5 | E|W | Hemisphere identifier, E - eastern, W - western |
| 6 | Fix Type | Navigation solution type | 
| 7 | Satellites in view | Number of available satellites (always 4 in RedWave) |
| 8 | HDOP | Horizontal dilution of precision, meters. (in RedWave this field conveys the radial error, the value of the residual function at the end of the solution) |
| 9 | Altitude | Altitude, meters. (in RedWave this field conveys depth, i.e. height with a "-" sign) |
| 10 | M | M - meters |
| 11 | Geoidal separation | The field is not supported and remains empty |
| 12 | Age of data |  The field is not supported and remains empty |
| 13 | Reference station ID | The field is not supported and remains empty |
| | * | NMEA checksum delimiter |
| | hh | NMEA checksum |
| | \<CR\>\<LF\> | End of sentence |

#### 2.1.2. RMC
Standard NMEA0183 sentence - Recommended minimum, sentence 'C'.

Sentence format: **`$GNRMC,hhmmss.sss,A|V,ddmm.mmm,N|S,dddmm.mmm,E|W,x.x,x.x,ddmmyy,,,A|D|V*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | GN | Standard data source - Global navigation |
|  | RMC | Standard sentence ID - Recommended minimum, sentence 'C' |
| 1 | UTC Time | UTC, hhmmss.sss |
| 2 | Data quality indicator | A - the data are correct |
| 3 | Latitude | Geographic latitude, ddmm.mmmmmm |
| 4 | N|S | Hemisphere identifier, N - northern, S - southern |
| 5 | Longitude | Geographic longitude, dddmm.mmmmmm |
| 6 | E|W | Hemisphere identifier, E - eastern, W - western |
| 7 | Speed | The field is not supported |
| 8 | Course | The field is not supported |
| 9 | Date | The field is not supported |
| 10 | Magnetic variation | The field is not supported |
| 11 | E|W | The field is not supported |
| 12 | A | Mode, A - GNSS |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

#### 2.1.3. MTW
Standard NMEA0183 sentence - Mean water temperature.

Sentence format: **`$GNMTW,x.x,C*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | GN | Standard data source - Global navigation |
|  | MTW | Standard sentence ID - Mean temperature of water |
| 1 | Temperature | Water temperature, °C
| 2 | C | C - Celsius |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

#### 2.1.4. IC_D2H_NEW_PFIX_UPDATE
Update of the geographic position of the receiver and the buoys.

Sentence format: **`$PTNTC,x,x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | C | Sentence ID |
| 1 | Own location - latitude | Geographic latitude, ° |
| 2 | Own location - longitude | Geographic longitude, ° |
| 3 | Own location - depth | Depth, m |
| 4 | Radial error | Radial error, m |
| 5 | Buoy #1 latitude | RedBase No. 1 geographic latitude, ° |
| 6 | Buoy #1 longitude | RedBase No. 1 geographic longitude, ° |
| 7 | Buoy #2 latitude | RedBase No. 2 geographic latitude, ° |
| 8 | Buoy #2 longitude | RedBase No. 2 geographic longitude, ° |
| 9 | Buoy #3 latitude | RedBase No. 3 geographic latitude, ° |
| 10 | Buoy #3 longitude | RedBase No. 3 geographic longitude, ° |
| 11 | Buoy #4 latitude | RedBase No. 4 geographic latitude, ° |
| 12 | Buoy #4 longitude | RedBase No. 4 geographic longitude, ° |
| 13 | Temperature | Water temperature, °C |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

#### 2.1.5. IC_D2H_DPTTMP_VAL
Depth and water temperature.

Sentence format: **`PTNTN,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | N | Sentence ID |
| 1 | Depth | Depth, m |
| 2 | Temperature | Water temperature, °C |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

#### 2.1.6. IC_D2H_BUOY_STATUS
Buoy status.

Sentence format: **`$PTNTM,x.x,x.x,x.x,x,x.x,x.x,x.x,x,x.x,x.x,x.x,x,x.x,x.x,x.x,x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | M | Sentence ID |
| 1 | Buoy #1 latitude | RedBase No. 1 geographic latitude, ° |
| 2 | Buoy #1 longitude | RedBase No. 1 geographic longitude, ° |
| 3 | Buoy #1 SNR | RedBase No. 1 MSR<sup>[2](#footnote2)</sup>, dB |
| 4 | Buoy #1 status | RedBase No. 1 status<sup>[3](#footnote3)</sup> |
| 5 | Buoy #2 latitude | RedBase No. 2 geographic latitude, ° |
| 6 | Buoy #2 longitude | RedBase No. 2 geographic longitude, ° |
| 7 | Buoy #2 SNR | RedBase No. 2 MSR<sup>[2](#footnote2)</sup>, dB |
| 8 | Buoy #2 status | RedBase No. 2 status<sup>[3](#footnote3)</sup> |
| 9 | Buoy #3 latitude | RedBase No. 3 geographic latitude, ° |
| 10 | Buoy #3 longitude | RedBase No. 3 geographic longitude, ° |
| 11 | Buoy #3 SNR | RedBase No. 3 MSR<sup>[2](#footnote2)</sup>, dB |
| 12 | Buoy #3 status | RedBase No. 3 status<sup>[3](#footnote3)</sup> |
| 13 | Buoy #4 latitude | RedBase No. 4 geographic latitude, ° |
| 14 | Buoy #4 longitude | RedBase No. 4 geographic longitude, ° |
| 15 | Buoy #4 SNR | RedBase No. 4 MSR<sup>[2](#footnote2)</sup>, dB |
| 16 | Buoy #4 status | RedBase No. 4 status<sup>[3](#footnote3)</sup> |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

________
<a name="footnote2"><sup>2</sup> MSR (_Main lobe to side peak ratio_) - a measure of signal reception quality. Reception conditions are good when the parameter value is >= 20 dB.  
<a name="footnote3"><sup>3</sup> Description of the possible values \([see 3.6.](#36-buoy-status-identifiers)\)

#### 2.1.7. IC_D2H_PRETMP_VAL
Pressure and temperature.

Sentence format: **`$PTNTO,x.x,x.x*hh<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | O | Sentence ID |
| 1 | Pressure | External hydrostatic pressure, mbar |
| 2 | Temperature | Water temperature, °C |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

#### 2.1.8. IC_H2D_SET_VAL
Request to change a local parameter.

Sentence format: **`$PTNTP,x,x.x<CR><LF>`**

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | P | Sentence ID |
| 1 | Value ID | Parameter ID \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | Value | New value |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

### 2.2. Additional sentences

This group of sentences includes requests to the device from the control system and the device's responses to them.

#### 2.2.1. IC_D2H_ACK
Device response to a request from the control system.

Sentence format: **`$PTNT0,x*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | 0 | Sentence ID |
| 1 | errCode | Error code \([see 3.2.](#32-error-codes)\) |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |


#### 2.2.2. IC_H2D_LOC_DATA_GET
Request for local data.

Sentence format: **`$PTNT4,xx,00*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | 4 | Sentence ID |
| 1 | dataID | Data ID \([see 3.3.](#33-local-data-identifiers)\) |
| 2 | reserved | Reserved, '00' |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |


#### 2.2.3. IC_D2H_LOC_DATA_VAL
Device response to the [IC_H2D_LOC_DATA_GET](#222-ic_h2d_loc_data_get) and [IC_H2D_SET_VAL](#218-ic_h2d_set_val) requests: the device transmits the requested data.

Sentence format: **`$PTNT5,x,x<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | 5 | Sentence ID | 
| 1 | Requested data ID | Data ID \([see 3.3.](#33-local-data-identifiers)\) | 
| 2 | Value | Requested value | 
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |


#### 2.2.4. IC_D2H_DEV_INFO_VAL
Device response to the [IC_D2H_LOC_DATA_GET](#222-ic_h2d_loc_data_get) command if the requested data ID = [LOC_DATA_DEV_INFO](#33-local-data-identifiers).

Sentence format: **`$PTNT!,c--c,x,x,c--c,x,c--c<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | ! | Sentence ID |
| 1 | System moniker | System name |
| 2 | System version | System version (BCD) |
| 3 | Communication subsystem moniker | Communication subsystem name |
| 4 | Communication subsystem version | Communication subsystem version (BCD) |
| 5 | Device type | Device type \([see 3.1.](#31-device-types)\) |
| 6 | Serial number | Device serial number |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |


#### 2.2.5. IC_H2D_SNT_ENABLE
Sentence output control.

Sentence format: **`$PTNTQ,b,b,b,b,b,b,b*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | Q | Sentence ID |
| 1 | isMTW | Output of [MTW](#213-mtw) sentences (0 - disabled, 1 - enabled) |
| 2 | isGGA | Output of [GGA](#211-gga) sentences (0 - disabled, 1 - enabled) |
| 3 | isRMC | Output of [RMC](#212-rmc) sentences (0 - disabled, 1 - enabled) |
| 4 | isM | Output of [TNTM](#216-ic_d2h_buoy_status) sentences (0 - disabled, 1 - enabled) |
| 5 | isC | Output of [TNTC](#214-ic_d2h_new_pfix_update) sentences (0 - disabled, 1 - enabled) |
| 6 | isN | Output of [TNTN](#215-ic_d2h_dpttmp_val) sentences (0 - disabled, 1 - enabled) |
| 7 | isO | Output of [TNTO](#217-ic_d2h_pretmp_val) sentences (0 - disabled, 1 - enabled) |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |


#### 2.2.6. IC_H2D_ACT_INVOKE
Request to perform a service action.

Sentence format: **`$PTNT6,xx,00*hh<CR><LF>`**  

| No. | Field/Parameter | Description |
| :--- | :--- | :--- |
|  | $ | Sentence start '$' |
|  | P | Proprietary code |
|  | TNT | TNT command system |
|  | 6 | Sentence ID |
| 1 | Action ID | Service action ID \([see 3.4.](#34-service-action-identifiers)\) |
| 2 | Reserved | Reserved, '00' |
|  | * | NMEA checksum delimiter |
|  | hh | NMEA checksum |
|  | \<CR\>\<LF\> | End of sentence |

## 3. Identifier tables
### 3.1. Device types

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | DEVICE_REDBASE | RedBase GNSS-equipped sonobuoy |
| '1' | DEVICE_REDNODE | RedNode navigation receiver |
| '2' | DEVICE_REDNAV | RedNav diver's navigation receiver |
| '3' | DEVICE_REDGTR | RedGTR code communication modem |

### 3.2. Error codes

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | NO_ERROR | Request accepted, no errors |
| '1' | INVALID_SYNTAX | Syntax error |
| '2' | UNSUPPORTED | Request not supported |
| '3' | TRANSMITTER_BUSY | Acoustic transmitter is busy |
| '4' | ARGUMENT_OUT_OF_RANGE | Argument is outside the range of valid values |
| '5' | INVALID_OPERATION | The requested operation cannot be performed on this device |
| '6' | UNKNOWN_FIELD_ID | Unknown configuration field value |
| '7' | VALUE_UNAVAILIBLE | The requested value is not available at the moment |
| '8' | RECEIVER_BUSY | The acoustic receiver is waiting for a response from the remote system |

### 3.3. Local data identifiers

| Value | Name | Description | RO/RW<sup>[4](#footnote4)</sup> |
| :--- | :--- | :--- | :--- |
| '0' | DEVICE_INFO | Device information, firmware versions and serial number | RO |
| '1' | MAX_REMOTE_TIMEOUT | Maximum waiting time, ms | RO |
| '2' | MAX_SUBSCRIBERS | Not supported | RO |
| '3' | DEPTH | Built-in depth sensor reading, m | RO |
| '4' | TEMPERATURE | Built-in temperature sensor reading, °C | RO |
| '5' | BAT_CHARGE | Not supported | RO |
| '6' | PRESSURE_RATING | Maximum permissible hydrostatic pressure, bar | RO |
| '7' | ZERO_PRESSURE | Pressure at the water surface, mbar | RW |
| '8' | WATER_DENSITY | Water density, kg/m<sup>3</sup> | RO |
| '9' | SALINITY | Water salinity, PSU | RW |
| '10' | SOUND_SPEED | Speed of sound, m/s | RW |
| '11' | GRAVITY_ACC | Gravitational acceleration, m/s<sup>2</sup> | RO |
| '12' | YEAR | Year | RW |
| '13' | MONTH | Month | RW |
| '14' | DATE | Day of the month | RW |
| '15' | HOUR | Hour | RO |
| '16' | MINUTE | Minute | RO |
| '17' | SECOND | Second | RO |


________
<a name="footnote4"><sup>4</sup> **RO** - Read-Only, the parameter can only be read; **RW** - the parameter can be read and written.  

### 3.4. Service action identifiers 

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | LOC_INVOKE_FLASH_WRITE | Save the settings to non-volatile memory |
| '1' | LOC_INVOKE_CLEAR_WAYPOINTS | Not supported |
| '2' | LOC_INVOKE_CLEAR_TRACK | Not supported |
| '3' | LOC_INVOKE_CLEAR_NDTABLE | Not supported |
| '4' | LOC_INVOKE_DPT_ZERO_ADJUST | Set the current pressure reading as the pressure at the water surface |

### 3.5. Fix types

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | NO_FIX | Geographic position is not available |
| '1' | GNSS_FIX | Geographic position based on GNSS |

### 3.6. Buoy status identifiers

| Value | Name | Description |
| :--- | :--- | :--- |
| '0' | BSTS_NO_DATA | State is unknown |
| '1' | BSTS_TIMEOUT | Waiting interval exceeded |
| '2' | BSTS_DISCHARGED | The buoy participates in navigation, but its battery needs charging |
| '3' | BSTS_OK | The buoy participates in navigation |
| '4' | BSTS_ALIVE | Communication with the buoy is established, but its battery charge data have not been received yet |

<div style="page-break-after: always;"></div>
  
### [Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RedWAVE/RedWAVE_Protocol_Specification_ru.md commit=140fa35b442722e691ae60c2bb0c567c1442b7a0 date=2023-03-19 -->
