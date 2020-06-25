| ![logo](https://ucnl.github.io/documentation/sm_logo.png) | ![logo](https://ucnl.github.io/documentation/zima_r_oem.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima-R OEM** - **Zima USBL** responder-beacon <br/> Device specification |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **Extremely small size and weight**
* **Operating range up to 3000<sup>[1](#footnote1)</sup> m**
* **For depths up to 1000<sup>[2](#footnote2)</sup> m**
* **Reliable and noise-immune technology of digital broadband acoustic communication**
* **Subscribers code division - up to 23 code channels**
* **Low power consumption (Rx/Tx) 0.33/25 W**
* **Patented technology of simultaneous positioning**

## ОПИСАНИЕ

**Zima-R OEM** - маяк-ответчик ультракороткобазисной навигационной системы [Zima USBL](Zima_DataBrief_ru.md).  

Устройство предназначено для получения команд телеуправления с базовой станции [Zima-B](Zima_B_Specification_ru.md) - базовая станция пеленгования, передачи телеметрической информации на базовую станцию [Zima-B](Zima_B_Specification_ru.md) - базовая станция пеленгования и для определения направления, как на маяк (для базовой станции) так и на базовую станцию (для маяка) и взаимного 
определения дистанции.  

Устройство поставляется в виде сборки печатных плат для монтажа внутри нормобарического корпуса пользователя и комплектуется 
гидроакустической антенной на глубины до 1000 метров.  

Возможно задание глубины как пользовательской системой, так и работа с отдельно поставляемыми датчиками.  

Предельно малый размер, низкое энергопотребление и простота использования делают пеленгационную систему [Zima USBL](Zima_DataBrief_ru.md) идеальным решением для работы с автономными и телеуправляемыми аппаратами а так же определения относительного местоположения водолазов.

<div style="page-break-after: always;"></div>

## TECHNICAL SPECIFICATIONS

| PARAMETER | VALUE |
| :--- | :--- |
| DIMENSIONS (Ф х h, PCBs) | Ф52 х 55 mm |
| РАЗМЕР (Ф х h, transducer) | Ф64 х 61 mm |
| WEIGHT (PCBs) | 0.12 kg |
| WEIGHT (transducer) | 0.35 kg |
| DEPTH RATING<sup>[2](#footnote2)</sup> | 1000 m |
| MAX. OPERATING RANGE<sup>[1](#footnote1)</sup> | 3000 m |
| ACOUSIC SOURCE LEVEL |	170 dB re 1 μPa @ 1 m |
| BANDWIDTH | 6 .. 18 kHz |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup> | -3 dB |
| MAX. RELATIVE VELOCITY | +/- 2 m/s |
| RATED STARTUP TIME | 100 msec |
| SUPPLY VOLTAGE | 12 V |
| DATA LINES VOLTAGE | 0 .. 3.3 V |
| WORKING TEMPERATURE RANGE | -5 .. 50 °C |
| INTERFACE | UART 9600 bit/s |
| PROTOCOL | NMEA 0183 [PZMA](Zima_Protocol_Specification_en.md) |
| CABLE LENGTH<sup>[4](#footnote4)</sup> | 1 m |
| SUBSCRIBER DIVISION SCHEME (commands/subscribers) | 32/23 |
| HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.)<sup>[3](#footnote3)</sup> | 1° |
| NOMINAL DISTANCE ESTIMATION ACCURACY<sup>[3](#footnote3)</sup> | 0.3 m |
  
________________
<a name="footnote1"><sup>1</sup></a> Without the presence of a multipath effect. A parameter that determines the maximum range at which a signal can be received, based on electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and the acoustic noise level.   
<a name="footnote2"><sup>2</sup></a> For transducer.  
<a name="footnote3"><sup>3</sup></a> Obtained under laboratory conditions in a static test.  
<a name="footnote4"><sup>4</sup></a> Can be changed by a special request.  
