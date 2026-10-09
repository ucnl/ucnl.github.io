[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: User's manual**

> ℹ This document can be printed directly from your browser.
> For best results:
> - select the range of pages to print, excluding the first and last
> - in advanced settings, disable footers and headers

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![](/documentation/rwlt_qr_manual_ru.png)  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - underwater acoustic tracking system <br/> User's manual |

# RWLT <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents

- [1. Introduction](#1-introduction)
  - [1.1. Purpose](#11-purpose)
  - [1.2. Features](#12-features)
  - [1.3. System composition](#13-system-composition)
- [2. Working with the RWLT system](#2-working-with-the-rwlt-system)
  - [2.0. Before operation](#20-before-operation)
  - [2.1. Preparation for operation and equipment check](#21-preparation-for-operation-and-equipment-check)
    - [2.1.2. Checking the buoy set](#212-checking-the-buoy-set)
      - [2.1.2.1. Charging the built-in power supply](#2121-charging-the-built-in-power-supply)
      - [2.1.2.2. Connecting the service cable](#2122-connecting-the-service-cable)
    - [2.1.3. Positioning the buoys on the water surface](#213-positioning-the-buoys-on-the-water-surface)
    - [2.1.4. Preparing the underwater equipment](#214-preparing-the-underwater-equipment)
    - [2.1.5. Preparing the radio dongle for operation](#215-preparing-the-radio-dongle-for-operation)
    - [2.1.6. Selecting a location for the operator console](#216-selecting-a-location-for-the-operator-console)
  - [2.2. Working with the system](#22-working-with-the-system)
  - [2.3. After operation](#23-after-operation)
- [3. Obligations and disclaimer](#3-obligations-and-disclaimer)
  - [3.1. Terms of replacement and free warranty service](#31-terms-of-replacement-and-free-warranty-service)
  - [3.2. Limitation of the manufacturer's liability](#32-limitation-of-the-manufacturers-liability)

<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1. Purpose

The underwater acoustic tracking system **RWLT** is designed for:

- determining the geographic location and depth of an underwater object (**AUV**, **ROV**, **HOV**, divers, etc.) equipped with a standalone [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon. In this system configuration, it is possible to track the position of one object equipped with a standalone pinger beacon.
- determining the geographic location of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless diver voice communication transceivers. In this system configuration, it is possible to track the position of 255 divers in one operating area.

### 1.2. Features

The **RWLT** system uses modern digital broadband noise-resistant underwater acoustic communication technology, and the signal used is specially designed for difficult hydrological conditions, including conditions typical of shallow bodies of water.

The **RWLT** system is **the easiest to use** and at the same time an accurate solution for tracking an underwater object. The system **does not require any calibration** or integration: simply place a standalone [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon on an underwater object (ROV, AUV, diver, etc.), and four [RWLT GIB](RWLT_GIB_Specification_en.md) navigation buoys on the water surface. This configuration allows you to monitor the movement of an underwater object in real time in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to use [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver telephone stations as pingers, thus combining two-way voice communication and navigation.

### 1.3. System composition

The minimum system composition includes:

- **Four sonobuoys** [RWLT GIB](RWLT_GIB_Specification_en.md):

| ![RWLT GIB](/documentation/rwlt_gib_h_small.png) |
| :---: |
| [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> Navigation receiving sonobuoy |

- A navigation solver/radio modem/dongle with a built-in GNSS receiver, [uNav RWLT RF Dongle](RWLT_RF_Dongle_en.md), for receiving navigation information from the buoys:

| ![RWLT RF Dongle](/documentation/uNav_rf_dongle.png) |
| :---: |
| [RWLT RF Dongle](RWLT_RF_Dongle_en.md) <br/> Digital radio receiver |

- A [Bat&Link Box](https://docs.unavlab.com/documentation/EN/Zima/Bat_n_link_box_Specification_en.html) autonomous power supply and interface converter, to which the radio modem/dongle is connected.

| ![Bat&Link Box](/documentation/batnlinkbox.png) |
| :---: |
| [Bat&Link Box](https://docs.unavlab.com/documentation/EN/Zima/Bat_n_link_box_Specification_en.html) <br/> Autonomous power supply and interface converter |


And, depending on the user's task:  
* If the location of divers needs to be determined simultaneously with voice communication, **up to 255** [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver telephone stations are used;

| ![RedPhone-DX](/documentation/redphone_dx.png) |
| :---: |
| [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) <br/> Wireless voice communication diver station |

In this configuration, the divers' geographic positions will be determined when they release the PTT button, i.e. finish transmitting a voice message; voice messages must be transmitted in turn.

* If the location of a remotely operated vehicle (ROV), or a diver without a need for voice communication, needs to be determined, **1** [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon is used. The pinger operates autonomously, and the geographic position of the object to which the pinger is attached will be updated every two seconds.

| ![RWLT Pinger](/documentation/dev_big_wbat_li_small.png) |
| :---: |
| [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger beacon |


## 2. Working with the RWLT system

### 2.0. Before operation
Depending on whether you are working with a pinger or tracking the movements of divers, you will need different versions of specialized software.

- To track an underwater object equipped with a standalone [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger, the [uNav](https://github.com/ucnl/uNav/releases/download/1.0/uNav.zip) application must be installed on the operator's PC. Before starting work, be sure to read the short user's manual: [uNav application: User's manual](uNav_application_Users_manual_en.md)

- To track the position of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diver stations, the [🤿 uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip) application must be installed on the operator's PC. Before starting work, be sure to read the short user's manual: [🤿 uTrackDiver application: User's manual](uTrackDiver_Users_Manual_en.md)

Download the required software in advance. Installation is not required - just unpack the contents of the archive to any convenient location.

Regardless of the underwater equipment used - wireless voice communication diver stations or a standalone pinger beacon - make sure that all equipment is fully charged before going out on the water and, if necessary, charge all devices.

Since the devices have built-in power supplies based on **LiFePO4**, they have a very flat discharge characteristic, and it is difficult to determine the charge level of the built-in power supply. Therefore, it is recommended to charge all devices no earlier than 1–2 days before use.

### 2.1. Preparation for operation and equipment check

#### 2.1.2. Checking the buoy set

- Make sure that all buoys of the set are intact, paying special attention to the transducer cable;
- Make sure that all buoys are operational and that their built-in power supplies are sufficiently charged. To do so, turn them on by placing the bottom part of each buoy in the water.
- Make sure that silicone grease is applied to the bronze contacts of the buoy's upper block.

The buoys have two-color light indication, with LEDs located in the upper part of the device under a layer of transparent compound. One indicator is intended to indicate the presence of the device on the water and lights up briefly 1 time per second; the other provides information about the device's status.

The buoys in each set have different addresses from 1 to 4. When a buoy is switched on, it reports its number in the set through the information indicator: the number of flashes corresponds to the buoy number.

After reporting its number, the buoy enters operating mode. If the buoy battery is charged, the information indicator stays lit continuously until the built-in GNSS receiver detects signals from the satellites of the global satellite navigation system. It will then flash 1 time every 4 seconds. The number of flashes in this case also corresponds to the buoy's number in the set.

If the buoy battery has less than 20% charge remaining, the information indicator will flash 1 time per second. The number of flashes in this case also corresponds to the buoy's number in the set.

> If the user notices that **both** indicators flash 1 time per second, the buoy should be switched off and put on charge as soon as possible.
> Prolonged operation with a discharged power supply is not allowed.

If the battery is critically discharged, the buoy will switch off automatically after reporting its number; in this case, both indicators will also be off. The buoy must be put on charge *immediately* to prevent failure of the built-in power supply.

If everything is done correctly and the upper parts of the buoys have a good view of the sky, after some time (usually no more than 1–2 minutes) you will be able to see the positions of the buoys in the main application window.

After that, you can place the buoys on the water surface.

#### 2.1.2.1. Charging the built-in power supply

The device is charged using the supplied accessory, and only when the device is switched off and completely dry.

| |
| :---: |
| ![RedBase water detector pads](/documentation/redbase_v2_charger.png) |
| Buoy charger |

Before connecting the accessory to the buoy, disconnect it from the mains. Make sure that the charging contacts of the accessory are seated in the sockets on the buoy, and then connect the charger to the mains.
Depending on the version of the charger, the operating mode indication may differ. For more complete information, refer to the charger's instructions.

| |
| :---: |
| ![RedBase water detector pads](/documentation/redbase_v2_charger_connecting.png) |
| Connecting the charger to the buoy |

| |
| :---: |
| ![RedBase water detector pads](/documentation/redbase_v2_charger_connected.png) |
| Charger connected |

When charging is complete, disconnect the charger from the mains and detach the charging accessory from the buoy.

#### 2.1.2.2. Connecting the service cable

Connecting the service cable may be required to change the address of the buoy, to determine its serial number or to update the software.
The service cable is connected using the supplied adapter, which is plugged into the group of contacts located in the lower part of the surface block of the device. The adapter connection is shown below.

| |
| :---: |
| ![RedBase water detector pads](/documentation/redbase_v2_scable.png) |
| Connecting the service cable adapter |

After connecting the adapter and cable to the buoy, connect it to a PC on which you install the required software:
- [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip) for updating the software

To switch on the buoy, place its lower part in the water so that the water detector contacts are submerged.
After completing the service operations, switch off the buoy and disconnect the service adapter.

#### 2.1.3. Positioning the buoys on the water surface

The buoys are placed on the water surface in the operating area and held in position by anchors.

> Keep in mind that although the buoys have a small positive buoyancy, they are not designed to be attached directly
> to the anchor line. To relieve the buoy of the weight of the anchor line, fenders (or floats) matched to the weight of the line must be used.

The figure below<sup>[1](#footnote1)</sup> shows the recommended layout for installing a buoy on a body of water.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_dep_scheme.png)|
| Recommended buoy installation layout |
| _1 - navigation sonobuoy, 2 - additional weight<sup>[2](#footnote2)</sup>, 3 - float, 4 - anchor line, 5 - anchor_ |

__________
<a name="footnote1"><sup>1</sup></a> Images may differ from the supplied products,
as the manufacturer is constantly working to improve the characteristics and is making changes to the design.  
<a name="footnote2"><sup>2</sup></a> Additional weight is used only in the underloaded version.

The buoys should be positioned in a convex quadrilateral that covers the entire intended work area with a small margin. For the system to operate effectively, it is important to observe several simple conditions:

- the buoys are located no closer than 40 m and no farther than 1500 m **from each buoy to each of the others**
- there must be a direct line of sight from each buoy to the receiving radio modem of the operator console
- there must be a direct line of sight from the underwater acoustic receiver of each buoy to the underwater object being positioned
- it is not recommended to place the buoys close to the shore, port infrastructure facilities or vessels
- the size of the navigation base (the average size of the rectangle formed by the buoys on the water surface) must not be less than the maximum depth of the object being positioned
- the size of the navigation base must be slightly larger than the intended work area

> _**CAUTION!**_  
> The buoys are not underwater devices and are designed to operate on the water surface. Although the protection class implies that the device may be briefly covered by a wave, keep in mind that the built-in radio equipment (the GNSS module and the radio modem) cannot operate in such conditions!

It is not recommended to throw the buoys overboard. Lower them carefully onto the water surface, making sure at the same time that the length of the anchor line is sufficient, that its weight is carried by the relief fender, and that the buoy floats vertically on the water surface and is not subjected to any additional loads.

#### 2.1.4. Preparing the underwater equipment

Preparation of the underwater equipment differs depending on the system configuration:

- For the configuration that tracks the locations of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diver stations, refer to the [RedPhone-DX diver station user's manual](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html).
Keep in mind that:
  - the stations must have **RWLT Pinger** mode enabled (the **RWLT Pinger enabled** setting);
  - when several voice communication stations are used in one body of water, they must be assigned **different** addresses (**RWLT Diver's ID**).

- For the system configuration with a standalone [RWLT Pinger](RWLT_Pinger_Specification_en.md) pinger beacon, no preliminary actions are required except for pre-charging the built-in power supply (battery block). For versions in which the pinger beacon and the battery block are joined by a detachable connection, first make sure that the watertight connector is firmly closed and serviced (for threaded connectors, make sure that the O-rings are lubricated with silicone grease; for SUBCONN-type and similar connectors, make sure that the lubricant recommended by the connector manufacturer is applied to both halves of the connector).

The pinger beacon switches on automatically when it enters the water (the water-activation contacts are located on the battery block). Keep in mind that immediately after switching on, the pinger beacon measures atmospheric pressure for **5** seconds to measure depth more accurately. Therefore, it is recommended to immerse the battery block in the water first and wait 5 seconds before immersing the pinger beacon itself.

> CAUTION! All versions of the pinger beacon transmit a navigation signal only when the excess pressure is greater than 50 mbar (approximately corresponding to a depth of 60 cm)

The pinger beacon must be fastened only by its mounting groove, using a soft clamp, so as to avoid any uneven loading of the beacon housing, excessive compression, and shading/shielding of the beacon housing. The figure below shows the basic requirements for mounting the acoustic part of the pinger beacon on the carrier:

| |
| :---: |
| ![0](/documentation/uWave_mounting_en.png)|
| Requirements for mounting the acoustic part of the pinger beacon on the carrier |
| _Shielding of the spatial hemisphere or of the parts of the transducer located above the mounting groove is not allowed; the pressure in the area under the mount must be balanced with the external pressure_ |

It is easy to check that the pinger beacon is working by lowering it into the water: when submerged to more than 1 meter, it begins to emit a navigation signal with a period of 2 seconds.

#### 2.1.5. Preparing the radio dongle for operation

Before operation, the radio modem must be connected to a [Bat&Link Box](/documentation/EN/Zima/Bat_n_link_box_Specification_en.md) autonomous power supply. Before using the autonomous power supply and interface converter, read its [user's manual](/documentation/EN/Zima/Bat_n_link_box_Users_manual_en.md).

Connect the radio modem cable to the **Bat&Link Box** autonomous power supply, and connect the latter to the PC on which the application appropriate to the system configuration is installed. Then switch on the power supply.

After power is applied, the radio modem's indicator turns on (blinks). The radio modem has a two-color indicator. One of the colors lights up synchronously with the arrival of messages from the buoys over the radio channel, thereby signaling that communication with the buoys is established, while the other lights up when the next batch of data is received from the built-in GNSS receiver, and goes out if the data is valid. If it stays lit continuously, this indicates that the built-in GNSS module has not yet determined its own location.

During normal operation of the system, one of the indicators will blink 1 time per second, and the other should blink four times within 2 seconds - this is the period within which the transmissions from all four buoys should arrive.

#### 2.1.6. Selecting a location for the operator console

Mount the radio modem at the highest possible point, so that throughout the entire operation of the system there is a direct line of sight between the radio modem antenna and all the buoys. To ensure this, the radio modem is equipped with a 10-meter cable.

The radio modem antenna must not be obstructed by any objects that block the radio signal: elements of the vessel's deck superstructure, the vessel's side, the mast and other radio equipment, trees, building walls, elements of port infrastructure, etc.

## 2.2. Working with the system

Keep in mind the factors that reduce the efficiency of the system:
- hydrological conditions: natural and man-made noise can degrade or completely preclude normal operation of the system; unfavorable underwater terrain and bottom vegetation can contribute to acoustic shadowing, etc.
- the positioned object(s) moving outside the navigation base (the figure formed by the buoys on the water surface): the most stable operation of the system is achieved inside the navigation base. As an approximation, the relative position of the diver and the navigation base is estimated by the **DOP** and **TBA** parameters. A position in the immediate vicinity of one of the buoys, or directly behind it, is also unfavorable.
- large vessels, especially those with a deep draft, can obstruct the passage of the acoustic signal.

The location of an underwater object or objects (when working with divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diver stations) can be determined when the following conditions are met:

- GNSS reception is available on all buoys, and the operator console receives radio signals from all buoys, i.e. the application displays the positions of all four buoys;

Additionally, when the system is configured to work with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) diver stations:
- the stations are correctly configured to work with the **RWLT** system;
- the special navigation signal emitted by a diver station after the diver finishes transmitting a voice message (releases the **PTT** button) is received by all four buoys of the **RWLT** system;
- signals from different divers do not overlap, and there is an interval of at least 2 seconds between signals from different divers;

## 2.3. After operation

The **navigation buoys** must be:
- removed from the anchors;
- cleaned of contamination (silt, dirt, algae, etc.);
- desalinated, if the work was not carried out in fresh water;
- wiped free of moisture with a soft cloth before being placed in the transport case;

The following is not allowed:
- Storage without rinsing in fresh water;
- Storage of the buoys together with wet anchor lines and other wet objects;

The **pinger beacon** must be:
- removed from the carrier;
- washed clean of contamination (silt, dirt, algae, etc.);
- desalinated, if the work was not carried out in fresh water;
- carefully wiped with a soft cloth and dried in air for at least 30 minutes;

The following is not allowed:
- mechanical impact on the pressure sensor opening;
- storage while damp (especially with seawater);
- freezing of water in the pressure sensor opening;

**Wireless voice communication diver stations**  
After operation, they do not require any additional actions and switch off automatically in air. Before placing them in the transport case, wash and/or desalinate them in fresh water, then wipe them with an absorbent cloth and dry them in air for at least 30 minutes.

For additional and up-to-date information, refer to the [wireless voice communication diver station user's manual](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html).

<div style="page-break-after: always;"></div>

## 3. Obligations and disclaimer
### 3.1. Terms of replacement and free warranty service
The manufacturer's warranty applies only to factory defects that become apparent during operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).  

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a factory defect.  

The grounds for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** to the equipment from the delivery set, including damage to the insulation of wires and cables;
- any **damage caused by exposure to moisture and contamination** as a result of improper operation of the equipment from the delivery set;
- any **electrical damage** caused by the **use of accessories not included in the delivery set** (the charger), or by the use of poor-quality and/or failed batteries; accessories supplied by the manufacturer or its representative to replace faulty or lost ones are not considered to be outside the delivery set;
- any **signs of unauthorized repair and/or opening** of the equipment from the delivery set.

<div style="page-break-after: always;"></div>

### 3.2. Limitation of the manufacturer's liability

_____________

_**ANY OF THE PARTS OF THE DELIVERY SET, INDIVIDUALLY AND AS PART OF THE SYSTEM, HEREINAFTER REFERRED TO AS THE "SUPPLIED EQUIPMENT":**_

- _**WAS NOT DESIGNED AS RESCUE EQUIPMENT**_  
- _**WAS NOT TESTED AS RESCUE EQUIPMENT**_  
- _**IS NOT RESCUE EQUIPMENT**_  
- _**THE MANUFACTURER DECLARES THAT THE SUPPLIED EQUIPMENT IS SAFE WHEN OPERATED IN ACCORDANCE WITH THESE INSTRUCTIONS, AND THE MANUFACTURER IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF THE USE OF THE SUPPLIED EQUIPMENT**_

______________

_**THE MANUFACTURER GUARANTEES THAT THE RWLT UNDERWATER ACOUSTIC TRACKING SYSTEM (HEREINAFTER - THE SYSTEM):**_  
- _**IS INTENDED ONLY FOR USE WITH PINGER BEACONS OR DIVER COMMUNICATION STATIONS DESIGNED TO OPERATE TOGETHER WITH THE SYSTEM**_  
- _**BY DESIGN CANNOT BE USED FOR TRACKING OBJECTS THAT ARE NOT EQUIPPED WITH PINGER BEACONS OR DIVER COMMUNICATION STATIONS NOT DESIGNED TO OPERATE TOGETHER WITH THE SYSTEM**_  
- _**CONTAINS ONLY CIVILIAN RADIO FREQUENCY MODULES THAT ARE NOT SUBJECT TO LICENSING: GNSS RECEIVERS AND RADIO MODEMS**_  
_**THE ABOVE LIMITATIONS CANNOT BE LIFTED BY ANY MANIPULATION OF THE SETTINGS AND/OR CONTROLS OF THE SYSTEM DEVICES AND/OR OF THE SOFTWARE INTENDED FOR USE WITH THE SYSTEM**_

______________

[Back to contents](#contents)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RWLT/RWLT_Users_Manual_ru.md commit=b7231faa0f1fc6a81ae94d4400df7a2d5725bc90 date=2024-04-18 -->
