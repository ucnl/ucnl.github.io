| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/def_zima_b_ant.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-B** - base station **Zima USBL** <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Operating range up to 3000 m**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Subscribers code division - up to 23 code channels**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented technology of simultaneous positioning**
* **Built-in depth/temperature sensor**

## DESCRIPTION

** Zima-B ** - direction-finding station of the ultrashort-baseline system [Zima USBL](Zima_DataBrief_ru.md).

The device uses a fixed-length signal with code division to provide direction and distance estimation, as well as transmitting telecontrol 
commands to the responder-beacons [Zima-R] (Zima_R_Specification_ru.md) and receiving telemetry data from them.

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
| WEIGHT (dry) | 0.44 kg |
| DEPTH RATING | 300 m |
| MAX OPERATING RANGE |	3000<sup>[1](#footnote1)</sup> m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[2](#footnote2)</sup> | 1° |
| МАКСИМАЛЬНЫЙ КОМПЕНСИРУЕМЫЙ ВСТРОЕННЫМ ИНКЛИНОМЕТРОМ НАКЛОН ПРИБОРА ОТНОСИТЕЛЬНО ВЕРТИКАЛИ (КРЕН/ДИФФЕРЕНТ) | +/- 30° |
| WORKING VERTICAL ANGLES (RELATIVE TO HORIZONTAL PLANE)<sup>[2](#footnote2)</sup> | +/-30° |
| BANDWIDTH | 6 .. 18 kHz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED START-UP TIME | 100 msec |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| ВРЕМЯ АВТОНОМНОЙ РАБОТЫ<sup>[3](#footnote3)</sup>WHEN SUPPLIED FROM [BAT&LINK BOX](Bat_n_link_box_Specification_en.md) | 8 hours |
| INTERFACE | USB (COM) 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 10 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
  
________________
<a name="footnote1"><sup>1</sup></a> Withoud cable and interface converter  
<a name="footnote2"><sup>2</sup></a> Значение получено без учета эффекта многолучевого распространения в лабораторном статическом эксперименте  
<a name="footnote3"><sup>3</sup></a> Considering 1 request in 3 seconds  
<a name="footnote4"><sup>4</sup></a> С учетом преобразователя интерфейса и удлиняющего кабеля до прибора [Bat&Link Box](Bat_n_link_box_Specification_ru.md). Опционально возможно увеличение до 20 метров  

