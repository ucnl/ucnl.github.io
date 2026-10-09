[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **AzimuthConsole v1.x: User's manual**

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
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **AzimuthConsole v1.x** - Cross-platform application for the Zima2 USBL system <br/> User's manual |

# AzimuthConsole v1.x <br/> User's manual

<div style="page-break-after: always;"></div>

<details>
<summary>Contents</summary>

  - [A.1.1. HELP](#a11-help)
  - [A.1.2. SETM](#a12-setm)
  - [A.1.3. SETA](#a13-seta)
  - [A.1.4. SETO](#a14-seto)
  - [A.1.5. SARP](#a15-sarp)
  - [A.1.6. CLS](#a16-cls)
  - [A.1.7. EXIT](#a17-exit)
  - [A.1.8. OCON](#a18-ocon)
  - [A.1.9. CCON](#a19-ccon)
  - [A.1.10. CNA?](#a110-cna)
  - [A.1.11. ITG?](#a111-itg)
  - [A.1.12. DET?](#a112-det)
  - [A.1.13. CREQ](#a113-creq)
  - [A.1.14. LHO?](#a114-lho)
  - [A.1.15. OFMT?](#a115-ofmt)
  - [A.1.16. PITG](#a116-pitg)
  - [A.1.17. RITG](#a117-ritg)
  - [A.1.18. LHOV](#a118-lhov)
  - [A.1.19. SRC3](#a119-src3)
  - [A.1.20. HKEYS](#a120-hkeys)
  - [A.1.21. PLAY](#a121-play)
  - [A.1.22. RRA?](#a122-rra)
  - [A.1.23. SRRA](#a123-srra)
  - [A.1.24. SIOC](#a124-sioc)
  - [A.1.25. FLTS](#a125-flts)
  - [A.1.26. FLTS](#a126-flts)
  - [A.1.27. NWEB](#a127-nweb)
- [A.2. Examples](#a2-examples)
  - [A.2.1. Command-line parameters](#a21-command-line-parameters)
  - [A.2.2. Frequently used commands](#a22-frequently-used-commands)
- [A.3. Frequently asked questions](#a3-frequently-asked-questions)

</details>

___

### A.1.1. HELP
Display help on the supported commands.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```help```

___

### A.1.2. SETM
**SETM** - **SET** **M**ain parameters.  
Set the main application settings.

Available via:

| | | 
| :--- | :--- |
| command line | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```setm,azmPort|auto,[azmBaudrate],[rctrl_in_ip_addr:port],[rctrl_out_ip_addr:port],[addr_mask],[salinity_PSU],[max_dist_m]```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | azmPort | Serial port for connecting the Zima2-B direction-finding antenna and its variants. If the port is not known in advance, it is recommended to specify "auto". |
| 2 | azmBaudRate | Baud rate of the serial port for connecting the Zima2-B direction-finding antenna. The default value is 9600. It is recommended to leave this field empty. |
| 3 | rctrl_in_ip_addr:port | IP address and port for receiving control commands over the UDP protocol. The default value is 255.255.255.255:28127. |
| 4 | rctrl_out_ip_addr:port | IP address and port for sending responses to control commands over the UDP protocol. The default value is 255.255.255.255:28129. |
| 5 | addr_mask | Address mask for interrogating the responder-beacons. The default value is 1 - only the beacon with address 1 will be interrogated. |
| 6 | salinity_PSU | Salinity in PSU in the range from 0.0 to 40.0. The default value is 0.0. |
| 7 | max_dist_m | Maximum operating range, from 500 m to 5500 m. This value determines the maximum waiting interval for the responder-beacon response. |

Example:
```SETM,AUTO,,255.255.255.255:28127,255.255.255.255:28129,1,0,1000 ```

___

### A.1.3. SETA
**SETA** - **SET** **A**uxilary sources parameters.  
Set the settings of the additional navigation data sources AUX1 and AUX2.

To determine absolute geographic coordinates, the system needs the geographic position of the direction-finding antenna and the azimuth angle. The geographic position is taken from the **$G*RMC** sentences, and the azimuth angle from the **$\*\*HDT** or **$\*\*HDG** or **$\*\*HDM** sentences.

If a GNSS compass is used that is the source of both the geographic position and the azimuth angle, only **AUX1** must be specified. If a GNSS receiver and a magnetic compass are used, or if for some reason the geographic position and the azimuth angle are obtained from two different devices, **AUX1** must be specified as the source of the geographic position, and **AUX2** as the source of the azimuth angle.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```seta,[aux1Port|auto],[aux1Baudrate],[aux2Port|auto],[aux2Baudrate]```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | aux1Port | Serial port for connecting a GNSS compass or a GNSS receiver. If the port is not known in advance, it is recommended to specify "auto". |
| 2 | aux1Baudrate | Baud rate of the serial port for connecting AUX1. The default value is 9600. |
| 3 | aux2Port | Serial port for connecting a magnetic compass or another source of the azimuth angle. If the port is not known in advance, it is recommended to specify "auto". |
| 4 | aux2Baudrate | Baud rate of the serial port for connecting AUX2. The default value is 9600. |

Example:
```SETA,AUTO,38400,,,```

___

### A.1.4. SETO
**SETA** - **SET** **O**utput parameters.  
Set the settings for the output ports.

The application can send navigation data to a serial port or to a UDP port.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```seto,[outPort],[outBaudrate],[out_ip_addr:port]```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | outPort | Serial port to which the generated navigation information is sent. If the field is empty, no serial port is used for output. |
| 2 | outBaudrate | Baud rate of the serial port. The default value is 9600. |
| 3 | out_ip_addr:port | UDP connection parameters for sending the generated navigation information, in the address:port format. If the field is empty, the UDP connection is not used for sending navigation information. |

Example:
```SETO,COM4,115200,255.255.255.255:28128```

___

### A.1.5. SARP
**SARP** - **S**et **A**ntenna **R**elative **P**osition.  
Set the position of the direction-finding antenna relative to the position reference point and the angular correction between the zero direction of the direction-finding antenna and that of the compass.
The Y axis is the longitudinal axis of the vessel from stern to bow, the X axis is the transverse axis of the vessel from port to starboard, the Z axis points vertically down. 

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```sarp,x_offset_m,y_offset_m,angular_offset_deg```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | x_offset_m | Offset of the direction-finding antenna, in meters, relative to the position reference point along the transverse axis of the vessel. |
| 2 | y_offset_m | Offset of the direction-finding antenna, in meters, relative to the position reference point along the longitudinal axis of the vessel. |
| 3 | angular_offset_deg | Angle between the zero direction of the compass and that of the underwater acoustic direction-finding antenna around the Z axis, clockwise, in the range from 0 to 360°. |

Example:
```SARP,0.7,2.1,0.5```

___

### A.1.6. CLS
Clear the screen.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ❌ |

Command format:
```cls```

___

### A.1.7. EXIT
Terminate the application.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ❌ |

Command format:
```exit```

___

### A.1.8. OCON
**OCON** - **O**pen **CON**nections.  
Connect the devices - open the connections. Equivalent to pressing the 'LINK' button in the AzimuthSuite application.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```OCON```

___

### A.1.9. CCON
**CCON** - **C**lose **CON**nections.  
Close all connections. Equivalent to pressing the 'LINK' button in the AzimuthSuite application.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```CCON```

___

### A.1.10. CNA?
**CNA?** - Are **C**o**N**nections **A**ctive**?**.  
Query the connection status.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```CNA?```

The result is returned in the form:
```CNA,true|false```

- true - the connections are active
- false - the connections are inactive

___

### A.1.11. ITG?
**ITG?** - Is **I**n**T**erro**G**ation active**?**.  
Query whether the interrogation of the responder-beacons is active.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```ITG?```

The result is returned in the form:
```ITG,true|false```

- true - the responder-beacons are being interrogated
- false - the responder-beacons are not being interrogated

___

### A.1.12. DET?
**DET?** - Is device **DET**ected **?**.  
Check whether the device has been detected.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```DET?,deviceID```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | deviceID | Device identifier, can take a value from the set: AZM, AUX1, AUX2 |

The result is returned in the form:
```DET,deviceID,true|false```

- true - the device is connected and identified
- false - the device has not been identified or is inactive

___

### A.1.13. CREQ
**CREQ** - **C**ustom **REQ**uest.  
Request user data.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```CREQ,rem_addr,data_id```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | rem_addr | Address of the responder-beacon in the range from 1 to 16. |
| 2 | data_id | Variable identifier in the range from 3 to 30. |

The result is returned in the form:
```CREQR,rem_addr,data_id,result```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | rem_addr | Address of the beacon that sent the user value |
| 2 | data_id | Variable identifier |
| 3 | result | Variable value |

___

### A.1.14. LHO?
**LHO?** - Is **L**ocation and **H**eading **O**verride feature active**?**.  
Query the status of the geographic position and azimuth override function.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```LHO?```

The result is returned in the form:
```LHO,true|false```
- true - the function is active
- false - the function is inactive

___

### A.1.15. OFMT?
**OFMT?** - **O**utput data **F**or**M**a**T?**.  
Query the format of the output messages.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```OFMT?```

As a result, the formats of the output messages in use are displayed.

___

### A.1.16. PITG
**PITG** - **P**ause **I**n**T**erro**G**ation.  
Pause the interrogation of the responder-beacons.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```PITG```

___

### A.1.17. RITG
**RITG** - **R**esume **I**n**T**erro**G**ation.  
Resume the interrogation of the responder-beacons.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```RITG```

___

### A.1.18. LHOV
**LHOV** - **L**ocation and **H**eading **OV**erride.  
Override the geographic position and the azimuth angle. This function can be used to set the geographic position and the azimuth angle manually if the direction-finding antenna is static and does not change its orientation and position in space. 

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```LHOV,lat_deg,lon_deg,hdn_deg```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | lat_deg | Geographic latitude in degrees in the range from -90 to 90° |
| 2 | lon_deg | Geographic longitude in degrees in the range from -180 to 180° |
| 3 | hdn_deg | Azimuth angle in degrees in the range from 0 to 360° |

___

### A.1.19. SRC3
**SRC3** - **S**set **R**esponders **C**oordinates for 3 items.
Set the coordinates of the three reference responder-beacons used as a long navigation base. 
The command is used in the long baseline (LBL) navigation mode, when the LBL transceiver determines its position from three responder-beacons that are stationary relative to each other. 

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```SRC3,mode,r1x,r1y,r2x,r2y,r3x,r3y```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | mode | 0 - clear the coordinates of the responder-beacons, 1 - Cartesian coordinate system |
| 2 | r1x | X coordinate of the responder-beacon with address 1 |
| 3 | r1y | Y coordinate of the responder-beacon with address 1 |
| 4 | r2x | X coordinate of the responder-beacon with address 2 |
| 5 | r2y | Y coordinate of the responder-beacon with address 2 |
| 6 | r2x | X coordinate of the responder-beacon with address 3 |
| 7 | r2y | Y coordinate of the responder-beacon with address 3 |

___

### A.1.20. HKEYS
**HKEYS** - Get **H**ot **K**eys hint.
Get the hotkeys hint.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ❌ |

Command format:
```HKEYS```

___

### A.1.21. PLAY
**PLAY** - **PLAY**back a log-file.
Play back a log file.

During operation, the application records a log of the information exchange with the connected device of the Zima2 system, saving the timestamps as well. This makes it possible to play back the operation of the system later without having to connect the device. If so configured, the application will send navigation data over the specified channels (serial port, UDP) just as it would when working with the device on the water.

This function can be useful for debugging when interfacing various software with AzimuthConsole.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ❌ |

Command format:
```PLAY,[mode],[logFileName]```

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | mode | Reserved |
| 2 | logFileName | Path to the log file to be played back. To stop the playback early, run the command with an empty file name. |

___

### A.1.22. RRA?
**RRA?** - **R**emote **R**esponder **A**ddress.
Query the current address value of the responder-beacon.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```RRA?```

The result is returned in the form:
```RRA,address```
address - the current address value of the responder-beacon

___

### A.1.23. SRRA
**SRRA** - **S**et **R**emote **R**esponder **A**ddress.
Set the current address value of the responder-beacon.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ❌ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```SRRA,address```

The result is returned in the form:
```RRA,address```
address - the current address value of the responder-beacon

| No. | Parameter name | Description |
| :--- | :--- | :--- |
| 1 | address | Address of the responder-beacon. |

___

### A.1.24. SIOC
**SIOC** - **S**et responder **I**ndividual **O**utput **C**hannel.
Set the UDP connection parameters for an individual responder-beacon. 

If the parameters of an individual connection are set for one or more beacons, the application will send the standard RMC, GGA and MTW (NMEA0183) sentences over them, with the coordinates (if available) of the corresponding responder-beacons.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ✔ |
| remote terminal (UDP) | ✔ |

Command format:
```SIOC,rem_addr,ip_addr:port```

___

### A.1.25. FLTS
**FLTS** - **F**i**lt**ering **S**ettings.
Set the navigation data filtering settings.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```FLTS,usbl_sf_fifo,usbl_sf_thld,usbl_df_fifo,usbl_df_mspeed,usbl_df_thld,lbl_rer_thld,lbl_sf_fifo,lbl_sf_thld,lbl_df_fifo,lbl_df_mspeed,lbl_df_thld```

| No. | Parameter name | Description | Default value |
| :--- | :--- | :--- | :--- |
| 1 | usbl_sf_fifo | USBL mode: FIFO size for the smoothing filter | 4 |
| 2 | usbl_sf_thld | USBL mode: Reset threshold of the smoothing filter, m | 100 |
| 3 | usbl_df_fifo | USBL mode: FIFO size of the ACHOD filter | 8 |
| 4 | usbl_df_mspeed | USBL mode: maximum possible speed of the positioned object, m/s | 1 |
| 5 | usbl_df_thld | USBL mode: Threshold distance (ACHOD filter), m | 5 |
| 6 | lbl_rer_thld | LBL mode: Radial error threshold value, m | 10 |
| 7 | lbl_sf_fifo | LBL mode: FIFO size for the smoothing filter | 4 |
| 8 | lbl_sf_thld | LBL mode: Reset threshold of the smoothing filter, m | 30 |
| 9 | lbl_df_fifo | LBL mode: FIFO size of the ACHOD filter | 8 |
| 10 | lbl_df_mspeed | LBL mode: maximum possible speed of the positioned object, m/s | 1 |
| 11 | lbl_df_thld | LBL mode: Threshold distance (ACHOD filter), m | 5 |

- If fields 7 and 8 are empty, the smoothing filter is not used in LBL mode.  
- If fields 9, 10 and 11 are empty, the ACHOD filter is not used in LBL mode.

___

### A.1.26. FLTS
**SETS** - **S**e**T**tings **S**how.
Display the current application settings.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```SETS```
___

### A.1.27. NWEB
**NWEB** - **N**o **WEB**
Do not initialize the built-in web server.

Available via:

| | | 
| :--- | :--- |
| command-line parameters | ✔ |
| terminal | ❌ |
| remote terminal (UDP) | ❌ |

Command format:
```SETS```

___


## A.2. Examples
### A.2.1. Command-line parameters
Standard settings, output over UDP:

```AzimuthConsole SETM,AUTO,,255.255.255.255:28127,255.255.255.255:28129,1,0,1000 SETO,,,255.255.255.255:28128```

Standard settings, connection of a GNSS compass transmitting at 38400 baud, output of navigation data over UDP:

```AzimuthConsole SETM,AUTO,,255.255.255.255:28127,255.255.255.255:28129,1,0,1000 SETA,AUTO,38400,, SETO,,,255.255.255.255:28128```

### A.2.2. Frequently used commands
Set the geographic position and orientation of the antenna manually:

```LHOV,44.123456,48.123456,17.5```

Latitude: 44.123456°
Longitude: 48.123456°
Azimuth of the antenna zero: 17.5°

## A.3. Frequently asked questions

**Q**: Can data be output to the serial port and over UDP at the same time?
> **A**: Yes, this is one of the possible options.

**Q**: Can specific port names be set?
> **A**: Yes, the commands that set the connection parameters allow specific port names to be set; to do this, it is enough to specify the actual port instead of the "AUTO" parameter. But if it turns out to be wrong, the application will try to find the port to which the device is actually connected.

<!-- docs-sync: source=documentation/RU/Zima/AzimuthConsole_v1x_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
