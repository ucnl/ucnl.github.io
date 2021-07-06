| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE** underwater communication system <br/> Version history & changes |
  
  
  
# uWAVE <br/> Version history & changes

<div style="page-break-after: always;"></div>

## 0. Changes and versions

| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 05-JUL-2021 | System: (all) , <br/> Core: uWAVE [JULY] v1.21 | - BUG FIX: fixed incorrect operation of the transmitter in the transparent channel mode, which led to the fact that when new data was received via the UART at the time of the end of the transfer, new data could be left untransmitted <br/> +/- Packet mode sentences changed - added a filed for azimuth for uWAVE USBL device |
| 28-JUN-2021 | System: (all), <br/> Core: uWAVE [JULY] v1.20 | + Packet mode no longer needs to be enabled separately (it is always enabled). The modem can receive packet mode messages while in both transparent channel mode and command mode |
| 21-JUN-2021 | System: --- | + Alternative firmwares: <br/> 156 bps (System: Easy) <br/> 314 bps (System: Lite) <br/> Alternative firmwares tested in real conditions on max. range 500 m |
| 14-MAY-2021 | System: STRONG 2.0, <br/> Core: uWAVE [JULY] v1.10 | + Packet mode (guaranteed delivery, ALO - At-least-once, logical addressing) <br/> - Bug fixed: Tx/Rx channel ID in remote requests |
| 21-DEC-2019 | System: STRONG 1.0, <br/> Core: uWAVE [JULY] v1.08 | + Gravity acceleration setting for more precise depth measuring |    


## 1. Features and difficult questions

### 1.1. Switching to command mode and back
Changing the state of the service core has a higher priority in relation to the transmission or reception of data. If the core is not pulled to the ground, on some models of interface converters, noise may be induced on the cable at the time of transmission in transparent channel mode. This causes the modem to switch to command mode during transmission, which can lead to premature completion of data transmission. To exclude this situation, the service core should not be left unconnected.

## 1.2. Using the same code channel for TX and RX
The use of the same code channel for receiving and transmitting in some small water areas can lead to a situation when working with short code requests, the requesting modem can receive its own request signal reflected from the coast or other objects. This is not a bug or a flaw in the modem, but a consequence of the laws of sound propagation in water. Therefore, it is recommended to use different code channels for transmission and reception.

________  
                    
<div style="page-break-after: always;"></div>
