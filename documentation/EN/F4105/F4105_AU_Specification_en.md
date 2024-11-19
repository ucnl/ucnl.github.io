[Главная](/README_RU) ❯ [Other equipment](/underwater_bespoke_systems_en) ❯ **Device specification: F4105-AU**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![F4105-AU](/documentation/F4105_AU.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **F4105-AU** <br/> Acoustic awakening unit <br/> Device specification |

## KEY FEATURES

* Ease of use
* Minimal dimensions, weight and power consumption
* Possibility of setting one of 64 unique addresses
* Response range up to 200<sup>[1](#footnote1)</sup> meters
* Maintenance-free cast-in housing
  
## DESCRIPTION

The miniature hydroacoustic awakener is designed to implement the long-term standby mode of hydroacoustic awakening. When a code corresponding to the code programmed into the non-volatile memory of the device is received via the hydroacoustic channel, it switches the **WAKE** cable core to the logical one state for 90 seconds.
The above-water control unit [F4105-SU](F4105_SU_Specification_en.md) is used to program the device address and send the awakening signal.
  
<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATION

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h)| 41 x 45 mm |
| WEIGHT (dry) | 0.16 kg |
| CABLE LENGTH (not less) | 0.3 m |
| MAX. ACOUSTIC RANGE<sup>[1](#footnote1)</sup> | 200 m |
| BANDWIDTH | 22 .. 29 kHz |
| POWER CONSUMPTION | 0.0055 W |
| POWER SUPPLY | 5 .. 10 V |
| WORKING TEMPERATURE RANGE | 0 .. 30 °С |
| DEPTH RATING | 300 m |
| EXT. EQUIPMENT AWAKENING | High level (logic one, TTL) 90 sec | 
| ADDRESSES | 64 |
| ADDRESS SET-UP | via UART, by connecting to [F4105-SU](F4105_SU_Specification_en.md) |

## CONNECTOR PINOUT

| № Pin | I/O | Function |
| :--- | :--- | :--- |
| 1 | I | Vcc +6 .. +9 В |
| 2 | I/O | RX/TX |
| 3 | - | NC |
| 4 | O | WAKE |
| 5 | - | Ground |

<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the environment, and the level of hydroacoustic interference.  

<div style="page-break-after: always;"></div>

