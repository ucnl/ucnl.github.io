[Main](/../../) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **Device specification: uSwitch**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uSwitch** - Underwater acoustic modem <br/> Device specification |

<div style="page-break-after: always;"></div>

## KEY FEATURES

* **Simple and affordable solution**
* **Communication range up to 300<sup>[1](#footnote1)</sup> m**
* **Data transmission speed 100 bit/s**
* **Signal propagation time measurement function**
* **Water contact switch function**
* **Can be used as a pinger for the [WAYU](documentation/navigation_and_tracking_systems_en#wayu) system**
* **Low power consumption (Rx/Tx) 20 mA / 2.5 A**
* **Ideal solution for educational projects and training**

<div style="page-break-after: always;"></div>

## DESCRIPTION

The **uSwitch** modem is a simple and affordable solution for transmitting data through the water column over short distances.
Working with the device requires minimal skills, which allows you to use it as a simple tool, focusing on the user's tasks.
For example, for testing various network algorithms, prototyping and building specialized navigation systems, remote control systems, etc.

The device is supplied as an assembly of printed circuit boards and a hydroacoustic antenna on a cable.

The following items can be used as an antenna:
- [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) - Affordable solution with minimal dimensions
- [RT-2.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_2_332820_1_Specification_en.html) - Dual-element antenna with increased sensitivity for surface operation
- [RT-1.524525-1](https://docs.unavlab.com/documentation/EN/Transducers/RT-1.524525-1_specification_en.html) - High sensitivity antenna

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS | 100 x 19 x 25 mm |
| WEIGHT | 0.03 kg |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 300 m |
| DATA TRANSFER RATE | 100 bps |
| POWER CONSUMPTION Rx/Tx | 20 mA / 2.5 A |
| SUPPLY VOLTAGE<sup>[2](#footnote2)</sup> | 7 .. 13 V |
| DATA LINE VOLTAGE | 0 .. 3.3 V |
| FREQUENCY RANGE | 23000 .. 27000 Hz |
| MAXIMUM ACOUSTIC PRESSURE<sup>[3](#footnote3)</sup> (In-band) | 165 dB re 1 µPa @ 1 m |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | UART 9600 bps |

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the environment, and the level of hydroacoustic interference.  
<a name="footnote2"><sup>2</sup></a> Maximum output power is achieved when the modem is powered by 12 V.  
<a name="footnote3"><sup>3</sup></a> When using an [RT-1.332820-1](https://docs.unavlab.com/documentation/ENTransducers/RT_1_332820_1_Specification_en.html) antenna.  

<div style="page-break-after: always;"></div>

## PINOUT AND CONNECTION

| ![image](https://github.com/user-attachments/assets/058c5ff9-68f8-4139-831d-2092fda60fd2) |
| :---: |
| Modem **uSwitch**</br>*location and functions of contact pads* |

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
| 9 | +U<sub>power</sub> | I | - | Power |
| 10 | +U<sub>power</sub> | I | - | Power |
| X1 | ANT | - | - | Hydroacoustic antenna connection |
| X2 | WATER_DET | - | - | Water detector contacts |


<div style="page-break-after: always;"></div>
