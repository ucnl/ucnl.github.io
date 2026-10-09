[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2-RK: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima2rk.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2-RK** - **Zima2 USBL** responder-beacon <br/> Device specification |

## KEY FEATURES

* **Operating depth up to 1000 m**
* **Communication range up to 3000<sup>[1](#footnote1)</sup> m**
* **Highly reliable digital underwater acoustic communication resistant to multipath propagation**
* **Code division multiple access - up to 16 isolating addresses**
* **Low power consumption (Rx/Tx) 0.33/10 W**
* **Built-in pressure/temperature sensor**

## DESCRIPTION

**Zima2-RK** - responder-beacon of the ultra-short baseline navigation system [Zima2 USBL](Zima2_DataBrief_en.md) for operation at depths up to 1000 m.  
The device is designed to be placed on an underwater object in order to determine the location of this object in real time using the direction-finding antenna [Zima2-BK](Zima2BK_Specification_en.md). 

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 80 x 147 mm |
| WEIGHT (dry)<sup>[2](#footnote2)</sup> | 1130 g |
| MAXIMUM DEPTH | 1000 m |
| DEPTH RESOLUTION | 2 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| ACOUSTIC SOURCE LEVEL | 170 dB re 1 μPa @ 1 m |
| CARRIER FREQUENCY | 20100 Hz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°C |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | ± 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| POWER CONSUMPTION (Rx/Tx) | 0.33 / 10 W |
| INTERFACE | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PAZM](Zima2_Protocol_Specification_en.md) |
| CONNECTORS | SubConn MCBH8F (Power and data) <br/> SubConn MCBH2F (Transducer) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 0.5 m |
| MAXIMUM NUMBER OF ADDRESSES | 16 |

<!-- | BANDWIDTH | 10 .. 30 kHz | -->

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Excluding the weight of the transducer. The device is supplied with the transducer [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en).   
<a name="footnote3"><sup>3</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
<a name="footnote4"><sup>4</sup></a> The value can be changed on request.  
<a name="footnote5"><sup>5</sup></a> Obtained in laboratory conditions in a static experiment.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima2RK_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
