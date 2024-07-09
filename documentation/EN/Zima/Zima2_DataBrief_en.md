[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 USBL: Data brief**
<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima_package.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima 2 USBL** <br/> Data brief |

<div style="page-break-after: always;"></div>

## Brief description
**Zima 2 USBL** is a hydroacoustic ultra-short baseline (USBL) navigation system designed to determine the location of underwater objects marked with hydroacoustic responder beacons [Zima2-R](Zima2R_Specification_en.md) using a direction-finding transceiver antenna [Zima2-B](Zima2B_Specification_en.md).

<div style="page-break-after: always;"></div>

## System Composition

|  |  |
| :---: | :--- |
| ![Zima2-B](/documentation/zima_b.png) | [Zima2-B](Zima2B_Specification_en.md) <br/> Direction-finding antenna |
| ![Zima2-R](/documentation/zima_r_wbat.png) | [Zima2-R](Zima2R_Specification_en.md) <br/> Responder-beacons (one base station can work with a maximum of 16 transponders in sequence) |
| ![Bat&Link Box](/documentation/batnlinkbox.png) | [Bat&Link Box](Bat_n_link_box_Specification_en.md) <br/> Autonomous power supply |

<div style="page-break-after: always;"></div>

## Tasks to be solved by the system
* Determining the location of up to 16 underwater objects in water area (tracking underwater objects)
* Relative location determination (**azimuth, distance, depth**)
* Absolute positioning (**latitude, longitude, azimuth, distance, depth**) when connected to an external **GNSS** and compass (or **GNSS with compass function**)

<div style="page-break-after: always;"></div>

## Distinctive features
* Compactness, long range and maximum ease of use make it possible to use the **Zima2** system to work with various **ROV** and **AUV**, as well as with **divers** in any combination
* High versatility of responders allows them to be used as a stand-alone version with a separate battery pack, as well as energetically and informationally connected with a vessel
* The system supports integration with external sources of navigation data: **GNSS** with compass function (connected to the control PC). In this case, the system determines the absolute geographical coordinates of underwater objects, allows you to save a track of movement of underwater objects and has GPS emulation functions for one of the selected beacons for integration with third-party software (for example, Hypack, SAS.Planet, etc.)
* Antenna Zima2-B is installed on a boom from almost any vessel, connected to a 12 V / 3.5 A power source, and to a control PC (Windows 10 and higher) - in this minimum configuration, the system determines the position of the responders (azimuth and distance) relative to the antenna. When a GNSS receiver with a compass function (**RMC, GGA, HDG**) is connected to the control PC, the system determines the geographic coordinates of the responders and can transmit them (**RMC, GGA**) to any serial port, thereby emulating a GNSS receiver for the selected responder beacon;
<div style="page-break-after: always;"></div>

| ![Zima2-B placement](/documentation/zima2_boat_gnss_1.png) |
| :---: |
| [Zima 2-B](Zima2B_Specification_en.md) deployment scheme <br/> _The antenna is mounted on a rigid rod so that it is no closer than 2 meters from the surface of the water and no closer than 1.5 meters from the bottom of the vessel. The antenna offsets relative to the geolocation point and the angular offset of the zero of the antenna and the GNSS compass are set_ |

<div style="page-break-after: always;"></div>

## Pairing schemes

### Work in relative coordinates
To determine the **relative location** of the responder beacons, the antenna is interfaced with a PC on which specialized open source software [AzimuthSuite](https://github.com/ucnl/AzimuthSuite) is installed. The antenna is connected to the PC via [Bat&Link Box](Bat_n_link_box_Specification_en.md), which converts the interface to USB and powers the antenna.

In this case, the following data and functions are available to the user:
* **Azimuth** (horizontal angle) to the used transponder beacons;
* **Distance** to responder beacons
* **Depths** of transponder beacons

| ![Zima2B relative scheme](/documentation/zima2_option1.png) |
| :---: |
| _Working in relative coordinates_ |

<div style="page-break-after: always;"></div>

### Working in absolute coordinates
To determine the **absolute location** of the responder beacons, the antenna is interfaced with a PC on which specialized control software [AzimuthSuite](https://github.com/ucnl/AzimuthSuite) is installed. The antenna is connected to the PC via [Bat&Link Box](Bat_n_link_box_Specification_en.md), which converts the interface to USB and powers the antenna. Additionally, an external **GNSS** system with compass function operating under the **NMEA 0183** protocol (**RMC** and **HDT** messages) is connected.

| ![Zima-B absolut scheme](/documentation/zima2_option2.png) |
| :---: |
| _Working in absolute coordinates_ |

In this case, the following data and functions are available to the user:
* Absolute **geographical coordinates** of responders and their depths
* **Azimuth** (relative to North)
* **Distance**
* Recording a track of the movement of underwater objects with the possibility of subsequent saving in Google KML format.

<div style="page-break-after: always;"></div>

## Geometric Constraints

Since the location of [Zima2-R](Zima2R_Specification_en.md) responder beacons is carried out by the horizontal angle of arrival of the signal, slant range and depth difference, the [Zima 2-B](Zima2B_Specification_en.md) direction finding station antenna array has the highest sensitivity in the range angles from 0° to 85° from the horizontal. The accuracy of the system when the responder is close to the nadir direction may be reduced.

| ![Zima2-B angular zones](/documentation/zima2_geometric_limitations.png) |
| :---: |
| Geometric constraints [Zima 2-B](Zima2B_Specification_en.md) <br/> _1 - DF antenna, 2 - upper hemisphere, 3 - working area (0° .. 85°, 0 .. -85°), 4 - area of accuracy reduction (85° .. -85°)_ |

<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [**Zima2 USBL**: User's manual](Zima2_Users_manual_en.md) |
| [**Zima2-R**: Responder beacon, device specification](Zima2R_Specification_en.md) |
| [**Zima2-B**: DF-antenna, device specification](Zima2B_Specification_en.md) |
| [**Bat&Link Box**: Autonomous power supply, device specification](Bat_n_link_box_Specification_en.md) |
| [**Zima2 USBL: Communication protocol specification**](Zima2_Protocol_Specification_en.md) |
