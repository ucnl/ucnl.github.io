| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE** underwater communication system <br/> Version history & changes |
  
  
  
# uWAVE <br/> Version history & changes

<div style="page-break-after: always;"></div>

## 0. Changes and versions

| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 14-MAY-2021 | System: STRONG 2.0, </br> Core: uWAVE [JULY] v1.10 | + Packet mode (guaranteed delivery, ALO - At-least-once, logical addressing) </br> - Bug fixed: Tx/Rx channel ID in remote requests |
| 21-DEC-2019 | System: STRONG 1.0, </br> Core: uWAVE [JULY] v1.08 | + Gravity acceleration setting for more precise depth measuring |    


## 1. Features and difficult questions

### 1.1. Switching to command mode and back
Changing the state of the service core has a higher priority in relation to the transmission or reception of data. If the core is not pulled to the ground, on some models of interface converters, noise may be induced on the cable at the time of transmission in transparent channel mode. This causes the modem to switch to command mode during transmission, which can lead to premature completion of data transmission. To exclude this situation, the service core should not be left unconnected.

________  
                    
<div style="page-break-after: always;"></div>
