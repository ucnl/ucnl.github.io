| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedWave** <br/> Underwater acoustic navigation system (diver version) <br/> **Test program and procedures** |

# **RedWave** <br/> Underwater acoustic navigation system (diver version) <br/> **Test program and procedures**

<div style="page-break-after: always;"></div>

## Contents
- [1. Test object](#1-test-object)
- [2. Test objective](#2-test-objective)
- [3. General information](#3-general-information)
  - [3.1. Developer and manufacturer](#31-developer-and-manufacturer)
  - [3.2. Procedure for using additional equipment and transport cases](#32-procedure-for-using-additional-equipment-and-transport-cases)
  - [3.3. Frequency of testing](#33-frequency-of-testing)
- [4. Equipment set](#4-equipment-set)
  - [4.1. The base equipment set for testing according to this procedure includes the following instruments](#41-the-base-equipment-set-for-testing-according-to-this-procedure-includes-the-following-instruments)
  - [4.2. Additional equipment set](#42-additional-equipment-set)
- [5. Test site requirements](#5-test-site-requirements)
- [6. Test plan](#6-test-plan)
- [6.1. Field tests](#61-field-tests)
  - [6.1.1. General information](#611-general-information)
  - [6.1.2. Preparation and checking of the equipment for testing](#612-preparation-and-checking-of-the-equipment-for-testing)
  - [6.1.3. Deployment of the long base](#613-deployment-of-the-long-base)
  - [6.1.4. Preliminary operability tests](#614-preliminary-operability-tests)
  - [6.1.5. Procedure 1 "Reaching a predefined point"](#615-procedure-1-reaching-a-predefined-point)
  - [6.1.6. Procedure 2 "Reaching a saved point"](#616-procedure-2-reaching-a-saved-point)
  - [6.1.7. Procedure 3 "Reaching a predefined point as a group"](#617-procedure-3-reaching-a-predefined-point-as-a-group)
  - [6.1.8. Completion of the tests](#618-completion-of-the-tests)
- [6.2. Reliability tests](#62-reliability-tests)
  - [6.2.1. General information](#621-general-information)
  - [6.2.2. Preparation and checking of the equipment for testing](#622-preparation-and-checking-of-the-equipment-for-testing)
  - [6.2.3. Procedure 4 "Buoy battery life check"](#623-procedure-4-buoy-battery-life-check)
  - [6.2.4. Procedure 5 "Checking the buoy housing for IP68 compliance"](#624-procedure-5-checking-the-buoy-housing-for-ip68-compliance)
  - [6.2.5. Procedure 6 "RedNav instrument battery life check"](#625-procedure-6-rednav-instrument-battery-life-check)

<div style="page-break-after: always;"></div>

## 1. Test object
The test object is the set of instruments and equipment included in the RedWave underwater acoustic navigation system (hereinafter referred to as the equipment set, ES). 

## 2. Test objective
Determination of the compliance of the ES with the declared technical specifications.

## 3. General information
### 3.1. Developer and manufacturer
The RedWave underwater acoustic navigation system was developed by UCNL LLC; the base equipment set includes the RedBase and RedNav instruments and the specialized RedNav Host software, which are manufactured at the facilities of UCNL LLC.

### 3.2. Procedure for using additional equipment and transport cases
Additional equipment means any devices and accessories that are not an integral part of the ES instruments, in particular:
- rigging accessories: anchors, carabiners, anchor lines, lines, floats, etc.;
- additional light signaling equipment: retroreflective markers, reflectors, light beacons, lamps, etc.;
- personal computers (PCs), laptops, tablets and other computing equipment on which the specialized ES software is intended to run;
- various devices: salinity, temperature and voltage meters;  

Transport cases are special cases for transporting the instruments included in the ES.
The additional equipment and transport cases are not manufactured by UCNL LLC and are not test objects under this test program and procedures; their composition is agreed with the customer separately. By separate agreement, it is also possible to carry out both delivery tests of a separate set of additional equipment and/or transport cases and their incoming inspection according to a procedure agreed separately with the customer.

### 3.3. Frequency of testing
Tests according to this procedure are carried out on one ES from each series of equipment. Additional tests are carried out when changes are made to the design of the instruments and/or to the specialized software of the ES.
By separate agreement, acceptance tests according to this procedure or according to a simplified scheme are possible.

## 4. Equipment set
### 4.1. The base equipment set for testing according to this procedure includes the following instruments:
#### **Table 1** - Base equipment set

| No. | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1 | [RedBase](RedBASE_Specification_en.md) navigation buoy | 4 | . . . |
| 2 | Charger for [RedBase](RedBASE_Specification_en.md) | 4 | . . . |
| 3 | [RedNav](RedNAV_Specification_en.md) diver's navigation instrument | 1 | The number of instruments participating in the tests may be increased by additional agreement with the customer and/or in accordance with the size of the purchased set |
| 4 | Charger for [RedNav](RedNAV_Specification_en.md) | 1 | Supplied in the set; the number of sets corresponds to the number of [RedNav](RedNAV_Specification_en.md) instruments participating in the tests |


### 4.2. Additional equipment set
This list includes the additional equipment required for testing and may differ from the delivery list.
#### **Table 2** - Set of required additional equipment

| No. | Name | Quantity | Note |
| :--- | :--- | :--- | :--- |
| 1 | Anchor | 4 | At least 1.5 kg |
| 2 | Anchor line | - | Depending on the conditions of the water body. Breaking strength of at least 80 kg. Braided synthetic. Twisted. |
| 3 | Float | 4 | Buoyancy at least 2 times the weight of the anchor line. Maximum size no more than 400 mm. |
| 4 | Compass | 1 | Required only when divers take part |
| 5 | Watercraft | 1 | With a load capacity of at least 3 persons and the ability to be anchored |
| 6 | PC with Windows 7/8/10 OS and a Bluetooth module | 1 | With the ability to install the [RedNav Host software](https://api.github.com/repos/ucnl/RedNavHost/zipball) on it. |

## 5. Test site requirements
The test site for testing according to this test program and procedures must meet a number of requirements, in particular:
- fresh or salt water body;
- sea state no more than 0.5;
- no currents with a speed of more than 1 m/s;
- water depth at the site not less than 3 and not more than 40 m (the lower limit is determined by the difficulty of anchoring the buoys);
- line-of-sight conditions must be ensured in accordance with [section 3 of the User's manual](RedWAVE_Users_Manual_en.md#3-effective-deployment-of-a-long-navigation-base);

The test site must have free access to the water so that the watercraft can be launched, people can board and disembark, and the long base consisting of four [RedBase](RedBASE_Specification_en.md) buoys can be deployed and recovered without hindrance.
Preference is given to water bodies with a relatively flat bottom composed of sandy and/or silty soils and a depth of about 10–15 m, with the size of the water body not less than 100 x 100 m.

## 6. Test plan
### 6.1. Field tests
#### 6.1.1. General information
The recommended set of procedures for full-scale tests for compliance with the declared specifications is presented below. This type of testing is normally carried out at the acceptance stage of the equipment set for one arbitrarily selected ES from the set of supplied equipment. By mutual written agreement with the customer, the tests according to selected procedures may be omitted.

#### 6.1.2. Preparation and checking of the equipment for testing
At the preparation stage, the built-in batteries of the ES under test must be charged: the batteries of all four [RedBase](RedBASE_Specification_en.md) buoys and the batteries of all [RedNav](RedNAV_Specification_en.md) instruments under test.  

On all [RedNav](RedNAV_Specification_en.md) instruments, all tracks, waypoints (route points) and saved points are also completely cleared [see RedNav Host: User's manual](RedNAV_Host_Users_Manual_en.md).  

All [RedNav](RedNAV_Specification_en.md) instruments taking part in the tests are configured [see RedNav Host: User's manual](RedNAV_Host_Users_Manual_en.md) according to the salinity of the water body selected as the test site.  

The set of additional equipment is also prepared: the ropes are tied to the anchors and floats in the manner described in the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#211-general-information).  

The preparatory stage must be carried out **no earlier than 1 day before** the tests according to procedures 1–3 described below.
After the described actions are completed, the electrical serviceability and charge of the devices are checked using their indicators (see the specifications of the [RedBase](RedBASE_Specification_en.md) and [RedNav](RedNAV_Specification_en.md) devices).

#### 6.1.3. Deployment of the long base
This stage is carried out immediately before the tests at the selected test site (water body).  
The deployment of the long base is described in detail in [section 3 of the User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#3-effective-deployment-of-a-long-navigation-base).

#### 6.1.4. Preliminary operability tests
This stage may be performed without the participation of a diver, and its purpose is to reject obviously inoperable equipment.  

To do this, with the buoys operating, an arbitrarily selected [RedNav](RedNAV_Specification_en.md) device from the ES is lowered on a rope from the watercraft within the figure of the long base so that it is at least 1.5 m below the surface and at least 1.5 m above the bottom of the water body.  

The device remains submerged for at least 10 and at most 30 minutes; during this time the engine of the watercraft (if any) must be switched off and the position of the watercraft must be fixed with an anchor.  

After the specified time has elapsed, the device is taken out and inspected for operability.  

In this case, the operable state means a state in which the instrument shows no external signs of seal failure (the screen is lit).  

* If the instrument is found inoperable at this stage, its testing is terminated and it is considered to have failed the test.
* If the instrument is found operable, it is switched off (see the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#23-rednav---divers-navigation-receiver)).
It is placed on the charger and connected to the PC using the specialized software included in the ES.  

* If synchronization with the PC does not occur, the instrument is considered to have failed the tests.
* Then, if synchronization with the PC is successful, the navigation data are downloaded.
The presence of the downloaded data confirms the operability of both the instrument itself and the long navigation base (all four [RedBase](RedBASE_Specification_en.md) devices).


#### 6.1.5. Procedure 1 "Reaching a predefined point"
* The [RedNav](RedNAV_Specification_en.md) device under test is synchronized with the PC using the specialized software included in the ES.  
* All saved data are erased on the [RedNav](RedNAV_Specification_en.md) device under test: the track, waypoints and route points.
* A previously selected point is loaded into the device under test (see the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#23-rednav---divers-navigation-receiver)); the point must be located within the figure of the long base.
By agreement, the point may be marked with an anchored marker buoy. Keep in mind that there is a significant discrepancy between positions referenced to different coordinate systems. Preferably, the marker buoy is set from the watercraft and its position is recorded with a portable GPS/GLONASS navigator.
* The [RedNav](RedNAV_Specification_en.md) instrument is handed over to the diver taking part in the tests, together with a compass (attached to the diver or to the diving console). The starting point of the dive is chosen arbitrarily, but not farther than 20 m from the figure of the navigation base.
* After waiting for the instrument to receive navigation data, the diver selects waypoint No. 1 as the target (see the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#23-rednav---divers-navigation-receiver)) and, following the instrument's readings of azimuth and distance to the target, tries to reach the specified point.
* If the instrument is unable to obtain navigation data for more than 10 minutes, the instrument is considered to have failed the tests.
* While moving, the diver must mark 1–2 points at places with clearly visually distinguishable objects and/or may personally place such objects on the bottom.
* Next, upon reaching a position where the distance to the target becomes no more than 2–3 m, the diver must signal that the target has been reached and confirm visual and/or tactile contact with the target.
* Next, the diver ascends to the surface.
* The instrument is synchronized with the PC, and the track is downloaded for subsequent analysis (loading the track into Google Earth software or similar).
* The tests are considered passed if the diver can confidently confirm reaching the target and the downloaded track passes at a distance of no more than 1–3 m from the specified point (or crosses it).

**Note:** by prior agreement with the customer, one of the buoys may be selected as the predefined point.  In this case, the step of loading the point is omitted and the diver is instructed to look for the buoy anchor.

#### 6.1.6. Procedure 2 "Reaching a saved point"
* The device is synchronized with the PC and its track is cleared; the saved points are not deleted.
* The device and the compass are handed over to a second diver, and after descending, the second diver tries to reach one of the points saved by the first diver.
* The procedure is generally similar to procedure 1, the only difference being that the target is a point saved by the first diver.
* The tests are considered passed if the second diver can confidently confirm that the target has been reached.
* After the second diver has ascended and the track has been downloaded, the track is analyzed to determine whether the second diver reached the targets designated by the first diver.

#### 6.1.7. Procedure 3 "Reaching a predefined point as a group"
* This procedure describes a test conducted by at least two divers simultaneously.
* It corresponds to procedure 1 in full, the only difference being that all the divers have different dive entry points.

#### 6.1.8. Completion of the tests
Completion of the tests consists of recovering the long navigation base and desalinating the equipment if the tests were conducted in a salt water body. Equipment maintenance is described in more detail in [section 3 of the User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#3-effective-deployment-of-a-long-navigation-base).


### 6.2. Reliability tests
#### 6.2.1. General information
The test plan described below is recommended and is carried out at the acceptance stage of the equipment set. By mutual written agreement with the customer, some procedures may be omitted.

#### 6.2.2. Preparation and checking of the equipment for testing
This stage consists of charging the built-in batteries of the equipment taking part in this test. Charging must be carried out immediately before the tests.

#### 6.2.3. Procedure 4 "Buoy battery life check"
* A fully charged, arbitrarily selected device (or all devices of the ES) is switched on, and its acoustic transmitter is placed in a water tank with a capacity of at least 10 L so that all parts of the transmitter are covered by a layer of water of at least 100 mm.
* The ambient air temperature must be 20 °C (±5 °C).
* The device is left in this state for 12 hours. 
* After this time has elapsed, the operability of the device is checked by its light indicator, see the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#212-operating-modes-and-light-indication);
* The condition for passing this test is the operability of the device, checked by any activity of the device's light indicator. If the indicator does not light up (does not flash, blink, etc.) for more than 2 minutes, the instrument is considered to have failed the test.

#### 6.2.4. Procedure 5 "Checking the buoy housing for IP68 compliance"
* A fully charged, arbitrarily selected device (or the entire ES), with the covers of the charging connectors screwed on, in the switched-on state, is placed in a water tank in a vertical position for at least 10 and at most 30 minutes so that the distance from the surface of the buoy to the surface of the water is 0.5–1 m.
* The device (or devices) is then removed from the tank and switched off.
* Instruments are considered to have passed the tests if their operability is in no way impaired, which is checked by the light indicator in accordance with the [User's manual](https://github.com/ucnl/ucnl.github.io/blob/master/documentation/EN/RedWAVE/RedWAVE_Users_Manual_en.md#212-operating-modes-and-light-indication).

#### 6.2.5. Procedure 6 "RedNav instrument battery life check"
* A fully charged, arbitrarily selected device (or the entire ES) is switched on and left switched on at an ambient temperature of 20 °C (fresh water or air) for 8 hours.
* After the specified time has elapsed, the operability of the instrument(s) is checked.
* Units are considered operable if their battery charge allows them to be switched on and they can remain switched on for at least 5 minutes.
* **Instruments whose operability is confirmed are considered to have passed the tests successfully.**


<div style="page-break-after: always;"></div>

_____________
[Back to contents](#contents)

<!-- docs-sync: source=documentation/RU/RedWAVE/RedNAV_PM_ru.md commit=526de9e271f6a71ed95771912f3722f1ab7c9bf0 date=2023-03-19 -->
