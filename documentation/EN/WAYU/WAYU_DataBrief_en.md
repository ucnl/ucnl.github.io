| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **WAYU** - Underwater tracking system <br/> Data brief |

<div style="page-break-after: always;"></div>

## General info
**WAYU** stands for **W**here **A**re **Y**ou **U**nderwater.
The **WAYU** system is a reliable and easy-to-use solution for the amateur segment. The user places a pinger beacon [WAYU Pinger](WAYU_Pinger_Specification_en.md) on the positioned object (TNLA, AUV, diver, etc.), and on the surface of the reservoir four small navigation buoys [WAYU GIB] (WAYU_GIB_Specification_ru.md).
From this moment on, the absolute geographic position of the underwater object is displayed on the PC screen, where the specialized software [WAYU] () open source is installed. The position of an underwater object can be easily transferred from the [WAYU] () application via a serial port (physical or virtual) to any mapping software that supports work with conventional GPS receivers via the NMEA0183 protocol.
Both the pinger and **WAYU** buoys turn on automatically when they enter the water, do not require any adjustments or calibrations other than charging the built-in power supplies.

<div style="page-break-after: always;"></div>

## Состав системы

|  |  |
| :---: | :--- |
| ![WAYU Pinger]() | [WAYU Pinger](WAYU_Pinger_Specification_ru.md) <br/> Навигационный гидроакустический маяк-пингер |
| ![WAYU GIB]() | [WAYU GIB](WAYU_GIB_Specification_ru.md) <br/> Навигационный буй |
| ![WAYU Radio dongle]() | [WAYU Radio dongle](WAYU_RF_Dongle_Specification_ru.md) <br/> Радиодонгл - приемник навигационныйх буев |


<div style="page-break-after: always;"></div>

## Решаемые задачи
- Определение географического местоположения подводного объекта в реальном времени
- Запись трека движения подводного объекта
- Определение курса движения подводного объекта
- Эмуляция GPS протокола для передачи местоположения подводного объекта в картографическое ПО

<div style="page-break-after: always;"></div>

## Отличительные черты
- Профессиональное решение по доступной цене
- Позиционирование подводного объекта в абсолютных географических координатах
- Максимально простое использование 
- Автоматическое включение от воды
- Работа "из коробки" - не требует никаких калибровок и настроек

<div style="page-break-after: always;"></div>

## Геометрические ограничения
* _От каждого до каждого из буев должно быть не более 300 метров и не менее 30 метров_
* _Буи должны располагаться выпуклым четырехугольником, чтобы его стороны были примерно равны и отличались не более чем в 2 раза_
* _Максимальная глубина погружения пингера не должна превышать размеры навигационной базы_
* _Наибольшая точность системы достигается внутри фигуры буев, и работа всегда должна начинаться внутри этой фигуры. Выход за пределы фигуры возможен, однако точность при этом может значительно снижаться по мере удаления позиционируемого объекта от фигуры буев_

<div style="page-break-after: always;"></div>

_________  

| **Дополнительная информация** |
| :--- |
| [Видео испытаний системы, треки полученные при работе в реальных условиях](media.md) |

