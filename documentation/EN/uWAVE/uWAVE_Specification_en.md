[Main](/../../) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **Device specification: uWave**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/RT_1_332820_1.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** underwater acoustic modem <br/> Device specifications |

## KEY FEATURES

* **Extremely small size and weight**
* **Can be applied in underwater wireless sensor networks**
* **Reliable data transmission with 78 bit/s**
* **Operating range up to 1000<sup>[1](#footnote1),[2](#footnote2)</sup> m**
* **Subscribers code division**
* **Propagation time measurement**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/6 W**
* **Open configuration protocol**
* **Built-in depth/temperature sensor**
* **Patented monoblock design**

## DESCRIPTION

**uWave** is the world smallest<sup>[3](#footnote3)</sup> underwater acoustic digital modem, which allows to communicate 
up to 20 subscribers in area 1000 x 1000 meters with both transparent channel and predefined code messages/telemetry transmission.
Extremely small size, low power consumption and simplicity of usage make **uWave** an ideal solution for AUV control as well as data 
transmission, where dimensions and weight are the bottleneck.

The device allows:
* transfer data in transparent channel mode - just connect the modem to a serial port
* request the depth, temperature, supply voltage of remote modems with simultaneous measurement of the signal propagation time (and hence the distance to them)
* transfer data in batch mode with guaranteed delivery (ALO - At-least-once) and delivery notification
* measure immersion depth, water temperature, and supply voltage of local modem.

Devices from [uWave family](uWAVE_Family_en.md) use a simple open [NMEA-like configuration protocol](uWAVE_Protocol_Specification_en.md), and the supplied open-source libraries [**uWaveLib**](https://github.com/ucnl/uWAVELib) (.NET) and [**uWave ALib**](https://github.com/ucnl/uWAVE_ALib) (Arduino) allows for the fastest and easiest integration of devices into custom solutions.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER                               | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h)                      | 41 x 45 mm |
| WEIGHT (dry)                            | 0.16 kg |
| DEPTH RATING                            | 300 m |
| MAX OPERATING RANGE<sup>[1](#footnote1),[2](#footnote2)</sup> | 1000 m |
| PAYLOAD DATA RATE                       | 78 bit/s |
| POWER CONSUMPTION Rx/Tx                 | 0.33/6 W |
| POWER SUPPLY<sup>[4](#footnote4),[7](#footnote7)</sup> | 5 .. 12 V |
| DATA LINES VOLTAGE                      | 0 .. 3.3 V |
| DATA LINES OUTPUT IMPEDANCE             | 1 kOhm |
| FREQUENCY BAND                          | 10 .. 30 kHz |
| ACOUSTIC SOURCE LEVEL (IN BAND)         | 169 dB re 1 uPa @ 1 m |
| BIT ERROR RATE                          | 10<sup>-6</sup> |
| SNR<sup>[5](#footnote5)</sup>           | -2 dB |
| MAX RELATIVE VELOCITY                   | +/- 1 m/s |
| RATED START-UP TIME                     | 100 ms |
| OPERATING TEMPERATURE RANGE             | -5 .. 50 °C |
| INTERFACE<sup>[6](#footnote6)</sup>     | UART 9600 bit/s |
| CONFIGURATION PROTOCOL                  | NMEA0183 [PUWV](uWAVE_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[6](#footnote6)</sup>  | 0.5 m |
| CABLE DIAMETER | 5 mm |
| SUBSCRIBERS CODE DIVISION               | 20 code channels |
| COMMAND MODE                            | 16 predefined messages (9 for user applications) |
| PACKET MODE                             | 254 subscribers with an acknowledgement; broadcasting; packet size up to 64 bytes |
| TX BUFFER SIZE                          | 127 bytes |
| PROPAGATION TIME MEASUREMENT RESOLUTION | 0.0001 sec |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Based on the test results in a shallow water body, using the **uWave** devices, the practical communication range **1092 m** was obtained.  
<a name="footnote3"><sup>3</sup></a> According to open sources, June 2021.  
<a name="footnote4"><sup>4</sup></a> Maximum output power can be achieved with 12V power supply.  
<a name="footnote5"><sup>5</sup></a> This value is obtained without the presence of the multipath effect.  
<a name="footnote6"><sup>6</sup></a> Сan be changed by special request.  
<a name="footnote7"><sup>7</sup></a> The device has built-in overvoltage protection of the amplifying circuit. At voltages over 12.8-13 volts, the device does not turn on the power amplifier, i.e. does not allow data transfer.  
<a name="footnote8"><sup>8</sup></a> Considering the given value, the resolution when measuring the distance, considering the speed of sound 1500 m/s is 0.15 m  
<div style="page-break-after: always;"></div>
