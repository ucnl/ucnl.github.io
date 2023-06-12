[Main](/../../) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave: Versions & changes**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE** underwater communication system <br/> Version history & changes |
  
# uWAVE <br/> Version history & changes

<div style="page-break-after: always;"></div>

## 0. Changes and versions

| Actual FW version | **uWave [JULY] 1.33** from 12-JUN-2023 |
| :--- | :--- |
| | |
  
| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 12-JUN-2023 | System: (all) <br/> Core: uWAVE [JULY] v1.33 | - BUGFIX: fixed a bug with packet processing and the absence of a message about unsuccessful transmission in some cases |
| 18-OCT-2022 | System: (all) <br/> Core: uWAVE [JULY] v1.32 | - BUGFIX: Fixed a bug due to which the device could not accept for transmission packets larger than 54 bytes |
| 31-JAN-2022 | System: (all) <br/> Core: uWAVE [JULY] v1.31 | - BUGFIX: Fixed a bug due to which the message about the delivered package came along with the ACK message to the previous command <br/> - The size of firmware has been reduced by almost 4 times due to extensive refactoring |
| 10-DEC-2021 | System: (all, except uWave USBL) <br/> Core: uWAVE [JULY] v1.30 | From this version, with the active setting of **IsCmdModeByDefault**, the CMD wire becomes not an input, but an output. It transmits a digital strobe signal synchronized with the moment of emission and reception. |
| 27-SEP-2021 | System: (all) <br/> Core: uWAVE [JULY] v1.24 | - BUG FIX: fixed a bug due to which it was impossible to interrupt retry attempts to transmit a packet message |
| 17-SEP-2021 | System: (all) <br/> Core: uWAVE [JULY] v1.23 | - BUG FIX: fixed a bug due to which in rare cases the modem could stay in the remote request awaiting mode |
| 30-AUG-2021 | System: (all) , <br/> Core: uWAVE [JULY] v1.22 | - BUG FIX: fixed a bug that could lead to disruption of the interface in the direction from the modem to the user system when working with command requests |
| 08-JUL-2021 | System: (all) , <br/> Core: uWAVE [JULY] v1.21 | - BUG FIX: fixed incorrect operation of the transmitter in the transparent channel mode, which led to the fact that when new data was received via the UART at the time of the end of the transfer, new data could be left untransmitted <br/> +/- Packet mode sentences changed - added a filed for azimuth for uWAVE USBL device <br/> + Supports range measurement and requests for depth, temperature and supply voltage within the logical addressing of the packet mode |
| 28-JUN-2021 | System: (all), <br/> Core: uWAVE [JULY] v1.20 | + Packet mode no longer needs to be enabled separately (it is always enabled). The modem can receive packet mode messages while in both transparent channel mode and command mode |
| 21-JUN-2021 | System: --- | + Alternative firmwares: <br/> 156 bps (System: Easy) <br/> 314 bps (System: Lite) <br/> Alternative firmwares tested in real conditions on max. range 500 m |
| 14-MAY-2021 | System: STRONG 2.0, <br/> Core: uWAVE [JULY] v1.10 | + Packet mode (guaranteed delivery, ALO - At-least-once, logical addressing) <br/> - Bug fixed: Tx/Rx channel ID in remote requests |
| 21-DEC-2019 | System: STRONG 1.0, <br/> Core: uWAVE [JULY] v1.08 | + Gravity acceleration setting for more precise depth measuring |    


## 1. Features and difficult questions

### 1.1. Switching to command mode and back
Changing the state of the service core has a higher priority in relation to the transmission or reception of data. If the core is not pulled to the ground, on some models of interface converters, noise may be induced on the cable at the time of transmission in transparent channel mode. This causes the modem to switch to command mode during transmission, which can lead to premature completion of data transmission. To exclude this situation, the service core should not be left unconnected.

### 1.2. Using the same code channel for TX and RX
The use of the same code channel for receiving and transmitting in some small water areas can lead to a situation when working with short code requests, the requesting modem can receive its own request signal reflected from the coast or other objects. This is not a bug or a flaw in the modem, but a consequence of the laws of sound propagation in water. Therefore, it is recommended to use different code channels for transmission and reception.

### 1.3. Modem returns 'TX Busy' error when trying to send something after receiving a message in the packet mode
A modem that receives a message in the packet mode immediately sends the ACK, so its transmitter is busy. The user can use the 'ACK On TX Finished' setting. In this case, the modem will inform the user at the end of each transmission. An alternative way to handle this situation is to retry transmission after a time of about 500 ms.

### 1.4. Code channels settings update should be followed with device restart
If you change these settings just restart (disconnect power supply, wait 1-2 seconds and connect power supply) the device to apply new settings.

## 2. Known issues

| Description | Status |
| :--- | :--- |
| Devices accepts all hexadecimal values only in upper-case. This affects all packet mode related commands | Not fixed |

________  
                    
<div style="page-break-after: always;"></div>
