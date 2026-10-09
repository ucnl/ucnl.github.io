[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 LBL: Data brief**

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

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima 2 LBL** <br/> Data brief |

<div style="page-break-after: always;"></div>

## General information

**Zima 2 LBL** is an underwater acoustic long baseline (LBL) navigation system designed to determine the location of an underwater object using a navigation base formed by [Zima2-R](Zima2R_Specification_en.md) responder-beacons.

The system is built on a **single hardware platform**: the [Zima2-L](Zima2L_Specification_en.md) and [Zima2-LX](/documentation/RU/Zima/Zima2LX_Specification_ru.md) transceivers can be reprogrammed into each other. This makes it possible to change the system configuration to suit the task without replacing the equipment.

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![Zima2-L](https://github.com/user-attachments/assets/4f28d018-0d80-4355-a7e2-eb72aa14cfc0) | [Zima2-L](Zima2L_Specification_en.md) <br/> LBL transceiver with a common request to the navigation base (3–4 responder-beacons with addresses 1-4) |
| ![Zima2-LX](https://github.com/user-attachments/assets/4f28d018-0d80-4355-a7e2-eb72aa14cfc0) | [Zima2-LX](/documentation/RU/Zima/Zima2LX_Specification_ru.md) <br/> LBL transceiver with sequential interrogation of up to 4 responder-beacons with arbitrary addresses |
| ![Zima2-SL](PENDING) | [Zima2-SL](/documentation/RU/Zima/Zima2SL_Specification_ru.md) <br/> Solver: position calculation and GNSS emulation |
| ![Zima2-R](/documentation/zima_r_wbat.png) | [Zima2-R](Zima2R_Specification_en.md) <br/> Reference responder-beacons |

<div style="page-break-after: always;"></div>

## System configuration options

The **Zima 2 LBL** system can be assembled in one of three modes, depending on the required update rate, the number of responder-beacons and where the result is to be calculated.

### Mode 1. Zima2-L – maximum update rate

The [Zima2-L](Zima2L_Specification_en.md) transceiver sends a **common (broadcast) request** to a fixed navigation base of **3 or 4 responder-beacons** with fixed addresses 1-4. The responder-beacons reply after fixed delays that depend on their address. The position is calculated by an **external application** on the user's side.

- **Advantages:** maximum position update rate, minimum latency. Possibility of placing the responder-beacons on a moving platform (the bottom of a vessel) with the coordinate system tied to the platform.
- **Limitations:** fixed responder-beacon addresses, the position is calculated by external software, all reference responder-beacons must be within a circle of 265 meters radius.

### Mode 2. Zima2-LX – arbitrary set of responder-beacons

The [Zima2-LX](/documentation/RU/Zima/Zima2LX_Specification_ru.md) transceiver **sequentially interrogates** 3 or 4 responder-beacons with arbitrary addresses and measures the range to each of them. The results are transmitted over UART to an external computing unit – the [Zima2-SL](/documentation/RU/Zima/Zima2SL_Specification_ru.md) module.

- **Advantages:** flexibility – responder-beacons with arbitrary addresses.
- **Limitations:** the update rate is lower than that of Zima2-L, because the interrogation is sequential.

### Mode 3. Zima2-LX + Zima2-SL – standalone position calculation

The [Zima2-LX](/documentation/RU/Zima/Zima2LX_Specification_ru.md) + [Zima2-SL](/documentation/RU/Zima/Zima2SL_Specification_ru.md) combination provides a **ready-made solution**: LX measures the ranges, SL stores the coordinates of the responder-beacons, calculates the position and outputs it to the user in the form of standard **GNSS sentences** (GGA, RMC, MTW). This makes it possible to connect the system wherever a regular GNSS receiver is expected.

- **Advantages:** no external software is needed, the output is a familiar GNSS stream.
- **Limitations:** the update rate is determined by the rate of the sequential interrogation by LX.

<div style="page-break-after: always;"></div>

## Comparison of modes

| Characteristic | Zima2-L | Zima2-LX | Zima2-LX + Zima2-SL |
| :--- | :---: | :---: | :---: |
| Number of responder-beacons | 3–4 | 3–4 | 3–4 |
| Interrogation scheme | common request | sequential | sequential |
| Position calculation | external software | external software | **Zima2-SL** |
| Output | ranges | ranges | **GGA, RMC, MTW** |
| Relative update rate | maximum | medium | medium |

<div style="page-break-after: always;"></div>

## Tasks to be solved

* Determining the location of an object in a local coordinate system (x, y, z) if the positions of the reference responder-beacons are specified in a local Cartesian coordinate system
* Determining the absolute location (**latitude, longitude, depth**) if the positions of the reference responder-beacons are specified in a geographic coordinate system

<div style="page-break-after: always;"></div>

## Distinctive features

* Compactness, long range and maximum ease of use make it possible to use the **Zima2** system to work with various **ROVs** and **AUVs** as well as with **divers**
* The high versatility of the responder-beacons makes it possible to use them either in a standalone version with a separate battery pack or integrated with the carrier for both power and data
* A **single hardware platform** for the transceivers and the solver: the role of a device is changed by changing the firmware
* A **unique feature** of the system is the possibility of placing the reference points on a moving base, for example, on the bottom of a vessel, so that the positioned object is tied to a coordinate system associated with the moving vessel

<div style="page-break-after: always;"></div>

## Geometric limitations

### Zima2-L mode (common request)
- the reference points must be located within a circle of **265 m** radius, but no closer than **40 m** to each other;
- the limitation is due to the TDMA interrogation scheme: the responder-beacons reply according to their address with a fixed delay;
- continuous line of sight through the water column between the transceiver and all reference points is required for the system to operate.

### Zima2-LX mode (sequential interrogation)
- **there are no restrictions on the geometry of the base** - responder-beacons with arbitrary addresses can be used;
- the positions of the reference responder-beacons are determined in advance, for example, by the VLBL method;
- the only limitation is the **acoustic communication range determined by the link budget, up to 3000 m<sup>[1]</sup>**;
- continuous line of sight through the water column between the transceiver and all reference points is required for the system to operate.
<div style="page-break-after: always;"></div>

_________

| **Additional information** |
| :--- |
| [Responder-beacon **Zima 2-R**: device specification](Zima2R_Specification_en.md) |
| [LBL transceiver **Zima 2-L**: device specification](Zima2L_Specification_en.md) |
| [LBL transceiver **Zima 2-LX**: device specification](/documentation/RU/Zima/Zima2LX_Specification_ru.md) |
| [Solver **Zima 2-SL**: device specification](/documentation/RU/Zima/Zima2SL_Specification_ru.md) |
| [Communication protocol specification for the devices of the **Zima 2** system](Zima2_Protocol_Specification_en.md) |

<!-- docs-sync: source=documentation/RU/Zima/Zima2_LBL_DataBrief_ru.md commit=bf13b8fd73f10e9e9187401418285536e751fe00 date=2026-10-06 -->
