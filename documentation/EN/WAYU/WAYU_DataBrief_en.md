[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **WAYU: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/28f252cd-a7e7-414a-a546-b737147c19dd) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU** - Underwater tracking system <br/> Data brief |

<div style="page-break-after: always;"></div>

## General info
**WAYU** stands for **W**here **A**re **Y**ou **U**nderwater.
The **WAYU** system is a reliable and easy-to-use solution for the amateur segment. The user places a pinger beacon [WAYU Pinger](WAYU_Pinger_Specification_en.md) on the positioned object (ROV, AUV, diver, etc.) and four small navigation buoys [WAYU GIB](WAYU_GIB_Specification_en.md) on the surface of the water body.
From this moment on, the absolute geographic position of the underwater object is displayed on the PC screen, where specialized open-source software [WAYU](https://github.com/ucnl/WAYU) is installed. The position of the underwater object can be easily transmitted from the [WAYU](https://github.com/ucnl/WAYU) application via a serial port (physical or virtual) to any mapping software that supports work with conventional GPS receivers via the NMEA0183 protocol.
Both the pinger and **WAYU** buoys turn on automatically when they hit the water, do not require any settings or calibrations except for charging the built-in power sources.

<div style="page-break-after: always;"></div>

## System composition

| | |
| :---: | :--- |
| ![wayu_pinger](/documentation/RT_1_332820_1.png) | [WAYU Pinger](WAYU_Pinger_Specification_en.md) <br/> Navigation hydroacoustic beacon-pinger |
| ![WAYU_GIB_](https://github.com/user-attachments/assets/2adaa0a0-2f97-4ba9-897c-cd4edc409028) | [WAYU GIB](WAYU_GIB_Specification_ru.md) <br/> Navigation buoy |
| ![uNav_WAYU_RF_Dongle](https://github.com/user-attachments/assets/0ec0811b-8283-460a-9036-9460f6c780c3) | [WAYU Radio dongle](WAYU_RF_Dongle_Specification_en.md) <br/> Radio dongle - navigation buoy receiver |

<div style="page-break-after: always;"></div>

## Tasks to be solved
- Determining the geographic location of an underwater object in real time
- Recording the track of the underwater object
- Determining the course of the underwater object
- Emulating the GPS protocol for transmitting the location of an underwater object to mapping software

<div style="page-break-after: always;"></div>

## Distinctive features
- Professional solution at an affordable price
- Positioning of an underwater object in absolute geographic coordinates
- Extremely easy to use
- Automatic switching on from water
- Works "out of the box" - does not require any calibrations or settings

<div style="page-break-after: always;"></div>

## Geometrical limitations
* _From each to each of the buoys should be no more than 300 meters and not less than 30 meters_
* _From each buoy to the navigation receiver should be no more than 300 meters; to ensure reliable reception of the radio signal from the buoys, it may be necessary to raise the receiving antenna several meters higher_
* _The buoys should be positioned in a convex quadrangle so that its sides are approximately equal and differ by no more than 2 times_
* _The maximum immersion depth of the pinger should not exceed the dimensions of the navigation base_
* _The greatest accuracy of the system is achieved inside the buoy figure, and work should always begin inside this figure. Going beyond the figure is possible, but the accuracy in this case can significantly decrease as the positioned object moves away from the buoy figure_
<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [Videos, Tutorials, Tracks, etc.](media.md) |

