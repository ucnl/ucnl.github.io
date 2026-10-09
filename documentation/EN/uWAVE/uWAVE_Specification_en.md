[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave: Device specification**

<details>
  <summary><b>ℹ Recommendations for printing / saving as PDF</b></summary>
  <br>
  <ol>
    <li>Press <b>Ctrl+P</b> (macOS: <b>Cmd+P</b>)</li>
    <li>Select <b>"Save as PDF"</b> (Microsoft Print to PDF) as the printer</li>
    <li>In <b>"Pages"</b>, enter a range that excludes the first and the last page</li>
    <li>Disable <b>headers and footers</b> (title, URL, page numbers)</li>
    <li>In <b>Chrome/Edge</b>: More settings → "Margins" → <b>None</b> | in <b>Firefox</b>: "Margins & Header/Footer" → <b>None</b></li>
    <li>Click <b>Print</b> and choose where to save the PDF</li>
  </ol>
</details>

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/RT_1_332820_1.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** - underwater acoustic modem <br/> Device specification |

<div style="page-break-after: always;"></div>

## KEY FEATURES

* **Extremely small size and weight**
* **Can be used in underwater wireless sensor networks**
* **Communication range up to 1000<sup>[1](#footnote1),[*](#footnote_a1)</sup> m**
* **Reliable data transmission at speeds up to 634<sup>[2](#footnote2)</sup> bit/s**
* **Code division multiple access**
* **Signal propagation time measurement**
* **Highly reliable digital underwater acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/6 W**
* **Open interfacing protocol**
* **Built-in pressure/temperature sensor**
* **Packet mode with guaranteed delivery (ALO - At-least-once)**
* **Patented<sup>[**](#footnote_a2)</sup> monoblock design**

<div style="page-break-after: always;"></div>

## DESCRIPTION

**uWave** is the world's smallest<sup>[***](#footnote_a3)</sup> underwater acoustic modem. The device provides underwater acoustic 
digital communication between 254 subscribers in water areas of 1000 x 1000 meters, using code mode, transparent channel mode or packet mode with logical addressing and guaranteed delivery. 
Extremely small size, low power consumption and ease of use make the [uWave family](uWAVE_Family_en.md) modems an ideal solution for controlling autonomous underwater devices and transferring data in applications sensitive to size and weight.

The device allows you to:
* transmit data in transparent channel mode - just connect the modem to the serial port
* request the depth, temperature and supply voltage of remote modems [of the uWave family](uWAVE_Family_en.md) with simultaneous measurement of the signal propagation time (and hence the distance to them)
* transmit data in packet mode with guaranteed delivery (ALO - At-least-once) and delivery notification
* measure local immersion depth, water temperature and supply voltage.

[uWave family](uWAVE_Family_en.md) devices use a simple [NMEA-like protocol](uWAVE_Protocol_Specification_en.md) for configuration, and the supplied open-source libraries [**uWaveLib**](https://github.com/ucnl/uWAVELib) (.NET) and [**uWave ALibs**](https://github.com/ucnl/UCNL_ALibs) (Arduino) make the integration of the modems into custom solutions as simple and fast as possible.

_________
<a name="footnote_a1"><sup>\*</sup></a> According to the results of tests in a shallow water body, a practical communication range of **1092 m** was achieved using **uWave** devices.  
<a name="footnote_a2"><sup>\*\*</sup></a> *Patents RU2659299C1, US11257472B2*.  
<a name="footnote_a3"><sup>\*\*\*</sup></a> *According to open sources as of November 2024*.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 41 x 45 mm |
| WEIGHT (dry) | 0.16 kg |
| MAXIMUM DEPTH | 300 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 1000 m |
| DATA RATE<sup>[2](#footnote2)</sup> | 78/156/314/634 bit/s |
| POWER CONSUMPTION Rx/Tx | 0.33/6 W |
| SUPPLY VOLTAGE<sup>[3](#footnote3),[4](#footnote4)</sup> | 5 .. 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| DATA LINE OUTPUT IMPEDANCE | 1 kΩ |
| CARRIER | 20050 Hz |
| MAXIMUM ACOUSTIC SOURCE LEVEL (in band) | 169 dB re 1 μPa @ 1 m |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[5](#footnote5)</sup> | -2 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 1 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[6](#footnote6)</sup> | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PUWV](uWAVE_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[6](#footnote6)</sup> | 0.5 m |
| CABLE DIAMETER | 5 mm |
| MULTIPLE ACCESS SCHEME<sup>[2](#footnote2)</sup> | 20 code channels |
| TRANSMITTER BUFFER SIZE | 127 bytes |
| COMMAND MODE| 16 preset messages (9 for user applications) |
| SIGNAL PROPAGATION TIME MEASUREMENT RESOLUTION<sup>[7](#footnote7)</sup> | 0.0001 s |
| PACKET MODE | 254 addresses with delivery notification, broadcast messages, packet size up to 64 bytes |
| DEPTH SENSOR RESOLUTION (local)<sup>[8](#footnote8)</sup> | 0.01 m |
| DEPTH SENSOR RESOLUTION (remote)<sup>[8](#footnote8)</sup> | 0.1 m |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the level of underwater acoustic noise. In the 78 bit/s data rate mode.  
<a name="footnote2"><sup>2</sup></a> By default, the devices operate in the **78 bit/s** data rate mode, which provides the maximum range, communication reliability and the maximum number of code channels. Different data rate modes are not compatible with each other. Switching the modem to another data rate mode is done by [replacing its firmware](uWAVE_FW_Updating_en.md).  
<a name="footnote3"><sup>3</sup></a> The maximum output power is achieved when the modem is supplied with 12 V.  
<a name="footnote4"><sup>4</sup></a> The device has built-in overvoltage protection of the amplifier circuit. At voltages above 12.8-13 volts, the device does not turn on the power amplifier, i.e. it does not allow data transmission.  
<a name="footnote5"><sup>5</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
<a name="footnote6"><sup>6</sup></a> The value can be changed on request.  
<a name="footnote7"><sup>7</sup></a> Given this value, the resolution when measuring distance, taking into account the speed of sound of 1500 m/s, is 0.15 m.  
<a name="footnote8"><sup>8</sup></a> A modem equipped with a depth sensor can transmit depth readings *locally* - via the cable, to the control system, and *remotely* - upon request from another modem.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uWAVE/uWAVE_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
