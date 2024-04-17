[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - Underwater tracking system <br/> Data brief |

<div style="page-break-after: always;"></div>

## General information
The **RWLT** system is **the easiest to use** and at the same time accurate solution for tracking underwater objects. The system **does not require any calibration** and integration: it is enough to place an autonomous pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) on an underwater object (ROV, AUV, diver, etc.), and four navigation buoys on the surface of the water [RWLT GIB](RWLT_GIB_Specification_en.md). This configuration allows the user to monitor in real time the movement of an underwater object in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to work with diver's wireless telephone [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) as a pinger, thus combining two-way voice communications and navigation.

When working with a pinger, the navigation receiver [uNav RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) emulates the protocol of conventional GNSS receivers, and it can be connected to any software that supports displaying the position of a GNSS receiver on the map. For example, GoogleEarth, SAS.Planet, etc.
<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![RWLT GIB](/documentation/rwlt_gib_h_small.png) | [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> GNSS-equipped sonobuoy |
| ![RWLT Pinger](/documentation/dev_big_wbat_li_small.png) | [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger-beacon |
| ![RWLT RF dongle](/documentation/uNav_rf_dongle.png) | [uNav RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) <br/> Navigation receiver/RF dongle |

The minimum set includes four sonobuoys [RWLT GIB](RWLT_GIB_Specification_en.md) and one transmitting device, depending on the user task:
* If it is necessary to provide the diver with navigation data simultaneously with voice communication, then a diver's wireless telephone [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) is used; In this case, the diver's geoposition will be determined at the moment when he releases the PTT button, i.e. ends the transmission of a voice message;
* If it is necessary to determine the location of a remotely controlled vehicle (ROV) or a diver without the need to use voice communication, then a pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) is used. The pinger works autonomously and the geoposition of the object on which the pinger is attached will be updated every two seconds.

### When working with pinger

It is enough to simply connect the navigation receiver to any card plotter that supports [NMEA0183 RMC and GGA](uNav_protocol_specification_en.md) messages. In this option, the user has access to:
- geographic location of the object on which the pinger is attached
- course of movement of the object

When using the open source application [uNav](https://github.com/ucnl/uNav/releases/download/1.0/uNav.zip), the following additionally become available:
- positions of navigation buoys and charge of their built-in power sources;
- course and range to the reference point, for which the user can select one of four buoys, the built-in navigation receiver [uNav RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) or a point with an arbitrarily specified coordinate;
- water temperature & depth;
- pinger supply voltage;

### When working with RedPhone-DX wireless diver's telephone

Requires open source application [uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip). In this case, the user has access to the positions of up to 255 divers, determined at the end of each voice transmission from the diver.


<div style="page-break-after: always;"></div>

## Solved problems
* Monitoring the position of an underwater object (divers, ROVs, AUVs, etc.);
* Determining the course of movement of an underwater object;
* Assistance in driving an underwater object to a surface control point and back;

<div style="page-break-after: always;"></div>

## Distinctive features
* Work in absolute geographical coordinates;
* A floating base of four sonobuoys allows you to monitor both the pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md) and the diving telephone exchange [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/ RedPhone_DX_Specification_en.html);
* No preliminary configuration and calibration of the system and its components is required;
* No information connection between the object and the pinger is required - the pinger is mechanically attached to the underwater carrier;
* Transferring the calculated position of an underwater object to third-party software via a serial port using the NMEA0183 protocol;
* Recording the movement track of an underwater object;

<div style="page-break-after: always;"></div>

## Geometric limitations
* _From each to each of the buoys there should be no more than 1500 meters and no less than 30 meters_
* _The buoys should be arranged in a convex quadrangle so that its sides are approximately equal and differ by no more than 2 times_
* _The maximum diving depth of the pinger should not exceed the dimensions of the navigation base_
* _The greatest accuracy of the system is achieved within the buoy figure, and work should always begin within this figure. Exiting the figure is possible, but the accuracy may decrease significantly as the positioned object moves away from the buoy figure_

<div style="page-break-after: always;"></div>

_________  

