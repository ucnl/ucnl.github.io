[Main](/) ❯ [Other equipment](/underwater_bespoke_systems_en) ❯ **F4105-AU: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![F4105-AU](/documentation/F4105_AU.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **F4105-AU** <br/> Acoustic wake-up unit <br/> Device specification |

## FEATURES

* Ease of use
* Minimal dimensions, weight and power consumption
* Ability to set one of 64 unique addresses
* Activation range up to 200<sup>[1](#footnote1)</sup> meters
* Maintenance-free potted housing

## DESCRIPTION

The miniature acoustic wake-up unit is designed for long-term standby while awaiting an underwater acoustic wake-up signal. When it receives a code matching the code programmed into its non-volatile memory over the underwater acoustic channel, it drives the **WAKE** cable wire to logic high for 90 seconds.  
The [F4105-SU](F4105_SU_Specification_en.md) surface control unit is used to program the device address and send the wake-up signal.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 41 x 45 mm |
| WEIGHT (dry) | 0.16 kg |
| CABLE LENGTH (at least) | 0.3 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 200 m |
| BANDWIDTH | 22 .. 29 kHz |
| POWER CONSUMPTION | 0.0055 W |
| SUPPLY VOLTAGE | 5 .. 10 V |
| OPERATING TEMPERATURE RANGE | 0 .. 30 °C |
| MAXIMUM IMMERSION DEPTH | 300 m |
| WAKE-UP OF EXTERNAL EQUIPMENT | A logic high signal lasting 90 seconds |
| NUMBER OF POSSIBLE ADDRESSES | 64 |
| ADDRESS CONFIGURATION | via UART, connected to the [F4105-SU](F4105_SU_Specification_en.md) surface wake-up unit |

## CONNECTOR PINOUT

| Pin No. | I/O | Function |
| :--- | :--- | :--- |
| 1 | I | Supply +6 .. +9 V |
| 2 | I/O | RX/TX |
| 3 | - | NC |
| 4 | O | WAKE (wake-up) |
| 5 | - | Common |

<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium, and the level of underwater acoustic interference.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/F4105/F4105_AU_Specification_ru.md commit=2adfb2000e61e639168cb9d915a11c9aea2c56e9 date=2022-09-13 -->
