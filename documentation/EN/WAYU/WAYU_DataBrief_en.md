| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU** - Underwater tracking system <br/> Data brief |

<div style="page-break-after: always;"></div>

## General info
**WAYU** stands for **W**here **A**re **Y**ou **U**nderwater.
The **WAYU** system is a reliable and easy-to-use solution for the amateur segment. The user places a pinger beacon [WAYU Pinger](WAYU_Pinger_Specification_en.md) on the positioned object (ROV, AUV, diver, etc.), and on the surface of the reservoir four small navigation buoys [WAYU GIB](WAYU_GIB_Specification_en.md).
From this moment on, the absolute geographic position of the underwater object is displayed on the PC screen, where the specialized software [WAYU](https://github.com/ucnl/WAYU) open source is installed. The position of an underwater object can be easily transferred from the [WAYU](https://github.com/ucnl/WAYU) application via a serial port (physical or virtual) to any mapping software that supports work with conventional GPS receivers via the NMEA0183 protocol.
Both the pinger and **WAYU** buoys turn on automatically when they touch the water, do not require any adjustments or calibrations other than charging the built-in power supplies.

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![WAYU Pinger]() | [WAYU Pinger](WAYU_Pinger_Specification_ru.md) <br/> Underwater pinger beacon |
| ![WAYU GIB]() | [WAYU GIB](WAYU_GIB_Specification_ru.md) <br/> Navigation buoy |
| ![WAYU Radio dongle](/documentation/wayu_rf_dongle.png) | [WAYU Radio dongle](WAYU_RF_Dongle_Specification_ru.md) <br/> RF dongle |


<div style="page-break-after: always;"></div>

## Tasks to be solved
- Determination of the geographic location of an underwater object in real-time
- Recording the track of the movement of an underwater object
- Determination of the course of movement of an underwater object
- Emulation of GPS protocol for transferring the location of an underwater object to any GIS software that supports conventional GPS-receivers

<div style="page-break-after: always;"></div>

## Distinctive features
- Professional solution at an affordable price
- Positioning an underwater object in absolute geographic coordinates
- The most simple use
- Automatic turn-on in water
- Work "out of the box" - does not require any calibrations and settings

<div style="page-break-after: always;"></div>

## Geometric limitations
* _From each to each of the buoys there should be no more than 300 meters and no less than 30 meters_
* _Buys should be located in apexes of a convex quadrilateral so that its sides are approximately equal and differ by no more than 2 times_
* _Maximum pinger immersion depth should not exceed the size of the navigation base_
* _The greatest system accuracy is achieved inside the buoys figure, and work should always start inside this figure. It is possible to go beyond the figure, but the accuracy can be significantly reduced as the positioned object moves away from the buoy figure_  

<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [Videos, Tutorials, Tracks, etc.](media.md) |

