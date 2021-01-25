| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - Underwater tracking system <br/> Data brief|

<div style="page-break-after: always;"></div>

## General information
**RWLT** system is **the easiest to use** and at the same time accurate solution for tracking an underwater object. The system **does not require any calibrations** and integration: it is enough to place an autonomous pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) on an underwater object (ROV, AUV, diver, etc.), and four navigation buoys on the water surface [RWLT GIB] (RWLT_GIB_Specification_en.md). This configuration allows real-time tracking of the movement of an underwater object in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to work simultaneously with wireless underwater telephone [RedPhone] (https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_Specification_en.html) as a pinger, thus combining two-way voice communication and navigation.
<div style="page-break-after: always;"></div>

## Состав системы

|  |  |
| :---: | :--- |
| ![RWLT GIB](https://ucnl.github.io/documentation/RWLT_GIB.png) | [RWLT GIB](RWLT_GIB_Specification_ru.md) <br/> Навигационный гидроакустический буй-приемник |
| ![RWLT Pinger](https://ucnl.github.io/documentation/RWLT_Pinger.png) | [RWLT Pinger](RWLT_Pinger_Specification_ru.md) <br/> Маяк-пингер |
| ![RWLT RF Dongle](https://ucnl.github.io/documentation/RWLT_RF_Dongle.png) | [RWLT RF Dongle](RWLT_RF_Dongle_Specification_ru.md) <br/> Цифровой радиоприемник |

Минимальный состав системы включает четыре гидроакустических буя [RWLT GIB](RWLT_GIB_Specification_ru.md) и одно передающее устройство, в зависимости от пользовательской задачи:
* Если требуется обеспечить навигационными данными водолаза одновременно с голосовой связью, то используется водолазная телефонная станция [RedPhone](https://docs.unavlab.com/documentation/RU/RedPhone/RedPhone_Specification_ru.html); В этом случае геопозиция водолаза будет определяться в момент, когда он отпускает кнопку PTT, т.е. завершает передачу голосового сообщения;
* Если требуется определять местоположение телеуправляемого аппарата (ТНПА, ROV), или водолаза без неоходимости использования голосовой связи, то применяется маяк-пингер [RWLT Pinger](RWLT_Pinger_Specification_ru.md). Пингер работает автономно и геопозиция объекта, на котором закреплен пингер будет обновляться каждые две секунды.

Для работы на ПК устанавливается специализированное ПО [RWLT Host](https://github.com/ucnl/RWLT_Host) с открытым исходным кодом, которое отображает:
- текущее географическое положение подводного объекта (долгота, широта)
- глубину
- температуру воды
- состояние встроенного источника питания
- географическое положение буев и состояние их источников питания
- при подключении внешнего GPS отображается положение надводного пункта слежения, расстояние и курс до подводного объекта

<div style="page-break-after: always;"></div>

## Решаемые задачи
* Слежение за положением подводного объекта в реальном времени (водолазы, ТНПА, АНПА и т.п.);
* Определение курса движения подводного объекта;
* Помощь в приводе подводного объекта к надводному пункту контроля и наоборот;

<div style="page-break-after: always;"></div>

## Отличительные черты
* Работа в абсолютных географических координатах;
* Плавучая базы из четырех гидроакустических буев позволяет следить как за пингером [RWLT Pinger](RWLT_Pinger_Specification_ru.md), так и за водолазной телефонной станцией [RedPhone](https://docs.unavlab.com/documentation/RU/RedPhone/RedPhone_Specification_ru.html);
* Не требуется никакой предварительной настройки и калибровки системы и ее составных частей;
* Не требуется никакого информационного сопряжения объекта с пингером - пингер механически закрепляется на подводном носителе;
* Передача вычисленнго положения подводного объекта в стороннее ПО через последовательный порт посредством протокола NMEA0183;
* Запись трека передвижения подводного объекта;
* Возможность подключения дополнительного GPS приемника для записи трека надводного пункта слежения (судна).

<div style="page-break-after: always;"></div>

## Геометрические ограничения
* _От каждого до каждого из буев должно быть не более 1500 метров и не менее 30 метров_
* _Буи должны располагаться выпуклым четырехугольником, чтобы его стороны были примерно равны и отличались не более чем в 2 раза_
* _Максимальная глубина погружения пингера не должна превышать размеры навигационной базы_
* _Наибольшая точность системы достигается внутри фигуры буев, и работа всегда должна начинаться внутри этой фигуры. Выход за пределы фигуры возможен, однако точность при этом может значительно снижаться по мере удаления позиционируемого объекта от фигуры буев_

<div style="page-break-after: always;"></div>

_________  

