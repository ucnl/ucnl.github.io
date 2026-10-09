[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT Pinger-K: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima2rk.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT Pinger-K** - Navigation pinger beacon for depths up to 1000 m <br/> Device specification |

## KEY FEATURES

* **Easy integration with the carrier**
* **Easy to maintain**
* **Minimum dimensions and weight**

## DESCRIPTION

The **RWLT Pinger-K** navigation pinger beacon of the **[RWLT](RWLT_DataBrief_en.md)** system is installed on the object to be positioned (an ROV, AUV or other underwater object) and emits a periodic navigation signal that is received by four floating **[RWLT GIB](RWLT_GIB_Specification_en.md)** navigation buoys. The geographic position of the pinger is determined from the navigation signal, and the telemetry transmitted by the pinger together with the navigation signal provides its depth, the water temperature and the battery voltage. Unlike the basic version of the device, **RWLT Pinger-K** is designed to operate at a maximum depth of up to 1000 m.
The device is powered by the carrier.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS<sup>[1](#footnote1)</sup> (Ø x h) | 80 x 147 mm |
| WEIGHT (dry)<sup>[1](#footnote1)</sup> | 1130 g |
| MAXIMUM DEPTH | 1000 m |
| DEPTH RESOLUTION | 0.6 m for the version up to 500 m, 1.2 m for the version up to 1000 m |
| CARRIER FREQUENCY | 20050 Hz |
| ACOUSTIC SIGNAL EMISSION PERIOD | 2 seconds |
| NAVIGATION SIGNAL DURATION | 0.2 seconds |
| TELEMETRY INFORMATION | Depth, Temperature, Supply voltage |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[2](#footnote2)</sup> | 1500 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 160 dB re 1 μPa @ 1 m |
| MAXIMUM VELOCITY RELATIVE TO BUOYS | ± 1.8 m/s |
| OPERATING TEMPERATURE RANGE | -10 .. 50 °C |

<!-- | BANDWIDTH | 10 .. 30 kHz | -->

________________
<a name="footnote1"><sup>1</sup></a> Without taking into account the weight and dimensions of the transducer. The device is equipped with the transducer [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en).   
<a name="footnote2"><sup>2</sup></a> A parameter that determines the maximum range at which signal reception is possible, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RWLT/RWLT_Pinger_K_Specification_ru.md commit=d45493345be17c4dcb09c4ce28b1cec376e7fa94 date=2025-02-26 -->
