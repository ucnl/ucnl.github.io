[Main](/../../) ❯ [Underwater Wireless voice systems (Underwater telephone)](/underwater_wireless_voice_systems_en) ❯ **User’s manual: RedPhone-OS**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![redphone_os](/documentation/redphone_os.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedPhone-OS** <br/> Underwater telephone. Surface station <br/> **User's manual** |

# **RedPhone-OS** <br/> Underwater telephone (surface station) <br/> **User's manual**

<div style="page-break-after: always;"></div>

## Content

- [1. Description of the RedPhone-OS station](#1-description-of-the-redphone-os-station)
  - [1.1. Purpose of the device](#11-purpose-of-the-device)
  - [1.2. Controls and connectors](#12-controls-and-connectors)
  - [1.3. Specifications](#13-specifications)
  - [1.4. Contents of the standard delivery set](#14-contents-of-the-standard-delivery-set)
- [2. Work with the device](#2-work-with-the-device)
  - [2.1. Preparation for work](#21-preparation-for-work)  
  - [2.2. Testing routines](#22-testing-routines) 
    - [2.2.1. External visual check](#221-external-visual-check) 
    - [2.2.2. Checking device performance](#222-checking-device-performance) 
    - [2.2.3. Checking the transducer and microphone](#223-checking-the-transducer-and-microphone) 
    - [2.2.4. Before work](#224-before-work) 
  - [2.3. Working with the station](#23-working-with-the-station) 
    - [2.3.1. Sound signals](#231-sound-signals) 
    - [2.3.2. Receiving voice messages](#232-receiving-voice-messages) 
    - [2.3.3. Sending voice messages](#233-sending-voice-messages) 
  - [2.4. Shutdown](#24-shutdown) 
- [3. Storage and maintenance](#3-storage-and-maintenance) 
  - [3.1. Storage and Maintenance conditions](#31-storage-and-maintenance-conditions) 
  - [3.2. Built-in Power Supply Charge](#32-built-in-power-supply-charge) 
- [4. Liability and disclaimer](#4-liability-and-disclaimer)
  - [4.1 Terms of replacement and free warranty service](#41-terms-of-replacement-and-free-warranty-service)
  - [4.2 Disclaimer of the manufacturer](#42-disclaimer-of-the-manufacturer)

<div style="page-break-after: always;"></div>

## 1. Description of the RedPhone-OS station
### 1.1. Purpose of the device
The surface station for voice underwater acoustic communication [RedPhone-OS](RedPhone_OS_Specification_en.md) (hereinafter referred to as 
the station) is intended for wireless transmission of voice messages from an overhead control point for diving descents to divers and 
receiving voice messages from divers equipped with wearable diving telephony devices that support signal parameters common with the station.

The general view of the station [RedPhone-OS](RedPhone_OS_Specification_ru.md), with the connected transducer and microphone, is shown in **Figure 1**.

| ![RedPhone-OS](/documentation/redphone_os_big.JPG) |
| :---: |
| **Figure 1 - The general view of the station [RedPhone-OS](RedPhone_OS_Specification_en.md)** |

The device is made in the form of a shockproof plastic device case, which, with the lid closed, provides protection class IP67. 
The built-in power supply made of **LiFePO4** batteries that operate at low temperatures and provide more than 1000 charge-discharge cycles.

### 1.2. Controls and Connectors
The dashboard of the device is made of high-quality stainless steel, on which, using laser engraving, are applied informational inscriptions.
**Figure 2** shows the location of the controls and connectors.

| ![RedPhone-OS top panel scheme](/documentation/redphone_os_top_panel_scheme_en.png) |
| :---: |
| **Figure 2 - Location of controls and connectors** |
| _1 - charger connector, 2 - speaker grill, 3 - transducer connector, 4 - volume control, 5 - channel switch, 6 - device toggle switch, 7 - speaker switch, 8 - microphone and PTT connector, 9 - headphone connector_ |

### 1.3. Specifications
The station uses single-band amplitude modulation (_SSB, Single side band_) and supports the bands most commonly used in such systems, 
which ensures compatibility with almost all analogues.  

**Table 1** shows the correspondence of station channel numbers and frequency bands.

### **Table 1** - Correspondence of the channel number and signal parameters

| Channel number | Carrier, Hz | Side band | Bandwidth, Hz |
| :---: | :--- | :--- | :--- |
| 1 | 32768 | Low | 28468 .. 32468 |
| 2 | 32768 | High | 33068 .. 37068 |
| 3 | 31250 | Low | 26950 .. 30950 |
| 4 | 31250 | High | 31550 .. 35550 |
| 5 | 28500 | Low | 24200 .. 28200 |
| 6 | 28500 | High | 28800 .. 32800 |
| 7 | 25000 | Low | 20700 .. 24700 |
| 8 | 25000 | High | 25300 .. 29300 |

General technical characteristics of the device are given in **table 2**:

### **Table 2** - Specifications

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (length х width х height) | 259 x 202 x 115 mm |
| WIGHT (dry) | 2 kg |
| MAX. OPERATING RANGE<sup>[1](#footnote1)</sup> | 1000 m |
| ACOUSIC SOURCE LEVEL | 160 dB re 1 μPa @ 1 m |
| TRANSDUCER'S CABLE LENGTH<sup>[2](#footnote2)</sup> | 7 m |
| NUMBER OF SUPPORTED CHANNELS | 8 |
| VOICE BANDWIDTH<sup>[3](#footnote3)</sup> | 300 .. 4300 Hz |
| BUILT-IN BATTERY | LiFePO4 60 W\*h | 
| BATTERY LIFE (RX MODE)<sup>[4](#footnote4),[5](#footnote5)</sup> | up to 30 hours |
| BATTERY LIFE (20% TX, 80% RX)<sup>[4](#footnote4),[5](#footnote5),[6](#footnote6)</sup> | up to 24 hours |
| BATTERY LIFE (50% TX, 50% RX)<sup>[4](#footnote4),[5](#footnote5),[7](#footnote7)</sup> | up 12 hours |
| WORKING TEMPERATURE RANGE | -10 .. 50 °С |
| MICROPHONE | Handheld, with PTT |
| EXTERNAL HEADPHONES RESISTANCE (not less) | 8 Ohm |
| PROTECTION CLASS | IP67<sup>[8](#footnote8)</sup> |
  
________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> By agreement, delivery with increased cable length is possible.  
<a name="footnote3"><sup>3</sup></a> The actual audible frequency range depends on the headset used.  
<a name="footnote4"><sup>4</sup></a> When playing on the built-in speaker, with a volume level of 40%.  
<a name="footnote5"><sup>5</sup></a> With a fully charged, new battery. At an ambient temperature of 20 ° C.  
<a name="footnote6"><sup>6</sup></a> In the mode, 2 minutes of transmission and 8 minutes of reception.  
<a name="footnote7"><sup>7</sup></a> In the mode, 5 minutes of transmission and 5 minutes of reception.  
<a name="footnote8"><sup>8</sup></a> With top cover closed


### 1.4. Contents of the standard delivery set
This paragraph describes the standard delivery set (see **table 3**).
By an additional agreement with the manufacturer, it is possible to supply a transducer with an extended cable.

### **Table 3** - RedPhone-OS Standard delivery set
  
| No. | Name | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| 1 | Station RedPhone-OS | 1 PC. |   |
| 2 | Transducer | 1 PC. | cable 7 m |
| 3 | Tangent Microphone | 1 PC. |   |
| 4 | AC Charger | 1 PC. |   |
| 5 | Carabiner for attaching antenna cable | 1 PC. |   |
| 6 | Waterproof bag for transportation and storage of transducer and microphone | 1 PC. |   |
| 7 | Adapter with Jack 3.5 mm jack for connecting headphones (earphones) | 1 PC. |   |

<div style="page-break-after: always;"></div>

## 2. Work with the device
### 2.1. Preparation for work
* Place the station on a stable non-slip horizontal base;
* Bind the station by the handle of the case with the help of a safety cord to the guard rail, railing, etc. to prevent the station from tipping over into the water;
* Open the station cover by pushing the locks down (see **Figure 3**):

| ![RedPhone-OS case lock](/documentation/smallcase_lock1.png) |
| :---: |
| **Figure 3 - Lock** |

* Fix the cable of the hydroacoustic antenna with a carabiner, as shown in **Figure 4**, to unload the antenna connector from possible jerking and tension. It is allowed to fix the cable to the load-carrying eye using a polymer cord with a thickness of at least 4 mm.

### 2.2. Testing routines
#### 2.2.1. External visual check
It is carried out with the station cover open. During this check, it is controlled that:

* The integrity of the protective caps on the toggle switches **"Speaker"** and **"Power"** of the front panel of the station is not broken;
* Water, salt and other contaminants are absent inside the connectors on the front panel of the station and mating connectors (transducer, microphone, headphones (when using));
* The integrity of the insulation of the cables of the transducer and microphone is not broken;

> **If the expected conditions do not coincide with those observed, the operation of the station is prohibited!**.

#### 2.2.2. Checking device performance
It is carried out after a successful visual inspection, according to [p. 2.2.1](#221-external-visual-check).

Additional verification conditions:
* toggle switch **"Power"** is installed in the position **"Off"**;
* Toggle switch **"Speaker"** is installed in the position **"On"**;
* regulator **"Volume"**, set for 12 hours (50% of the scale);

During the inspection, it is controlled that:

* When translating the toggle switch **"Power"** to the position **"On"** the station emits a short beep, indicating the presence of power and that the device is working;

[Sound example](/documentation/redphone_pwon.wav)

After the check the toggle switch **"Power"** should be moved to the position **"Off"**

> **If the expected conditions do not coincide with those observed, the operation of the station is prohibited!**.

#### 2.2.3. Checking the transducer and microphone
It is carried out after successful checks in accordance with [p. 2.2.1](#221-external-visual-check) and [p. 2.2.2](#222-checking-device-performance).

Additional verification conditions:
* Toggle switch **"Power"** is installed in the position **"Off"**;
* Toggle switch **"Speaker"** is installed in the position **"On"**;
* Regulator **"Volume"**, set to **12 hours (50% of the scale)**;
* Complete **transducer** connected to the connector **"Antenna"** on the front panel of the station;
* Complete **microphone** is connected to the connector **"Microphone"**;
* **Tangent** (_PTT, Push-to-talk_) on the microphone **not pressed**;

During the inspection, it is controlled that:

* When translating the toggle switch **"Power"** to the position **"On"** the station emits a short beep, indicating the presence of power and that the device is working;
* A constant noise background is heard from the station speaker, the intensity of which can vary;
* When you touch the transducer, the station reacts with a change in noise (for example, when you lightly tap the sonar antenna from the speaker of the station, these clicks should be heard;
* When **the tangent is pressed** the noise from the speakers completely stops (transmission is in progress), and when **is released** the station emits a short beep, after which the background noise can be heard again;

After the check the toggle switch **"Power"** should be moved to the position **"Off"**

[Sound sample](/documentation/redphone_pwon_rx_check.wav)

> **If the expected conditions do not coincide with those observed, the operation of the station is prohibited!**.

> To check the operability of the headphones, the toggle switch **“Speaker”** must be in the state **“Off”** and all sound signals, including the background noise, should be controlled using the headphones according to the method described above.  

#### Video tutorial: RedPhone-OS check before usage

<a href="https://youtu.be/j6Sgx4F4Q8E" 
target="_blank"><img src="http://img.youtube.com/vi/j6Sgx4F4Q8E/0.jpg" 
alt="RedPhone: check before usage" width="240" height="180" border="10" /></a>

#### 2.2.4. Before work
It is carried out after successful checks according to paragraphs. [2.2.1](#221-external-visual-check) .. [2.2.3](#223-checking-the-transducer-and-microphone).

Make sure that:
* The station is installed on a stable non-slip horizontal base and tied by the handle to the rail, railings, etc. to prevent the station from tipping over into the water;
* The device cover is open;
* **Transducer** is connected to the connector **"Antenna"**;
* **Microphone** is connected to the connector **"Microphone"**;
* If the station is used without headphones:
  * Toggle switch **"Speaker"** is in the position **"On"**;
* If the station is used with headphones:
  * Toggle switch **"Speaker"** is in the position **"Off"**;
  * Headphones are connected to the connector **Headphones**;
* The covers of all unused connectors are screwed with a light effort;
* Nuts on all connected cable connectors are screwed with light effort;
* Toggle switch **"Power" ** is installed in the position **"On"**;
* Toggle Switch **"Channel"** is set to the position corresponding to the communication channel installed on diving devices;
* The transducer is lowered into the water to such a depth that it is at least 2 meters from the bottom of the vessel and at least 1.5 meters from the bottom;
* There is direct visibility between the transducer of the station and the transducers of diving stations (not obscured by elements of the underwater landscape, parts of various structures, ships, etc.).

### 2.3. Working with the station
Before work, all preparations and checks provided in [p. 2.2](#22-testing-routines).

The underwater telephone works in half-duplex mode: transmission and reception alternate; if the device is in transmission mode, it cannot receive incoming messages.

#### 2.3.1. Sound signals
Possible sound alerts are summarized in **table 4**.

### **Table 4** - Sound alerts

| Alert Description | Cause of alert | Example |
| :--- | :--- | :--- |
| Short rising and then lowering tone | The station power-on and switch to receive mode | [Sound sample](/documentation/redphone_pwon.wav) |
| Short rising tone | Switching to receive mode after completion of transmission (releasing tangents **PTT**) | [Sound sample](/documentation/redphone_switch_to_rx.wav) |
| Short falling tone (~ every 30 seconds) | Low charge internal power supply |   |

#### 2.3.2. Receiving voice messages
To receive voice messages from divers, the **PTT** button on the microphone must be released. In this case, incoming messages will be played by the device’s speaker (or headphones, if the latter are connected and the toggle switch **“Speaker”** is in the state **“Off”**).

The volume of reproduced incoming voice messages depends on the slant range between the antenna station and the diver, as well as on hydrological conditions. It may decrease when a diver enters the acoustic shadow zone (when elements of the underwater landscape, parts of structures, ships, algae, etc. are on the signal path).

The user must independently set a comfortable volume level using the **Volume** control depending on the current communication conditions.

#### 2.3.3 Sending voice messages
To send voice messages, the following sequence of actions is performed:
* Bring the microphone to the mouth with at a distance of **0.5 - 2** cm;
* Press the tangent **PTT**;
* Hold a short pause (~ **0.5** seconds) so that the station switches to transmission mode;
* Pronounce voice messages with pronounced articulation; It is recommended to end the voice message with the word **"Reception!"**, signalling to the addressee that the message is over;
* Maintain a short pause (~**0.5** seconds);
* Release the tangent **PTT**;
* The station emits a short beep, indicating that the device has switched to receive mode.

### 2.4. Shutdown
Upon completion of the work, the actions should be performed in the following sequence:
* Toggle switch **"Power"** translate into position **"Off"**;
* Pull the transducer cable out of the water;
* Further actions are performed only if there is no risk of water entering the open connectors:
  * Disconnect all connected connectors;
  * Screw protective covers of all connectors;
  * Disconnect the carabine of the load-carrying eye from the device cover;
  * Close the device cover.
  
<div style="page-break-after: always;"></div>

## 3. Storage and maintenance
### 3.1. Storage and Maintenance conditions
The station and the complete equipment: transducer, microphone and charger do not have special storage conditions, except for the following:
- Storage at temperatures from -20° to 60° C;
- All connectors are disconnected, the protective covers are screwed with a slight effort, the station is turned off (toggle switch 
**"Power"** in position **"Off"** the device cover is closed;
- For long-term storage (more than a month), it is recommended to recharge the built-in power supply of the station;
- If moisture gets on the loudspeaker diffuser, it should be removed by turning the station upside down, the remaining moisture should be removed by natural evaporation;
- A brief rinse with a weak stream of water is allowed with the connector covers closed;
- No mechanical impact on the speaker cone;
- To remove contaminants from the device’s case, it is allowed to use a weak solution of household detergents with the connector covers and device cover closed;
- Do not allow moisture to enter the connectors of the transducer, microphone, headphones, charger and adapter for connecting headphones;
- Do not bend the cable of the transducer with a radius of less than 5 cm;
- Moisture is not allowed on the microphone, moisture that has gotten must be removed with a dry absorbent cloth, after which the device must dry for at least 8 hours in a dry room at a temperature of 15° C to 50° C and relative humidity not more than 50%;
- Storage and transportation of the antenna and the microphone is carried out in a waterproof bag;
- Before placing the antenna and microphone in the shipping bag, **they must be completely freed from moisture**.

> **FORBIDDEN:**  
>
> **- OPENING OF EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [par. 1.4.](#14-contents-of-the-standard-delivery-set)**  
> **- ACCESS TO USE OF EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [par. 1.4.](#14-contents-of-the-standard-delivery-set) PERSONS WHO ARE NOT FAMILIAR TO THESE INSTRUCTIONS**  
> **- ACCESS TO USE OF EQUIPMENT FROM THE DELIVERY SET ACCORDING TO [par. 1.4.](#14-contents-of-the-standard-delivery-set) PERSONS WHO ARE NOT ADULTS**  
> **- ENABLING TRANSMISSION MODE (PRESSING THE PTT BUTTON ON THE MICROPHONE) WHILE TRANSDUCER IS UNCONNECTED**  


### 3.2. Built-in Power Supply Charge
The charge of the station’s built-in power supply is allowed only with the original charger when the station is off (toggle switch **“Power”** in position **“Off”**) and all other connectors are disconnected.
Before using the charger, you must read the operating instructions for the charger.

<div style="page-break-after: always;"></div>

## 4. Liability and disclaimer
### 4.1 Terms of replacement and free warranty service
The manufacturer’s warranty applies only to factory defects that were discovered during the operation of the device in accordance with this manual during the warranty period (2 years from the date of purchase).

The manufacturer guarantees free repair or replacement of faulty equipment from the delivery set that has failed due to a factory defect.

The reasons for refusing free warranty service, free repair and replacement include:
- any **mechanical damage** of the equipment supplied according to [p. 1.4.](#14-contents-of-the-standard-delivery-set), Including violation of insulation of wires and cables;
- any **damage caused by exposure to moisture and pollution** due to improper use of the equipment from the delivery set according to [p. 1.4.](): Moisture in the connectors, inside the microphone, adapter for connecting headphones, etc.
- any **electrical damage** caused by **use of not original accessories** (transducer, microphone, adapter for connecting headphones, headphones with resistance less than that specified in the specification of the device, charger);  
- any **signs of self-repair and/or opening** of the equipment from the delivery set according to [p. 1.4.](#14-contents-of-the-standard-delivery-set).

<div style = "page-break-after: always;"> </div>

### 4.2 Disclaimer of the manufacturer
_____________

_**ANY OF THE PARTS OF THE DELIVERY SET ACCORDING TO [par. 1.4.](#14-contents-of-the-standard-delivery-set) SEPARATELY AND IN THE COMPOSITION OF THE SYSTEM, NAME FURTHER "DELIVERED EQUIPMENT":**_  

_**- ARE NOT DESIGNED FOR WATER RESCUE USE**_  
_**- NOT TESTED AS RESCUE EQUIPMENT**_  
_**- NOT RESCUE EQUIPMENT**_  
_**- THE MANUFACTURER DECLARES THAT THE SUPPLIED EQUIPMENT IS SAFE WHEN OPERATING ACCORDING TO THESE INSTRUCTIONS AND IS NOT RESPONSIBLE FOR ANY CONSEQUENCES OF USE OF THE SUPPLIED EQUIPMENT**_  

_____________

<div style="page-break-after: always;"></div>

[Back to content](#content)
