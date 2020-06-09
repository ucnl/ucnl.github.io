| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedWAVE**<br/> Data brief |

## General information
**RedWAVE** - the only system in the world that implements the so-called "underwater GPS", following the ideology of satellite 
navigation systems as closely as possible, it allows an unlimited number of underwater objects, such as divers and various mobile robots (ROV, AUV, etc.) to determine
its geographical location and depth in real-time.

**RedWAVE** is a long-base (LBL, long-baseline) navigation system. The floating navigation base is formed by four small-sized
sonobuoys [RedBASE](RedBASE_Specification_en.md); with the support of the base can simultaneously work
unlimited number of underwater objects equipped with navigation receivers [RedNODE](RedNODE_Specification_en.md) and divers using diving 
navigators [RedNAV](RedNAV_Specification_en.md).

## System composition

|  |  |
| :---: | :--- |
| ![RedBASE](https://ucnl.github.io/documentation/def_redbase_yellow.png) | [RedBASE](RedBASE_Specification_en.md) <br/> GNSS-equipped sonobuoy |
| ![RedNODE](https://ucnl.github.io/documentation/def_modem_black.png) | [RedNODE](RedNODE_Specification_en.md) <br/> Navigation receiver |
| ![RedNAV](https://ucnl.github.io/documentation/def_rednav_yellow.png) | [RedNAV](RedNAV_Specification_en.md) <br/> Diver's navigation received |

The minimum composition of the system includes four sonobuoys [RedBASE](RedBASE_Specification_en.md) and one receiving device, 
depending on the user task:
* If you want to provide navigation data to the diver, then use the diving navigator [RedNAV](RedNAV_Specification_en.md);
* If it is required to estimate the location of the remote-controlled device (ROV, AUV), then the navigation receiver 
[RedNODE](RedNODE_Specification_en.md) is used, which is interfaced with the vessel, and the data generated at the receiver must be 
transmitted via the cable of the device to the control panel, where they can be displayed on any mapping software that supports the 
connection of standard GNSS receivers (RMC and GGA messages).

## Tasks to be solved
* Simultaneous determination of 3D geographical position by an unlimited number of underwater objects (divers, ROV, AUV, etc.);
* Recording tracks of divers moving;
* Pre-loading waypoints, navigation to loaded points, saving (marking) the current position of the diver;

## Distinctive features
* Work in absolute geographical coordinates;
* A floating base of four sonobuoys is enough for an unlimited number of navigation receivers;
* No preliminary adjustment and calibration of the system and its components is required;
* Small size and power consumption of navigation receivers;
* Emulation of the protocol of standard GNSS receivers for integrated devices


## Geometric restrictions
In view of the fact that **RedWAVE** system uses modern technology of digital broadband acoustic communication, the signals emitted by 
buoys have a significant duration (about 200 milliseconds). The buoy signals have time and code division multiplexing, and in view of 
the finiteness of the speed of sound propagation in water and the period of emission of signals, under certain conditions, the signals 
can overlap each other at the receiving point. There are also limitations associated with the physical basis of the long navigation base.
Therefore, the system has a restriction on the relative position of navigation sonobuoys, and navigation receivers relative to buoys:
* _From each to each of the buoys there should be no more than 700 meters and not less than 30 meters_
* _Buoys should be located with a convex quadrangle so that its sides are approximately equal and differ by no more than 2 times_
* _Maximum immersion depth of navigation receivers should not exceed the size of the navigation base_
* _The highest accuracy of the system is achieved inside the figure of buoys, and work should always begin inside this figure. 
Going beyond the limits of the figure is possible, however, the accuracy can significantly decrease as the positioned object moves away 
from the figure of buoys_

_________  

| **Additional information** |
| :--- |
| [Video, tracks etc.](media.md) |
| [RedBASE - GNSS-equipped sonobuoy: Device specification](RedBASE_Specification_en.md) |
| [RedNAV - Diver's navigation receiver: Device specification](RedNAV_Specification_en.md) |
| [RedNODE - navigation receiver: Device specification](RedNODE_Specification_en.md) |
| [RedWAVE - RedNODE interfacing protocol description](RedWAVE_Protocol_Specification_en.html) |
| [RedWAVE - User's manual]() |
