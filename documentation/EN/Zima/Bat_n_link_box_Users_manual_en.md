[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Bat&Link Box: User's manual**

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

| ![logo](/documentation/sm_logo.png) | ![Bat&Link Box](/documentation/batlink_w_qr.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Bat & Link Box** - power supply and interface converter <br/> User's manual |

# Bat & Link Box <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents
- [1. Introduction](#1-introduction)
- [2. Appearance and controls](#2-appearance-and-controls)
- [3. Connector pinouts](#3-connector-pinouts)
- [4. Working with the device](#4-working-with-the-device)
- [5. Storage and maintenance](#5-storage-and-maintenance)
- [6. Obligations and disclaimer](#6-obligations-and-disclaimer)
  - [6.1. Terms of replacement and free warranty service](#61-terms-of-replacement-and-free-warranty-service)
  - [6.2. Limitation of the manufacturer's liability](#62-limitation-of-the-manufacturers-liability)

<div style="page-break-after: always;"></div>

## 1. Introduction
The [Bat & Link Box](Bat_n_link_box_Specification_en.md) device combines the functions of an autonomous power source for the direction-finding station Zima2-B (Zima-B) and a switching hub for interfacing the station with the user's PC, as well as for connecting sources of heading and position data for the direction-finding station. It contains protection circuits against reverse polarity and overvoltage for the connected devices.

The unit is housed in a small impact-resistant plastic case. It has a front panel made of high-quality stainless steel. The modern lithium iron phosphate batteries used in the unit provide operation at sub-zero temperatures and more than a thousand charge-discharge cycles. If necessary, the unit can be operated from an AC mains supply using an external power supply, with the built-in battery being charged at the same time.

<div style="page-break-after: always;"></div>

## 2. Appearance and controls
The appearance of the front panel of the device is shown in **Figure 1**. In the center of the panel there are connectors for connecting devices that support communication via the RS-422/485 interface, and USB-B connectors. The connectors are combined into groups **1** and **8**<sup>[1](#footnote21)</sup>. External devices are connected to connectors **X1** and **X3**; these connectors also provide power to the connected external devices. The USB-B connectors **X2** and **X4** are intended for connection to the USB port of a PC.

| ![Bat&Link Box panel](/documentation/batlinkbox_panel2ch.png) |
| :---: |
| **Figure 1 - Appearance of the front panel of the device** |
| _1 - Line 1, 2 - Charge indicator, 3 - Power indicator, 4 - Power switch, 5 - Built-in battery circuit fuse<sup>[2](#footnote22)</sup>, 6 - External power/charging circuit fuse<sup>[2](#footnote22)</sup>, 7 - Power supply connector<sup>[2](#footnote22)</sup>, 8 - Line 2_ |

Indicator **2** is lit when the built-in battery is being charged and is off when it is not being charged.
The two-color indicator **3** is used to show the power status of the entire system. **Table 1** lists all possible light signals.

Switch **4** is intended for turning the power of the device on and off.

Fuses **5** and **6** protect the circuits of the built-in battery and of the external power (charging), respectively. Fuses of size **5.2x20** with a nominal current of 5 A are used.

Connector **7** is used for connecting a mains adapter (charger), through which the built-in battery is charged and, if necessary, the device itself is powered.

### Table 1 - Indicator **3** states

| No. | Indicator state | Indicator state | Description | Action to be taken |
| :---: | :---: | :--- | :--- | :--- |
| 1 | 🟢 | Green on continuously | OK | Not required |
| 2 | ⚪🟢 | Green blinking | Low charge of the built-in power source | Connect the charger (adapter) |
| 3 | 🔴 | Red on continuously | Short circuit at the output | Turn off the device power, check all cables and connectors |
| 4 | ⚪🔴 | Red blinking | External power circuit error | Turn off the device power, check all cables and the charger |

_____________
<a name="footnote21"><sup>1</sup></a> Group **8** is present only in the extended version of the device.  
<a name="footnote22"><sup>2</sup></a> On devices manufactured before July 2020, the fuses and the connector for connecting external power may be located on the side surfaces of the device housing.

<div style="page-break-after: always;"></div>

## 3. Connector pinouts

### Table 2 - Pinout of connector **7** for connecting the mains charger (adapter)

| No. | Pin number | Function |
| :---: | :--- | :--- |
| 1 | 1, 3 | +U CHARGE |
| 2 | 2 | GND CHARGE |
| 3 | 4 | RESERVED |

### Table 3 - Pinout of connector X1 (Group 1)

| Pin number | Function |
| :---: | :--- |
| 1 | +U |
| 2 | GND |
| 3 | Tx+ |
| 4 | NC |
| 5 | Tx- |
| 6 | Rx+ |
| 7 | Rx- |

### Table 4 - Pinout of connector X3 (Group 8)

| Pin number | Function |
| :---: | :--- |
| 1 | +U |
| 2 | GND |
| 3 | Tx+ |
| 4 | NC |
| 5 | Tx- |
| 6 | Rx+ |
| 7 | Rx- |
  
<div style="page-break-after: always;"></div>

## 4. Working with the device
Before use, the device must be installed on a stable horizontal base. When working on ships and similar moving objects, it is recommended to secure the device by the handle with a rope.

Mate and unmate the connectors with the device power off, when switch **4** is in the **OFF** position.

After the connectors are connected and switch **4** is set to the **ON** position, the state of the device is shown by indicator **3** according to [Table 1](#table-1---indicator-3-states).

<div style="page-break-after: always;"></div>

## 5. Storage and maintenance
- Storage of the device is allowed only when it is switched off (switch **4** in the **OFF** position), with the connectors disconnected and the lid of the unit closed;
- During long-term storage (more than a month), it is recommended to periodically check the condition of the built-in power source (battery) and, if necessary, to recharge it in order to prevent battery degradation;
- Contamination can be removed from the surfaces of the device with the lid of the device closed, using household soap solutions, followed by their complete removal;
- Contamination on the front panel of the device may be removed only with a soft cloth, avoiding dirt and moisture getting into the open connectors and fuses;
- The use of third-party chargers is not allowed;

<div style="page-break-after: always;"></div>

## 6. Obligations and disclaimer
### 6.1 Terms of replacement and free warranty service

The manufacturer's warranty covers only factory defects that appear during operation of the device in accordance with these instructions during the warranty period (2 years from the date of purchase).

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a manufacturing defect.

The grounds for refusing free warranty service, free repair and replacement are:
- any **mechanical damage** to the equipment from the delivery set, including damage to the insulation of wires and cables;
- any **damage caused by exposure to moisture and dirt** due to improper use of the supplied equipment;
- any **electrical damage** caused by the **use of accessories not included in the delivery set**; accessories supplied by the manufacturer or its representative to replace faulty or lost ones are not considered to be outside the delivery set;
- any **traces of unauthorized repair and/or opening** of the supplied equipment.

<div style="page-break-after: always;"></div>

### 6.2 Limitation of the manufacturer's liability

_____________

_**ANY PARTS OF THE DELIVERY SET, SEPARATELY AND AS PART OF A SYSTEM, HEREINAFTER REFERRED TO AS THE "SUPPLIED EQUIPMENT":**_  

_**- WERE NOT DEVELOPED AS A MEANS OF RESCUE**_  
_**- WERE NOT TESTED AS RESCUE EQUIPMENT**_
_**- ARE NOT RESCUE EQUIPMENT**_
_**- THE MANUFACTURER DECLARES THAT THE SUPPLIED EQUIPMENT IS SAFE WHEN USED IN ACCORDANCE WITH THESE INSTRUCTIONS AND IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF THE USE OF THE SUPPLIED EQUIPMENT**_

<div style="page-break-after: always;"></div>

_____________
[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/Zima/Bat_n_link_box_Users_manual_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
