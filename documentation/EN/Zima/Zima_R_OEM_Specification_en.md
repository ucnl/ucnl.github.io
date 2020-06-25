| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/zima_r_oem.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-R OEM** - **Zima USBL** responder-beacon <br/> Device specification |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **Extremely small size and weight**
* **Operating range up to 3000<sup>[1](#footnote1)</sup> m**
* **For depths up to 1000<sup>[2](#footnote2)</sup> m**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Subscribers code division - up to 23 code channels**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented technology of simultaneous positioning**

## DESCRIPTION

**Zima-R OEM** is the [Zima USBL](Zima_DataBrief_ru.md) ultrashort base-line navigation system responder-beacon.

The device is designed to receive telecontrol commands from the [Zima-B](Zima_B_Specification_en.md) base station - the direction-finding station, transmitting telemetry information to the [Zima-B](Zima_B_Specification_en.md) base station - the direction-finding base station and to determine the direction to the responder-beacon (for the base station) and the base station (for responder-beacon) and mutual estimation of distance.

The device is supplied in the form of an assembly of printed circuit boards for installation inside the user's normobaric enclosure and is equipped with a transducer with **1000** meters depth rating.

Depth value should be set from a user system.

Extremely small size, low power consumption and ease of use make the [Zima USBL](Zima_DataBrief_ru.md) system an ideal solution for working with autonomous and telecontrolled devices.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h, PCBs) | Ф52 х 55 mm |
| РАЗМЕР (Ф х h, transducer) | Ф64 х 61 mm |
| WEIGHT (PCBs) | 0.12 kg |
| WEIGHT (transducer) | 0.35 kg |
| DEPTH RATING<sup>[2](#footnote2)</sup> | 1000 m |
| MAX. OPERATING RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| BANDWIDTH | 6 .. 18 kHz |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| SUPPLY VOLTAGE | 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | UART 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 1 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote3)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY<sup>[3](#footnote3)</sup> | 0.3 m |
  
________________
<a name="footnote1"><sup>1</sup></a> Without the presence of a multipath effect. A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.   
<a name="footnote2"><sup>2</sup></a> For transducer.  
<a name="footnote3"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote4"><sup>4</sup></a> Can be changed by a special request.  
