| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE** - underwater communication devices family <br/> Brief description |
  
# uWAVE devices family <br/> Brief description

<div style="page-break-after: always;"></div>

## 1. List of devices

The **uWAVE** family (_&mu;WAVE, pronounced: "mu-wave"_) is specifically designed for applications that are extremely sensitive to weight 
and size and is presented currently by three devices:

* [uWAVE](uWAVE_Specification_en.md) - underwater acoustic modem. It is the smallest underwater acoustic modem in the world: its size is 
only **Ф40х45** mm, and dry weight does not exceed 160 grams. With these parameters, it allows user to transfer data at distances of more 
than **1000** meters.
* [uWAVE Max](uWAVE_Max_Specification_en.md) - underwater acoustic modem. Reinforced version of the base device. Due to an increased
transducer and power amplifier allows user to transmit data at a distance of more than **3000** meters. Dimensions in this case are
**Ф62х65** mm, and dry weight 360 grams.
* [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md) - underwater acoustic modem with the function of determining the horizontal 
angle of arrival signal. The device is equipped with a phased array and integrated inclinometer, which allows user to determine the 
horizontal direction, from which the signal came from any other devices of the **uWAVE** family. Dimensions [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md)
**Ф64х128** mm, the dry weight of the device is 440 grams.

All devices within the family are fully acoustically compatible and have a common, [NMEA-like protocol](uWAVE_Protocol_Specification_en.md)
interfacing.

<div style="page-break-after: always;"></div>

## 2. Features of the acoustic protocol and code channels
Acoustic Transfer Protocol **uWAVE** implements code division multiple access (CDMA) and supports 20
isolating code channels. Any device from the **uWAVE** family can be configured with any code channels for reception and transmission.

The isolating code channel ensures that data transmitted on one channel is not received by the device receiving on any
other code channel.

All devices of the **uWAVE** family can receive at the same time in only one code channel.

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

The devices [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md) allow users to determine the horizontal angle of arrival of any
incoming message from other devices of the **uWAVE** family. Including for user messages transmitted in transparent channel mode.

<div style="page-break-after: always;"></div>

## 4. Built-in sensors
All devices of the family have built-in depth and temperature sensors, and also measure the supply voltage, devices
[uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_en.md) additionally have built-in dual-axis inclinometers
(to measure roll and pitch angles). the user can configure the output of this data periodically, with a given
period (from 0.5 to 60 seconds) or in tandem - upon receipt of any data from remote devices.

All devices, when turned on in the air, automatically calibrate the pressure sensor, which eliminates the error of
determining the depth associated with changes in atmospheric pressure and zero drift of the sensor. To achieve the highest possible 
accuracy for this technology, the device allows users to set an adequate value of the acceleration of gravity for the place of work
(for example, according to the WGS84 Gravity model, thereby eliminating the influence of its change from geographical latitude).

All devices are designed for a maximum immersion depth of 300 meters.

<div style="page-break-after: always;"></div>

## 5. Application and integration
All **uWAVE** family devices are paired with the user system using the 3.3 V UART physical interface, and by default
operate in transparent channel mode. This does not require any additional integration and configuration.

To work in command mode, a simple [NMEA-like ASCII protocol](uWAVE_Protocol_Specification_en.md) is used.

Our [GitHub](https://github.com/ucnl) provides open-source examples for interfacing with **uWAVE** devices:
* Library [uWAVELib](https://github.com/ucnl/uWAVELib) (.NET)
* Demo software [uWAVE Host](https://github.com/ucnl/uWAVE_Host)
* Demo project [uWAVE VLBL](https://github.com/ucnl/uWAVE_VLBL) - navigation on a virtual long base using two modems [uWAVE](uWAVE_Specification_en.md)
* Repository with examples of the operation of modems [uWAVE](uWAVE_Specification_en.md) on the Arduino platform:
  * [Example 1](https://github.com/ucnl/uWAVE_Arduino/blob/master/uWAVE_Example_1.ino) - Switching to command mode,
  requesting device information, updating device settings, configuring settings for issuing environmental parameters, requesting of a remote device
  * [Example 2](https://github.com/ucnl/uWAVE_Arduino/blob/master/uWAVE_Example_2.ino) - Work in a transparent channel: a simple terminal for transferring
  text messaging via underwater acoustic channel
  * [Example 3](https://github.com/ucnl/uWAVE_Arduino/blob/master/uWAVE_Example_1.ino) - The reference point of the virtual long base. Analyzes
  RMC messages from a GNSS-receiver, requests a remote modem, sends its location and data received from a remote modem, as well as the slant range measured to it to a radio channel.
  * [uMCPIno](https://github.com/AlekUnderwater/uMCPIno) - Protocol with guaranteed delivery and message sequence (implementations for Arduino, STM32 and .NET)
  
  <div style="page-break-after: always;"></div>

  
  
