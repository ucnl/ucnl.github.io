| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/utro_pcb_rt_1_524525_1_2.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE Max OEM** - Underwater acoustic modem <br/> Device specifications |

## KEY FEATURES

* **Extremely small dimensions and weight**
* **Reliable data transmission at 78 bps**
* **Communication range up to 3000<sup>[1](#footnote1), [2](#footnote2)</sup> m**
* **Code division of subscribers**
* **Measurement of signal propagation time**
* **Highly reliable digital broadband acoustic communication technology**
* **Low power consumption (Rx/Tx) 0.33/15 W**
* **Open pairing protocol**
* **Batch transmission with guaranteed delivery and acknowledgement**

## DESCRIPTION

**uWAVE Max OEM** is based on **UTRO** platform and is supplied as a printed circuit board module with [RT-1.524525-1](/documentation/EN/Transducers/RT-1.524525-1_specification_en.md) transducer.

With the **uWAVE Max OEM** modems, the user can:
* transfer arbitrary digital data between devices [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_ru.md), **uWAVE Max** and [uWAVE](uWAVE_Specification_ru.md) in any combination;
* transmit up to 9 code user commands of telecontrol;
* request from remote devices [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_ru.md), **uWAVE Max** and [uWAVE](uWAVE_Specification_ru.md) their depth, temperature and supply voltage;
* transfer data in batch mode with acknowledgment (ALO - At-least-once)
* measure its own supply voltage;

Devices from [uWAVE family](uWAVE_Family_en.md) use a simple open [NMEA-like configuration protocol](uWAVE_Protocol_Specification_en.md), and the supplied open-source library
[**uWAVELib**](https://github.com/ucnl/uWAVELib) allows for the fastest and easiest
integration of devices into custom solutions.

Differences from the basic version [uWAVE](/documentation/EN/uWAVE/uWAVE_Specification_en.md):
* Increased to 3000<sup>[1](#footnote1), [2](#footnote2)</sup> m maximum communication range
* OEM
* No built-in depth/temperature sensor


## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (PCB, l х w х h) | 80 х 43 х 29 mm |
| WEIGHT | 54 g |
| DIMENSIONS (Transducer, Ф х h) | 64 x 62 mm |
| WEIGHT (Transducer, dry) | 360 g |
| DEPTH RATING (Transducer) | 400 m |
| MAX OPERATING RANGE<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000 м |
| PAYLOAD DATA RATE | 78 bps |
| POWER CONSUMPTION Rx/Tx | 0.33/15 W |
| POWER SUPPLY | 5 .. 13 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| FREQUENCY BAND | 10 .. 30 kHz |
| ACOUSTIC SOURCE LEVEL (IN BAND) | 175 dB re 1 uPa @ 1 m |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -2 dB |
| MAX RELATIVE VELOCITY | +/- 1 m/s |
| RATED START-UP TIME | 100 msec |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[4](#footnote4)</sup> | UART 9600 bps |
| CONFIGURATION PROTOCOL | NMEA 0183 [PUWV](uWAVE_Protocol_Specification_en.md) |
| TRANSDUCER CABLE LENGTH<sup>[4](#footnote4)</sup> | 1 m |
| SUBSCRIBERS CODE DIVISION | 20 code channels |
| COMMAND MODE | 16 predefined messages (9 for user applications) |
| PACKET MODE | 254 subscribers with an acknowledgement; broadcasting; packet size up to 64 bytes |
| TX BUFFER SIZE | 127 bytes |
| PROPAGATION TIME MEASUREMENT RESOLUTION | 0.0001 sec |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> When working with another **uWAVE Max/uWAVE Max OEM** or when working with [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md). The maximum communication range with standard modems [uWAVE](uWAVE_Specification_en.md) is 1000 meters.  
<a name="footnote3"><sup>3</sup></a> This value is obtained without the presence of the multipath effect.  
<a name="footnote4"><sup>4</sup></a> Сan be changed by special request.  
