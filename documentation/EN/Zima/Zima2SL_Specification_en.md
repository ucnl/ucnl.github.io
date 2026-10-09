[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2-SL: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![zima2_sl](PENDING) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2-SL** — solver of the **Zima2 LBL** navigation system <br/> Device specification |

## KEY FEATURES

* **Position calculation from ranges to beacons with known coordinates**
* **Storage of beacon coordinates (up to 4)**
* **GNSS protocol emulation (GGA, RMC, MTW)** for the data consumer
* **Communication with Zima2-LX over 3.3 V UART**
* **Compact board that can be placed underwater or on the surface**
* **Configuration via the [PAZM](Zima2_Protocol_Specification_en.md) protocol**

## DESCRIPTION

**Zima2-SL** is the computing module (solver) of the long baseline navigation system [Zima2 LBL](/documentation/EN/Zima/Zima2_LBL_DataBrief_en.md).

The module receives over UART the measured range data from the [Zima2-LX](/documentation/EN/Zima/Zima2LX_Specification_en.md) transceiver, stores the coordinates of the [Zima2-R](Zima2R_Specification_en.md) responder-beacons and calculates its own position. The result is output to the data consumer in the form of standard GNSS sentences (**GGA**, **RMC**, **MTW**), which allows **Zima2-SL** to be used as a "transparent" replacement for a GNSS receiver in existing systems.

The module can be placed either underwater or on the surface, depending on the task to be solved.

________________

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | PENDING |
| WEIGHT | PENDING |
| SUPPLY VOLTAGE | 12 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| INTERFACE WITH Zima2-LX | UART 9600 bit/s |
| INTERFACE WITH THE DATA CONSUMER | UART 9600 bit/s |
| CONFIGURATION PROTOCOL | NMEA 0183 [PAZM](Zima2_Protocol_Specification_en.md) |
| EMULATED GNSS SENTENCES | GGA, RMC, MTW |
| OPERATING TEMPERATURE RANGE | PENDING |
| POWER CONSUMPTION | PENDING |
| MAXIMUM POSITION UPDATE RATE<sup>[1](#footnote1)</sup> | PENDING |
| NOMINAL POSITIONING ACCURACY (RMS)<sup>[2](#footnote2)</sup> | PENDING |

________________
- <a name="footnote1"><sup>1</sup></a> Determined by the speed of sequential interrogation of the beacons by the [Zima2-LX](/documentation/EN/Zima/Zima2LX_Specification_en.md) transceiver and by the number of beacons in the set.
- <a name="footnote2"><sup>2</sup></a> PENDING.

<div style="page-break-after: always;"></div>

### CONNECTOR / CABLE WIRE ASSIGNMENT

| WIRE COLOR / PIN | FUNCTION |
| :--- | :---: |
| PENDING | + U<sub>supply</sub> |
| PENDING | - U<sub>supply</sub> (GND) |
| PENDING | UART to Zima2-LX: Rx |
| PENDING | UART to Zima2-LX: Tx |
| PENDING | UART to the data consumer: Tx (GNSS stream) |

<!-- docs-sync: source=documentation/RU/Zima/Zima2SL_Specification_ru.md commit=413c653f7a7e96a5662261e98877d522267ea7aa date=2026-10-06 -->
