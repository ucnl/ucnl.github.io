[Main](/) ❯ [Educational projects](/educational_projects_en) ❯ **WAYU: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/bddf7931-4682-4c58-b804-9f3aab1e8d4b) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU** - Underwater acoustic tracking system <br/> Data brief |

<div style="page-break-after: always;"></div>

## General information
**WAYU** stands for **W**here **A**re **Y**ou **U**nderwater.  
The **WAYU** system is a reliable and easy-to-use solution for the amateur segment. The user places a pinger beacon [WAYU Pinger](WAYU_Pinger_Specification_en.md) on the positioned object (ROV, AUV, diver, etc.) and four small navigation buoys [WAYU GIB](WAYU_GIB_Specification_en.md) on the surface of the water body.
From this moment on, the absolute geographic position of the underwater object is displayed on the PC screen, where specialized open-source software [WAYU](https://github.com/ucnl/WAYU) is installed. The position of the underwater object can be easily transmitted from the [WAYU](https://github.com/ucnl/WAYU) application via a serial port (physical or virtual) to any mapping software that supports work with conventional GPS receivers via the NMEA0183 protocol.
Both the pinger and the **WAYU** buoys turn on automatically when they enter the water and do not require any settings or calibrations except for charging the built-in power sources.

<div style="page-break-after: always;"></div>

## System composition

|  |  |
| :---: | :--- |
| ![wayu_pinger](/documentation/RT_1_332820_1.png) | [WAYU Pinger](WAYU_Pinger_Specification_en.md) <br/> Underwater acoustic navigation pinger beacon |
| ![WAYU_GIB_1(1)(1)](https://github.com/user-attachments/assets/2adaa0a0-2f97-4ba9-897c-cd4edc409028) | [WAYU GIB](WAYU_GIB_Specification_en.md) <br/> Navigation buoy |
| ![uNav_WAYU_RF_Dongle](https://github.com/user-attachments/assets/0ec0811b-8283-460a-9036-9460f6c780c3) | [WAYU Radio dongle](WAYU_RF_Dongle_Specification_en.md) <br/> Radio dongle - navigation buoy receiver |


<div style="page-break-after: always;"></div>

## Tasks to be solved
- Determining the geographic location of an underwater object in real time
- Recording the movement track of an underwater object
- Determining the course of movement of an underwater object
- Emulating the GPS protocol for transmitting the location of an underwater object to mapping software

<div style="page-break-after: always;"></div>

## Distinctive features
- Professional solution at an affordable price
- Positioning of an underwater object in absolute geographic coordinates
- Maximum ease of use
- Automatic activation in water
- Works "out of the box" - does not require any calibrations or settings

<div style="page-break-after: always;"></div>

## Geometric limitations
* _The distance between any two buoys must be no more than 300 m and no less than 30 m_
* _The distance from each buoy to the navigation receiver must be no more than 300 m; to ensure reliable reception of the radio signal from the buoys, it may be necessary to raise the receiving antenna several meters higher_
* _The buoys should be arranged in a convex quadrangle so that its sides are approximately equal and differ by no more than a factor of 2_
* _The maximum immersion depth of the pinger should not exceed the dimensions of the navigation base_
* _The greatest accuracy of the system is achieved inside the buoy figure, and work should always begin inside this figure. Going beyond the figure is possible, but the accuracy in this case can significantly decrease as the positioned object moves away from the buoy figure_

<div style="page-break-after: always;"></div>

_________  

| **Additional information** |
| :--- |
| [System test videos, tracks obtained during operation in real conditions](media.md) |

<!-- docs-sync: source=documentation/RU/WAYU/WAYU_DataBrief_ru.md commit=a1dbdfb7e340f61cc5561303f8d0ff70928825a7 date=2025-06-04 -->
