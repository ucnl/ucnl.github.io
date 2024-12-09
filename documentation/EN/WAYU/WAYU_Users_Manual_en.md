[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **WAYU: User’s manual**

> ℹ Этот документ можно распечатать прямо из браузера. 
> Для лучшего результата:
> - выберите диапазон страниц для печати, исключая первую и последнюю
> - в дополнительных настройках отключите нижние и верхние колонтитулы

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/39fce8cb-6f97-4697-a1ab-6dcd68e56239) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU** - Underwater acoustic tracking system <br/> User's manual |

# WAYU <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents



<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1. Purpose

The underwater acoustic tracking system **WAYU** is designed to:

- determine the geographic location of an underwater object (**AUV**, **ROV**, **OPA**, diver, etc.) equipped with a pinger beacon [WAYU Pinger](WAYU_Pinger_Specification_en.md).

### 1.2. Features

The **WAYU** system is the most **easy** to use, **affordable** and at the same time **precise enough** solution for tracking an underwater object. The system **does not require any calibrations** and integration: it is enough to place a [WAYU Pinger](WAYU_Pinger_Specification_en.md) beacon-pinger on an underwater object (ROV, AUV, diver, etc.), and four [WAYU GIB](WAYU_GIB_Specification_en.md) navigation buoys on the water surface. This configuration allows real-time monitoring of the underwater object's movement. 

### 1.3. System composition

The minimum system composition includes:

- **Four hydroacoustic buoys** [WAYU GIB](WAYU_GIB_Specification_en.md):

| ![WAYU_GIB_1](https://github.com/user-attachments/assets/2adaa0a0-2f97-4ba9-897c-cd4edc409028) |
| :---: |
| [WAYU GIB](WAYU_GIB_Specification_en.md) <br/> Navigation hydroacoustic buoy-receiver |

- Navigation solver/radio modem/dongle with built-in GNSS receiver [uNav WAYU RF Dongle](WAYU_RF_Dongle_Specification_en.md), for receiving navigation information from buoys:

| ![uNav_WAYU_RF_Dongle](https://github.com/user-attachments/assets/0ec0811b-8283-460a-9036-9460f6c780c3) |
| :---: |
| [WAYU RF Dongle](WAYU_RF_Dongle_Specification_en.md) <br/> Digital radio receiver |

- beacon-pinger [WAYU Pinger](WAYU_Pinger_Specification_en.md). The pinger works independently and the geolocation of the object to which the pinger is attached will be updated every two seconds.

| ![wayu_pinger](/documentation/RT_1_332820_1.png) |
| :---: |
| [WAYU Pinger](WAYU_Pinger_Specification_en.md) <br/> Beacon-pinger |


## 2. Working with the system

### 2.0. Before work

To track an underwater object equipped with an autonomous pinger [WAYU Pinger](WAYU_Pinger_Specification_en.md), the operator's PC must have the [uNav](https://github.com/ucnl/uNav/releases/download/1.0/uNav.zip) application installed. Before work, be sure to read the quick user guide: [uNav Application: User Manual](documentation/RU/RWLT/uNav_application_Users_manual_en.md)

Download the necessary software in advance. Installation is not required - just unzip the contents of the archive to a convenient location.

Before going to the reservoir, make sure that all equipment is fully charged, and charge all devices if necessary.

Since the devices have built-in power sources based on **LiFePO4**, they have a very flat discharge characteristic and it is difficult to determine the charge level of the built-in source. Therefore, it is recommended to charge all devices no earlier than 1-2 days before use.

### 2.1. Preparation for work and equipment check

#### 2.1.2. Checking the buoy set

- Make sure all buoys in the set are intact, paying special attention to the hydroacoustic antenna cable;
- Make sure all buoys are operational and their built-in power sources are sufficiently charged by turning them on by placing the bottom of the buoy in water: if there is a GNSS signal, even if there is no ping signal, each buoy transmits a status message in the radio channel containing information about its address, the voltage of the built-in power source and its geographic location.

The buoys in each set have different addresses from 1 to 4, the buoy number is marked on the float.

If the battery is in a critical discharge state (voltage below 11.9 V), the buoy must be *immediately* charged to avoid failure of the built-in power source.

If everything is done correctly, and the tops of the buoys have a good view of the celestial hemisphere, then after some time (usually no more than 1-2 minutes) you will be able to see the positions of the buoys in the main window of the application.

After that, you can place the buoys on the surface of the water.

#### 2.1. Charging the built-in power source

The device is charged using the included accessory and only when the device is turned off and completely dry.

| |
| :---: |
| ![wayu_gib_charger](https://github.com/user-attachments/assets/ad0b822e-87ae-4807-b09a-5bf984996d5f) |
| Buoy charger |

There are two bronze contacts at the bottom of the buoy, which are used both to turn on the device when it hits the water and to charge its built-in power source. Each of the contacts is marked with the symbols "+" or "-", meaning plus and minus power, respectively. Observe the polarity when connecting the charger. The plus power on the charger is marked in red.

Before connecting the accessory to the buoy, disconnect the accessory from the network. Make sure that the charging contacts of the accessory are inserted into the sockets on the buoy observing the polarity, then connect the charger to the network.

> Depending on the version of the charger, the operating mode indication may differ. For more information, please refer to the instructions for the charger.

As a rule, chargers have the following indication:

| Mode/Status | Indicator |
| :--- | :--- |
| Charger is connected to the network | Red lights |
| Battery is connected, charging | Not lit |
| Charging complete | Red lights |

| |
| :---: |
| ![image](https://github.com/user-attachments/assets/3332cb46-2e70-4708-8632-9e6b110e1c3f) |
| Connecting the charger to the buoy |

Once charging is complete, unplug the charger and disconnect the charging accessory from the buoy.

#### 2.1.3. Positioning buoys on the water surface

The buoys are placed in the water area on the water surface, their position is fixed using anchors.

> It is worth remembering that although the buoys have a small positive buoyancy, they are not intended for direct fastening to the
> anchor rope. To unload the buoy from the weight of the anchor rope, fenders (or floats) corresponding to the weight of the rope should be used.

The figure below<sup>[1](#footnote1)</sup> shows the recommended scheme for installing a buoy on a reservoir.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_dep_scheme.png)|
| Recommended buoy installation scheme |
| _1 - hydroacoustic navigation buoy, 2 - additional weight<sup>[2](#footnote2)</sup>, 3 - float, 4 - anchor rope, 5 - anchor_ |

__________
<a name="footnote1"><sup>1</sup></a> Images may differ from the supplied products,
as the manufacturer is constantly working to improve the characteristics and makes changes to the design.
<a name="footnote2"><sup>2</sup></a> Additional weight is used only in the underloaded version.

Buoys should be positioned in a convex quadrangle covering the entire intended work area with a small margin. It is important to comply with several simple conditions for the efficient operation of the system:

- the buoys are located no closer than 30 and no further than 300 meters **from each to each**
- there must be a direct line of sight from each buoy to the receiving radio modem of the operator's console
- there must be a direct line of sight from each hydroacoustic receiver of the buoy to the positioned underwater object
- it is not recommended to place buoys close to the shore, port infrastructure facilities, or ships
- the size of the navigation base (the average size of the rectangle formed by the buoys on the water surface) must not be less than the maximum depth of the positioned object
- the size of the navigation base must be slightly larger than the expected area of ​​work

> _**ATTENTION!**_
> The buoys are not underwater devices and are designed to operate on the water surface. Although the protection class implies a short-term overlap of the device by a wave, it is worth remembering that the built-in radio equipment (GNSS module and radio modem) cannot operate in such conditions!

It is not recommended to throw buoys overboard. It is necessary to carefully lower them to the surface of the water, while making sure that the length of the anchor rope is sufficient and its weight is supported by the unloading fender, and the buoy is located vertically on the surface of the water and does not experience any additional loads.
#### 2.1.4. Подготовка подводного оборудования

Не требуется никаких предварительных действий кроме предварительной зарядки встроенного источника питания (батарейного блока) для исполнения с автономным маяком-пингером. 
При наличии разъемного соединения маяка-пингера и батарейного блока необходимо предварительно убедиться в том, что герморазъем плотно закрыт и обслужен (для резьбовых разъемов убедиться что уплотнительные кольца смазаны силиконовой смазкой, для разъемов типа SUBCONN и подобных - убедиться, что на обе части разъема нанесена смазка, рекомендованная производителем разъемов).

Включение маяка-пингера в автономном исполнении происходит автоматически, при попадании его в воду (контакты для включения от воды расположены на разъеме). 

Маяк-пингер должен крепиться только за специальный паз мягким хомутом таким образом, чтобы исключить любое неравномерное нагружение корпуса маяка, излишнее сдавливание и затенение/экранирование корпуса маяка. Ниже на рисунке представлены базовые требования по монтажу акустической части маяка-пингера на носителе:

| |
| :---: |
| ![0](/documentation/uWave_mounting_en.png)|
| Requirements for mounting the acoustic part of the pinger beacon on the carrier |
| _Shielding of the spatial hemisphere or parts of the antenna located above the mounting groove is not allowed; the pressure in the area under the mount must be balanced with the external pressure_ |

The operability of the pinger beacon can be easily checked: when turned on, it begins to emit a navigation signal (heard as a click) with a period of 2 seconds.

#### 2.1.5. Preparing the radio dongle for operation

Connect the radio dongle to a PC with the uNav application installed using a USB-B cable.

After power is supplied, the radio modem turns on the indicator light (blinks). The radio modem has a two-color indicator light. One of the colors lights up synchronously with the arrival of messages from the buoys via the radio channel, thereby signaling the presence of communication with the buoys, and the other lights up when the next portion of data is received from the built-in GNSS receiver, and goes out if the data is valid. If it is constantly lit, this signals that the built-in GNSS module has not yet determined its own location.

During normal operation of the system, one of the indicators will blink once per second, and the other should blink four times for 2 seconds - this is the period during which messages from all four buoys should arrive.

#### 2.1.6. Selecting a location for the operator console

Attach the radio modem at the highest possible point so that there is direct visibility between the radio modem antenna and all buoys throughout the entire operation of the system.

The radio modem antenna should not be shaded by any objects that block the radio signal: elements of the ship's deck superstructure, the side, mast and other radio equipment, trees, building walls, elements of port infrastructure, etc.

## 2.2. Working with the system

It is necessary to remember the factors that reduce the efficiency of the system:
- hydrological conditions: natural and man-made noise can worsen and completely exclude the normal operation of the system; unfavorable underwater landscape and bottom vegetation can contribute to the occurrence of acoustic shading, etc.
- the positioned object(s) goes beyond the navigation base (the figure formed by the buoys on the water surface): the most stable operation of the system is achieved inside the navigation base. The position in the immediate vicinity of one of the buoys or directly behind it is also unfavorable.
- large vessels, especially those with a large draft, can impede the passage of the acoustic signal.

Determining the location of an underwater object is possible when all buoys have GNSS reception, and the operator's console has radio signal reception from all buoys. That is, the application displays the positions of all four buoys;

## 2.3. Upon completion of work

**Navigation buoys** must be:
- removed from anchors;
- cleaned of contaminants (silt, dirt, algae, etc.);
- desalinated, if the work was not carried out in fresh water;
- wiped with a soft cloth to remove moisture before placing in the transport case;

The following is not allowed:
- Storage in a non-desalinated form;
- Storage of buoys together with wet anchor ropes and other wet objects;

**Pinger beacon** must be:
- dismantled from the carrier;
- washed from contaminants (silt, dirt, algae, etc.);
- desalinated, if the work was not carried out in fresh water;
- carefully wiped with a soft cloth and dried in the air for at least 30 minutes;

The following is not allowed:
- Storage in the presence of moisture (especially sea moisture);

<div style="page-break-after: always;"></div>

## 3. Obligations and Disclaimer
### 3.1. Terms of Replacement and Free Warranty Service
The manufacturer's warranty applies only to manufacturing defects that appear during operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a manufacturing defect.

The grounds for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** to the equipment from the delivery set, including damage to the insulation of wires and cables;
- any **damage caused by exposure to moisture and dirt**, due to improper use of the equipment from the delivery set;
- any **electrical damage** caused by **use of incomplete accessories** (charger), use of low-quality and/or faulty batteries; Incomplete accessories do not include accessories supplied by the manufacturer or its representative to replace faulty or lost ones; - any **traces of independent repair and/or opening** of the equipment from the delivery set.
<div style="page-break-after: always;"></div>

### 3.2. Limitation of Manufacturer's Liability

_____________

_**ANY OF THE PARTS OF THE DELIVERY KIT, INDIVIDUALLY OR AS PART OF A SYSTEM, HEREIN ARE REFERRED TO AS "SUPPLIED EQUIPMENT":**_

- _**NOT DESIGNED AS A RESCUE MEANS**_
- _**NOT TESTED AS A RESCUE MEANS**_
- _**IS NOT A RESCUE MEANS**_
- _**THE MANUFACTURER DECLARETHAT THE SUPPLIED EQUIPMENT IS SAFE WHEN USED IN ACCORDANCE WITH THESE INSTRUCTIONS AND IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF USING THE SUPPLIED EQUIPMENT EQUIPMENT**_

______________

_**THE MANUFACTURER WARRANTS THAT THE RWLT HYDROACOUSTIC TRACKING SYSTEM (HEREINAFTER - THE SYSTEM):**_
- _**IS INTENDED ONLY TO WORK WITH PINGER BEACONS OR DIVING COMMUNICATION STATIONS DESIGNED FOR JOINT OPERATION WITH THE SYSTEM**_
- _**BY DESIGN CANNOT BE USED TO TRACK OBJECTS NOT EQUIPPED WITH PINGER BEACONS OR DIVING COMMUNICATION STATIONS NOT DESIGNED FOR JOINT OPERATION WITH THE SYSTEM**_
- _**CONTAINS ONLY CIVILIAN AND NON-LICENSABLE RADIO FREQUENCY MODULES: GNSS RECEIVERS AND RADIO MODEMS**_
_**THE ABOVE LIMITATIONS CANNOT BE REMOVED BY ANY MANIPULATION OF THE SETTINGS AND/OR CONTROLS OF THE SYSTEM INSTRUMENTS AND/OR SOFTWARE DESIGNED TO WORK WITH THE SYSTEM**_
______________

[Back to contents]()

<div style="page-break-after: always;"></div>


