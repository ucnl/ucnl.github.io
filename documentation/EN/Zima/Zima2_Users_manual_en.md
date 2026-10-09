
[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2 USBL: User's manual**

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

| ![logo](/documentation/sm_logo.png) | ![qr_link](/documentation/zima2_users_manual_qr_link.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2 USBL** - underwater acoustic navigation system <br/> User's manual |

# Zima2 USBL <br/> User's manual

<div id="toc"></div>

## Contents

- [1.1. Purpose](#11-purpose)
- [1.2. Features](#12-features)
- [1.3. System composition](#13-system-composition)
- [1.4. Versions](#14-versions)
  - [1.4.1. Standard version](#141-standard-version)
  - [1.4.2. Version 35](#142-version-35)
  - [1.4.3. Version K](#143-version-k)
- [2.0. Before operation](#20-before-operation)
- [2.1. Preparation for operation and equipment check](#21-preparation-for-operation-and-equipment-check)
  - [2.1.1. Positioning and setting up the direction-finding antenna](#211-positioning-and-setting-up-the-direction-finding-antenna)
  - [2.1.2. Mounting the responder-beacon on the carrier](#212-mounting-the-responder-beacon-on-the-carrier)
  - [2.1.3. Angular misalignment calibration](#213-angular-misalignment-calibration)
- [2.2. AzimuthConsole application](#22-azimuthconsole-application)
- [2.3. AzimuthSuite application (obsolete)](#23-azimuthsuite-application-obsolete)
- [2.4. Working with the system](#24-working-with-the-system)
- [2.4.1. Interacting with the system](#241-interacting-with-the-system)
  - [2.4.2. Manual setting of coordinates and direction](#242-manual-setting-of-coordinates-and-direction)
- [2.5. After operation](#25-after-operation)
- [3.1. Terms of replacement and free warranty service](#31-terms-of-replacement-and-free-warranty-service)
- [3.2. Limitation of the manufacturer's liability](#32-limitation-of-the-manufacturers-liability)




 
<div style="page-break-after: always;"></div>

# 1. Introduction
## 1.1. Purpose
The **Zima2** underwater acoustic navigation system is designed to determine, in real time, the location of underwater objects equipped with [Zima2-R](Zima2R_Specification_en.md) responder-beacons.
 
The responder-beacons (hereinafter, beacons) can be installed on:
- remotely operated underwater vehicles (ROVs)
- human-occupied vehicles (HOVs)
- autonomous unmanned underwater vehicles (AUVs)
- recreational and technical divers (when the standalone version of the beacon is used).

The system makes it possible to determine:
- the relative location of underwater objects (azimuth angle, range, depth) 
- the absolute location of underwater objects (latitude, longitude, depth) when external sources of navigation data (a GNSS receiver and a compass) are used.

## 1.2. Features
The **Zima2** navigation system is an ultra-short baseline (USBL) navigation system whose principle of operation is based 
on the use of a phased antenna array to determine the horizontal angle of arrival of the signal and on determining the distance to the beacon by the "request-response" method. 
The **Zima2** system uses modern digital wideband, noise-resistant underwater acoustic communication technology, and its signal is specifically
designed for difficult hydrological conditions, including those typical of shallow bodies of water. 

<div style="page-break-after: always;"></div>

## 1.3. System composition

The system includes:

- Direction-finding antenna [Zima2-B](Zima2B_Specification_en.md) 
- Cable with an integrated RS-422 interface converter [uWire](/documentation/EN/Accessories/RS422_extension_cable_en.html)
- Responder-beacon [Zima2-R](Zima2R_Specification_en.md)
- Power supply and switching unit [Bat&Link Box](Bat_n_link_box_Specification_en.md)
- Underwater battery pack (battery unit) [SB-24-48-LF](/documentation/EN/Accessories/Sub_batteries_en.html#sb2448lf).

| ![Zima2-B](/documentation/zima_b.png) |
| :---: |
| *Direction-finding antenna [Zima2-B](Zima2B_Specification_en.md)* |
|  |
| ![Zima2-B-Interface-cable](/documentation/rs422_cable.png) |
| *[UART-RS422](/documentation/EN/Accessories/RS422_extension_cable_en.html) cable with an integrated interface converter* |
|  |
| ![Zima2-R](/documentation/zima_r.png) | 
| *Responder-beacon [Zima2-R](Zima2R_Specification_en.md) (integrated version)* |
|  |
| ![Zima2-R](/documentation/zima_r_wbat.png) | 
| *Responder-beacon [Zima2-R](Zima2R_Specification_en.md) with a [battery pack](/documentation/EN/Accessories/Sub_batteries_en.html#sb2448lf) (standalone version)* |
|  |
| ![Bat&Link Box](/documentation/batnlinkbox.png) | 
| *Power supply and switching unit [Bat&Link Box](Bat_n_link_box_Specification_en.md)* |
|  |

**We are constantly working to improve our products, so the appearance, color, and type of the connectors, cables and chargers used may differ slightly.**

## 1.4. Versions

The system is available in different versions for different depth ranges. When this document refers to the base version of a device, for example Zima2-B, it should be understood as applying to all versions of the device, unless additional clarifications are given.

> CAUTION! Devices of different versions are not compatible with each other, and using them together in one system will inevitably result in incorrect navigation data.

### 1.4.1. Standard version 

In the standard version, the system can operate at depths of up to 300 m. The responder-beacon can be powered either from the carrier or from a standalone source.

| Device | Technical specification |
| :--- | :--- |
| Direction-finding antenna Zima2-B | [![Device specification: Zima2-B - direction-finding antenna](https://github.com/user-attachments/assets/696ef046-4b15-489f-8576-adea91bcb5e8)](https://docs.unavlab.com/documentation/EN/Zima/Zima2B_Specification_en.html) |
| Responder-beacon Zima2-R | [![Zima2-R - responder-beacon: Device specification](https://github.com/user-attachments/assets/ec9a4cfc-e256-486a-84e4-eaaf51ad0298)](https://docs.unavlab.com/documentation/EN/Zima/Zima2R_Specification_en.html) |

### 1.4.2. Version 35

In this version, the system can work with responder-beacons located at depths of up to 350 m. The built-in pressure sensors in the responder-beacons have a protective metal diaphragm. The responder-beacon can be powered either from the carrier or from a standalone source.

| Device | Technical specification |
| :--- | :--- |
| Direction-finding antenna Zima2-B35 | [![Device specification: Zima2-B35 - direction-finding antenna](https://github.com/user-attachments/assets/496c0dd8-79f6-4247-b085-1b13179f4fa6)](https://docs.unavlab.com/documentation/RU/Zima/Zima2B35_Specification_ru.html) |
| Responder-beacon Zima2-R35 | [![Zima2-R35 - responder-beacon: Device specification](https://github.com/user-attachments/assets/d086915b-ba1b-4ec3-9906-c9341024409d)](https://docs.unavlab.com/documentation/RU/Zima/Zima2R35_Specification_ru.html) |

### 1.4.3. Version K

In this version, the system can work with responder-beacons located at depths of up to 1000 m. The responder-beacon is supplied in a metal one-atmosphere (normobaric) housing with a transducer on a cable. Only the carrier-powered option is available.

| Device | Technical specification |
| :--- | :--- |
| Direction-finding antenna Zima2-BK | [![Device specification: Zima2-BK - direction-finding antenna](https://github.com/user-attachments/assets/2e8dec84-abb4-42c1-81ba-38fd8c6b6362)](https://docs.unavlab.com/documentation/EN/Zima/Zima2BK_Specification_en.html) |
| Responder-beacon Zima2-RK | [![Zima2-RK - responder-beacon: Device specification](https://github.com/user-attachments/assets/10ab9aea-3eb2-4ef8-8e32-28316e6e4527)](https://docs.unavlab.com/documentation/EN/Zima/Zima2RK_Specification_en.html) |

<div style="page-break-after: always;"></div>

# 2. Working with the Zima2 system

## 2.0. Before operation

Specialized software [🖵 AzimuthConsole](https://github.com/ucnl/AzimuthConsole/releases) is required to work with the system.
Builds for all supported platforms are available at the download link.

Previously, the [🐙 AzimuthSuite](https://github.com/ucnl/AzimuthSuite/releases/download/beta/AzimuthSuite.zip) application, which runs under Windows, was used.

Download the required software in advance. Installation is not required - simply unpack the contents of the archive to a location convenient for you.
Before heading out to the water, make sure that all equipment is fully charged and, if necessary, charge all devices.

Pay particular attention to the power supply and switching units and the responder-beacons: since these devices have built-in power sources based on **LiFePO4**, their discharge curve is very flat and it is difficult to determine the state of charge of the built-in source. Therefore, it is recommended to charge all devices before use, no earlier than 1–2 days in advance.

We use batteries based on **LiFePO4** because they are the most durable and withstand the greatest number of charge-discharge cycles compared to **Li-ion** and **Li-Po** batteries, and can also operate at low temperatures.

<div style="page-break-after: always;"></div>

## 2.1. Preparation for operation and equipment check

### 2.1.1. Positioning and setting up the direction-finding antenna

> CAUTION!!!  
> UNLIKE THE PREVIOUS VERSION OF THE SYSTEM, THE POSITION OF THE ZERO DIRECTION OF THE ANTENNA HAS BEEN CHANGED!

The zero direction of the antenna coincides with the molding seam on the side where the antenna array is closer to the surface of the cylinder (see the figure below). The Z axis points down; the azimuth angle is measured clockwise from the zero direction when looking at the antenna from the cable side.

| ![zima2_zero_direction](/documentation/zima2_zero_direction_1.png) | 
| :---: |
| Zero direction of the antenna |
| *The horizontal angle is measured clockwise from the zero direction of the antenna, the vertical axis points down* |

The antenna must be mounted with the supplied bracket [uClamp-S](/documentation/EN/Accessories/Flange_rod_mound_Specification_en.html). The upper part of the bracket has a cutout that marks the zero of the antenna.

Because the antenna determines the horizontal angle of arrival of the signal relative to its zero direction, observe the following requirements when mounting it:
- The antenna must be placed on a deployment pole that holds it in a stable position no closer than 2 m to the water surface and no higher than 1.5 from the lowest point of the vessel's keel
- The antenna must be secured with a clamp in such a way that its position does not change during operation (the antenna must not rotate inside the clamp)
- The antenna must not be squeezed too tightly by the mount
- The mount and its parts must not protrude below the mounting groove and thereby cover the working surfaces of the antenna
- The mount and its parts must not block the pressure sensor opening
- The thin cable coming out of the antenna must not be bent with a radius of less than 50 mm, the thick cable - with a radius of less than 100 mm.

**It is not recommended** to install the antenna near large objects: quay walls, piers, breakwaters, large vessels, massive supports and other water infrastructure objects.

The antenna is connected to the power supply and switching unit using an extension cable with an integrated interface converter. The cable has two connectors: one topside - for connecting to the power supply and switching unit, the other underwater - for connecting the antenna.

Before submerging the antenna, make sure that:
- there is no moisture, traces of corrosion or contamination in either part of the antenna's underwater connector
- the seals on both parts of the underwater connector are intact
- there is a sufficient amount of thick silicone grease on the seals of the underwater connector
- the connector is mated and the locking ring is screwed on tightly by hand

> CAUTION!  
> Water ingress into any connector is absolutely unacceptable and will result in damage not covered by the warranty!

The extension cable must not have large slack along its submerged length. It is recommended to secure the cable to the pole with rope or nylon cable ties.

> CAUTION!  
> Before connecting the antenna to the power supply and switching unit via the extension cable, make sure that the power supply and switching unit is switched off!

The following sequence of actions is recommended when installing the antenna:

- check the underwater connector of the antenna
- connect the antenna to the extension cable by mating and tightening the underwater connector
- install the antenna in the clamp
- secure the cable to the pole with nylon cable ties or pieces of rope at points spaced no more than 500 mm apart
- make sure that the power supply and switching unit is switched off
- connect the topside connector of the extension cable to the power supply and switching unit
- connect the power supply and switching unit to the PC using a USB-B cable

For the version of the power supply and switching unit with two channels (for connecting an external GNSS compass), additional steps are required:
- connect the GNSS compass to the supplied cable
- connect the GNSS compass cable to the power supply and switching unit

**Switch on the power supply and switching unit** only **after launching the specialized software** on the host PC. Operation of the software and its setup are described below.

To find out the names of the connectors on the panel of the power supply and switching unit, refer to the [user's manual of the Bat&Link Box power supply and switching unit](Bat_n_link_box_Users_manual_en.md).

### 2.1.2. Mounting the responder-beacon on the carrier

The responder-beacon must be fastened only by its mounting groove, using a soft clamp, so as to avoid any uneven loading of the beacon housing, excessive squeezing, and shading/shielding of the beacon housing. The figure below shows the basic requirements for mounting the acoustic part of the responder-beacon on the carrier:

| ![0](/documentation/uWave_mounting_en.png)|
| :---: |
| Requirements for mounting the acoustic part of the responder-beacon on the carrier |
| *Shielding of the spatial hemisphere or of the parts of the transducer located above the mounting groove is not allowed; the pressure in the area under the mount must be balanced with the external pressure* |

The responder-beacon should not be positioned near thruster or propeller wash or directly in its path. The system requires a direct line of sight (through the water column) between the direction-finding antenna and the responder-beacon, so the beacon must be installed at the highest point of the carrier.

**For a responder-beacon in the standalone version:**
A responder-beacon in the standalone version switches on automatically when it enters the water. Keep in mind that, immediately after switching on, the responder-beacon determines the atmospheric pressure for **5** seconds for a more accurate depth measurement. Therefore, it is recommended to first immerse the battery pack in the water and wait 5 seconds before immersing the responder-beacon itself. 

> CAUTION! If the battery pack is deeply discharged, a charger must be connected to it as soon as possible. Otherwise, this may result in damage to the battery pack.

**For a responder-beacon in the integrated version:**
A responder-beacon in the integrated version switches on when power is supplied from an external system. After switching on, the responder-beacon determines the atmospheric pressure for **5** seconds for a more accurate depth measurement. If the current value of the external pressure is more than 1200 mbar, the beacon assumes that it was switched on while submerged, and the atmospheric pressure calibration does not take place.

The operability of the responder-beacon is easy to check by switching it on: 2 seconds after power is applied, a navigation signal is emitted once. 

**In the version with the standard connector, the water-activation contacts are located on both parts of the connector: on the beacon and on the mating part. Thus, when the standard battery pack is used, the device switches on when the mated connector is immersed in water.**


### 2.1.3. Angular misalignment calibration

The zero direction of the direction-finding antenna and the zero direction of the compass (GNSS compass or magnetic) may not coincide — for example, because of inaccurate installation of the antenna in the bracket. This leads to a systematic error in determining the azimuth to the responder-beacon. An angular calibration procedure is performed to eliminate it.

**Calibration principle:** during the procedure, the antenna and the responder-beacon must move relative to each other so that the **geographic azimuth to the beacon** changes over a wide range of angles. The system performs a series of **N measurements** at different azimuths to the beacon and then iterates over possible values of the angular correction within a specified range. For each candidate correction, the beacon coordinates are recalculated and the scatter of the resulting points is evaluated (DRMS — circular error probable). The optimal correction is the one that gives the **minimum DRMS** — that is, the "most tightly clustered" cloud of points.

When the specified number of measurements is reached, the procedure finishes automatically. The computed correction is applied and displayed in the web interface ("Angular Calibration" panel) and in the application log.

Two calibration scenarios are possible:

- **The antenna is mobile (on a vessel):** the vessel moves in a circle around a stationary beacon
- **The antenna is stationary (on a pier, quay, ice):** the beacon on a mobile carrier (diver, ROV) moves around the antenna

In both cases the physical principle is the same: measurements must be obtained at different geographic azimuths to the beacon so that the algorithm can compute the angular correction.

> **ℹ Why moving around matters, as opposed to rotating in place**
> 
> When the antenna rotates about its own axis (without any change in its geographic position relative to the beacon), the relative azimuth to the beacon measured by the antenna changes, but the **geographic azimuth to the beacon remains constant** — the beacon is stationary and the antenna does not move. Because of this, the angular error δ affects all measurements equally, and DRMS does not depend on the correction being iterated over — the algorithm cannot determine the optimum.
> 
> When the vessel moves **around the beacon** (or the beacon moves around the antenna), the geographic azimuth to the beacon changes from measurement to measurement. The error δ is projected onto the coordinates differently at different azimuths, and DRMS becomes a function of δ — the algorithm finds the correction that gives the minimum scatter.

**Procedure (antenna on a vessel):**

1. Place the responder-beacon at a distance of 20–50 m from the vessel. Make sure there is a direct acoustic line of sight between the antenna and the beacon.
2. Launch the **AzimuthConsole** application, make sure that the system is configured to work only with the single beacon selected for calibration, and establish a connection with the system (the `OCON` command).
3. Make sure the compass (external GNSS compass or magnetic) is connected and is transmitting current data.
4. Start moving the vessel slowly **around the beacon** in a circle, keeping the speed and the distance as constant as possible. The beacon must remain at the center of the circle being described.
5. Run the command: `ACAL,start=0,end=360,step=0.5,n=512,addr=X`, where `addr=X` is the address of the responder-beacon being used.
6. After the specified number of measurements has been collected, the procedure will finish automatically. The computed correction will be displayed in the web interface ("Angular Calibration" panel) and in the application log.
7. Save the settings with the `SAVEINIT` command so that the correction is applied at subsequent launches.

**Procedure (antenna on a pier/ice):**

1. Install the direction-finding antenna on a pier, quay or ice. Fix its position — the antenna must remain stationary throughout the whole procedure.
2. Launch the **AzimuthConsole** application, make sure that the system is configured to work only with the single beacon selected for calibration, and establish a connection with the system (the `OCON` command).
3. Make sure the compass is connected, fixed coaxially with the antenna and transmitting current data. If the compass is not installed coaxially, first measure the offset and enter it with the `OFS` command.
4. Place the responder-beacon on a mobile carrier (diver, ROV) at a distance of at least 50 m from the antenna. The initial direction to the beacon does not matter.
5. Start **moving the beacon slowly and steadily around the antenna** in a circle. Recommendations:
- Move in such a way that the beacon describes a full circle (or at least 180°) around the antenna
- Keep the distance to the antenna as constant as possible (variations within ±20% are acceptable)
- The movement speed must be low and constant — especially when using compasses with an update rate of 1 Hz
- Avoid sudden accelerations and stops
- If the carrier is a diver: walk at a smooth pace, monitoring the distance using the application readings
- If the carrier is an ROV: set a slow movement in a circle at a constant speed
6. Run the command: `ACAL,start=0,end=360,step=0.5,n=512,addr=X`, where `addr=X` is the address of the responder-beacon being used.
7. After the specified number of measurements has been collected, the procedure will finish automatically. The computed correction will be displayed in the web interface ("Angular Calibration" panel) and in the application log. Save the settings with the `SAVEINIT` command.

**ACAL command parameters:**

| Parameter | Description | Recommendation |
| :--- | :--- | :--- |
| `start` | Start of the correction search range, ° | 0 (if the offset is unknown) |
| `end` | End of the correction search range, ° | 360 |
| `step` | Correction search step, ° | 0.5 (a step in the range from 0.1° to 1° is acceptable) |
| `n` | Total number of measurements | 200–500 (more measurements give higher accuracy but take longer) |
| `addr` | Responder-beacon address (1–16) | Specify explicitly if several beacons are within range |

**General recommendations:**

- **Movement speed:** the slower, the better. When using magnetic compasses and GNSS compasses with an update rate of 1 Hz, it is critically important to move slowly so that the compass has time to provide current data at every measurement; this is especially important in the case of a vessel.
- **Number of measurements:** if the movement is slow and the compass update rate is low, increase `n` so that the measurements cover the whole circle. As a rough guide: at a rate of 1 Hz and a full circle in 5 minutes, it makes sense to set `n=250`.
- **Accuracy:** for a more accurate result, reduce the iteration step `step` to 0.1°. For most cases a step of 0.5° is sufficient.
- **Automatic completion:** the procedure finishes by itself after `n` measurements have been collected. The result is displayed in the web interface ("Angular Calibration" panel) and in the application log.
- **Saving:** after the calibration is completed, be sure to run `SAVEINIT`; otherwise the correction will not be applied at subsequent launches.
- **Repeat calibration:** it is recommended to perform the calibration every time the antenna is reinstalled, and also after strong mechanical impacts on the bracket.

> **ℹ Note**
> 
> The procedure is supported only in **AzimuthConsole**. If you are using the obsolete AzimuthSuite application, the angular correction must be measured manually and entered in the settings (the "Angular correction" field).

<div style="page-break-after: always;"></div>

## 2.2. AzimuthConsole application

A detailed user's manual for the AzimuthConsole application is available as a separate document:

| Document | QR |
| :--- | :--- |
| AzimuthConsole: user's manual | [![AzimuthConsole: User's manual](https://github.com/user-attachments/assets/2a70ad5c-db4d-4dee-8c26-5c8cf04a91b6)](/documentation/RU/Zima/AzimuthConsole_manual_ru) |


## 2.3. AzimuthSuite application (obsolete)

> **ℹ Information**
> 
> The **AzimuthSuite** application is no longer supported. It is recommended to use [AzimuthConsole](/documentation/RU/Zima/AzimuthConsole_manual_ru).

| Document | QR |
| :--- | :--- |
| AzimuthSuite: user's manual | [![AzimuthSuite: User's manual](https://github.com/user-attachments/assets/ca59ab7b-870c-4946-8342-ab7b6eb52d1c)](/documentation/RU/Zima/AzimuthSuite_manual_ru) |

<div style="page-break-after: always;"></div>

## 2.4. Working with the system
The system performs almost all of the work in automatic mode; the following must be set in the system:
- the addresses of the beacons that are to be used
- the water salinity, for correct calculation of the depth and the speed of sound
- the maximum range at which the beacons may be located from the direction-finding antenna
- the connection parameters of an external source of navigation data (GNSS compass), if necessary
- the connection parameters of an external receiver port, for GNSS emulation for the selected responder-beacon (if an external GNSS compass is present).

Next, the system automatically polls the responder-beacons from the specified address range and, depending on the configuration used, displays the result on the screen and/or transmits it to consumers over one of the channels (Serial, UDP).
During operation, the host application writes log files, which can then be played back in the same time scale in which they were recorded.

## 2.4.1. Interacting with the system

At this stage it is assumed that:

- The antenna's underwater connector has been checked and mated (the extension cable is connected to the direction-finding antenna)
- The antenna is properly secured to the pole, and the extension cable has no slack
- The topside connector of the extension cable is connected to the power supply and switching unit, and the unit itself is switched off
- The power supply and switching unit is connected to the PC with a USB-B cable
- If a two-channel power supply and switching unit is used:
  - The external GNSS compass is connected to the power supply and switching unit
  - The offset of the direction-finding antenna relative to the position reference point (the position of the GNSS receiver) has been measured and entered in the application settings
  - The angle between the zero direction of the compass and that of the direction-finding antenna has been measured and entered in the application settings
  - The second channel of the power supply and switching unit is connected to the PC with a USB-B cable
- All responder-beacons that are to be used have different addresses
- The addresses of all responder-beacons that are to be used are specified in the application settings
- If responder-beacons in the standalone version are used, the connectors joining them to the battery packs have been checked and are tightly mated, and the battery packs are fully charged
- If responder-beacons in the integrated version are used, the cable connections to the carrier have been checked for watertightness (according to the connection type)
- The specialized software (AzimuthConsole or AzimuthSuite) is running

It is recommended to switch the beacons on at the surface: in this case, atmospheric pressure calibration takes place during the first five seconds after power is applied, which allows depth to be measured with greater absolute accuracy.

Since standalone beacons switch on when the battery pack is immersed in water, it is recommended to immerse the battery pack in the water first, and the responder-beacon itself only after five seconds have passed.

Beacons in the integrated version should preferably be switched on before immersion, if this is possible under the current conditions.

To start work, launch the specialized software (AzimuthConsole or AzimuthSuite) and establish a connection with the system. After that, switch on the Bat&Link Box power supply and switching unit. The connection status is displayed in the application interface.

> Keep in mind that the application is designed to work with only one device of the system at a time: if both the direction-finding antenna and one of the beacons are connected to the PC, there is a high probability that the beacon will be detected first during the port search. In this case the port of the direction-finding station will not be searched for.

After the corresponding port (or ports) is detected, the system immediately proceeds to poll the responder-beacons whose addresses are specified in the settings.
Operation is fully automatic.

If an external GNSS receiver is used, or the position and orientation of the antenna relative to the cardinal directions are set manually, the system calculates the absolute geographic coordinates of the responder-beacons. Depending on the application, import and transmission of navigation information in various forms are available (the saving methods, channels and data transmission formats depend on the application used — see the corresponding manuals).

The system supports transmission of the calculated coordinates of the responder-beacons as standard NMEA sentences (RMC, GGA) via a serial port or UDP.

Keep in mind the factors that reduce the efficiency of the system, in particular:
- insufficient depth of the direction-finding antenna
- location in the immediate vicinity of massive, weakly absorbing infrastructure objects and vessels
- absence of a direct line of sight through the water column between the direction-finding antenna and the responder-beacons
- high noise level (both electromagnetic interference, for example in the vessel's power supply network, and acoustic noise - the running engine of the vessel or carrier, surf, other underwater acoustic systems, for example - sonars, etc.)
- shallow water depth, and small bodies of water in general, create difficult hydrological conditions for the operation of underwater acoustic navigation and communication systems
- shielding of the direction-finding antenna and of the transducers of the responder-beacons
- exposure of the antennas to turbulent thruster/propeller wash and/or to the wake
- water density stratification (thermocline, etc.)

### 2.4.2. Manual setting of coordinates and direction

If using an external GNSS compass is difficult or impossible, the system allows the coordinates and orientation of the antenna to be set manually.

- **AzimuthConsole:** the `LHOV,lat=...,lon=...,hdg=...` command
- **AzimuthSuite:** the `UTILS > Location override` menu item

For details, see the manuals of the corresponding applications.


<div style="page-break-after: always;"></div>

## 2.5. After operation

- Switch off the power supply and switching unit
- Disconnect all connectors on the panel of the power supply and switching unit
- Close all connectors that have transport plugs
- If there is any contamination, or after work in salt water, rinse all submersible parts of the equipment in fresh water
- Remove the direction-finding antenna from the pole
- For long-term storage (more than a week) or for transportation, unmate the underwater connector
- Before packing the equipment in its transport case, remove all moisture by natural drying, out of direct sunlight
- For responder-beacons in the integrated version, if they cannot be removed from the carrier, rinsing in fresh water and removal of any contamination is mandatory

<div style="page-break-after: always;"></div>

# 3. Obligations and disclaimer
## 3.1. Terms of replacement and free warranty service
The manufacturer's warranty covers only factory defects that become apparent during operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).  

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a factory defect.  

Grounds for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** to the equipment from the delivery set, including damage to the insulation of wires and cables;
- any **damage caused by exposure to moisture and contamination** as a result of improper operation of the equipment from the delivery set;
- any **electrical damage** caused by the **use of accessories not included in the delivery set** (chargers); accessories supplied by the manufacturer or its representative to replace faulty or lost ones are not considered to be outside the delivery set;
- any **signs of unauthorized repair and/or opening** of the equipment from the delivery set.

<div style="page-break-after: always;"></div>

## 3.2. Limitation of the manufacturer's liability

_____________

_**ANY OF THE PARTS OF THE DELIVERY SET, INDIVIDUALLY AND AS PART OF THE SYSTEM, HEREINAFTER REFERRED TO AS THE "SUPPLIED EQUIPMENT":**_

* _**WAS NOT DESIGNED AS RESCUE EQUIPMENT**_
* _**WAS NOT TESTED AS RESCUE EQUIPMENT**_
* _**IS NOT RESCUE EQUIPMENT**_
* _**THE MANUFACTURER DECLARES THAT THE SUPPLIED EQUIPMENT IS SAFE WHEN OPERATED IN ACCORDANCE WITH THESE INSTRUCTIONS, AND THE MANUFACTURER IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF THE USE OF THE SUPPLIED EQUIPMENT**_

______________

_**THE MANUFACTURER GUARANTEES THAT THE ZIMA2 UNDERWATER ACOUSTIC SYSTEM (HEREINAFTER - THE SYSTEM):**_
* _**IS INTENDED ONLY FOR USE WITH RESPONDER-BEACONS DESIGNED TO OPERATE TOGETHER WITH THE SYSTEM**_
* _**BY DESIGN CANNOT BE USED FOR TRACKING OBJECTS THAT ARE NOT EQUIPPED WITH RESPONDER-BEACONS DESIGNED TO OPERATE TOGETHER WITH THE SYSTEM**_
* _**DOES NOT CONTAIN MEANS OF RADIO COMMUNICATION, OR OF RECORDING AND LONG-TERM STORAGE OF AUDIO SIGNALS**_  

_**THE ABOVE LIMITATIONS CANNOT BE LIFTED BY ANY MANIPULATION OF THE SETTINGS AND/OR CONTROLS OF THE SYSTEM DEVICES AND/OR OF THE SOFTWARE INTENDED FOR USE WITH THE SYSTEM**_

______________

<div style="page-break-after: always;"></div>

[Back to contents](#toc)

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/Zima/Zima2_Users_manual_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
