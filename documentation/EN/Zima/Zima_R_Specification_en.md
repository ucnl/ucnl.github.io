[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima-R: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima_r.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-R** - **Zima USBL** responder-beacon <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Communication range up to 3000<sup>[1](#footnote1)</sup> m**
* **Highly reliable digital underwater acoustic communication resistant to multipath propagation**
* **Code division multiple access - up to 23 isolating addresses**
* **Highly reliable digital underwater acoustic communication**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented<sup>[*](#footnote_a1)</sup> simultaneous navigation technology**
* **Built-in pressure/temperature sensor**
* **Patented<sup>[**](#footnote_a1)</sup> monoblock design**

## DESCRIPTION

**Zima-R** - responder-beacon of the ultra-short baseline navigation system [Zima USBL](Zima_DataBrief_en.md).  

The device is designed to receive remote control commands from the base station [Zima-B](Zima_B_Specification_en.md) - direction-finding base station, to transmit telemetry information to the base station [Zima-B](Zima_B_Specification_en.md) - direction-finding base station, and to determine the direction, both to the responder-beacon (for the base station) and to the base station (for the responder-beacon), and the mutual 
distance.  

The device can be either standalone (with an additional battery pack) or interfaced with the carrier for both power and data. 
In this case, remote control commands, the distance to the base station and the azimuth angle to the base station can be transmitted to the carrier.  

Extremely small size, low power consumption and ease of use make the direction-finding system [Zima USBL](Zima_DataBrief_en.md) an ideal solution for working with autonomous and remotely controlled vehicles, as well as for determining the relative position of divers.

________________
<a name="footnote_a1"><sup>*</sup></a> Patent RU156897U1.  
<a name="footnote_a2"><sup>**</sup></a> Patent RU2659299C1.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry)<sup>[2](#footnote2)</sup> | 0.3 kg |
| MAXIMUM DEPTH | 300 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°C |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE<sup>[4](#footnote4)</sup> | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 0.5 m |
| MULTIPLE ACCESS SCHEME (COMMANDS/SUBSCRIBERS) | 32/23 |
| NOMINAL HORIZONTAL ANGLE DETERMINATION ACCURACY<sup>[5](#footnote5)</sup> | 1° |
| NOMINAL DISTANCE DETERMINATION ACCURACY<sup>[5](#footnote5)</sup> | 0.3 m |

<!-- | BANDWIDTH | 6 .. 18 kHz | -->
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Excluding the weight of the battery pack. Standard battery pack Ø50x165 mm, 0.58 kg, 2.9 A·h 12 V. 
Operating time with the standard battery pack in standby mode - up to 70 hours, with 1 transmission every 3 seconds - up to 8 hours.  
<a name="footnote3"><sup>3</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
<a name="footnote4"><sup>4</sup></a> The value can be changed on request.  
<a name="footnote5"><sup>5</sup></a> Obtained in laboratory conditions in a static experiment.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima_R_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
