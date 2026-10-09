[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2-LX: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![zima2_lx](https://github.com/user-attachments/assets/4f28d018-0d80-4355-a7e2-eb72aa14cfc0) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2-LX** — LBL transceiver of the **Zima2 LBL** navigation system <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Communication range up to 3000<sup>[1](#footnote1)</sup> m**
* **Reliable digital underwater acoustic communication resistant to multipath propagation**
* **Low power consumption (Rx/Tx) 0.33/10 W**
* **Built-in pressure/temperature sensor**
* **Sequential interrogation of responder-beacons with arbitrary addresses**
* **Patented<sup>[*](#footnote_a1)</sup> monoblock design**

## DESCRIPTION

**Zima2-LX** is the transceiver of the long baseline navigation system [Zima2 LBL](/documentation/EN/Zima/Zima2_LBL_DataBrief_en.md).

The device is designed to be placed on an underwater object in order to measure the ranges to the [Zima2-R](Zima2R_Specification_en.md) responder-beacons, whose positions are known.

Unlike [Zima2-L](/documentation/EN/Zima/Zima2L_Specification_en.md), which works with a fixed navigation base of 3 or 4 beacons with addresses 1-4 using the common request scheme and is limited by a base size of 265 m, Zima2-LX provides sequential interrogation of 3 or 4 beacons with arbitrary addresses without restrictions on the geometry of the base. The only limitation is the acoustic communication range determined by the link budget (up to 3000 m).
The position of the transceiver is calculated by the external [Zima2-SL](/documentation/EN/Zima/Zima2SL_Specification_en.md) device based on the measured ranges and the known coordinates of the beacons.

**Zima2-LX** and [Zima2-L](/documentation/EN/Zima/Zima2L_Specification_en.md) use **the same hardware platform**.

________________
<a name="footnote_a1"><sup>*</sup></a> Patent RU2659299C1.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry) | 0.3 kg |
| MAXIMUM DEPTH | 300 m |
| DEPTH RESOLUTION | 0.1 m |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| ACOUSTIC SOURCE LEVEL | 170 dB re 1 μPa @ 1 m |
| CARRIER FREQUENCY | 20100 Hz |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1 °C |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2)</sup> | -3 dB |
| MAXIMUM RELATIVE VELOCITY | ± 2 m/s |
| STARTUP TIME | 100 ms |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| POWER CONSUMPTION (Rx/Tx) | 0.33 / 10 W |
| INTERFACE | UART 9600 bit/s |
| COMMUNICATION PROTOCOL | NMEA 0183 [PAZM](Zima2_Protocol_Specification_en.md) |
| MAXIMUM NUMBER OF BEACONS IN THE BASE | 4 |
| CABLE LENGTH<sup>[3](#footnote3)</sup> | 0.5 m |
| MAXIMUM RANGE UPDATE RATE<sup>[4](#footnote4)</sup> | PENDING |
| NOMINAL RANGE MEASUREMENT ACCURACY (RMS)<sup>[5](#footnote5)</sup> | PENDING |

________________
- <a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level. The maximum communication range is not equivalent to the maximum operating range of the navigation system.
- <a name="footnote2"><sup>2</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.
- <a name="footnote3"><sup>3</sup></a> The value can be changed on request.
- <a name="footnote4"><sup>4</sup></a> Depends on the number of beacons in the set and their addresses; with sequential interrogation the update rate is lower than that of [Zima2-L](/documentation/EN/Zima/Zima2L_Specification_en.md).
- <a name="footnote5"><sup>5</sup></a> PENDING.

<div style="page-break-after: always;"></div>

### CABLE WIRE ASSIGNMENT

| WIRE COLOR | FUNCTION |
| :--- | :---: |
| 🟥 Red | + U<sub>supply</sub> |
| 🟩 Green | Tx |
| ⬜ White/Transparent | Rx |
| 🟨 Yellow | SVC |
| Shield | - U<sub>supply</sub> |

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima2LX_Specification_ru.md commit=badd40c099b839486b24f54e3d70a62c416f78b1 date=2026-10-06 -->
