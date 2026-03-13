[Main](/README) ❯ [Our educational projects](/educational_projects_en) ❯ **ACubes A<sup>3</sup>T: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/8c524cae-93f6-450d-a30b-7fd8835d5bb5) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **ACubes A<sup>3</sup>T** <br/> Device specification |


## KEY FEATURES

* **Perfect solution for educational projects and learning**
* **Compatibility with [A<sup>3</sup>R](A3R_Datasheet_en.md) modules**
* **Low power consumption (Idle/Tx) 20 mA / 0.5 A**

## DESCRIPTION

**ACoubes A<sup>3</sup>T** is a pulse acoustic single-frequency transmitter module controlled by a digital line.
The device can be combined with the [**A<sup>3</sup>R**](A3R_Datasheet_en.md) receiver module and share a single acoustic transceiving antenna.
The device can also be stacked (up to 12 units) with [**A<sup>3</sup>R**](A3R_Datasheet_en.md) receiver modules. In this case, each receiver and transmitter uses a separate antenna.

The following antennas can be used:
- [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) - affordable solution with minimal dimensions
- [RT-2.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_2_332820_1_Specification_en.html) - dual-element antenna with enhanced sensitivity for surface operation
- [RT-1.524525-1](https://docs.unavlab.com/documentation/EN/Transducers/RT-1.524525-1_specification_en.html) - antenna with enhanced sensitivity

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS | 100 x 50 x 10 mm |
| WEIGHT | 0.015 kg |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 300 m |
| POWER CONSUMPTION Rx/Tx | 20 mA / 0.5 A |
| SUPPLY VOLTAGE<sup>[2](#footnote2)</sup> | 5 .. 15 V |
| DATA LINE VOLTAGE | TTL/LVTTL (0 .. 3.3/0 .. 5) V |
| CARRIER FREQUENCY | 25000 Hz |
| PULSE DURATION | 4 ms |
| MINIMUM PULSE INTERVAL | 40 ms |
| MAXIMUM ACOUSTIC PRESSURE<sup>[3](#footnote3)</sup> (In band) | 160 dB re 1 μPa @ 1 m |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |

________________
<a name="footnote1"><sup>1</sup></a> Parameter defining the maximum range at which signal reception is possible, based on the electroacoustic parameters of the transmitter and receiver, spatial decay of sound energy intensity, medium attenuation, and ambient acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> Maximum output power is achieved when the device is powered with 12 V.  
<a name="footnote3"><sup>3</sup></a> When using [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) antenna.  

<div style="page-break-after: always;"></div>

## PINOUT AND CONNECTION

| ![image](https://github.com/user-attachments/assets/413f0bb4-4001-4e0c-b196-20ea50dd4bdf) |
| :---: |
| **A<sup>3</sup>T** <br/> *pad layout and functions* |

### CONNECTOR XS1

| PIN NUMBER | I/O   | FUNCTION |
| :---       | :---: | :--- |
| 1          | O     | Antenna output |
| 2          | -     | GND |
| 3          | -     | GND |
| 4          | O     | Connected to pin №1 |

### CONNECTOR XS2

| PIN NUMBER | I/O   | ACTIVE STATE | FUNCTION |
| :---       | :---: | :---:        | :--- |
| 1          | -     | -            | GND |
| 2          | O     | 0            | Transmission start strobe |
| 3          | -     | -            | GND |
| 4          | I     | 0            | Pulse transmission trigger |
| 5          | -     | -            | GND |
| 6          | O     | 0            | Receiver №1 strobe |
| 7          | -     | -            | GND |
| 8          | O     | 0            | Receiver №2 strobe |
| 9          | -     | -            | GND |
| 10         | O     | 0            | Receiver №3 strobe |
| 11         | -     | -            | GND |
| 12         | O     | 0            | Receiver №4 strobe |
| 13         | -     | -            | GND |
| 14         | O     | 0            | Receiver №5 strobe |
| 15         | -     | -            | GND |
| 16         | O     | 0            | Receiver №6 strobe |
| 17         | -     | -            | GND |
| 18         | -     | -            | NC |
| 19         | -     | -            | GND |
| 20         | -     | -            | +U<sub>supply</sub> |

### CONNECTOR XS3

| PIN NUMBER | I/O   | ACTIVE STATE | FUNCTION |
| :---       | :---: | :---:        | :--- |
| 1          | O     | 0            | Common receiver strobe |
| 2          | -     | -            | GND |
| 3          | -     | -            | Reserved |
| 4          | -     | -            | GND |
| 5          | O     | 0            | Receiver №7 strobe |
| 6          | -     | -            | GND |
| 7          | O     | 0            | Receiver №8 strobe |
| 8          | -     | -            | GND |
| 9          | O     | 0            | Receiver №9 strobe |
| 10         | -     | -            | GND |
| 11         | O     | 0            | Receiver №10 strobe |
| 12         | -     | -            | GND |
| 13         | O     | 0            | Receiver №11 strobe |
| 14         | -     | -            | GND |
| 15         | O     | 0            | Receiver №12 strobe |
| 16         | -     | -            | GND |
| 17         | -     | -            | Reserved |
| 18         | -     | -            | GND |
| 19         | -     | -            | +U<sub>supply</sub> |
| 20         | -     | -            | GND |

### CONNECTOR XP2

| PIN NUMBER | I/O   | FUNCTION |
| :---       | :---: | :--- |
| 1          | I     | 5 .. 15 V |
| 2          | -     | GND |

<div style="page-break-after: always;"></div>
