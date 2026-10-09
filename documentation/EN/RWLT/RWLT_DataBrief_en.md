[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![RWLT_Pack](/documentation/rwlt_pack_small.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT**<br/> Data brief |

<div style="page-break-after: always;"></div>

## General information
The **RWLT** system is **the easiest to use** while also providing an accurate solution for tracking an underwater object. The system **does not require any calibration** or integration: simply attach an autonomous [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon to an underwater object (ROV, AUV, diver, etc.) and place four [RWLT GIB](RWLT_GIB_Specification_en.md) navigation buoys on the water surface. This configuration allows the movement of an underwater object to be tracked in real time in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is its ability to use [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver telephone stations as pingers, thus combining two-way voice communication and navigation.

When used with a pinger, the [uNav RWLT RF Dongle](RWLT_RF_Dongle_en.md) navigation receiver emulates the protocol of conventional GNSS receivers and can be connected to any software that supports displaying the position of a GNSS receiver on a map, such as Google Earth, SAS.Planet, etc.

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![RWLT GIB](/documentation/rwlt_gib_h_small.png) | [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> Navigation sonobuoy (receiver) |
| ![RWLT Pinger](/documentation/dev_big_wbat_li_small.png) | [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger beacon |
| ![RWLT RF dongle](/documentation/uNav_rf_dongle.png) | [uNav RWLT RF Dongle](RWLT_RF_Dongle_en.md) <br/> Digital radio receiver |

The minimum system configuration includes four [RWLT GIB](RWLT_GIB_Specification_en.md) sonobuoys and one transmitting device, depending on the user's task:
* If a diver needs navigation data along with voice communication, a [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver telephone station is used. In this case, the diver's position is determined when they release the PTT button, i.e., finish transmitting a voice message;
* If the position of a remotely operated vehicle (ROV) or a diver needs to be determined without voice communication, an [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon is used. The pinger operates autonomously, and the position of the object to which it is attached is updated every two seconds.

### When used with a pinger

Simply connect the navigation receiver to any chartplotter that supports [NMEA0183 RMC and GGA](uNav_protocol_specification_en.md) messages. In this configuration, the user has access to:
- the geographic position of the object to which the pinger is attached
- the object's course of movement

When using the open source [uNav](https://github.com/ucnl/uNav/releases/download/1.0/uNav.zip) application, the following are also available:
- the positions of the navigation buoys and the charge levels of their built-in power sources;
- the course and range to a reference point, which the user can select as one of the four buoys, the built-in navigation receiver [uNav RWLT RF Dongle](RWLT_RF_Dongle_en.md), or a point with an arbitrarily specified coordinate;
- water temperature;
- pinger supply voltage;

### When used with RedPhone-DX diver stations

The open source [uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip) application is required. In this case, the user has access to the positions of up to 255 divers, determined at the end of each voice transmission from a diver.


<div style="page-break-after: always;"></div>

## Tasks to be solved
* Tracking the position of an underwater object in real time (divers, ROVs, AUVs, etc.);
* Determining the course of movement of an underwater object;
* Assistance in guiding an underwater object to a surface control point, and vice versa;

<div style="page-break-after: always;"></div>

## Distinctive features
* Operation in absolute geographic coordinates;
* A floating base of four sonobuoys allows tracking of both an [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger and a [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver telephone station;
* No preliminary setup or calibration of the system or its components is required;
* No data interface is required between the object and the pinger: the pinger is mechanically attached to the underwater carrier;
* Transfer of the calculated position of an underwater object to third-party software via a serial port using the NMEA0183 protocol;
* Recording the movement track of an underwater object;

<div style="page-break-after: always;"></div>

## Geometric limitations
* _The distance between any two buoys must be no more than 1500 meters and no less than 30 meters_
* _The buoys must be arranged in a convex quadrilateral so that its sides are approximately equal and differ by no more than a factor of 2_
* _The maximum diving depth of the pinger must not exceed the dimensions of the navigation base_
* _The greatest system accuracy is achieved within the polygon formed by the buoys, and operation must always begin within this polygon. Operation outside the polygon is possible, but accuracy may decrease significantly as the object being positioned moves away from the buoy polygon_

<div style="page-break-after: always;"></div>

_________  

<!-- docs-sync: source=documentation/RU/RWLT/RWLT_DataBrief_ru.md commit=aba65119297af8b6f40a400139c44460f30a367b date=2024-04-11 -->
