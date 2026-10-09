[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima-B: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_zima_b_ant.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-B** - **Zima USBL** direction-finding station <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Communication range up to 3000<sup>[1](#footnote1)</sup> m**
* **Highly reliable digital underwater acoustic communication resistant to multipath propagation**
* **Code division multiple access - up to 23 isolating addresses**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented<sup>[*](#footnote_a1)</sup> simultaneous navigation technology**
* **Built-in pressure/temperature sensor**
* **Patented<sup>[**](#footnote_a2)</sup> monoblock design**

## DESCRIPTION

**Zima-B** - direction-finding station of the ultra-short baseline system [Zima USBL](Zima_DataBrief_en.md).  

The device uses a fixed-length signal with code division to determine the direction and distance, 
as well as to transmit remote control commands to the responder-beacons [Zima-R](Zima_R_Specification_en.md) and to receive telemetry data from them.

When an external **GNSS** receiver and a compass are used, the device can determine the absolute coordinates of the responder-beacons.
Sequential transmission of up to 32 control commands for 23 responder-beacons is provided.
 
The ideal solution for determining the direction and distance to **ROVs**, **AUVs** and **divers**.

Extremely small size, low power consumption and ease of use make the direction-finding system [Zima USBL](Zima_DataBrief_en.md) an ideal solution for working with autonomous and remotely controlled vehicles, as well as determining the relative position of divers.

_________
<a name="footnote_a1"><sup>*</sup></a> Patent RU156897U1.  
<a name="footnote_a2"><sup>**</sup></a> Patent RU2659299C1.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 128 mm |
| WEIGHT (dry)<sup>[2](#footnote2)</sup> | 0.44 kg |
| MAXIMUM DEPTH | 40 m |
| NOMINAL DEPTH ACCURACY | 0.1 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| NOMINAL HORIZONTAL ANGLE OF ARRIVAL ACCURACY<sup>[3](#footnote3)</sup> | 1° |
| MAXIMUM DEVICE TILT RELATIVE TO THE VERTICAL COMPENSATED BY THE BUILT-IN INCLINOMETER (ROLL/PITCH) | +/- 30° |
| OPERATING CONE (RELATIVE TO THE HORIZONTAL)<sup>[3](#footnote3)</sup> | +/-30° |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1°C |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| BATTERY LIFE<sup>[4](#footnote4)</sup> WHEN SUPPLIED FROM [BAT&LINK BOX](Bat_n_link_box_Specification_en.md) | 8 h |
| INTERFACE | USB (COM) 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[5](#footnote5)</sup> | 10 m |
| MULTIPLE ACCESS SCHEME (COMMANDS/SUBSCRIBERS) | 32/23 |

<!-- | BANDWIDTH | 6 .. 18 kHz | -->
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Excluding the weight of the converter and cable.  
<a name="footnote3"><sup>3</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
<a name="footnote4"><sup>4</sup></a> With the station operating at 1 request per 3 seconds.  
<a name="footnote5"><sup>5</sup></a> Including the interface converter and extension cable up to the [Bat&Link Box](Bat_n_link_box_Specification_en.md) device. Optionally, the length can be increased up to 20 m.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima_B_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
