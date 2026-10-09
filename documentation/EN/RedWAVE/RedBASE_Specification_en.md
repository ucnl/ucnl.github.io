[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RedBase: Device specification**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![def_redbase_v2](/documentation/def_redbase_v2.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedBase** - GNSS-equipped sonobuoy <br/> Device specification |

## KEY FEATURES

* **High-performance combined GPS/GLONASS receiver**
* **Rugged, durable, easily noticeable, maintenance-free housing**
* **Simultaneous positioning for an unlimited number of [RedNode](RedNODE_Specification_en.md)/[RedNav](RedNAV_Specification_en.md) devices**
* **Long battery life of up to 48 hours**
* **Automatic activation in water**
* **Reliable and noise-resistant digital broadband underwater acoustic communication technology**

## DESCRIPTION

The **RedBase** GNSS-equipped sonobuoy, in a set of four such devices, forms a floating long navigation base, 
which supports the simultaneous positioning of an unlimited<sup>[*](#footnote_a1)</sup> number of [RedNode](RedNODE_Specification_en.md)/[RedNav](RedNAV_Specification_en.md) navigation receivers.  

The device consists of two blocks potted in a polyurethane compound: an underwater block, which houses the LiFePO4 battery, and a surface block, which houses the underwater acoustic transmitter and the GNSS receiver. The blocks are connected to each other by a plastic tube on which additional buoyancy blocks are mounted. The device is equipped with a light indication system for the status and the sequence number of the buoy in the set: the light sources are located in the upper part of the surface block, which is made of transparent polymer with the addition of a phosphor.
RedBase buoys switch on automatically when immersed in water and switch off automatically when taken out of the water. 
For attachment to an anchor line, load-bearing eyes are provided in the lower part of the battery block.

_________
<a name="footnote_a1"><sup>*</sup></a> Patents US10989815B2, WO2017044012A1, EP3349040A4, RU2599902C1.  

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ø x h) | 125 x 790 mm |
| WEIGHT (dry) | 3.8 kg |
| EXCESS BUOYANCY | 1 kg |
| CARRIER FREQUENCY | 20100 Hz |
| MAXIMUM BATTERY LIFE | 48 hours |
| MAXIMUM ACOUSTIC COMMUNICATION RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| MAXIMUM ACOUSTIC SOURCE LEVEL | 170 dB re 1 μPa @ 1 m |
| MAXIMUM PERMISSIBLE DISTANCE TO OTHER BUOYS OF THE SET<sup>[2](#footnote2),[3](#footnote3)</sup> | 700 m |
| MINIMUM PERMISSIBLE DISTANCE TO OTHER BUOYS OF THE SET<sup>[3](#footnote3)</sup> | 30 m |
| MAXIMUM VELOCITY RELATIVE TO RECEIVERS | +/- 1.8 m/s  |
| OPERATING TEMPERATURE RANGE | -10 .. 50 °C |
| REFERENCE ELLIPSOID | WGS-84 |
| BUILT-IN BATTERY TYPE | LiFePO4 |
| BUILT-IN BATTERY CAPACITY | 76 W·h |
| UNDERWATER ACOUSTIC TRANSMITTER CABLE LENGTH | 1 m |
| FULL CHARGE TIME FROM 220 V / 50 Hz MAINS | 5 h |

## ADDITIONAL INFORMATION

| [MSDS OF THE BUILT-IN POWER SUPPLY](https://docs.unavlab.com/documentation/EN/Misc/RedBase_v3_LiFEPO4_msds_en.html) | [ELECTRONIC VERSION OF THIS DOCUMENT](https://docs.unavlab.com/documentation/EN/RedWAVE/RedBASE_Specification_en.html) |
| :---: | :---: |
| ![image](https://github.com/user-attachments/assets/eb6e547e-70d5-4f68-85a9-7575d14608ea) | ![image](https://github.com/user-attachments/assets/2b34fa2d-9c74-4496-aaea-238a7556d6e5) |

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which signal reception is possible, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> The buoys are placed on the water surface in a convex polygon so that the distance from each buoy to any other does not exceed the specified value.  
<a name="footnote3"><sup>3</sup></a> The immersion depth of the navigation receivers must not exceed the dimensions of the navigation base.  

<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/RedWAVE/RedBASE_Specification_ru.md commit=183207200b939eea64d7be305068cf1d7adc96a3 date=2024-12-12 -->
