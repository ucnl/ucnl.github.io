| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE Max** underwater acoustic modem specifications |

## KEY FEATURES

* **Extremely small size and weight**
* **Reliable data transmission with 78 bit/s**
* **Operating range up to 3000<sup>[1](#footnote1),[2](#footnote2)</sup> m**
* **Subscribers code division**
* **Propagation time measurement**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Open & easy interfacing protocol**
* **Built-in depth/temperature sensor**

## DESCRIPTION

Using **uWAVE Max**, the user can:

* transfer arbitrary user data between **uWAVE USBL Modem**, **uWAVE Max** and **uWAVE modems** in any combination;
* transmit up to 9 short code telecontrol user commands;
* request from remote modems **uWAVE USBL Modem**, **uWAVE Max** and **uWAVE** their depth, temperature and voltage;
* measure own depth, temperature and voltage;

**uWAVE** family devices use a simple open NMEA-like configuration protocol, and the supplied open-source [uWAVELib](https://github.com/ucnl/uWAVELib) library allows 
the fastest and easiest integration of devices into user solutions.

## TECHNICAL SPECIFICATIONS

| PARAMETER                              | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h)                     | 64 x 62 mm |
| WEIGHT (dry)                           | 0.36 kg |
| DEPTH RATING                           | 300 m |
| MAX OPERATING RANGE<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000 m |
| PAYLOAD DATA RATE                      | 78 bit/s |
| POWER CONSUMPTION Rx/Tx                | 0.33/25 W |
| POWER SUPPLY                           | 12 V |
| DATA LINES VOLTAGE                     | 0 .. 3.3 V |
| FREQUENCY BAND                         | 10 .. 30 kHz |
| BIT ERROR RATE                         | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup></sup>    | -2 dB |
| MAX RELATIVE VELOCITY                  | +/- 1 m/s |
| RATED START-UP TIME                    | 100 ms |
| OPERATING TEMPERATURE RANGE            | -5 .. 50 °C |
| INTERFACE<sup>[4](#footnote4)</sup>    | UART 9600 bit/s |
| CONFIGURATION PROTOCOL                 | NMEA 0183 PUWV |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 0.5 m |
| SUBSCRIBERS CODE DIVISION              | 20 code channels |
| COMMAND MODE                           | 16 predefined messages (9 for user applications) |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> While working with [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md) or **uWAVE Max**. Max operating range with [uWAVE](uWAVE_Specification_en.md) modems is 1000 m.  
<a name="footnote3"><sup>3</sup></a> This value is obtained without the presence of the multipath effect  
<a name="footnote4"><sup>4</sup></a> Can be changed by the special request  
