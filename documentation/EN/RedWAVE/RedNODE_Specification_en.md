| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedNODE** - Underwater navigation receiver <br/> Device specification |

## KEY FEATURES

* **3D position in absolute geographical coordinates**
* **Emulation of the protocol of conventional GNSS receivers**
* **Update rate of 3D position to 1 Hz**
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
| BANDWIDTH | 10 .. 30 кГц |
| ПРЕДЕЛЬНОЕ СООТНОШЕНИЕ СИГНАЛ/ШУМ В ПОЛОСЕ<sup>[3](#footnote3)</sup> | -6 дБ |
| REFERENCE ELLIPSOID | WGS-84 |
| НОМИНАЛЬНАЯ ГОРИЗОНТАЛЬНАЯ ПОГРЕШНОСТЬ<sup>[4](#footnote4)</sup> (2DRMS) | 0.84 м |
| НОМИНАЛЬНАЯ ПОГРЕШНОСТЬ ПО ГЛУБИНЕ<sup>[5](#footnote5)</sup>  | 0.1 м |
| НОМИНАЛЬНОЕ ВРЕМЯ ДО ПЕРВОГО УТОЧНЕНИЯ МЕСТОПОЛОЖЕНИЯ | 28 c |
| НОМИНАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ ГЕОГРАФИЧЕСКОГО ПОЛОЖЕНИЯ | 1 Гц |
| НОМИНАЛЬНОЕ ВРЕМЯ СТАРТА | 100 мсек |
| ТОЧНОСТЬ ВСТРОЕННОГО ДАТЧИКА ТЕМПЕРАТУРЫ | 0.1 °C |
| CABLE LENGTH | 1 m |
| CABLE DIAMETER | 5 mm |
| ИНТЕРФЕЙС СОПРЯЖЕНИЯ<sup>[6](#footnote6)</sup> | UART, 9600  |
| ИНФОРМАЦИОННЫЙ [ПРОТОКОЛ](RedWAVE_Protocol_Specification_ru.md) | NMEA0183 (RMC, GGA, WTW) <br/> + расширенный набор сообщений |

________________
<a name="footnote1"><sup>1</sup></a> Для устройств, выпущенных после июня 2020 года. Для устройств, выпущенных ранее напряжение питания 5 В.    
<a name="footnote2"><sup>2</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из 
электроакустических параметров передатчика и приемника, пространственным убыванием интенсивности звуковой энергии, затуханием в среде 
и уровня гидроакустических помех.  
<a name="footnote3"><sup>3</sup></a> Величина получена без учета эффекта многолучевого распространения.  
<a name="footnote4"><sup>4</sup></a> Величина получена путем измерения в реальном водоеме при неподвижно закрепленных буях и навигационном
приемнике в течение 60 минут.  
<a name="footnote5"><sup>5</sup></a> Величина может зависеть от правильности задания пользователем солености воды, в котором производятся
работа.  
<a name="footnote6"><sup>6</sup></a> По договоренности возможна поставка с преобразователем интерфейса RS422, монтируемым на кабель в необслуживаемый уретановый корпус. 
