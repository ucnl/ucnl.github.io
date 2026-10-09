[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **RedLine: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedLine** - Underwater acoustic modem <br/> Device specification |

<div style="page-break-after: always;"></div>

### KEY FEATURES
* **Communication range up to 8000<sup>[1](#footnote1)</sup> m**
* **Reliable data transmission at 80 bit/s**
* **Extremely small size and weight**
* **Can be used in wireless underwater sensor networks**
* **Code division multiple access**
* **Highly reliable digital underwater acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/10 W**
* **Open communication protocol**
* **Patented<sup>[*](#footnote_a1)</sup> monoblock design**

### DESCRIPTION
**RedLine** - a family of wireless underwater digital communication modems that implement a transparent transmission channel.

**RedLine** modems offer an unrivaled balance of power consumption, dimensions, reliability and transmission range.
The monoblock housing shared with **RedNode** devices allows the use of standard solutions for integration.

Small size, low power consumption and ease of use make **RedLine** an ideal solution for small-sized ROVs/AUVs as well
as for larger devices.

The code division multiple access function enables the most efficient data transmission for multiple devices.

_________
<a name="footnote_a1"><sup>*</sup></a> Patent RU2659299C1.  

<div style="page-break-after: always;"></div>

### TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry) | 0.36 kg |
| MAXIMUM DEPTH | 400 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 8000 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 170 dB re 1 μPa @ 1 m |
| DATA RATE | 80 bit/s |
| POWER CONSUMPTION Rx/Tx | 0.33/10 W |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BANDWIDTH | 5 .. 15 kHz |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2)</sup> | -6 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 3 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[3](#footnote3)</sup> | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PTNT](RedLINE_Protocol_Specifications_en.md) |
| CABLE LENGTH<sup>[3](#footnote3)</sup> | 0.5 m |
| MINIMUM PACKET SIZE FOR TRANSMISSION | 7 bytes |
| TRANSMITTER BUFFER SIZE | 256 bytes |
| MULTIPLE ACCESS SCHEME | 20 code channels |

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> This value was obtained in a static laboratory experiment without accounting for the effect of multipath propagation.  
<a name="footnote3"><sup>3</sup></a> The value can be changed on request.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RedLINE/RedLine_Specification_ru.md commit=59685e10c6017fc5a066b1f06ecab29b8a7e3e03 date=2022-04-13 -->
