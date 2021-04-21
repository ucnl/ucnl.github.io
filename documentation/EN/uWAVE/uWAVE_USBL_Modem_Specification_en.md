| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_zima_b_ant.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE USBL Modem** underwater acoustic modem <br/> Device specifications |

## KEY FEATURES

* **Extremely small size and weight**
* **Simultaneous data transmission & USBL navigation**
* **Reliable data transmission with 78 bit/s**
* **Operating range up to 3000<sup>[1](#footnote1),[2](#footnote2)</sup> m**
* **Subscribers code division**
* **Propagation time measurement**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Open & easy interfacing protocol**
* **Built-in depth/temperature sensor**
* **Patented monoblock design**

## DESCRIPTION

**uWAVE USBL Modem** - a device that combines the functions of transmitting data through a underwater acoustic channel and a navigation 
system on an ultra-short base.

Using **uWAVE USBL Modems**, the user can:
* transfer arbitrary user data between **uWAVE USBL Modem**, [uWAVE Max](uWAVE_Max_Specification_en.md) and [uWAVE modems](uWAVE_Specification_en.md) in any combination with the simultaneous estimation of the horizontal angle of arrival;
* estimate the location of the **uWAVE USBL Modem**, [uWAVE Max](uWAVE_Max_Specification_en.md) and [uWAVE modems](uWAVE_Specification_en.md) in command mode by slant range and horizontal angle of arrival;
* transmit up to 9 short code telecontrol user commands;
* request from remote modems **uWAVE USBL Modem**, [uWAVE Max](uWAVE_Max_Specification_en.md) and [uWAVE modems](uWAVE_Specification_en.md) their depth, temperature and voltage;
* measure own depth, temperature and voltage;

**uWAVE** family devices use a simple open NMEA-like configuration [protocol](uWAVE_Protocol_Specification_en.md), and the supplied open-source [**uWAVELib**](https://github.com/ucnl/uWAVELib) library allows for the fastest and easiest integration of devices into user solutions.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 х 128 mm |
| WEIGHT (dry) | 0.44 kg |
| DEPTH RATING | 300 m |
| MAX. OPERATING RANGE<sup>[1](#footnote1),[2](#footnote2)</sup> |	3000 m |
| PAYLOAD DATA RATE |	78 bit/s |
| POWER CONSUMPTION Rx/Tx |	0.33/25 W |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.) |	2° |
| SUPPLY VOLTAGE | 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| FREQUENCY BAND | 10 .. 30 kHz |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -2 dB |
| MAX RELATIVE VELOCITY | +/- 1 m/s |
| RATED STARTUP TIME | 100 msec |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[4](#footnote4)</sup> | UART 9600 bit/s |
| INTERFACING PROTOCOL | NMEA0183 [PUWV](uWAVE_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 1 m |
| SUBSCRIBERS CODE DIVISION | 20 code channels |
| COMMAND MODE | 16 predefined code messages (9 for user applications) |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> While working with **uWAVE USBL Modem** or [uWAVE Max](uWAVE_Max_Specification_en.md). Max. operating range with [uWAVE](uWAVE_Specification_en.md) modems is 1000 m.  
<a name="footnote3"><sup>3</sup></a> This value is obtained without the presence of the multipath effect.  
<a name="footnote4"><sup>4</sup></a> Can be changed by the special request.  
