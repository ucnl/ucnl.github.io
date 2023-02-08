[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Bat & Link Box: User's manual**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![Bat&Link Box](/documentation/batnlinkbox.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Bat & Link Box** - Autonomous power supply and interface converter <br/> User's manual |

# Bat & Link Box <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents
- [1. Introducation]()
- [2. Appearance and controls]()
- [3. Connector pinouts]()
- [4. Working with the device]()
- [5. Storage and maintenance]()
- [6. Liability and Disclaimer]()
  - [6.1. Terms of replacement and free warranty service]()
  - [6.2. Manufacturer Liability Limitation]()

<div style="page-break-after: always;"></div>

## 1. Introduction
The device [Bat & Link Box](Bat_n_link_box_Specification_en.md) combines the functions of an autonomous power source for the direction finding station Zima2-B (and older version - Zima-B) and a switching hub for interfacing the station with the user's PC, as well as for connecting data sources about the heading and position of the direction finding station. Contains protection circuits against polarity reversal and overvoltage of connected devices.

The device is housed in a small impact-resistant plastic case. Has the front panel from high-quality stainless steel. The modern lithium-iron phosphate batteries used in the device provide operation at negative temperatures and more than 3000 charge-discharge cycles. If necessary, it is possible to work from an AC source via complect AC adaptor.

<div style="page-break-after: always;"></div>

## 2. Appearance and controls
The appearance of the front panel of the device is shown in **Figure 1**. In the center of the panel there are connectors for connecting devices that support communication via the RS-422/485 interface and USB-B connectors. Connectors are grouped as **1** and **8**<sup>[1](#footnote21)</sup>. External devices are connected to connectors **X1** and **X3**, these connectors provide power to connected external devices. The USB-B connectors **X2** and **X4** are intended for connection to the USB port of a PC.

| ![Bat&Link Box panel](/documentation/batlinkbox_panel2ch.png) |
| :---: |
| **Fig. 1 - Control panel** | 
| _1 - Line 1, 2 - Charge indicator, 3 - Power state indicator, 4 - power switch, 5 - battery line fuse<sup>[2](#footnote22)</sup>, 6 - external power line fuse<sup>[2](#footnote22)</sup>, 7 - Charger (AC/DC adaptor) connector<sup>[2](#footnote22)</sup>, 8 - line 2_ |

Индикатор **2** горит, когда идет заряд встроенного источника питания, и не горит, когда заряд не идет.
Двухцветный индикатор **3** служит для отображения состояния питания системы. В **таблице 1** приведены все варианты возможных световых сигналов.
Тумблер **4** предназначен для включения питания устройства.

Предохранители **5** и **6** защищают цепи встроенного АКБ и внешнего питания соответственно. Применяются предохранители типоразмера **5.2х20** номиналом 5А.

Разъем  **7** предназначен для подключения сетевого адаптера, посредством которого осуществляется заряд встроенного источника питания и питание прибора от сети переменного тока.

### Таблица 1 - Сигналы световой индикации

| № | Напряжение встроенной АКБ |	Внешнее напряжение | Состояние индикатора |
| :---: | :--- | :--- | :--- |
| 1 | Ниже нормы | Ниже нормы | Часто загорается зеленый |
| 2 | Ниже нормы | Норма | Поочередно загораются зеленый и красный ( по 1 сек) |
| 3 | Ниже нормы | Выше нормы | Загорается и гаснет красный (на 1 сек) |
| 4 | Норма | Ниже нормы | Горит зеленый с короткими вспышками красного |
| 5 | Норма | Норма | Непрерывно горит зеленый |
| 6 | Норма | Выше нормы | Поочередно загораются зеленый и красный (по 200 мсек) |
| 7 | Выше нормы | Ниже нормы | Короткие вспышки красного |
| 8 | Выше нормы | Норма | Горит красный с короткими вспышками зеленого |
| 9 | Выше нормы | Выше нормы | Непрерывно горит красный |

_____________
<a name="footnote21"><sup>1</sup></a> Группа 8 присутствует только в расширенном исполнении. Стандартное исполнение содержит только группу 1.  
<a name="footnote22"><sup>2</sup></a> На устройствах, выпущенных до июля 2020 года разъемы предохранителей и подключения внешнего источника питания могут располагаться на боковых и/или задней поверхности кейса устройства.

## 3. Распиновки разъемов

### Таблица 2 - Контакты разъема 7 для подключения сетевого адаптера

| № | Номер контакта | Напряжение, В |
| :---: | :--- | :--- |
| 1 | 1, 3 | +U CHARGE |
| 2 | 2, 4 | GND CHARGE |

### Таблица 3 - Контакты раъема X1 (группа 1)
#### Указаны номера контактов для разъема на кабеле

| Номер контакта | Функция |
| :---: | :--- |
| 1 | плюс питания |
| 2 | общий питания |
| 3 | Rx+ |
| 4 | Rx- |
| 5 | Tx+ |
| 6 | Tx- |

<div style="page-break-after: always;"></div>

### Таблица 4 - Контакты разъема X3 (группа 8)
#### Указаны номера контактов для разъема на кабеле

| Номер контакта | Функция |
| :---: | :--- |
| 1 | плюс питания |
| 2 | общий питания |
| 3 | Rx+ | 
| 4 | не подключен |
| 5 | Rx- |
| 6 | Tx+ |
| 7 | Tx- |
  
<div style="page-break-after: always;"></div>

## 4. Работа с устройством
Перед использованием устройство должно быть расположено на устойчивом горизонтальном основании. При работе на судах и подвижных объктах рекомендуется фиксировать устройство за ручку кейса при помощи шнура.  

Подключение и отключение разъемов рекомендуется производить когда тумблер **4** находится в положении **OFF**. 

После завершения подключения и перевода тубмлера **4** в положение **ON**. Состояние устройства отображается при помощи индикатора **3** в соответствие с [таблицей 1]().

<div style="page-break-after: always;"></div>

## 5. Хранение и обслуживание
- Хранение устройства допускается только в выключенном состоянии (тумблер **4** в положение **OFF**), при закрытой крышке кейса и закрытых разъемах;
- При длительном (более месяца) хранении рекомендуется периодически проверять состояние встроенного АКБ и при необходимости заряжать его для исключения деградации встроенного АКБ;
- Загрязнения с корпуса устройства (кейса) допускается удалять при закрытой крышке помощи бытовых мыльных растворов, с последующим тщательным их удалением;
- Загрязнения на лицевой панели допускается устранять при помощи влажной ветоши, избегая попадания влаги и загрязнений в разъемы и гнезда предохранителей;
- Не допускается использование сторонних зарядных устройств;

<div style="page-break-after: always;"></div>

## 6. Обязательства и отказ от ответственности
### 6.1 Условия замены и бесплатного гарантийного обслуживания
Гарантия производителя распространяется только на заводские дефекты, выявивщиеся при эксплуатации устройства в соответствие с настоящим руководством в течении гарантийного срока (2 года с момента покупки).  

Производитель гарантирует бесплатный ремонт или замену неисправного оборудования из комплекта поставки, вышедшего из строя по причине заводского дефекта.  

К поводам для отказа от бесплатного гарантийного обслуживания, бесплатного ремонта и замены относятся:
- любые **механические повреждения** оборудования из комплекта поставки, в т.ч. нарушение изоляции проводов и кабелей;
- любые **повреждения, вызванные воздействием влаги и загрязнейний**, вследствие неправильной эксплуатации оборудования из комплекта поставки;
- любые **электрические повреждения**, вызванные **использованием некомплектных аксессуаров**; к некомплектным не отностятся аксессуары, поставленные производителем или его представителем в замен неисправных или утраченых;
- любые **следы самостоятельного ремонта и/или вскрытия** оборудования из комплекта поставки.

<div style="page-break-after: always;"></div>

### 6.2 Ограничение ответственности производителя

_____________

_**ЛЮБАЯ ИЗ ЧАСТЕЙ КОМПЛЕКТА ПОСТАВКИ В ОТДЕЛЬНОСТИ И В СОСТАВЕ СИСТЕМЫ, ИМЕНУЕМЫЕ ДАЛЕЕ "ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ":**_

_**- НЕ РАЗРАБАТЫВАЛОСЬ КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ТЕСТИРОВАЛОСЬ, КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ЯВЛЯЕТСЯ СРЕДСТВОМ СПАСЕНИЯ**_  
_**- ПРОИЗВОДИТЕЛЬ ЗАЯВЛЯЕТ, ЧТО ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ БЕЗОПАСНО ПРИ ЭКСПЛУАТАЦИИ СОГЛАСНО НАСТОЯЩЕЙ ИНСТРУКЦИИ И НЕ ОТВЕЧАЕТ ЗА ЛЮБЫЕ ПОСЛЕДСТВИЯ ИСПОЛЬЗОВАНИЯ ПОСТАВЛЯЕМОГО ОБОРУДОВАНИЯ**_

<div style="page-break-after: always;"></div>

_____________
[Back to contents]()
