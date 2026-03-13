[Home](/README) ❯ [Our educational projects](/educational_projects_en) ❯ **ACubes A<sup>3</sup>R: Device Specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/b3b28b79-613e-4149-9b05-c916b2075334) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **ACubes A<sup>3</sup>R** <br/> Device specification |

## KEY FEATURES

* **Perfect solution for educational projects and learning**
* **Compatibility with [A<sup>3</sup>T](A3T_Datasheet_en.md) modules**
* **Stackable up to 12 units**
* **Low power consumption - 20 mA**

## DESCRIPTION

**ACubes A<sup>3</sup>R** is a single-frequency acoustic receiver module with logic output.
**A<sup>3</sup>R** devices can be combined with the pulse transmitter **[A<sup>3</sup>T](A3T_Datasheet_en.md)** and share a single acoustic transceiving antenna.
Devices can also be stacked up to 12 units, and each such stack can be combined with one transmitter. In this case, each receiver and transmitter uses a separate antenna.

The following antennas can be used:
- [R-1.d3505-1](/documentation/EN/Transducers/R_1.d3505_1_Specification_en) - receiving antenna based on plate piezoelectric element
- [RT-1.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_1_332820_1_Specification_en.html) - compact transceiving antenna
- [RT-2.332820-1](https://docs.unavlab.com/documentation/EN/Transducers/RT_2_332820_1_specification_en.html) - dual-element antenna with enhanced sensitivity for surface operation
- [RT-1.524525-1](https://docs.unavlab.com/documentation/EN/Transducers/RT-1.524525-1_specification_en.html) - antenna with enhanced sensitivity

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS | 100 x 50 x 10 mm |
| WEIGHT | 0.015 kg |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 300 m |
| POWER CONSUMPTION | 20 mA |
| SUPPLY VOLTAGE | 5 .. 15 V |
| DATA LINE VOLTAGE | TTL/LVTTL (0 .. 3.3/0 .. 5) V |
| CARRIER FREQUENCY | 25000 Hz |
| SIGNAL DETECTION LOCKOUT INTERVAL | 100 ms |
| MAXIMUM RELATIVE VELOCITY | +/- 2 m/s |
| OPERATING TEMPERATURE RANGE | -5 .. 50 °C |

________________
<a name="footnote1"><sup>1</sup></a> Parameter defining the maximum range at which signal reception is possible, based on the electroacoustic parameters of the transmitter and receiver, spatial decay of sound energy intensity, medium attenuation, and ambient acoustic noise level.

<div style="page-break-after: always;"></div>

## PINOUT AND CONNECTION

| ![image](https://github.com/user-attachments/assets/d494f73e-ced3-482b-9993-693503a7a97a) |
| :---: |
| **A<sup>3</sup>R** <br/> *pad layout and functions* |

### CONNECTOR XS1

| PIN NUMBER | I/O   | FUNCTION |
| :---       | :---: | :--- |
| 1          | I     | Antenna input |
| 2          | -     | GND |
| 3          | -     | GND |
| 4          | I     | Connected to pin №1 |

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

### CONNECTOR XS4

| PIN NUMBER | I/O   | FUNCTION |
| :---       | :---: | :--- |
| 1          | O     | Preamplifier output |
| 2          | O     | Connected to pin #1 |
| 3          | -     | Reserved |

### CONNECTOR XP2

| PIN NUMBER | I/O   | FUNCTION |
| :---       | :---: | :--- |
| 1          | I     | 5 .. 15 V |
| 2          | -     | GND |

### SWITCHES (JUMPERS) P0 - P12

### Switch P0 - Transponder Mode

The jumper connects pin 1 (Common receiver strobe) of connector XS3 and pin 4 (Pulse transmission trigger) of connector XS2.
Thus, if the jumper is installed and the A<sup>3</sup>R module is paired with the [A<sup>3</sup>T](A3T_Datasheet_en.md) module, then upon receiving an acoustic signal, a response pulse transmission will be triggered.

Switch P0 controls enabling and disabling of the transponder mode for paired A<sup>3</sup>R and [A<sup>3</sup>T](A3T_Datasheet_en.md) modules.

### Switches P1 - P12 - Bus Address

These switches allow routing the receiver strobe to a specified line of the bus formed by connectors XS2 and XS3. This function can be used when interfacing multiple receivers with individual receiving antennas to enable output of the signal from each receiver to different bus lines.

<div style="page-break-after: always;"></div>
