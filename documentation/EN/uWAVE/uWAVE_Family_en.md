| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** - underwater communication devices family <br/> Brief description |
  
# uWave devices family <br/> Brief description

<div style="page-break-after: always;"></div>

## 1. List of devices

The **uWave** family (_&mu;Wave, pronounced: "mu-wave" or, if you like it more - "you-wave"_) is specifically designed for applications that are extremely sensitive to weight 
and size and is presented currently by three devices:

* [uWave](uWAVE_Specification_en.md) - underwater acoustic modem. It is the smallest underwater acoustic modem in the world: its size is 
only **Ф40х45** mm, and dry weight does not exceed 160 grams. With these parameters, it allows user to transfer data at distances of more 
than **1000** meters.
* [uWave Max](uWAVE_Max_Specification_en.md) - underwater acoustic modem. Reinforced version of the base device. Due to an increased
transducer and power amplifier allows user to transmit data at a distance of more than **3000** meters. Dimensions in this case are
**Ф62х65** mm, and dry weight 360 grams.
* [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) - underwater acoustic modem. Reinforced version of the base device. Due to an increased
transducer and power amplifier allows user to transmit data at a distance of more than **3000** meters. Supplied as a modem PCB module and sonar antenna. 
* [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) - underwater acoustic modem with the function of determining the horizontal 
angle of arrival signal. The device is equipped with a phased array and integrated inclinometer, which allows user to determine the 
horizontal direction, from which the signal came from any other devices of the **uWAVE** family. Dimensions [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md)
**Ф64х128** mm, the dry weight of the device is 440 grams.

More detailed comparison can be found in [uWave modems comparison tables](uWAVE/uWAVE_Modems_comparison_en.md).

All devices within the family are fully acoustically compatible and have a common, [NMEA-like protocol](uWAVE_Protocol_Specification_en.md)
interfacing.

<div style="page-break-after: always;"></div>

## 2. Features of the acoustic protocol and code channels
Acoustic Transfer Protocol **uWave** implements code division multiple access (CDMA) and supports 20
isolating code channels. Any device from the **uWave** family can be configured with any code channels for reception and transmission.

The isolating code channel ensures that data transmitted on one channel is not received by the device receiving on any
other code channel.

All devices of the **uWave** family can receive at the same time in only one code channel.

### 2.1. Acoustic baud rate
The standard mode for **uWave** devices is 78 bps. This mode provides maximum communication range and reliability. It is in this mode that the largest number of code channels is available.

All devices in the **uWave** family support alternate modes, providing baud rates of 156 and 314 bps. The higher the speed, the less noise immunity, and, accordingly, the reliability and range of communication.

Different speed modes are not compatible with each other. Transfer of the modem to another speed mode is provided by replacing its firmware.


<div style="page-break-after: always;"></div>

## 3. Device working modes
All devices of the family can work in two modes, switching between which is carried out by the user:
* Transparent channel mode
* Command mode

These modes determine how the modem perceives data coming from the control system:

### 3.1. Transparent channel mode
In the transparent channel mode, the devices do not analyze the data coming from the control system and without any changes transmit them 
to the underwater acoustic channel, where they can be received by any device from the family that receives in the same code channel,
in which the transmission was performed.

### 3.2. Command mode
In command mode, devices analyze data coming from the control system and interact with them within very simple 
[NMEA-like ASCII protocol](uWAVE_Protocol_Specification_en.md). In this mode, devices allow you to send short code requests to other 
devices: request of depth, temperature, power supply voltage and transmit 8 user commands.
Code requests have fixed lengths of request and response signals, which allows the requesting system to estimate the propagation time 
(and slant range) to the requested system.

The remote modem receives and processes the code request, regardless of the mode in which it is, which frees the user
from the need to monitor the status of a remote modem.

The devices [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) allow users to determine the horizontal angle of arrival of any
incoming message from other devices of the **uWave** family. Including for user messages transmitted in transparent channel mode.

### 3.2.1. Packet mode
Packet mode allows transmitting data packets with guaranteed delivery (ALO - At-least-once), delivery notification to the addressee. In packet mode, logical addressing of up to 254 subscribers is used over each code channel (255 is a broadcast address without notification and guaranteed delivery). Packet mode can only be used when the modem is in command mode.


<div style="page-break-after: always;"></div>

## 4. Built-in sensors
**All** devices in the family have a built-in supply voltage measurement module. The supply voltage for all devices in the family can be remotely requested by any other devices of the family.

Devices [uWave](uWAVE_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) have built-in depth/temperature sensors. Depth and temperature readings can be remotely requested by any device of the family.

[uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) devices additionally have built-in two-axis inclinometers
(measure the angles of roll and pitch). The user can configure the output of this data, with a given
period (from 0.5 to 60 seconds) or tandem - when any data is received from remote devices. Inclinometer readings are only available locally.

All devices equipped with depth/temperature sensors, when switched on in the air, automatically calibrate the pressure sensor, which eliminates the error in determining the depth associated with changes in atmospheric pressure and zero drift of the sensor. To achieve the maximum possible for
of this precision technology, the device allows you to set an adequate value for the acceleration of gravity for the place of work
(for example, according to the WGS84 Gravity model, thereby excluding the influence of its variation from geographical latitude).

The devices are designed for a maximum immersion depth of 300 meters.

<div style="page-break-after: always;"></div>

## 5. Application and integration
All **uWave** family devices are paired with the user system using the 3.3 V UART physical interface, and by default
operate in transparent channel mode. This does not require any additional integration and configuration.

To work in command mode, a simple [NMEA-like ASCII protocol](uWAVE_Protocol_Specification_en.md) is used.

On our [GitHub](https://github.com/ucnl) you can find examples and linbraries to interface with **uWAVE** devices:
* [uWave ALib](https://github.com/ucnl/uWAVE_ALib) - Arduino library
* [uWaveLib](https://github.com/ucnl/uWAVELib) - .NET Library
* [uWave Host](https://github.com/ucnl/uWAVE_Host) - Demo application
* [uWave VLBL](https://github.com/ucnl/uWAVE_VLBL) - Demo application (VLBL navigation system on two [uWave](uWAVE_Specification_ru.md) modems)
* [uMCPIno](https://github.com/AlekUnderwater/uMCPIno) - Point-to-point protocol with guaranteed delivery and packets ordering (Arduino, STM32, .NET)
* [uWave](uWAVE_Specification_ru.md) Some Arduino examples (old version):

  <div style="page-break-after: always;"></div>

  
  
