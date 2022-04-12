| ![logo](/documentation/sm_logo.png) | ![RedPhone-DX](/documentation/redphone_dx.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedPhone-DX** <br/> Wireless telephone for divers <br/> **User's manual** |

# **RedPhone-DX** <br/> Wireless telephone for divers
## **User's manual**

<div style="page-break-after: always;"></div>

## Contents

- [1. General information](#1-general-information)
  - [1.1. Purpose](#11-purpose)
  - [1.2. Description](#12-description)
  - [1.3. Specifications](#13specifications)
  - [1.4. Equipment set](#14-equipment-set)  
- [2. Working with the device](#2-working-with-the-device)
  - [2.1. Preliminary checks](#21-preliminary-checks)
  - [2.2. Work](#22-work)
    - [2.2.1. Sound alerts](#221-sound-alerts)
    - [2.2.2. Receiving voice messages](#222-receiving-voice-messages)
    - [2.2.3. Sending voice messages](#223-sending-voice-messages)
  - [2.3. Shutdown](#23-shutdown)
- [3. Storage and maintenance](#3-storage-and-maintenance)
   - [3.1. Storage and maintenance conditions](#31-storage-and-maintenance-conditions)
   - [3.2. Charging the device](#32-charging-the-device)
   - [3.3. Configuration](#33-configuration)
     - [3.3.1. Step 1](#331-step-1)
     - [3.3.2. Step 2](#331-step-2)
     - [3.3.3. Step 3](#331-step-3)
     - [3.3.4. Step 4](#331-step-4)
     - [3.3.5. Step 5](#331-step-5)
     - [3.3.6. Step 6](#331-step-6)
     - [3.3.7. Step 7](#331-step-7)
     - [3.3.8 Station settings](#338-station-settings)
- [4. Liability and disclaimer](#4-liability-and-disclaimer)
  - [4.1 Terms of replacement and free warranty service](#41-terms-of-replacement-and-free-warranty-service)
  - [4.2 Disclaimer of the manufacturer](#42-disclaimer-of-the-manufacturer)

<div style="page-break-after: always;"></div>

## 1. General information
### 1.1. Purpose
The diving station of voice hydroacoustic communication [RedPhone-DX](RedPhone_DX_Specification_en.md) (hereinafter referred to as the station) is intended for:
- wireless exchange of voice messages between divers equipped with diving communication devices that support signal parameters common with the station;
- wireless exchange of voice messages between divers and a surface control station equipped with a surface station [RedPhone-OS](RedPhone_OS_Specification_ru.md) or other diving communication devices that support signal parameters common with the station;
- determining the location (tracking) of divers using the long-base navigation system [RWLT] (/documentation/EN/RWLT/RWLT_DataBrief_en.md).

The general view of the [RedPhone-DX](RedPhone_DX_Specification_en.md) station is shown in **Figure 1**.

| ![RedPhone-DX](/documentation/redphone_dx.png) |
| :---: |
| **Fig 1 - [RedPhone-DX](RedPhone_DX_Specification_en.md): General view** |

### 1.2. Description
The device is made in the form of a maintenance-free polyurethane monoblock, with built-in LiFePO4 batteries that provide more than 3000 charge-discharge cycles. On the top of the device in its upper part are located:
- hydroacoustic transceiver antenna;
- contacts for connecting the charging cradle;
- contacts for automatic switching on when entering the water / switching off when removed from the water;
- cable inlet with a connector and a PTT (Push-To-Talk) for connecting a communication headset.

> Standard devices are equipped with a connector and a PTT for connecting a headset that does not contain a PTT.

Charging is carried out with a complete cradle (chassis) with a charger. Switching channels and the compatibility mode with the navigation tracking system [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) is carried out using the built-in radio transceiver and the bundled [USB radio dongle](RedPhone_RF_Dongle_Specification_en.md).

To ensure the best working conditions and communication quality, subscribers' acoustic antennas must have a direct line of sight. The recommended mounting location for the device is on the tank on the diver's back. Fastening should be carried out with a belt or rubber band through the fixing eyes. The cables must not restrict the diver's movements. The PTT has a special loop for attaching to the suit.

### 1.3.Specifications
The station uses single-sideband amplitude modulation (_English SSB, Single side band_) and supports the most commonly used bands in such systems, which ensures compatibility with almost all analogues.
**Table 1** shows the correspondence between station channel numbers and frequency bands.

### **Table 1** - Correspondence between channel number and signal parameters

| Channel number | Carrier, Hz | Side band | Bandwidth, Hz |
| :---: | :---: | :---: | :---: |
| 1 | 32768 | Lower | 28468 .. 32468 |
| 2 | 32768 | Upper | 33068 .. 37068 |
| 3 | 31250 | Lower | 26950 .. 30950 |
| 4 | 31250 | Upper | 31550 .. 35550 |
| 5 | 28500 | Lower | 24200 .. 28200 |
| 6 | 28500 | Upper | 28800 .. 32800 |
| 7 | 25000 | Lower | 20700 .. 24700 |
| 8 | 25000 | Upper | 25300 .. 29300 |

The general technical characteristics of the device are given in **Table 2**:

### **Table 2** - Technical characteristics

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS<sup>[1](#footnote1)</sup> (l х w х h) | 203 x 105 x 45 mm |
| WEIGHT<sup>[2](#footnote2)</sup> (dry) | 0.6 kg |
| MAX. WORKING DEPTH | 70 m |
| MAX. ACOUSTIC RANGE<sup>[3](#footnote3)</sup> | 1000 m |
| MAX. ACOUSTIC PRESSURE | 150 dB re 1 uPa @ 1 m |
| VOICE BANDWIDTH<sup>[4](#footnote4)</sup> | 300 .. 4300 Hz |
| NUMBER OF CHANNELS | 8 |
| BATTERY LIFE IN RECEIVING MODE<sup>[5](#footnote5)</sup> | up to 50 hours |
| BATTERY LIFE IN MIXED MODE (20%)<sup>[5](#footnote5),[6](#footnote6)</sup> | up to 8 hours |
| BATTERY LIFE IN MIXED MODE (50%)<sup>[5](#footnote5),[7](#footnote7)</sup> | up 2.5 hours |
| WORKING TEMPERATURES | 0 .. 50° С |
| BUILT-IN POWER SUPPLY | 28 W\*h, LiFePO4, up to 3000 charge-discharge cycles |
| CHANNEL SWITCHING | Wireless, using a [USB-RF Dongle](RedPhone_RF_Dongle_Specification_en.md) |
| BODY MATERIAL | Polyurethane |
| CABLE INSULATION MATERIAL | Polyurethane |
| NAVIGATION SIGNAL CARRIER<sup>[8](#footnote8)</sup> СИГНАЛА | 20050 Hz |
| NAVIGATION SIGNAL MODULATION<sup>[8](#footnote8)</sup> СИГНАЛА | BPSK |
| NAVIGATION SIGNAL DURATION<sup>[8](#footnote8)</sup> СИГНАЛА | 200 msec |

________________
<a name="footnote1"><sup>1</sup></a> Including hydroacoustic antenna.  
<a name="footnote2"><sup>2</sup></a> With a PTT and mask connector, depending on the connector, the value may differ by the weight of the connector.  
<a name="footnote3"><sup>3</sup></a> A parameter that determines the maximum range at which signal reception is possible, based on the electroacoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the level of hydroacoustic interference.  
<a name="footnote4"><sup>4</sup></a> Actual frequency range depends on headset specifications.  
<a name="footnote5"><sup>5</sup></a> With a new, fully charged battery, at an ambient temperature of 20°C.  
<a name="footnote6"><sup>6</sup></a> In a mode 2 minutes transmit 8 minutes receive.  
<a name="footnote7"><sup>7</sup></a> In a mode 5 minutes transmit 5 minutes receive.  
<a name="footnote8"><sup>8</sup></a> The function is provided by buoys of the [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) navigation system.  


### 1.4. Equipment set

### **Table 3** - Contents of delivery

| № | Item | Number | Notes |
| :--- | :--- | :--- | :--- |
| 1 | [RedPhone-DX](RedPhone_DX_Specification_en.md) with a headset connector | 1 pcs. |  |
| 2 | Charger with the cradle | 1 pcs. | |
| 3 | [USB-RF dongle](RedPhone_RF_Dongle_Specification_en.md) for wireless connection to a PC | 1 pcs. | |


Figure 2 shows the scope of delivery

| ![RedPhone-DX](/documentation/redphone_dx_package.png) |
| :---: |
| **Fig 2 - Contents of delivery** |
| The numbers indicate: *1 - charger, 2 - charging chassis (cradle), 3 - PTT, 4 - connector, 5 - USB radio dongle, 6 - RedPhone-DX station* |

The pinout of the connector in the standard version is shown in **Table 4**

### **Table 4** - Connector Pinout

| Pin number | Function |
| :--- | :--- |
| 1 | MIC "+" |
| 2 | SPEAKER "-" |
| 3 | MIC "-" |
| 4 | SPEAKER "+" |


<div style="page-break-after: always;"></div>

## 2. Working with the device
### 2.1 Preliminary checks
Before immersing the device in water, the user must ensure that:
- O-rings (if any) on the headset connector are not mechanically damaged, not dirty, properly lubricated (in accordance with the manufacturer's recommendations);
- a headset is connected to the jack (the jack is connected);
- the device is securely fastened with a strap to the tank (**recommended mounting location**) or to the diver's belt.

Before starting work, the user must:
- check the correctness of the selected communication channels on all devices participating in the work in the immediate vicinity according to p.p. [2.2.2](#222-receiving-voice-messages) and [2.2.3.](#223-sending-voice-messages).

### 2.2. Work
Before work, all preparations and checks provided for in [p. 2.1](#21-preliminary-checks).

Diver's hydroacoustic voice communication works on a half-duplex scheme: transmission and reception alternate, if the device is in transmit mode, it cannot receive incoming messages.

#### 2.2.1. Sound alerts
Possible sound alerts are summarized in **Table 5**.

### **Table 5** - Sound alerts

| Alert | Description |
| :--- | :--- |
| A short rising and then falling tone | The station turned on |
| A short rising tone | Switching to receive mode (when the navigation function is off) |
| A short falling tone (~ every 30 seconds) | Low battery |

#### 2.2.2. Receiving voice messages
To receive voice messages from divers, the **PTT** button on the headset must be released. In this case, incoming messages will be played by the headset.

The volume of the replayed incoming voice messages depends on the distance between the subscriber's antennas, as well as on hydrological conditions. It can decrease when a diver enters the zone of acoustic shadow (when elements of the underwater landscape, parts of structures, vessels, algae, etc. are on the path of the signal).

#### 2.2.3. Sending voice messages
To send voice messages, the following sequence of actions is performed:
* Press PTT ;
* The station emits a short beep, indicating that the device is entering transmission mode;
* Wait a short pause (~**0.5** seconds) for the station to switch to transmit mode;
* Speak voice messages with pronounced articulation; It is recommended to end a voice message with the phrase **"Do you copy?"**, signaling to the addressee that the message is over;
* Sustain a short pause (~**0.5** seconds);
* Release the **PTT**;
* The station emits a short beep to indicate that the device has switched to receive mode if the [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) navigation system compatibility mode is disabled or will emit a navigation signal using a hydroacoustic antenna if navigation compatibility mode [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) is enabled.

### 2.3. Shutdown
Upon completion of the work, the diving station does not require any additional manipulations and turns off automatically when in the air. Before packing in a shipping container, it is necessary to rinse and/or desalinate in fresh water, followed by wiping with an absorbent cloth and air drying for at least 30 minutes.

<div style="page-break-after: always;"></div>

## 3. Storage and maintenance
### 3.1. Storage and maintenance conditions
The station does not need special storage conditions, except for the following:
- Storage at temperatures from -20 ° to 60 °C;
- The headset connector must be disconnected;
- In case of long-term storage (more than a month), it is recommended to recharge the station's built-in power supply;
- To remove impurities from the body of the device and after working in seawater, rinsing in freshwater is required. It is allowed to use a weak solution of household detergents with the battery compartment cover closed; When flushing, avoid getting moisture and / or detergents into the open connector of the headset;
- Bending of cables with a radius of less than 5 cm is not allowed;
- The application of torsion forces to the acoustic antenna or cable entry is not allowed;
- Before placing the device in the shipping container, moisture on the device **must be completely removed**.

> **PROHIBITED:**  
>  
> **- OPENING EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [p. 1.4.](#14-equipment-set)**  
> **- ACCESS TO USE OF EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [p. 1.4.](#14-equipment-set) PERSONS WHO ARE NOT FAMILIAR WITH THESE INSTRUCTIONS**  
> **- ACCESS TO USE OF EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [p. 1.4.](#14-equipment-set) PERSONS UNDER THE ADVANCED**  


### 3.2. Charging the device
Charging the built-in power supply of the station is allowed only with the supplied charger when the headset is disconnected.
Before using the charger, read the instruction manual for the charger.
To charge the device, you must install it in the charging cradle and connect the supplied charger to the household electrical network.
The end of the charge is determined by the indicator of the complete mains charger. It is recommended to leave the device on charge for another 1-1.5 hours after the end of charging according to the indicator on the network adapter.

Charging chassis installation is shown in Figure 3:

| ![RedPhone-DX](/documentation/redphone_dx_charging_cradle.png) |
| :---: |
| **Fig 3 - Charging chassis installation** |


### 3.3. Configuration

Station can be configured:
- one of the supported communication channels from [Table 1](#table-1---correspondence-between-channel-number-and-signal-parameters)
- compatibility mode with tracking system [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md)
- Address (diver ID) for tracking system
- System channel ID [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) (Reserved for future versions, should be 0)

To wirelessly connect the station to a PC, follow these steps:

#### 3.3.1. Step 1

Download the [RedPhoneDXConfig](https://github.com/ucnl/RedPhoneDXConfig/releases/download/1.0/RedPhoneDXConfig.zip) utility (requires PC with Windows 8 or higher).
The application does not require installation: just unzip the archive to a location convenient for you.

#### 3.3.2. Step 2

Disconnect the USB dongle from the PC if connected.

#### 3.3.3. Step 3

Run the application **RedPhoneDXConfig.exe**

#### 3.3.4. Step 4

In the **RedPhone DX Dongle PORT** combo box, pay attention to the ports already present:

| ![Step 4](/documentation/rpdx_cfg1.png) |
| :---: |
| Step 4 |

#### 3.3.5. Step 5

Connect USB dongle to PC, wait a few seconds and click **🗘** (Update) button.
In some cases, you may need to install a driver on the USB converter.
The new port that appears in the list corresponds to the port of the dongle. It must be selected:

| ![Step 5](/documentation/rpdx_cfg2.png) |
| :---: |
| Step 5 |

#### 3.3.6. Step 6

The wireless connection is established exclusively, which means that at one time the configuration work is carried out with only one device [RedPhone-DX](RedPhone_DX_Specification_en.md).
Place the device to be configured up to 5 meters away from the USB dongle.
To turn on telephony without immersing it in water: you can use a wet cloth by placing it on the contacts shown in the figure:

| ![Step 6](/documentation/rpdx_cfg4.png) |
| :---: |
| Step 6 |

You can close the contacts with a metal object, provided that the connection is reliable: if the contact between the conductors is lost, the station will instantly turn off.
You can also put the device in a container of water with the antenna down so that only the antenna and contacts are covered with water. Otherwise, water will interfere with radio communication.

#### 3.3.7. Step 7

In the app, press the **CONNECTION** button. If everything is done correctly, then the text field **RedPhone DX Device Information** will display information about the device:

- Serial number
- The name of the system, its version, as well as the name and version of the communication subsystem

The **RedPhone DX Device settings** field will display the current device settings:

- communication channel number from [Table 1](#table-1---correspondence-between-channel-number-and-signal-parameters)
- indication of enabled/disabled tracking function
- diver's address (identifier) in the [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) tracking system
- [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) system channel identifier (reserved for future use, should always be 0)

| ![шаг 7](/documentation/rpdx_cfg3.png) |
| :---: |
| Step 7 |

#### 3.3.8 Station settings

After the  wireless connection is established, in the **RedPhone DX Device settings** field, the user can set one of the communication channels supported by the station using the **Channel** input field.

> We recommend using **channel number 8**, because the frequency band used in this channel allows the most efficient use of the analog circuitry of the [RedPhone-DX](RedPhone_DX_Specification_en.md) and [RedPhone-OS](RedPhone_OS_Specification_en.md) stations.

> **Always make sure that all devices are set to the same channel when diving together!**

The **RWLT Pinger enabled** checkbox controls the built-in diver tracking feature. When the tracking function is enabled, at the end of each voice transmission from a diver (after releasing the PTT), the station will transmitt a special navigation signal that is received by the buoys of the [RWLT](/documentation/RU/RWLT/RWLT_DataBrief_en.md) system, which allows to determine the geographical position of the diver .

The **RWLT Diver's ID** input field specifies the diver's address (identifier) to be displayed on the map.

> When working with the [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) system, it is very important to set different addresses for all diving stations, otherwise the locations of different divers with the same addresses will be displayed as a single track.

If you do not plan to use the tracking system [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) be sure to uncheck **RWLT Pinger enabled**, this will save battery power and eliminate an additional pause after a voice transmission during which navigation signal is being transmitted.

The current version of the system does not use the **RWLT Channel** setting. Be sure to leave this field set to zero.

To save the settings to a station, press the **APPLY SETTINGS** button. Based on the results, a pop-up window will be displayed confirming the successful recording of new settings:

| ![шаг 8](/documentation/rpdx_cfg5.png) |
| :---: |
| Settings successfully updated |

If it doesn't, check if the dongle and/or station has been disconnected and try again, make sure the station is not turned off or discharged.
If the error persists, contact the developer.


<div style="page-break-after: always;"></div>

## 4. Liability and disclaimer
### 4.1 Terms of replacement and free warranty service
The manufacturer’s warranty applies only to factory defects that were discovered during the operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).

The manufacturer guarantees free repair or replacement of faulty equipment from the equipment set that has failed due to a factory defect.

The reasons for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** of the equipment supplied according to [p. 1.4.](#14-equipment-set), Including violation of insulation of wires and cables;
- any **damage caused by exposure to moisture and pollution** due to improper use of the equipment from the equipment set according to [p. 1.4.](#14-equipment-set);
- any **electrical damage** caused by **use of not original accessories** (charger, headset etc.);  
- any **signs of self-repair and/or opening** of the equipment from the equipment set according to [p. 1.4.](#14-equipment-set).

<div style = "page-break-after: always;"> </div>

### 4.2 Disclaimer of the manufacturer
_____________

_**ANY OF THE PARTS OF THE EQUIPMENT SET ACCORDING TO [par. 1.4.](#14-equipment-set) SEPARATELY AND IN THE COMPOSITION OF THE SYSTEM, NAME FURTHER "DELIVERED EQUIPMENT":**_  

_**- ARE NOT DESIGNED FOR WATER RESCUE USE**_  
_**- NOT TESTED AS RESCUE EQUIPMENT**_  
_**- NOT RESCUE EQUIPMENT**_  
_**- THE MANUFACTURER DECLARES THAT THE DELIVERED EQUIPMENT IS SAFE WHEN OPERATING ACCORDING TO THESE INSTRUCTIONS AND IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF USE OF THE DELIVERED EQUIPMENT**_  

_____________

<div style = "page-break-after: always;"> </div>

[Back to contents](#contents)
