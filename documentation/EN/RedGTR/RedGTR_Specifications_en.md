[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **RedGTR: Device specification**

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedGTR** - Underwater acoustic code communication modem <br/> Device specification |

## KEY FEATURES

* **Communication range up to 8000<sup>[1](#footnote1)</sup> m**
* **Extremely small size and weight**
* **Can be used in wireless underwater sensor networks**
* **Code division multiple access**
* **Highly reliable digital underwater acoustic communication**
* **40 code commands / 25 subscribers**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Open communication protocol**
* **Built-in depth/temperature sensor**


## DESCRIPTION

**RedGTR** - underwater acoustic code communication modem.

The device uses a fixed-length signal with code division to enable operation of a point-to-point network consisting of 25 devices,
located in the same body of water.

**RedGTR** modems support up to 25 addresses - isolating code channels. Each modem can receive 40 different code commands
with a very high level of guaranteed reliability.
 
An ideal solution for controlling underwater actuators or creating specialized acoustic releases.

Extremely small size, low power consumption, ease of use and high reliability make **RedGTR** code modems
an ideal solution for controlling autonomous underwater devices.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry) | 0.36 kg |
| MAXIMUM DEPTH<sup>[2](#footnote2)</sup> | 300 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 8000 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 170 dB re 1 μPa @ 1 m |
| POWER CONSUMPTION Rx/Tx | 0.33/25 W |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BANDWIDTH | 5 .. 15 kHz |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -6 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 3 m/s |
| STARTUP TIME | 100 ms |
| SIGNAL DURATION | 400 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[4](#footnote4)</sup> | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PTNT](RedGTR_Protocol_Specifications_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 0.5 m |
| MULTIPLE ACCESS SCHEME | 25 isolating code channels |
| NUMBER OF DISTINCT CODE MESSAGES | 40 |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in sound energy intensity, attenuation in the medium and the underwater acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> The device can be supplied without a built-in pressure sensor on request. In this case, the maximum immersion depth is 400 m.  
<a name="footnote3"><sup>3</sup></a> The value was obtained in a static laboratory experiment without accounting for the effect of multipath propagation.  
<a name="footnote4"><sup>4</sup></a> The value can be changed on request.  

<!-- docs-sync: source=documentation/RU/RedGTR/RedGTR_Specifications_ru.md commit=98ab94fc9151c38fd3a9fff9091820add1f3ec77 date=2021-04-21 -->
