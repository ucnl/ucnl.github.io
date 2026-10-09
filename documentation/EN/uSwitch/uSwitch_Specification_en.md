[Main](/) ❯ [Educational projects](/educational_projects_en) ❯ **uSwitch: Device specification**

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

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/f8f639cc-327c-4561-8040-318befd29b4a) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uSwitch** - Underwater acoustic modem <br/> Device specification |

## KEY FEATURES

* **Simple and affordable solution**
* **Communication range up to 300<sup>[1](#footnote1)</sup> m**
* **Data transmission speed 32 bit/s**
* **Signal propagation time measurement function**
* **Switch-on function upon contact with water**
* **Can be used as a pinger for the [WAYU](/navigation_and_tracking_systems_en#wayu) system**
* **Low power consumption (Rx/Tx) 30 mA / 2.5 A**
* **Ideal solution for educational projects and training**

## DESCRIPTION

The **uSwitch** underwater acoustic modem is a simple and affordable solution for transmitting data through the water column over short distances.
Working with the device requires minimal skills, which allows you to use it as a simple tool, focusing on the user's tasks.
For example, for testing various network algorithms, prototyping and building specialized navigation systems, remote control systems, etc.

The device is supplied as a printed circuit board assembly and a transducer on a cable.

The following can be used as the transducer:
- [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) - affordable solution with minimal dimensions
- [RT-2.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_2_332820_1_specification_en.html) - dual-element transducer with increased sensitivity for operation from the surface
- [RT-1.524525-1](https://docs.unavlab.com/documentation/EN/Transducers/RT-1.524525-1_specification_en.html) - transducer with increased sensitivity

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS | 100 x 19 x 25 mm |
| WEIGHT | 0.03 kg |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 300 m |
| DATA RATE | 32 bit/s |
| POWER CONSUMPTION Rx/Tx | 20 mA / 2.5 A |
| SUPPLY VOLTAGE<sup>[2](#footnote2)</sup> | 7 .. 13 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| FREQUENCY RANGE | 24000 .. 26000 Hz |
| MAXIMUM ACOUSTIC SOURCE LEVEL<sup>[3](#footnote3)</sup> (in band) | 165 dB re 1 μPa @ 1 m |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | UART 9600 bit/s |

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the level of underwater acoustic noise.  
<a name="footnote2"><sup>2</sup></a> The maximum output power is achieved when the modem is supplied with 12 V.  
<a name="footnote3"><sup>3</sup></a> When using the transducer [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html).  

<div style="page-break-after: always;"></div>

## PINOUT AND CONNECTION

| ![image](https://github.com/user-attachments/assets/058c5ff9-68f8-4139-831d-2092fda60fd2) |
| :---: |
| **uSwitch** modem <br/> *location and functions of the contact pads* |

| DESIGNATION | NAME | I/O | ACTIVE STATE | FUNCTION |
| :--- | :--- | :---: | :---: |:--- |
| 1 | GND | - | - | Ground/Common |
| 2 | STR_TRX | O | 1 | Strobe at the beginning of transmission/reception, not less than 10 ms |
| 3 | GND | - | - | Ground/Common |
| 4 | TX_OVF | O | 0 | If the transmit buffer is full, 0 is set |
| 5 | GND | - | - | Ground/Common |
| 6 | TX | O | - | Receiver Tx |
| 7 | GND | - | - | Ground/Common |
| 8 | RX | I | - | Transmitter Rx |
| 9 | +U<sub>supply</sub> | I | - | Power |
| 10 | +U<sub>supply</sub> | I | - | Power |
| X1 | ANT | - | - | Transducer connection |
| X2 | WATER_DET | - | - | Water detector contacts |

<div style="page-break-after: always;"></div>

## ADDITIONAL INFORMATION

The device allows you to switch the maximum power of the transmit path for operation at maximum range and for operation in small bodies of water, such as swimming pools.

The modes are switched by soldering the corresponding jumper (0 Ω resistor, size 1206).

- for operation at maximum range:
  - R1 is not soldered, R2 is soldered

- for operation in swimming pools:
  - R1 is soldered, R2 is not soldered

> IMPORTANT! Soldering both jumpers R1 and R2 at the same time will cause the device to fail and result in a breakdown not covered by the warranty

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uSwitch/uSwitch_Specification_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
