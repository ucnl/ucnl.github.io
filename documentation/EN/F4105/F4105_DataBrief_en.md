[Main](/) ❯ [Other equipment](/underwater_bespoke_systems_en) ❯ **F4105: Data brief**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **F4105** <br/> Acoustic release <br/> **Data brief** |

# **F4105** <br/> Acoustic release <br/> **Data brief**

<div style="page-break-after: always;"></div>

### 1. Purpose
The system is an easy-to-use and functional solution for raising the line of bottom equipment deployed for a long period (up to 2 months). Uncoupling from the anchor is performed by a reliable screw mechanism, initiated by an addressed command transmitted over the underwater acoustic channel from the water surface (by means of a lowered transducer).
The system allows setting up to 64 unique addresses for acoustic wake-up units. The maximum acoustic communication range is up to 200 meters, and the maximum depth is up to 100 meters. The autonomous operating time of the acoustic wake-up unit is up to 60 days.

After uncoupling, the lifting line unwinds from the float-reel, while the lower end of the line remains connected to the anchor (and the bottom equipment). This makes it possible to raise the bottom equipment by the upper end of the line.

### 2. System composition
In the current version, the system is structurally represented by three devices:
- setting device: a standalone surface module designed to issue ascent commands and to set the address;
- control device: the acoustic wake-up unit, responsible for receiving the addressed signal and issuing the command to the actuator;
- actuating device: the actuator, containing a screw mechanism for uncoupling from the anchor and a power source, which also powers the control device
#### 2.1. F4105-SU programming and control unit
The programming and control unit is the setting device, designed for setting (programming) the addresses of acoustic wake-up units and issuing addressed commands to acoustic wake-up units. It is made in the form of an impact-resistant plastic case with a stainless steel front panel on which the controls are located.

| ![F4105-SU](/documentation/F4105_SU.png) |
| :---: |
| Figure 1 - Programming and control unit for releases [**F4105-SU**](F4105_SU_Specification_en.md) <br/> with a transducer on a cable |

#### 2.2. F4105-AU acoustic wake-up unit
The acoustic wake-up unit is the control device that supplies a signal which switches on the actuating device (actuator) upon receiving an addressed request over the underwater acoustic channel.
The acoustic wake-up unit is equipped with a cable and a connector for interfacing with the setting device for address programming and for interfacing with the actuating device.

| ![F4105-AU](/documentation/F4105_AU.png) |
| :---: |
| Figure 2 - Acoustic wake-up unit [**F4105-AU**](F4105_AU_Specification_en.md) |

#### 2.3. F4105-BU release unit
The release unit is both the actuating device and the power source. It is designed for uncoupling the device from the anchor by means of a screw mechanism.
Upon receiving a signal from the control device, a geared motor is activated in the actuator, which unscrews the lock nut connected to the anchor and thereby allows the actuator with the float to rise under the action of the buoyant force.

| ![F4105-BU](/documentation/F4105_BU.png) |
| :---: |
| Figure 3 - Release unit [**F4105-BU**](F4105_BU_Specification_en.md) |

The actuator has a connector on a cable for:
- connecting the control device (acoustic wake-up unit)
- connecting the charger
- connecting to the setting device for testing

<!-- docs-sync: source=documentation/RU/F4105/F4105_DataBrief_ru.md commit=f9bb043aa78c7f790980a18e12a2da37cf03d906 date=2025-04-10 -->
