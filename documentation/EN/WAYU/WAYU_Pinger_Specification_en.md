[Main](/) ❯ [Educational projects](/educational_projects_en) ❯ **WAYU Pinger: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![wayu_pinger](/documentation/RT_1_332820_1.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU Pinger** - Navigation pinger beacon <br/> Device specification |

## KEY FEATURES

* **Maximum ease of maintenance**
* **Automatic activation in water<sup>[1](#footnote1)</sup>**
* **Minimum dimensions and weight**
* **Patented<sup>[*](#footnote_a1)</sup> monoblock design**

## DESCRIPTION

The **WAYU Pinger** navigation pinger beacon of the **[WAYU](WAYU_DataBrief_en.md)** system is placed on the object to be positioned: an ROV, AUV, diver or other underwater object, and emits a periodic navigation signal that is received by four floating **[WAYU GIB](WAYU_GIB_Specification_en.md)** navigation buoys. The geographic position of the pinger is determined from the navigation signal.
The device can be powered by the carrier or equipped with an autonomous power source.

_________
<a name="footnote_a1"><sup>\*</sup></a> *Patent RU2659299C1*.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 41 x 45 mm |
| WEIGHT (dry) | 0.15 kg |
| ACOUSTIC SIGNAL FREQUENCY | 25000 ± 100 Hz |
| ACOUSTIC SIGNAL EMISSION PERIOD | 2 ± 0.1 seconds |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[2](#footnote2)</sup> | 300 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 163 dB re 1 μPa @ 1 m |
| SUPPLY VOLTAGE<sup>[3](#footnote3)</sup> | 7 .. 13.5 V |
| CURRENT CONSUMPTION (Idle/Transmit) | 20 mA / 2.5 A |
| MAXIMUM VELOCITY RELATIVE TO BUOYS | ± 2 m/s  |
| MAXIMUM IMMERSION DEPTH | 100 m |
| OPERATING TEMPERATURE RANGE | -10 .. 50 °C |

## CABLE WIRE ASSIGNMENT AND PINOUT

In the integrated version, the device is supplied with an unterminated cable.  
In the standalone version, the device is supplied with a connector for connecting [underwater battery packs](/documentation/EN/Accessories/Sub_batteries_en).

| CONNECTOR PIN No. | WIRE COLOR |  FUNCTION |
| :---: | :--- | :--- |
| 1 | 🟥 Red | U<sub>supply</sub> |
| 2 | NC | NC |
| 3 | NC | NC |
| 4 | NC | NC |
| 5 | ⬛ Black + Shield | Common/GND |

## STANDALONE VERSIONS

| BATTERY TYPE | MAXIMUM BATTERY LIFE<sup>[5](#footnote5)</sup>, h |
| :--- | :---: |
| [SB-23-64-LI](/documentation/EN/Accessories/Sub_batteries_en#sb2364li) | up to 32 |
| [SB-24-48-LF](/documentation/EN/Accessories/Sub_batteries_en#sb2448lf) | up to 24 |

________________
<a name="footnote1"><sup>1</sup></a> In the standalone version  
<a name="footnote2"><sup>2</sup></a> A parameter that determines the maximum range at which signal reception is possible, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote3"><sup>3</sup></a> The maximum communication range is achieved at a supply voltage of 12 ± 1 V  
<a name="footnote4"><sup>4</sup></a> The current consumption is calculated for a supply voltage of 12 V. The signal emission period is 2 seconds, the signal duration is 10 ms  
<a name="footnote5"><sup>5</sup></a> With a new, fully charged battery at an ambient temperature of 20 °C

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/WAYU/WAYU_Pinger_Specification_ru.md commit=b43f8a0f6cb6988cb936f98adf8dc53a67d2e71a date=2025-06-04 -->
