| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedNODE** - Underwater navigation receiver <br/> Device specification |

## KEY FEATURES

* **3D position in absolute geographical coordinates**
* **Emulation of the protocol of conventional GNSS receivers**
* **Update rate of 3D position up to 1 Hz**
* **Completely acoustically passive device**
* **Minimum dimensions and weight**
* **Simultaneous operation of an unlimited number of devices**
* **Reliable and noise-immune technology of digital broadband acoustic communication**

## DESCRIPTION

**[RedNWAVE](RedWAVE_DataBrief_ru.md)** - the only system to date that implements the so-called "underwater GPS": following exactly
the ideology of GPS and other satellite systems, allows an unlimited number of underwater objects to determine their geographical 
location at the same time.
 
With the support of four sonobuoys [RedBASE](RedBASE_Specification_en.md), it is possible in one water area
to perform the simultaneous operation of an unlimited number of **RedNODE** and [RedNAV](RedNAV_Specification_en.md) devices.

**RedNODE** - navigation receiver of the **[RedWAVE](RedWAVE_DataBrief_en.md)** system, receiving hydroacoustic
navigation signals from buoys, determines its own geographical coordinates, which it transmits via a serial interface (**UART**)
to control system. At the same time, the message format used in conventional GNSS receivers is emulated, which ensures maximum 
simplicity of integration.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h) | 64 x 62 mm |
| WEIGHT (dry) | 0.3 kg |
| SUPPLY VOLTAGE<sup>[1](#footnote1)</sup> | 12 V |
| DATA LINES VOLTAGE | 3.3 V |
| POWER CONSUMPTION | 0.35 W |
| MAX. RELATIVE VELOCITY | +/- 1.8 m/s  |
| WORKING TEMPERATURE RANGE | -5 .. 50 °С |
| DEPTH RATING | 300 m |
| ACOUSTIC RANGE (ENEGRY)<sup>[2](#footnote2)</sup> | 3000 m |
| BANDWIDTH | 10 .. 30 kHz |
| SNR<sup>[3](#footnote3)</sup> | -6 dB |
| REFERENCE ELLIPSOID | WGS-84 |
| NOMINAL 2D-ACCURACY <sup>[4](#footnote4)</sup> (2DRMS) | 0.84 m |
| NOMINAL DEPTH ACCURACY<sup>[5](#footnote5)</sup>  | 0.1 m |
| MINIMAL TIME TO FIRST POSITION FIX | 28 s |
| NOMINAL POSITION UPDATE RATE | 1 Hz |
| RATE STARTUP TIME | 100 msec |
| BUILT-IN TEMPERATURE SENSOR ACCURACY | 0.1 °C |
| CABLE LENGTH | 1 m |
| CABLE DIAMETER | 5 mm |
| INTERFACE<sup>[6](#footnote6)</sup> | UART, 9600  |
| COMMUNICATION [PROTOCOL](RedWAVE_Protocol_Specification_en.md) | NMEA0183 (RMC, GGA, WTW) <br/> + extended sentences set |

________________
<a name="footnote1"><sup>1</sup></a> For devices released after June 2020. For devices previously released, 5 V.  
<a name="footnote2"><sup>2</sup></a> A parameter that determines the maximum range at which a signal can be received, based on
electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.  
<a name="footnote3"><sup>3</sup></a> The value obtained without taking into account the multipath effect.  
<a name="footnote4"><sup>4</sup></a> The value is obtained by measuring in a real water body with buoys and navigation receiver fixed, within 60 minutes.  
<a name="footnote5"><sup>5</sup></a> The value may depend on the correctness of the user setting the salinity of the water.  
<a name="footnote6"><sup>6</sup></a> By agreement, delivery with an RS422 interface converter mounted on a cable in an unattended urethane housing is possible. 
