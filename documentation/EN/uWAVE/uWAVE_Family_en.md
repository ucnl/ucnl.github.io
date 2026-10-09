[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave devices family: Data brief**

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

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** - family of underwater acoustic digital communication devices <br/> Data brief |

# uWave devices family <br/> Data brief

<div style="page-break-after: always;"></div>

## 1. Devices of the family

The **uWave** family (_pronounced: "mu-wave" or "you-wave"_) is specifically designed for applications that are extremely sensitive to weight and size, and is currently represented by three devices:

* [uWave](uWAVE_Specification_en.md) - underwater acoustic modem. It is the smallest underwater acoustic modem in the world: its size is only **Ø40x45** mm, 
and its dry weight does not exceed 160 grams. With these parameters, it can transmit data over distances of more than **1000** meters.
* [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) - underwater acoustic modem. A reinforced version of the base device. Thanks to an enlarged transducer and a power amplifier, it can transmit data over distances of more than **3000** meters. Supplied as a modem printed circuit board module and a transducer.
* [uWave Max](uWAVE_Max_Specification_en.md) - underwater acoustic modem. A reinforced version of the base device. Thanks to an enlarged transducer
and a power amplifier, it can transmit data over distances of more than **3000** meters. Its dimensions are **Ø62x65** mm, 
and its dry weight is 360 grams.
* [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) - underwater acoustic modem with the function of determining the horizontal angle of arrival of the signal. 
The device is equipped with a phased array and a built-in inclinometer, which makes it possible to determine the horizontal direction 
from which the signal from any other device of the **uWave** family arrived. The dimensions of the [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) are **Ø64x128** mm, 
and the dry weight of the device is 440 grams.

A more detailed comparison of the characteristics of the family devices can be found in the [uWave modems comparison tables](uWAVE_Modems_comparison_en.md).

All devices within the family are fully acoustically compatible and have a common [NMEA-like protocol](uWAVE_Protocol_Specification_en.md) for interfacing.

<div style="page-break-after: always;"></div>

## 2. Features of the acoustic protocol and code channels
The **uWave** acoustic transmission protocol implements code division multiple access (CDMA) and supports 20 
isolating code channels. Any device of the uWave family can be configured with any code channels for reception and transmission.

An isolating code channel guarantees that data transmitted in one channel will not be received by a device receiving in any 
other code channel. 

All devices of the **uWave** family can receive in only one code channel at a time.

### 2.1. Data rate
The standard mode for **uWave** devices is the mode with a data rate of **78 bit/s**. This mode provides the maximum range and reliability of communication. It is in this mode that the largest number of code channels is available.

All devices of the **uWave** family support alternative modes providing data rates of **156**, **314** and **634 bit/s**. The higher the rate, the lower the noise immunity and, accordingly, the reliability and range of communication. 

Different data rate modes are not compatible with each other. Switching the modem to another data rate mode is done by [replacing its firmware](uWAVE_FW_Updating_en.md).


<div style="page-break-after: always;"></div>

## 3. Device operating modes
All devices of the family can operate in two modes; switching between them is performed by the user:
* Transparent channel mode
* Command mode

These modes determine how the modem perceives the data coming from the control system:

### 3.1. Transparent channel mode
In the transparent channel mode, the devices do not analyze the data coming from the control system and transmit it unchanged 
to the underwater acoustic channel, where it can be received by any device of the family that is receiving in the same code channel 
in which the transmission was made.

### 3.2. Command mode
In command mode, the devices analyze the data coming from the control system, and interaction with them is carried out within a 
very simple [NMEA-like ASCII protocol](uWAVE_Protocol_Specification_en.md).  
In this mode, the devices can send short code requests to other devices: to request the depth, temperature and 
supply voltage of a remote modem, and to transmit 9 user commands.  
Code requests have fixed lengths of the request and response signals, which allows the requesting system to determine the propagation 
time (and slant range) to the requested system.

The remote modem receives and processes a code request regardless of the mode it is in, which relieves the user 
system of the need to monitor the state of the remote modem.

The [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) devices make it possible to determine the horizontal angle 
of arrival of any incoming message from other devices of the **uWave** family. This includes user messages transmitted in transparent channel mode. 

### 3.2.1. Packet mode
Packet mode allows transmitting data packets with guaranteed delivery (ALO - At-least-once) and delivery notification to the addressee. In packet mode, logical addressing of up to 254 subscribers is used on top of the code channels (255 is a broadcast address without notification and guaranteed delivery). Packet mode can be used only when the modem is in command mode.

<div style="page-break-after: always;"></div>

## 4. Device equipment
The [uWave](uWAVE_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) devices have a built-in supply voltage measurement module. The supply voltage of all devices of the family can be requested remotely by any other devices of the family.  
**Starting from firmware version 1.30, with command mode enabled by default, the SVC/CMD cable wire becomes a digital output. Strobing rectangular pulses synchronized with the moment the emission starts and the moment an incoming message is detected are transmitted to it. This option makes it possible to build navigation systems based on the modems.**

The [uWave](uWAVE_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) devices have built-in depth/temperature sensors. Depth and temperature readings can be requested remotely by any device of the family.

The [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) devices additionally have built-in two-axis inclinometers 
(they measure the roll and pitch angles). The user can configure the output of this data in any ratios, or periodically, with a set 
period (from 0.5 to 60 seconds), or in tandem - when any data is received from remote devices. Inclinometer readings are available only locally.

All devices equipped with depth/temperature sensors, when switched on in air, automatically calibrate the pressure sensor, which eliminates the depth determination error associated with changes in atmospheric pressure and the zero drift of the sensor. To achieve the maximum accuracy possible for 
this technology, the device allows setting an appropriate value of the acceleration due to gravity for the place of work 
(for example, according to the WGS84 Gravity model, thereby eliminating the influence of its variation with geographic latitude).

The devices are designed for a maximum immersion depth of 300 meters.

### 4.1. Parameters available locally

Parameters that can be obtained from the device locally, i.e. when connected to it by cable.

|  | [uWave](uWAVE_Specification_en.md) | [uWave Max](uWAVE_Max_Specification_en.md) | [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) | [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) |
| :--- | :---: | :---: | :---: | :---: |
| Pressure           | ✓ | ✓ | ✘ | ✓ |
| Temperature        | ✓ | ✓ | ✘ | ✓ |
| Depth              | ✓ | ✓ | ✘ | ✓ |
| Supply voltage     | ✓ | ✓ | ✓ | ✘ |
| Roll               | ✘ | ✘ | ✘ | ✓ |
| Pitch              | ✘ | ✘ | ✘ | ✓ |

### 4.2. Parameters available remotely

Parameters that can be requested from the device remotely, i.e. via the underwater acoustic communication channel, using any other modem of the **uWave** family.

|  | [uWave](uWAVE_Specification_en.md) | [uWave Max](uWAVE_Max_Specification_en.md) | [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) | [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) |
| :--- | :---: | :---: | :---: | :---: |
| Temperature        | ✓ | ✓ | ✘ | ✓ |
| Depth              | ✓ | ✓ | ✘ | ✓ |
| Supply voltage     | ✓ | ✓ | ✓ | ✘ |

### 4.3. Ranges of measured values

| Parameter          | Min | Max | Units <br/> of measurement | 
| :---               | :--- | :--- | :--- |
| Pressure           | 0 | 30000 | mbar |
| Temperature        | -4 | 46 | °C |
| Depth              | 0 | 300 | m |
| Supply voltage     | 0 | 15 | V |
| Roll               | -180 | 180 | ° |
| Pitch              | -180 | 180 | ° |

### 4.4. Resolution when transmitting built-in sensor readings

| Parameter          | Resolution <br/> locally | Resolution <br/> remotely |
| :---               | :--- | :--- |
| Pressure           | 0.1 mbar | - |
| Temperature        | 0.1 °C | 0.1 °C |
| Depth              | 0.01 m | 0.1 m |
| Supply voltage     | 0.1 V | 0.1 V |
| Roll               | 0.1 ° | - |
| Pitch              | 0.1 ° | - |


<div style="page-break-after: always;"></div>

## 5. Application and integration

All devices of the **uWave** family interface with the user system via the 3.3 V UART physical interface and operate in transparent channel mode 
by default. This requires no additional integration or configuration.

To operate in command mode, a simple [NMEA-like ASCII protocol](uWAVE_Protocol_Specification_en.md) is used.

Open-source examples for interfacing **uWave** devices are available on our [GitHub](https://github.com/ucnl):
* [uWave ALibs](https://github.com/ucnl/UCNL_ALibs) libraries with usage examples for the **Arduino** platform
* (Old version) [uWave ALib](https://github.com/ucnl/uWAVE_ALib) library for the **Arduino** platform for the easiest possible use of all the capabilities of the modems
* [uWaveLib](https://github.com/ucnl/uWAVELib) library (.NET)
* Demo software [uWave Host](https://github.com/ucnl/uWAVE_Host)
* Demo project [uWave VLBL](https://github.com/ucnl/uWAVE_VLBL) - navigation on a virtual long baseline using two [uWave](uWAVE_Specification_en.md) modems
* [uMCPIno](https://github.com/AlekUnderwater/uMCPIno) - Protocol with guaranteed delivery and message ordering (implementations for Arduino, STM32 and .NET)
* Repository (old version) with examples of operation of [uWave](uWAVE_Specification_en.md) modems on the Arduino platform: [uWAVE_ALib](https://github.com/ucnl/uWAVE_ALib)

  
<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uWAVE/uWAVE_Family_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
