[Main](/../../) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **Device specification: uWave Max OEM**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/utro_pcb_rt_1_524525_1_2.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave Max OEM** - Underwater acoustic modem <br/> Device specifications |

## KEY FEATURES

* **Extremely small size and weight**
* **Can be used in underwater wireless sensors networks**
* **Communication range is up to 3000<sup>[1](#footnote1) m**
* **Reliable data transmission on speed up to **634**<sup>[2](#footnote2)</sup> bit/s**
* **Code subscribers division**
* **Signal propagation time measurement feature**
* **State of the art digital broadband underwater acoustic communication technology**
* **Low power consumption (Rx/Tx) 0.33/15 W**
* **Easy and open interfacing protocol**
* **Packet mode with guaranteed delivery (ALO - At-least-once)**

## DESCRIPTION

**uWave Max OEM** is based on **UTRO** platform and is supplied as a printed circuit board module with [RT-1.524525-1](/documentation/EN/Transducers/RT-1.524525-1_specification_en.md) transducer.

The device allows to provide hydroacoustic digital communication between 254 subscribers in water areas of 3000 x 3000 meters using code mode, transparent channel mode or packet mode with logical addressing and guaranteed delivery.
Extremely small size, low power consumption and ease of use make the [uWave family](uWAVE_Family_en.md) modems the ideal solution for autonomous underwater device control and data transmission in size and weight sensitive applications.

The device allows:
* transmit data in transparent channel mode - just connect the modem to the serial port
* request depth, temperature, supply voltage of remote modems [of the uWave family](uWAVE_Family_en.md) with simultaneous measurement of the signal propagation time (and hence the distance to them)
* transfer data in packet mode with guaranteed delivery (ALO - At-least-once) and delivery notification.

[uWave family](uWAVE_Family_en.md) devices use a simple [NMEA-like protocol](uWAVE_Protocol_Specification_en.md) settings, and the supplied open-source libraries [**uWaveLib**](https://github.com/ucnl/uWAVELib) (.NET) and [**uWave ALibs**](https://github.com/ucnl/UCNL_ALibs) (Arduino) allow you to make the integration of modems into custom solutions as simple and fast as possible.

Differences from the basic version [uWave](/documentation/EN/uWAVE/uWAVE_Specification_en.md):
* Increased to 3000<sup>[1](#footnote1), [3](#footnote3)</sup> m maximum communication range
* OEM
* No built-in depth/temperature sensor

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (PCB, l х w х h) | 80 х 43 х 29 mm |
| WEIGHT | 54 g |
| DIMENSIONS (Transducer, Ф х h) | 64 x 62 mm |
| WEIGHT (Transducer, dry) | 360 g |
| DEPTH RATING (Transducer) | 400 m |
| MAX. ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| PAYLOAD DATA RATE<sup>[2](#footnote2)</sup> | 78/156/314/634 bps |
| POWER CONSUMPTION Rx/Tx | 0.33/15 W |
| SUPPLY VOLTAGE<sup>[3](#footnote3),[4](#footnote4)</sup> | 5 .. 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| DATA LINES OUTPUT IMPEDANCE | 1 kOhm |
| BANDWIDTH | 10 .. 30 kHz |
| MAX. ACOUSTIC SOURCE LEVEL (in band) | 180 dB re 1 uPa @ 1 m |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[5](#footnote5)</sup> | -2 дБ |
| MAX RELATIVE VELOCITY | +/- 1 m/s |
| RATED STARTUP TIME | 100 msec |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[6](#footnote6)</sup> | UART 9600 bps |
| COMMUNICATION PROTOCOL | NMEA 0183 [PUWV](uWAVE_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[6](#footnote6)</sup> | 0.5 m |
| CABLE DIAMETER | 5 mm |
| SUBSCRIBERS DIVISION<sup>[2](#footnote2)</sup> | up to 20 code channels |
| TRANSMITTER BUFFER SIZE | 128 bytes |
| COMMAND MODE | 16 preset messages (9 for user commands) |
| SIGNAL PROPAGATION TIME MEASUREMENT RESOLUTION<sup>[7](#footnote7)</sup> | 0.0001 sec |
| PACKET MODE | 254 addresses, broadcast messages, packet size is up to 64 bytes |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level. In 78 bps speed mode.  
<a name="footnote2"><sup>2</sup></a> **78 bps** speed mode used as a default. This mode provide the maximum noise and multipath immunity, reliability and number of code channels. Different speed modes are not compatible, and can be set by [reflashing](uWAVE_FW_Updating_en.md) the modem's firmware.  
<a name="footnote3"><sup>3</sup></a> The maximum output power can be achieved with 12 V supply voltage only.  
<a name="footnote4"><sup>4</sup></a> The device has a built-in overvoltage protection of the amplifying circuit. At voltages above 12.8-13 volts, the device does not turn on the power amplifier, i.e. it does not allow data transfer.  
<a name="footnote5"><sup>5</sup></a> The value was obtained without taking into account the effect of multipath propagation in a laboratory stationary experiment.  
<a name="footnote6"><sup>6</sup></a> Can be changed by a special request.  
<a name="footnote7"><sup>7</sup></a> Given this value, the resolution when measuring distance, taking into account the sound speed of 1500 m/s, is 0.15 m.  

<div style="page-break-after: always;"></div>
