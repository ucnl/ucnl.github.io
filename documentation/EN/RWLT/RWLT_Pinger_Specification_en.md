[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT Pinger: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/dev_big_wbat_li_small.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT Pinger** - Navigation pinger beacon <br/> Device specification |

## KEY FEATURES

* **No integration required - simply attach it mechanically to the object being positioned**
* **Maximum ease of maintenance**
* **Automatic activation in water**
* **Minimum dimensions and weight**

## DESCRIPTION

The **RWLT Pinger** navigation pinger beacon of the **[RWLT](RWLT_DataBrief_en.md)** system is placed on the object being positioned: an ROV, AUV, diver, or other underwater object. It emits a periodic navigation signal received by four floating **[RWLT GIB](RWLT_GIB_Specification_en.md)** navigation buoys. The signal is used to determine the geographic position of the pinger. Navigation is combined with telemetry transmission from the pinger, allowing its depth, water temperature, and battery supply voltage to be determined.
The pinger requires no interface with the object being positioned; simply attach it to the object.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (excluding the battery pack, Ø x h) | 41 x 45 mm |
| WEIGHT (dry, excluding the battery pack weight) | 0.16 kg |
| STANDARD BATTERY PACK | [SB-24-48-LF](/documentation/EN/Accessories/Sub_batteries_en#sb2448lf) |
| BATTERY LIFE<sup>[1](#footnote1)</sup> | 10 h |
| CARRIER FREQUENCY | 20050 Hz |
| ACOUSTIC SIGNAL EMISSION PERIOD | 2 seconds |
| NAVIGATION SIGNAL DURATION | 0.2 seconds |
| TELEMETRY INFORMATION | Depth, Temperature, Supply voltage |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[2](#footnote2)</sup> | 1500 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 160 dB re 1 μPa @ 1 m |
| MAXIMUM VELOCITY RELATIVE TO BUOYS | ± 1.8 m/s  |
| MAXIMUM IMMERSION DEPTH | 300 m |
| OPERATING TEMPERATURE RANGE | -10 .. 50 °C |
| BATTERY PACK CHARGING | From the mains using the supplied charging chassis |

________________
<a name="footnote1"><sup>1</sup></a> When operating from a standard, new, fully charged battery pack at an ambient temperature of 20 °C.  
<a name="footnote2"><sup>2</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium, and the level of underwater acoustic interference.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RWLT/RWLT_Pinger_Specification_ru.md commit=88fd0cc542bdd5dbd473485d26c437c35d66262a date=2024-04-11 -->
