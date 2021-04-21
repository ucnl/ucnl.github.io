| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima USBL**<br/> Data brief |

<div style="page-break-after: always;"></div>

## General information
**Zima USBL** - underwater acoustic ultrashort-baseline (USBL) navigation system designed to determine the location
underwater objects marked by responder-beacons [Zima-R](Zima_R_Specification_en.md) using direction-finding
antenna [Zima-B](Zima_B_Specification_en.md).

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![Zima-B](/documentation/def_zima_b_ant.png) | [Zima-B](Zima_B_Specification_en.md) <br/> Base station |
| ![Zima-R](/documentation/zima_r.png) | [Zima-R](Zima_R_Specification_en.md) <br/> Responder-beacons (One base station supports up to 23 responder-beacons) |
| ![Bat&Link Box](/documentation/batnlinkbox.png) | [Bat&Link Box](Bat_n_link_box_Specification_en.md) <br/> Autonomous power supply and interfacing unit |

<div style="page-break-after: always;"></div>

## Tasks that system solves
* Locating up to 23 underwater objects in the water area (tracking underwater objects)
* Estimation of relative location (**azimuth, distance, depth**)
* Estimation of absolute location (**latitude, longitude, azimuth, distance, depth**) when connecting external **GNSS** and compass (or **GNSS with compass function**)
* Mutual navigation: transmission of the azimuth to the beacon on the direction-finding antenna and measurement of the distance by the beacon to the antenna (when pairing the beacon with the ROV/AUV and when connecting an external compass or **GNSS** with the compass function to the control PC);
* Remote control: transmission of up to 32 code commands to underwater objects (when pairing of the beacon with the carrier);

<div style="page-break-after: always;"></div>

## Key features
* Compactness, long-range and maximum ease of use allows using **Zima USBL** system for working with
various **ROVs**, **AUVs** and  with **divers** in any combination
* The high versatility of the beacons allows them to be used both stand-alone with a separate battery pack, and paired with the underwater vehicle, in this case, it is possible to transmit up to 32 address code commands of telecontrol to an underwater vehicle
* The system supports integration with external sources of navigation data: **GNSS** and a magnetic compass (connected to the control PC).
In this case, the system determines the absolute geographical coordinates of underwater objects, allows saving the track of the movement of underwater objects and has GNSS emulation functions for one of the selected responder-beacons for integration with third-party software (for example, Hypack, SAS.Planet, etc.)
* Zima-B antenna is mounted on the rod from the side of almost any vessel. It can be connected to a 12 V / 3.5 A power supply, and to a control PC (Windows 7 and above) - in this minimum configuration, the system determines the position of the beacons (azimuth and distance) relative to the antenna. When connecting a GNSS receiver (**RMC, GGA**) and magnetic compass (**HDG/HDT**) the system determines the geographical coordinates of the beacons and can transmit them (**RMC, GGA**) to any serial port, thereby emulating a GNSS receiver;
* Instead of a magnetic compass, **a GNSS system** with several antennas can be used (**HDT** sentences);

<div style="page-break-after: always;"></div>

| ![Zima-B placement](/documentation/zima_boat_placement.png) |
| :---: |
| [Zima-B](Zima_B_Specification_en.md) Installation scheme <br/> _1 - rod, 2 - boat, 3 - water surface, 4 - cable, 5 - antenna [Zima-B](Zima_B_Specification_en.md), 6 - antenna's direction_ |

<div style="page-break-after: always;"></div>

## Working options
### Working in relative coordinates
To determine **the relative location** of the responder-beacons, the antenna is paired to a control PC on which it is installed
open-source software [ZHost](https://api.github.com/repos/ucnl/ZHost/zipball). The antenna connects to the PC via
[Bat & Link Box](Bat_n_link_box_Specification_en.md), which provides the conversion of the interface to USB and antenna power.
In this case, the user has access to data and functions:
* **Azimuth** (horizontal angle) to the used responder-beacons;
* **Distance** to responder-beacons;
* Depths of responder-beacons;
* Ability **address transmission of up to 32 code commands** for each responder-beacon (when responder-beacons is paired with a underwater vehicle).

| ![Zima-B relative scheme](https://ucnl.github.io/documentation/zima_relative_scheme.png) |
| :---: |
| _Connection scheme for relative coordinates_ |

<div style="page-break-after: always;"></div>

### Working in absolute coordinates
To determine **the absolute location** of the responder-beacons, the antenna is paired with the PC on which [ZHost](https://api.github.com/repos/ucnl/ZHost/zipball) software is installed. The antenna connects to the PC via
[Bat & Link Box](Bat_n_link_box_Specification_en.md), which provides the conversion of the interface to USB and antenna power.
Also, an external GNSS system and a magnetic compass working under the **NMEA0183** protocol (messages **RMC** and **HDG**) are connected,
or external **GNSS** - a system with a compass function operating on the **NMEA0183** protocol (messages **RMC** and **HDT**).

| ![Zima-B absolut scheme](/documentation/zima_abs_scheme.png) |
| :---: |
| _Connection scheme for absolute coordinates_ |

In this case, the following data and functions are available to the user:
* Absolute **geographic coordinates** and depth of responder-beacons;
* **Azimuth** (relative to north)
* **Distance**
* Ability **address transmission of up to 32 code commands** for each responder-beacon (when responder-beacon is paired with the underwater vehicle);
* Recording of the motion track of underwater objects with the possibility of saving in Google KML format.

<div style="page-break-after: always;"></div>

## Geometric limitations
Since the location of the responder-beacons [Zima-R](Zima_R_Specification_en.md) is determined by the horizontal angle of arrival of the 
signal, slant range and depth difference, the phased array of the direction-finding station [Zima-B](Zima_B_Specification_en.md) has the 
best sensitivity in the horizontal plane. This imposes geometric limitations on the relative positioning of the direction-finding antenna 
and responder-beacons. The working vertical angle of the antenna is **+/-30°** from the horizontal plane. It is possible, but not recommended, 
to work with such relative positions of the antenna and the responder-beacon when the vertical angle to the beacon is in the range from 
**30°** to **45°** due to a decrease in the accuracy of determining the angle of arrival of the signal. Operation at vertical angles to the 
responder-beacons above 45° is highly not recommended.

| ![Zima-B angular zones](/documentation/zima_dir.png) |
| :---: |
| Geometric limitations [Zima-B](Zima_B_Specification_ru.md) <br/> _1 - working zone (+/- 30°), 2 - low accuracy zone (30 .. 45°), 3 - shadow zone ( > 45°), 4 - direction-finding antenna. The deviation is indicated from the horizontal plane passing through the centre of the antenna phased array_ |

<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [**Zima USBL**: User's manual](Zima_Users_manual_en.md) |
| [Responder-beacon **Zima-R**: Device specification](Zima_R_Specification_en.md) |
| [Base station **Zima-B**: Device specification](Zima_B_Specification_en.md) |
| [Autonomous power supply and interfacing unit **Bat&Link Box**: Device specification](Bat_n_link_box_Specification_en.md) |
| [Interfacing protocol **Zima USBL**](Zima_Protocol_Specification_en.md) |
| [GNSS and heading sensor compatibility requirements](Zima_GNSS_requirements_en.md) |

> The export version of the system is limited in range to 3000 meters

