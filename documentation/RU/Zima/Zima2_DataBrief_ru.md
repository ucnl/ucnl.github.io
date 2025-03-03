[Главная](/README_RU) ❯ [Гидроакустические навигационные и трекинговые системы](/navigation_and_tracking_systems_ru) ❯ **Zima 2 USBL: Краткое опсиание**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/zima_package.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima 2 USBL** <br/> Краткое описание |

<div style="page-break-after: always;"></div>

## Общие данные
**Zima 2 USBL** – гидроакустическая ультракороткобазисная (УКБ) навигационная система, предназначенная для определения местоположения подводных объектов, помеченных гидроакустическими маяками-ответчиками [Zima2-R](Zima2R_Specification_ru.md) при помощи пеленгационной приемо-передающей антенны [Zima2-B](Zima2B_Specification_ru.md).

<div style="page-break-after: always;"></div>

## Состав системы

|  |  |
| :---: | :--- |
| ![Zima2-B](/documentation/zima_b_wcable.png) | [Zima2-B](Zima2B_Specification_ru.md) <br/> Базовая станция пеленгования (с удлинителем [UART-RS422](/documentation/RU/Accessories/RS422_extension_cable_ru.html)) |
| ![Zima2-R](/documentation/zima_r_wbat.png) | [Zima2-R](Zima2R_Specification_ru.md) <br/> Маяки-ответчики (одна базовая станция может последовательно работать максимум с 16 ответчиками) |
| ![Bat&Link Box](/documentation/batnlinkbox.png) | [Bat&Link Box](Bat_n_link_box_Specification_ru.md) <br/> Автономный блок питания и коммутации базовой станции |

<div style="page-break-after: always;"></div>

## Решаемые задачи
* Определение местоположения до 16 подводных объектов в акватории (слежение за подводными объектами)
* Определение относительного местоположения (**азимут, дистанция, глубина**)
* Определение абсолютного местоположения (**широта, долгота, азимут, дистанция, глубина**) при подключении внешней **GNSS** и компаса (или **GNSS с функцией компаса**)

<div style="page-break-after: always;"></div>

## Отличительные черты
* Компактность, большой радиус действия и максимальная простота использования позволяют использовать систему **Zima2** для работы как с различными **ТНПА** и **АНПА**, так и с **водолазами** в любых сочетаниях
* Высокая универсализация маяков позволяет использовать их как автономном исполнении с отдельным блоком батарей, так и энергетически и информационно сопрягать их с носителем
* Система поддерживает интеграцию с внешними источниками навигационных данных: **GNSS** с функцией компаса(подключаются к пультовому ПК). В этом случае система определяет абсолютные географические координаты подводных объектов, позволяет сохранять трек перемещения подводных объектов и имеет функции эмуляции GPS для одного из выбранных маяков для интеграции со сторонним ПО (например, Hypack, SAS.Planet, и пр.)
* Антенна ZIMA2-B устанавливается на штанге с борта практически любого судна, подключается к источнику питания 12 В / 3.5 А, и к пультовому ПК (Windows 10 и выше) – в такой минимальной конфигурации система определяет положение маяков (азимут и дистанция) относительно антенны. При подключении к пультовому ПК GNSS-приемника с функцией компаса (**RMC, GGA, HDG**) система определяет географические координаты маяков и может передавать их (**RMC, GGA**) в любой последовательный порт, эмулируя тем самым GNSS приемник для выбранного маяка-ответчика;

<div style="page-break-after: always;"></div>

| ![Zima2-B placement](/documentation/zima2_boat_gnss_1.png) |
| :---: |
| Схема установки антенны [Zima 2-B](Zima2B_Specification_ru.md) <br/> _Антенна монтируется на жесткой штанге таким образом, чтобы быть не ближе 2 метров от поверхности воды и не ближе 1.5 метров от нижней точки судна. Задаются смещения антенны относительно точки топопривязки и угловое смещение нуля антенны и GNSS-компаса_ |

<div style="page-break-after: always;"></div>

## Схемы сопряжения

### Работа в относительных координатах
Для определения **относительного местоположения** маяков-ответчиков, антенна информационно сопрягается с ПК, на котором установлено специализированное пультовое ПО с открытым исходным кодом [AzimuthSuite](https://github.com/ucnl/AzimuthSuite). Антенна подключается к ПК через [Bat&Link Box](Bat_n_link_box_Specification_ru.md), обеспечивающий преобразование интерфейса в USB и питание антенны. 

В этом случае пользователю доступны данные и функции:
* **Азимут** (горизонтальный угол) на используемые маяки-ответчики;
* **Дистанция** до маяков-ответчиков
* Глубины маяков-ответчиков


| ![Zima2B relative scheme](/documentation/zima2_option1.png) |
| :---: |
| _Схема подключения при работе в относительных координатах_ |

<div style="page-break-after: always;"></div>

### Работа в абсолютных координатах
Для определения **абсолютного местопложения** маяков-ответчиков антенна информационно сопрягается с ПК, на котором установлено специализированное пультовое ПО [AzimuthSuite](https://github.com/ucnl/AzimuthSuite). Антенна подключается к ПК через [Bat&Link Box](Bat_n_link_box_Specification_ru.md), обеспечивающий преобразование интерфейса в USB и питание антенны. Дополнительно подключаются внешняя **GNSS**-система с функцией компаса, работающая по протоколу **NMEA 0183** (сообщения **RMC** и **HDT**).

| ![Zima-B absolut scheme](/documentation/zima2_option2.png) |
| :---: |
| _Схема подключения при работе в абсолютных координатах_ |

В этом случае пользователю доступны следующие данные и функции:
* Абсолютные **географические координаты** маяков и глубина
* **Азимут** (относительно направления на север)
* **Дистанция**
* Запись трека движения подводных объектов с возможностью последующего сохранения в формате Google KML.

<div style="page-break-after: always;"></div>

## Геометрические ограничения

Так как определение местоположения маяков-ответчиков [Zima2-R](Zima2R_Specification_ru.md) осуществляется по горизонтальному углу прихода сигнала, наклонной дальности и разности глубин, антенная решетка пеленгационной станции [Zima 2-B](Zima2B_Specification_ru.md) имеет наибольшую чувствительность в диапазоне углов от 0° до 85° от горизонтали. Точность системы, когда маяк-ответчик находится близко к направлению на надир, может снижаться.

| ![Zima2-B angular zones](/documentation/zima2_geometric_limitations.png) |
| :---: |
| Геометрические ограничения [Zima 2-B](Zima2B_Specification_ru.md) <br/> _1 - Пеленгационная антенна, 2 - верхняя полусфера, 3 - рабочая зона (0° .. 85°, 0 .. -85°), 4 - зона снижения точности (85° .. -85°)_ |

<div style="page-break-after: always;"></div>

_________  

| **Дополнительная информация** |
| :--- |
| [**Zima 2 USBL**: Инструкция по эксплуатации](Zima2_Users_manual_ru.md) |
| [Маяк-ответчик **Zima 2-R**: спецификация устройства](Zima2R_Specification_ru.md) |
| [Станция пеленгования **Zima 2-B**: спецификация устройства](Zima2B_Specification_ru.md) |
| [Блок питания и коммутации **Bat&Link Box**: спецификация устройства](Bat_n_link_box_Specification_ru.md) |
| [Протокол информационного сопряжения устройств системы **Zima 2 USBL**](Zima2_Protocol_Specification_ru.md) |
