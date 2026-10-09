[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2-R: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![zima_r_wbat](/documentation/zima_r_wbat.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2-R** - **Zima2 USBL** responder-beacon <br/> Device specification |

## KEY FEATURES

* **Extremely small size and weight**
* **Communication range up to 3000<sup>[1](#footnote1)</sup> m**
* **Highly reliable digital underwater acoustic communication resistant to multipath propagation**
* **Code division multiple access - up to 16 isolating addresses**
* **Low power consumption (Rx/Tx) 0.33/10 W**
* **Built-in pressure/temperature sensor**
* **Patented<sup>[*](#footnote_a1)</sup> monoblock design**

## DESCRIPTION

**Zima2-R** - responder-beacon of the ultra-short baseline navigation system [Zima2 USBL](Zima2_DataBrief_en.md).  

The device is designed to be placed on an underwater object in order to determine the location of this object in real time using the direction-finding antenna [Zima2-B](Zima2B_Specification_en.md). 

The device can be either standalone (with an additional [battery pack](/documentation/EN/Accessories/Sub_batteries_en#sb2448lf)) or interfaced with the carrier for power. 

Extremely small size, ease of use and low power consumption make the direction-finding system [Zima2 USBL](Zima2_DataBrief_en.md) an ideal solution for working with autonomous and remotely controlled vehicles, as well as for determining the relative position of divers.

________________
<a name="footnote_a1"><sup>*</sup></a> Patent RU2659299C1.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 64 x 62 mm |
| WEIGHT (dry)<sup>[2](#footnote2)</sup> | 0.3 kg |
| MAXIMUM DEPTH | 300 m |
| DEPTH RESOLUTION | 0.6 m |
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
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 0.5 m |
| MAXIMUM NUMBER OF ADDRESSES | 16 |

<!-- | BANDWIDTH | 10 .. 30 kHz | -->
________________
- <a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
- <a name="footnote2"><sup>2</sup></a> Excluding the weight of the battery pack. Standard battery pack [SB-24-48-LF](/documentation/EN/Accessories/Sub_batteries_en#sb2448lf).  
- <a name="footnote3"><sup>3</sup></a> The value was obtained in a laboratory static experiment, without taking into account the multipath propagation effect.  
- <a name="footnote4"><sup>4</sup></a> The value can be changed on request.  
- <a name="footnote5"><sup>5</sup></a> Obtained in laboratory conditions in a static experiment.  

<div style="page-break-after: always;"></div>

## ADDITIONAL INFORMATION

In the standalone version, the device is equipped with the battery pack [SB-24-48-LF](/documentation/EN/Accessories/Sub_batteries_en#sb2448lf) based on LiFePO4 (lithium iron phosphate) batteries, which provide more than a thousand charge-discharge cycles and operation at low ambient temperatures. 

The responder-beacon is connected to the battery pack through a sealed connector, which additionally provides the function of automatically switching the device on when it is immersed in water.

The operating time of the responder-beacon on the battery pack depends on the intensity of the exchange with the direction-finding antenna, which in turn depends on the range, the number of responder-beacons polled by the direction-finding antenna and the hydrological conditions.

### BATTERY LIFE 

| POLLING PERIOD, s | OPERATING TIME, h | NOTE |
| :---:              | :---: | :--- |
| -                  | 70 | Without polling, in receiving mode |
| 1                  | 8 | Shortest possible polling period |
| 2                  | 16 | |
| 4                  | 32 | |
| 8                  | 64 | |
| 16                 | up to 70 | |

### CABLE WIRE ASSIGNMENT (In the integrated version)

| WIRE COLOR | FUNCTION |
| :--- | :---: |
| 🟥 Red | + U<sub>supply</sub> |
| 🟩 Green | Tx |
| ⬜ White/Transparent | Rx |
| 🟨 Yellow | SVC |
| Shield | - U<sub>supply</sub> |

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima2R_Specification_ru.md commit=2b17417450cfa3cfcbfa17c0eb055c768aa356fd date=2026-10-06 -->
