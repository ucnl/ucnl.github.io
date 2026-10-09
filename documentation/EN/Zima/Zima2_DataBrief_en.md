[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 USBL: Data brief**

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

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima_package.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima 2 USBL** <br/> Data brief |

<div style="page-break-after: always;"></div>

## General information
**Zima 2 USBL** is an underwater acoustic ultra-short baseline (USBL) navigation system designed to determine the location of underwater objects marked with acoustic responder-beacons [Zima2-R](Zima2R_Specification_en.md) using a direction-finding transceiver antenna [Zima2-B](Zima2B_Specification_en.md).

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![Zima2-B](/documentation/zima_b_wcable.png) | [Zima2-B](Zima2B_Specification_en.md) <br/> Direction-finding base station (with [UART-RS422](/documentation/EN/Accessories/RS422_extension_cable_en.html) extension cable) |
| ![Zima2-R](/documentation/zima_r_wbat.png) | [Zima2-R](Zima2R_Specification_en.md) <br/> Responder-beacons (one base station can work sequentially with a maximum of 16 responders) |
| ![Bat&Link Box](/documentation/batnlinkbox.png) | [Bat&Link Box](Bat_n_link_box_Specification_en.md) <br/> Autonomous power supply and switching unit for the base station |

<div style="page-break-after: always;"></div>

## Tasks to be solved
* Determining the location of up to 16 underwater objects in the water area (tracking underwater objects)
* Determining the relative location (**azimuth, distance, depth**)
* Determining the absolute location (**latitude, longitude, azimuth, distance, depth**) when connected to an external **GNSS** and compass (or **GNSS with compass function**)

<div style="page-break-after: always;"></div>

## Distinctive features
* Compactness, long range and maximum ease of use make it possible to use the **Zima2** system to work with various **ROVs** and **AUVs**, as well as with **divers**, in any combination
* The highly versatile beacons can be used either in a standalone version with a separate battery pack or integrated with the carrier for both power and data
* The system supports integration with external sources of navigation data: **GNSS** with compass function (connected to the host PC). In this case, the system determines the absolute geographic coordinates of underwater objects, allows saving the track of movement of underwater objects and has GPS emulation functions for one of the selected beacons for integration with third-party software (for example, Hypack, SAS.Planet, etc.)
* The ZIMA2-B antenna is mounted on a pole over the side of almost any vessel and connected to a 12 V / 3.5 A power source and to a host PC (Windows 10 or later) – in this minimum configuration, the system determines the position of the beacons (azimuth and distance) relative to the antenna. When a GNSS receiver with compass function (**RMC, GGA, HDG**) is connected to the host PC, the system determines the geographic coordinates of the beacons and can transmit them (**RMC, GGA**) to any serial port, thereby emulating a GNSS receiver for the selected responder-beacon;

<div style="page-break-after: always;"></div>

| ![Zima2-B placement](/documentation/zima2_boat_gnss_1.png) |
| :---: |
| Installation diagram of the [Zima 2-B](Zima2B_Specification_en.md) antenna <br/> _The antenna is mounted on a rigid pole so that it is no closer than 2 meters to the surface of the water and no closer than 1.5 meters to the lowest point of the vessel. The antenna offsets relative to the position reference point and the angular offset between the antenna zero and the GNSS compass are set_ |

<div style="page-break-after: always;"></div>

## Interfacing schemes

### Working in relative coordinates
To determine the **relative location** of the responder-beacons, the antenna is interfaced with a PC on which specialized open-source host software [AzimuthSuite](https://github.com/ucnl/AzimuthSuite) is installed. The antenna is connected to the PC via [Bat&Link Box](Bat_n_link_box_Specification_en.md), which converts the interface to USB and powers the antenna.

In this case, the data and functions available to the user are:
* **Azimuth** (horizontal angle) to the responder-beacons in use;
* **Distance** to the responder-beacons
* Depths of the responder-beacons

| ![Zima2B relative scheme](/documentation/zima2_option1.png) |
| :---: |
| _Wiring diagram for working in relative coordinates_ |

<div style="page-break-after: always;"></div>

### Working in absolute coordinates
To determine the **absolute location** of the responder-beacons, the antenna is interfaced with a PC on which specialized host software [AzimuthSuite](https://github.com/ucnl/AzimuthSuite) is installed. The antenna is connected to the PC via [Bat&Link Box](Bat_n_link_box_Specification_en.md), which converts the interface to USB and powers the antenna. Additionally, an external **GNSS** system with compass function, operating via the **NMEA 0183** protocol (**RMC** and **HDT** sentences), is connected.

| ![Zima-B absolut scheme](/documentation/zima2_option2.png) |
| :---: |
| _Wiring diagram for working in absolute coordinates_ |

In this case, the following data and functions are available to the user:
* Absolute **geographic coordinates** of the beacons and depth
* **Azimuth** (relative to north)
* **Distance**
* Recording a track of the movement of underwater objects with the possibility of subsequent saving in Google KML format.

<div style="page-break-after: always;"></div>

## Geometric limitations

Since the location of the [Zima2-R](Zima2R_Specification_en.md) responder-beacons is determined from the horizontal angle of arrival of the signal, the slant range and the depth difference, the antenna array of the [Zima 2-B](Zima2B_Specification_en.md) direction-finding station has the highest sensitivity in the angle range from 0° to 85° from the horizontal. The system accuracy may decrease when the responder-beacon is close to the nadir direction.

| ![Zima2-B angular zones](/documentation/zima2_geometric_limitations.png) |
| :---: |
| Geometric limitations of [Zima 2-B](Zima2B_Specification_en.md) <br/> _1 - Direction-finding antenna, 2 - upper hemisphere, 3 - working zone (0° .. 85°, 0 .. -85°), 4 - accuracy reduction zone (85° .. -85°)_ |

<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [**Zima 2 USBL**: User's manual](Zima2_Users_manual_en.md) |
| [Responder-beacon **Zima 2-R**: device specification](Zima2R_Specification_en.md) |
| [Direction-finding station **Zima 2-B**: device specification](Zima2B_Specification_en.md) |
| [Power supply and switching unit **Bat&Link Box**: device specification](Bat_n_link_box_Specification_en.md) |
| [Communication protocol specification for the devices of the **Zima 2 USBL** system](Zima2_Protocol_Specification_en.md) |

<!-- docs-sync: source=documentation/RU/Zima/Zima2_DataBrief_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
