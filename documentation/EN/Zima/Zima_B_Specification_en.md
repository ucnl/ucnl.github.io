| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/def_zima_b_ant.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-B** - **Zima USBL** base station <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Operating range up to 3000<sup>[1](#footnote1)</sup> m**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Subscribers code division - up to 23 code channels**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented technology of simultaneous positioning**
* **Patented monoblock design**
* **Built-in depth/temperature sensor**

## DESCRIPTION

**Zima-B** - direction-finding station of the ultrashort-baseline system [Zima USBL](Zima_DataBrief_en.md).

The device uses a fixed-length signal with code division to provide direction and distance estimation, as well as transmitting telecontrol 
commands to the responder-beacons [Zima-R](Zima_R_Specification_en.md) and receiving telemetry data from them.

When using an external **GNSS**-receiver  and a Compass, the device calculates the absolute coordinates of the responder-beacons.
Sequential transmission of up to 32 control commands for 23 transponder beacons is provided.
 
An ideal solution for determining the direction and distance to **ROVs**, **AUVs** and **divers**.

Extremely small size, low power consumption and ease of use make the [Zima USBL](Zima_DataBrief_en.md) system an ideal solution for 
working with autonomous and remote-controlled devices, as well as determining the relative location of divers.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 х 128 mm |
| WEIGHT<sup>[2](#footnote2)</sup> (dry) | 0.44 kg |
| DEPTH RATING | 300 m |
| MAX. OPERATING RANGE<sup>[1](#footnote1)</sup> |	3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote3)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY | 0.3 m |
| MAX. TILT COMPENSATED BY THE BUILT-IN INCLINOMETER RELATED TO VERTICAL AXIS (pitch/roll) | +/- 30° |
| WORKING VERTICAL ANGLES (RELATIVE TO HORIZONTAL PLANE)<sup>[3](#footnote3)</sup> | +/-30° |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| BATTERY LIFE<sup>[4](#footnote4)</sup> (WHEN SUPPLIED FROM [BAT&LINK BOX](Bat_n_link_box_Specification_en.md)) | 8 hours |
| INTERFACE | USB(COM) 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[5](#footnote5)</sup> | 10 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Withoud cable and interface converter.  
<a name="footnote3"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote4"><sup>4</sup></a> Considering 1 request in 3 seconds.  
<a name="footnote5"><sup>5</sup></a> With additional cable and interface converter [Bat&Link Box](Bat_n_link_box_Specification_en.md). Can be increased by a request up to 20 m.  

