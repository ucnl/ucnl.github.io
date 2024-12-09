[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Device specification: WAYU Pinger**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![wayu_pinger](/documentation/RT_1_332820_1.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU Pinger** - Underwater pinger beacon <br/> Device specification |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **Maximum ease of maintenance**
* **Automatic switching on from water<sup>[1](#footnote1)</sup>**
* **Minimum dimensions and weight**
* **Patented<sup>[*](#footnote_a1)</sup> monoblock design**

## DESCRIPTION

The navigation beacon-pinger **WAYU Pinger** of the **[WAYU](WAYU_DataBrief_en.md)** system is placed on the positioned object: ROV, AUV, diver or other underwater object and emits a periodic navigation signal, which is received by four floating navigation buoys **[WAYU GIB](WAYU_GIB_Specification_en.md)**, the geographic position of the pinger is determined by the navigation signal.
The device can be powered from a vessel or equipped with an autonomous power source.

_________
<a name="footnote_a1"><sup>\*</sup></a> Patents RU2659299C1, US11257472B2.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф x h) | 41 x 45 mm |
| WEIGHT (dry) | 0.15 kg |
| ACOUSTIC SIGNAL FREQUENCY | 28400 ± 100 Hz |
| ACOUSTIC SIGNAL RADIATION PERIOD | 2 ± 0.1 seconds |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[2](#footnote2)</sup> | 300 m |
| MAXIMUM ACOUSTIC PRESSURE | 163 dB re 1 μPa @ 1 m |
| SUPPLY VOLTAGE<sup>[3](#footnote3)</sup> | 7 .. 13.5 V |
| CURRENT CONSUMPTION (Idle/Transmitt) | 20 mA / 2.5 A |
| MAXIMUM SPEED RELATIVE TO BUOYS | ± 2 m/s |
| MAXIMUM DIVE DEPTH | 100 m |
| OPERATING TEMPERATURE RANGE | -10 .. 50 °C |

## PINOUT

In the integrated version, the device is supplied with an unterminated cable.

In the autonomous version, the device is supplied with a connector for connecting [underwater battery assemblies](/documentation/EN/Accessories/Sub_batteries_en).

| PIN # | WIRE COLOR | FUNCTION |
| :---: | :--- | :--- |
| 1 | 🟥 Red | U<sub>supply</sub> |
| 2 | NC | NC |
| 3 | NC | NC |
| 4 | NC | NC |
| 5 | ⬛ Black + Shield | Common/GND |

## AUTONOMOUS OPTIONS

| BATTERY TYPE | MAXIMUM TIME<sup>[5](#footnote5)</sup> OF OPERATION, h |
| :--- | :--- |
| [SB-23-64-LI](/documentation/RU/Accessories/Sub_batteries_ru#sb2364li) | up to 32 |
| [SB-34-140-LF](/documentation/RU/Accessories/Sub_batteries_ru#sb2448lf) | up to 24 |

________________
<a name="footnote1"><sup>1</sup></a> For autonomous operation  
<a name="footnote2"><sup>2</sup></a> Parameter determining the maximum range at which signal reception is possible, based on the electroacoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the environmentand the level of hydroacoustic interference.  
<a name="footnote3"><sup>3</sup></a> The maximum communication range is achieved with a supply voltage of 12 ± 1 V  
<a name="footnote4"><sup>4</sup></a> The current consumption is calculated for a supply voltage of 12 V. The signal emission period is 2 seconds, the signal duration is 10 ms  
<a name="footnote5"><sup>5</sup></a> On a new, fully charged battery at an ambient temperature of 20 °C  

<div style="page-break-after: always;"></div>
