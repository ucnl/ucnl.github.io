| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima_r.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-R** - **Zima USBL** responder-beacon <br/> Device specification |

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

**Zima-R** - responder-beacon of ultrashort baseline underwater tracking system [Zima USBL](Zima_DataBrief_en.md).  

The device is designed to receive telecontrol commands from the base station [Zima-B](Zima_B_Specification_en.md) - the base station for direction finding and to determine the direction to the responder-beacon (for the base station) and to the base station (for responder-beacons) and the mutual
distance estimation.

The device can be either stand-alone (with an additional battery pack) or paired with the carrier vehicle.
In this case, telecontrol commands, the distance to the base station and the azimuth angle to the base station can be transmitted to the carrier vehicle.

Extremely small size, low power consumption and ease of use make the [Zima USBL](Zima_DataBrief_en.md) tracking system an ideal solution for working with autonomous and remotely operated underwater vehicles as well as determining the location of divers.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 x 62 mm |
| WEIGHT<sup>[2](#footnote2)</sup> (dry) | 0.3 kg |
| DEPTH RATING | 300 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAX. OPERATING RANGE<sup>[1](#footnote1)</sup> |	3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| SUPPLY VOLTAGE | 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | USB(COM) 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 1 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote3)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY<sup>[3](#footnote3)</sup> | 0.3 m |

<!-- | BANDWIDTH | 6 .. 18 kHz | -->
  
________________
<a name="footnote1"><sup>1</sup></a> Without the presence of a multipath effect. A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.   
<a name="footnote2"><sup>2</sup></a> Without a battery pack. Standard battery pack ф50х165 mm, 0.58 kg, 2.9 A\*h 12 V. 
Battery life with standard battery pack - up to 70 hours in receiving mode, up to 8 hours with 1 request in 3 seconds schedule.  
<a name="footnote3"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote4"><sup>4</sup></a> Can be changed by a special request.  
