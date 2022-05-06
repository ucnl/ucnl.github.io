[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - Underwater tracking system <br/> Data brief|

<div style="page-break-after: always;"></div>

## General information
**RWLT** system is **the easiest to use** and at the same time accurate solution for tracking an underwater object. The system **does not require any calibrations** and integration: it is enough to place an autonomous pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) on an underwater object (ROV, AUV, diver, etc.), and four navigation buoys on the water surface [RWLT GIB](RWLT_GIB_Specification_en.md). This configuration allows real-time tracking of the movement of an underwater object in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to work simultaneously with wireless underwater telephone [RedPhone](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_Specification_en.html) as a pinger, thus combining two-way voice communication and navigation.

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![RWLT GIB](/documentation/RWLT_GIB.png) | [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> Hydroacoustic navigation buoy |
| ![RWLT Pinger](/documentation/RWLT_Pinger.png) | [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger beacon |
| ![RWLT RF Dongle](/documentation/RWLT_RF_Dongle.png) | [RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) <br/> Digital RF dongle |

The minimum composition of the system includes four sonar buoys [RWLT GIB](RWLT_GIB_Specification_en.md) and one transmitting device, depending on the user's task:
* If it is required to provide a diver with navigation data simultaneously with voice communication, then the diving telephone exchange [RedPhone](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_Specification_en.html) is used; In this case, the geo-position of the diver will be determined at the moment when he releases the PTT button, i.e. ends the transmission of a voice message;
* If it is required to determine the location of a remotely controlled vehicle (ROV, AUV), or a diver without the need to use voice communication, then a pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) is used. The pinger works autonomously and the location of the object on which the pinger is attached will be updated every two seconds.

To work on a PC, specialized open-source software is installed [uTrack](https://github.com/ucnl/uTrack), which displays:
- current geographic position of the underwater object (longitude, latitude)
- depth
- water temperature
- the voltage of the built-in battery
- the geographic location of the buoys and voltages of their built-in batteries
- when an external GPS is connected, the position of the surface tracking point, distance and course to the underwater object is displayed

<div style="page-break-after: always;"></div>

## Tasks to be solved
* Tracking the position of an underwater object in real time (divers, ROV, AUV, etc.);
* Determination of the course of movement of an underwater object;
* Assistance in driving the underwater object to the surface control point and vice versa;

<div style="page-break-after: always;"></div>

## Distinctive features
* Work in absolute geographic coordinates;
* A floating base of four sonar devices provides security both behind the pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md), and behind the diving telephone exchange [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html);
* No preliminary setup and calibration of the system and its components is required;
* No informational pairing of the object with the pinger is required - the pinger is mechanically fixed on the underwater carrier;
* Transfer of the calculated position of the underwater object to third-party software via the serial port using the NMEA0183 protocol;
* Recording the track of the movement of an underwater object;
* Ability to connect an additional GPS receiver to record the track of a surface tracking location (vessel).

<div style="page-break-after: always;"></div>

## Geometric limitations
* _From each to each of the buoys there must be no more than 1500 meters and no less than 30 meters_
* _Buys should be located in apexes of a convex quadrilateral so that its sides are approximately equal and differ by no more than 2 times_
* _Maximum pinger immersion depth should not exceed the size of the navigation base_
* _The greatest system accuracy is achieved inside the buoy figure, and work should always start inside this figure. It is possible to go beyond the figure, but the accuracy can be significantly reduced as the positioned object moves away from the buoy figure_

<div style="page-break-after: always;"></div>

_________  

<div style="page-break-after: always;"></div>

