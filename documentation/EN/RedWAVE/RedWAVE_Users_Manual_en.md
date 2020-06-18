| ![logo](https://ucnl.github.io/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedWAVE** - underwater acoustic navigation system <br/> User's manual |

# THIS DOCUMENT IS UNDER CONSTRUCTION!

# RedWAVE <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents


<div style="page-break-after: always;"></div>

## 1. Introduction
Underwater acoustic navigation system **RedWAVE** is designed to provide navigation data (absolute geographic coordinates and depth) of various underwater objects in a submerged state:
- remote-controlled unmanned underwater vehicles (**ROV**);
- manned underwater vehicles;
- autonomous unmanned underwater vehicles (**AUV**);
- recreational divers, technical divers (when using a diver's version of the system).

The principle of operation of the **RedWAVE** system is similar to the principle of operation of global satellite navigation systems such as **GPS**, **GLONASS** and the like.
The main difference is that small floating buoys [RedBASE](RedBASE_Specification_en.md) - repeaters of satellite navigation signal act as navigation satellites.

Geographic coordinates are generated directly on the navigation receiver, which is an acoustically passive device.
This architecture of the system allows to simultaneously provide navigation data to an unlimited number of navigation receivers with the use of one set of four buoys in one water area.

**RedWAVE** uses state-of-the-art digital broadband acoustic communication technology, and the applied signal is specially
Designed for difficult hydrological conditions, including conditions characteristic of shallow water bodies.

<div style="page-break-after: always;"></div>

## 2. System composition
### 2.1. RedBASE - GNSS-equipped sonobuoy
Regardless of the positioned objects - divers or robots, the **RedWAVE** system necessarily includes four navigation buoys [RedBASE](RedBASE_Specification_ru.md).

#### 2.1.1. General information
GNSS-equipped sonobuoys [RedBASE](RedBASE_Specification_en.md) are designed to build a long navigation base in
water bodies for supporting diving navigation receivers [RedNAV](RedNAV_Specification_en.md) and/or navigation receivers for robots [RedNODE](RedNODE_Specification_en.md).

A long navigation base is formed by four buoys [RedBASE](RedBASE_Specification_en.md). Each buoy set contains four buoys with numbers (addresses) from "1" to "4", the number in the set determines the isolating code channel of communication. Therefore, for the operation of the system requires the presence of all buoys of the set.

> It is possible to replace buoys with buoys from another set with the same addresses, **any other options are unacceptable** and will lead to the inability to determine coordinates using navigation receivers.

A general view of the buoy is presented in **figure1 **.

| |
| :---: |
| ![RedBASE general view](https://ucnl.github.io/documentation/def_redbase_yellow.png)|
| **Figure 1 - GNSS-equipped sonobuoy [RedBASE](RedBASE_Specification_en.md)** |

Buoys are to located in the water area on the water surface, their position is fixed using anchors.

> It is worth remembering that although the buoys have a small positive buoyancy, they are not intended for direct mounting on
anchor rope. To unload the buoy from the weight of the anchor rope, additional floats corresponding to the weight of the rope should be used.

**Figure 2** <sup>[1](#footnote1)</sup> shows the recommended deployment scheme for a buoy in a water body.

| |
| :---: |
| ![RedBASE deployment scheme](https://ucnl.github.io/documentation/def_redbase_dep_scheme.png)|
| **Figure 2 - [RedBASE](RedBASE_Specification_ru.md) recommended deployment scheme** |
| _1 - GNSS-equipped sonobuoy [RedBASE](RedBASE_Specification_ru.md), 2 - additional weight<sup>[2](#footnote2)</sup>, 3 - float, 4 - anchor rope, 5 - anchor_ |

__________
<a name="footnote1"><sup>1</sup></a>Images may vary slightly from supplied products.
as the manufacturer is constantly working to improve the performance and make design changes.  
<a name="footnote2"><sup>2</sup></a> Additional weight is used only in underloaded version. 

**Figure 3** shows the location of the controls and indicators on the buoy cover.

| |
| :---: |
| ![RedBASE deployment scheme](https://ucnl.github.io/documentation/def_redbase_cover_scheme.png)|
| **Figure 3 - Controls and indicators on the cover of [RedBASE](RedBASE_Specification_en.md)** |
| _1 - power toggle switch, 2 - indicator lights, 3 - charging connector_ |

#### 2.1.2. Operating modes and light indication
The buoys in each set have different numbers (addresses) from 1 to 4. When a buoy is turned on using the toggle switch 4 (see **Figure 3**), the buoy through **indicator 2** reports its number in the set: the number of flashes corresponds to the number of the buoy.

If the buoy is equipped with a light mast, the flashes will be duplicated on it.

After blinking its number, the buoy turns into operating mode. If the buoy’s battery is charged, the indicator will light constantly, until the built-in GPS/GLONASS receiver detects signals from satellites of the global satellite navigation system. After which it will flash 1 time in 4 seconds. The number of flashes in this case also corresponds to the number of buoys in the set.

If the buoy's battery is in a state where less than 20% of the charge remains, the indicator will flash 1 time per second. The number of flashes in this case also corresponds to the number of buoys in the set.

> If the user noticed flashes 1 time per second, the buoy should be turned off as soon as possible and put on charge. Long-term operation with a discharged power source is not allowed.

If the battery is in a critical discharge state, then after blinking with its number, the buoy will automatically turn off, in which case the indicator will also turn off. The buoy must be charged immediately to avoid failure of the internal power source.

#### 2.1.3. Preparation for use and verification
Before installing the buoy directly, make sure:
- in the integrity of the rubber cap of the toggle switch _1_ (see **Figure 3**);
- that the cover of the charging connector _3_ (see **Figure 3**) is tightly screwed;
- the light indication is OK and the built-in power source of the buoy is not discharged (see [2.1.2.]())

> _**ATTENTION!**_
> Almost all known cases of buoy failure are related to the fact that the user uses a buoy with an opened cover of charging connector!
> Do not use buoys with an opened connector cover and may result in water entering the device.
> Failure of buoys due to water entering through an open charging connector is _**non-warranty**_!


#### 2.1.4. Storage and maintenance
No special storage and maintenance requirements are imposed on buoys, with the exception of the following:

- When used in seawater and/or heavily polluted water, desalination is necessary (sediment and flushing in freshwater);
- The use of any organic solvents, strong acids, alkalis and other aggressive substances is not allowed;
- If necessary, washing in household soap solutions is possible;
- The impact of shock or significant static loads is not allowed, both on the buoy body and on the controls: toggle switch, light indicator lamps, charging connector, etc.;
- During long-term storage (more than 1 month), it is necessary to recharge the devices to prevent degradation of the built-in battery;
- The use of third-party chargers is not allowed;
- Strong (with a radius of less than 5 cm) bending of the cable of the hydroacoustic transmitter is not allowed;
- Do not store upside down, hanging on a load-carrying eye, etc .;

The chargers supplied with the buoys may vary slightly from kit to kit (in terms of indicating the status and completion of the charging process), so carefully read the attached instructions carefully before using them.

#### 2.2.1. General information
It is easiest to understand its purpose and the functionality of the integrated navigation receiver [RedNODE](RedNODE_Specification_en.md), starting from the analogy with ordinary GNSS receivers: when connected to a vessel, the receiver receives hydroacoustic signals from four buoys [RedBASE](RedBASE_Specification_en.md) and determines its own geographical position, and the built-in temperature and pressure sensor allows the vessel to additionally determine the depth, thereby providing the user with information about the position in three-dimensional space.
Coordinates are generated in the receiver itself and are accessible via the serial interface according to the [NMEA0183-like protocol](RedWAVE_Protocol_Specification_ru.md). In this regard, if transmission of the coordinates calculated by the receiver to the control panel is required, this should be done through the vessel's information channel.

#### 2.2.2. Interfacing and placement requirements
The receiver should be installed in a position in which line of sight with transmitters of all four buoys will be ensured (see paragraph [3]()). It should be located as far as possible from outputs of propulsors and various noisy mechanisms, sonars, etc. And also from units and modules that give strong electromagnetic interference (switching power supplies, motors, etc.).

When physically pairing the device with the vessel, it is necessary to ensure a reliable and tight cable entry that prevents water from flowing through the free end of cable. When sealing the free end of the cable, aggressive sealants and compounds (for example, silicone sealant based on acetic acid, etc.) should not be used, since its components can cause corrosion of the cable cores and lead to failure of the device.

It is not recommended to use compositions based on epoxy resins for sealing cable glands, as the latter, firstly, often collapse and lose their properties under prolonged exposure to moisture, and secondly, they give significant shrinkage after the cure.

The most reliable and suitable are compounds and sealants based on polyurethanes. In case of any questions about sealing, it is recommended to consult with the manufacturer.

Power requirements are specified in [device specification](RedNODE_Specification_en.md).
For information on information exchange with the device and changes in its configuration, refer to the [description of the pairing protocol](RedWAVE_Protocol_Specification_ru.md).

### 2.3. RedNAV - Diver's navigation receiver
Diver's navigation receiver [RedNAV](RedNAV_Specification_en.md) designed to provide navigation data to divers and
accordingly, it is necessary only in the case of diving operations.

#### 2.3.1. General information
The diver's navigation receiver [RedNAV](RedNAV_Specification_en.md) allows a diver to determine the geographic location when submerged without the need for ascent and the use of floating GPS antennas on the cable.
Working with the device [RedNAV](RedNAV_Specification_en.md) is in many ways similar to working with GPS/GLONASS trackers and navigators, with the only difference being that small-sized floating buoy transponders of a satellite navigation system signal play the role of positioning system satellites. For the operation of an unlimited number of devices [RedNAV](RedNAV_Specification_ru.md) in one water area, 4 floating relay buoys [RedBASE](RedBASE_Specification_ru.md) are required.
The unique functionality and ease of use make [RedNAV](RedNAV_Specification_en.md) an ideal solution for recreational diving, as well as for search, archaeological and other underwater operations.
The general view of the device is shown in **Figure 4**.

| |
| :---: |
| ![RedNAV general view](https://ucnl.github.io/documentation/def_rednav_yellow.png)|
| **Figure 4 - diver's navigation receiver [RedNAV](RedNAV_Specification_en.md)** |
| _General view_ |

The interface unit contains the following main controls and modules:
- a screen for displaying navigation and service information;
- two piezo buttons on the sides, to control the device;
- built-in battery;
- Bluetooth module;
- DSP unit;
- wireless charge receiver.

The acoustic navigation receiver is connected to the interface unit using a cable and can be installed:
- on the shoulder of a diver;
- on a special panel that the diver holds in his hands;
- on the tank to ensure the minimum possible acoustic shading.

Optimum operating conditions for the acoustic receiver are achieved when there is a line of sight between the navigation receiver and the acoustic transmitters of all four buoys [RedBASE](RedBASE_Specification_en.md) throughout the entire time of use. This position is discussed in more detail in [par. 3.3.]().

#### 2.3.2. Work with the device, modes and user interface
##### 2.3.2.1. Navigation mode
**To turn on** the device user must simultaneously press both buttons of the device located on the side surfaces of the interface unit.

> ATTENTION! The diver's navigation receiver is equipped with piezo buttons to exclude the possibility of device failure due to water entering the housing through mechanical button seals. Piezo buttons have some operational features, in particular, the lack of feedback when pressed. Buttons perceive only a short change in pressure, therefore, all presses in order to control the device should be short.

After switching on, the device, not installed on the charging pad, automatically switches to navigation mode.
The appearance of the device screen in navigation mode immediately after switching on is shown in **Figure 5**.

> ATTENTION! Immediately after switching on, the device calibrates atmospheric pressure for **10 seconds** to more accurately determine the depth. Therefore, turning on the device is recommended only in the air. If at startup the hydrostatic pressure exceeds ** 1100 mbar **, then atmospheric pressure calibration is not performed, and the standard value ** 1013.25 mbar ** is taken as atmospheric pressure.

| |
| :---: |
| ![RedNAV after start](https://ucnl.github.io/documentation/rednav_scr1.png) |
| **Figure 5 - Main screen in navigation mode** |
| _After start up_ |
| _1 - Left button function (target switch), 2 - buoys status, 3 - azimuth and distance to target, 4 - right button function (mark current position), 5 - water temperature, 6 - depth (distance to the water surface), 7 -battery charge_ |

When buoy signals are not received (for example, immediately after switching on), the azimuth and distance to the target are not displayed on the screen, because the geographic location of the navigation receiver is either unknown or obviously out of date. Button functions are also not available in this case.
**Figure 6** illustrates the situation when the navigation receiver received a signal from the first buoy, but its own location has not yet been determined.
It is worth remembering that the transmission of buoy signals is time-divided, and the receiver awaits their signals sequentially. Accordingly, if the reception of the 1st buoy does not occur, then the reception of the 2nd is not conducted, etc.  

|  |
| : ---: |
| ![RedNAV after start](https://ucnl.github.io/documentation/rednav_scr2.png) |
| **Figure 6 - The main screen of the device during operation** |
| _Device has received signal from Buoy #1. Own location has not been determined yet_ |

When signals from all buoys are received and the coordinates of the navigation receiver are updated, the main screen has the form, as in **Figure 7**. For example, buoys with numbers **2** and **4** have a low charge of the built-in power supply, therefore, they are displayed as open squares with colour inversion. Buoy **#1** is selected as the navigation target and its icon is displayed enlarged.

|  |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr3.png) |
| **Figure 7 - The main screen of the device during operation** |
| _Location determined. The buoy No. 1_ was chosen as the navigation target |

In the **3** field (see **Figure 5**) **Azimuth and distance to the target** *Azimuth* and *distance* to the selected buoy are displayed. By *azimuth* here we mean *the angular direction from the northern half-meridian clockwise to the line to the target*.

> ATTENTION! When approaching the target at a distance of fewer than 3 meters, instead of the angular direction to the target, dashes **"- - -"** are displayed.

When the location is determined (azimuth and distance to the selected target are displayed), when the user presses the left button (**>**), the next target in the list is selected (after Buoy #1, Buoy #2, #3 and #4). If waypoints have been preloaded into the device, they are located in the target list after the buoys. When switching navigation targets, the corresponding navigation information (Azimuth and distance) also changes.

When the user presses the right button (**+**), the current location is saved separately (the marked point is saved), which is placed at the end of the target list. An informational message is displayed, as in **Figure 8**.

|  |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr3a.png) |
| **Figure 8 - Message confirming that the current location has been saved** |

The preloaded and marked points are numbered, and when the user selects them as targets using the **> ** button, they are displayed as in ** Figure 9 **.

|  |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr4.png) |
| **Figure 9 - The main screen of the device during operation** |
| _The first waypoint/marked point is selected as a navigation target_ |

To turn off the device, the user must simultaneously press both buttons. In this case, the device will ask for confirmation of shutdown, as shown in **Figure 10**.

| |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr5.png) |
| **Figure 10 - Shutdown confirmation** |

##### 2.3.2.2. Service mode
When the interface unit is installed on the charging pad, it switches into service mode. In this mode, the built-in power supply is charged and the device configuration is possible. **Figures 11 and 12** show the device screen after installation on the charging pad. The state of charge and wireless connection are displayed by the brightness of the corresponding icons.

It should be remembered that the charging platform must contact directly with the housing of the interface unit. If a belt is attached to the interface unit, it should be pulled back and a charging pad placed between the interface unit housing and the belt. Otherwise, the distance between the transmitter of the charger and the receiver inside the housing of the interface unit will be too far to provide the required charging current.

| |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr6.png) |
| **Figure 11 - Screen view of the device in service mode** |
| _The charging icon lights up brightly - the charge is on, the Bluetooth icon is darkened - the connection is not established_ |

| |
| : ---: |
| ![RedNAV](https://ucnl.github.io/documentation/rednav_scr7.png) |
| **Figure 12 - Screen view of the device in service mode** |
| _Both icons glow brightly - there is a charge, a Bluetooth connection is established_ |

When the device is on the charging platform, after **5 minutes** inactivity, the screen turns off in order to save energy and charge the built-in power supply faster. Pressing any button on the interface device again turns on the screen.

When the interface unit is removed from the charging pad, the device automatically turns off.


##### 2.3.2.3. Встроенный Bluetooth модуль и синхронизация
Водолазный навигационный приемник содержит Bluetooth модуль, служащий для:
- конфигурации устройства при помощи ПК;
- передачи координат внешней системе в реальном времени (эмуляция Bluetooth GNSS-приемника).

Модуль включается при старте устройства независимо от режима, в котором оно находится и выключается через **10 минут** для энергосбережения, если за это время к нему не произошло подключения. 

Модуль каждого навигационного приемника имеет уникальное имя Bluetooth устройства, имеющего формат:
`RDNV-XXXX`  
где `XXXX` - уникальный идентификатор, состоящий из латинских букв в верхнем регистре и цифр. Пример того, как отображается имя Bluetooth устройства показан на **рисунках 11 и 12** (RDNV-AD48). Ниже, под строкой с именем устройства отображается подсказка, содержащая пин-код (в данном пример пин-код **1945**), который необходимо ввести при первоначальном подключении устройства к внешней системе.

Если подключение по Bluetooth происходит когда устройство находится в навигационном режиме, то оно передает навигационную информацию, в частности сообщения [GGA](RedWAVE_Protocol_Specification_en.md#211-gga), [RMC](RedWAVE_Protocol_Specification_en.md#212-rmc) и [MTW](RedWAVE_Protocol_Specification_en.md#213-mtw).

Таким образом, водолазный навигационный приемник [RedNAV](RedNAV_Specification_en.md) может выступать в качестве Bluetooth GNSS-приемника, данные с которого могут быть использованы при отображении местоположения водолаза в реальном времени на каком-либо картографическом устройстве, например, на водолазном планшете, поддерживающим подключение внешнего GNSS-приемника по Bluetooth. 
Стоит помнить, что радиоволны практически не проникают через толщу воды, и для устойчивой работы Bluetooth соединения под водой, приборы (интерфейсный блок водолазного навигационного приемника и картографическое устройство) должны как можно ближе касаться друг друга корпусами.

Когда устройство стоит на зарядной площадке и находится в сервисном режиме, Bluetooth соединение применяется для изменения настроек водолазного навигационного применика при помощи специализированного ПО [RedNAV Host](https://api.github.com/repos/ucnl/RedNavHost/zipball).

Установка Bluetooth-соединения и работа с ПО [RedNAV Host](https://api.github.com/repos/ucnl/RedNavHost/zipball) описывается в документе [RedNAV Host: Руководстве пользователя](RedNAV_Host_Users_Manual_en.md).

#### 2.3.3. Хранение и обслуживание
Водолазный навигатор [RedNAV](RedNAV_Specification_en.md) не требует особых условий хранения и обслуживания, за исключением следующих:
- Не допускается полный разряд встроенного аккумулятора навигатора. При длительном (более 1 месяца) хранении рекомендуется периодически заряжать устройство;
- После использования в соленой воде устройство должно быть тщательно промыто в пресной воде;
- Не допускается использование моющих средств и органических растворителей. Возникшие загрязнения удаляются мягкой влажной тряпкой. Допускается использование мыла с последующей промывкой в пресной проточной воде;
- Не допускается оставлять надолго устройство под действием прямых солнечных лучей;
- Защитное стекло-крышка выполнено из абразивостойкого поликарбоната, но рекомендуется избегать любых возможных контактов стекла-крышки с твердыми(острыми) предметами во избежание появления царапин и сколов на стекле-крышке;
- Не допускается перегиб кабеля, соединяющего интерфейсный блок с навигационным приемником, с радиусом менее 5 см;
- Следует избегать любых ударных нагрузок как к корпусу интерфейсного блока, так и к акустическому приемнику;
- Не допускается контакт отверстия датчика давления акустического приемника с твердыми(острыми) предметами; Возникшие загрязнения в отверстии датчика давления должны удалятся только промывкой в проточной пресной воде.

<div style="page-break-after: always;"></div>

## 3. Эффективное развертывание длинной навигационной базы
Развертывание длинной навигационной базы в общем случае состоит из постановки четырех буев-ретрансляторов [RedBASE](RedBASE_Specification_en.md) в акватории, где предполагается работа, и их включения. Каждый из четырех буев комплекта отличается от других адресом, определяющим кодовый канал гидроакустической связи по которому буй передает данные.

> _**ВНИМАНИЕ**_!
> Не допускается одновременная работа нескольких комплектов буев на одном водоеме, а также использование буев из разных комплектов с одинаковыми адресами. В этом случае правильность определения координат и работоспособность системы не гарантируется!

**Правильная установка буев подразумевает соблюдение трех основных условий:**
1. обеспечение безопасного и стабильного положения буев на поверхности воды;
2. обеспечение хорошего обзора небесной полусферы для установленных на буях приемных антенн спутниковых навигационных систем;
3. обеспечение прямой видимости между акустическими передающими антеннами буев и всеми навигационными приемниками в погруженном положении.

Рассмотрим эти три условия более подробно:

### 3.1. Обеспечение безопасного и стабильного положения буев на воде
Для обеспечения первого условия, плавучие буи должны устанавливаться на якоря, обеспечивающие сохранение положения буев от воздействия ветра и течений. При этом вес якорный веревки должен восприниматься дополнительным поплавком, а буй не должен воспринимать никакой дополнительной вертикальной нагрузки. На **рисунке 2** представлена рекомендуемая схема крепления буя [RedBASE](RedBASE_Specification_en.md) на якоре.

Не рекомендуется применение системы при волнении моря более **1.5 баллов**. При волнении моря **2 и более баллов** применение системы _крайне не рекомендуется_ и производитель не несет ответственности за повреждение отдельных устройств системы их утерю и неправильную работу и пр.

### 3.2. Обеспечение обзора небесной полусферы
Второе условие связано с тем, что буи [RedBASE](RedBASE_Specification_en.md) являются ретрансляторами спутникового навигационного сигнала. Они имеют встроенные комбинированные **GPS/GLONASS** приемники и для правильной работы навигационной базы, образуемой буями, необходимо обеспечить хороший прием спутникового навигационного сигнала на всех буях. Всвязи с этим буи стоит располагать на максимальном удалении от различных преград, которые могут повлиять на качество принимаемого спутникового сигнала. Например металлические корпуса судов, причальные стенки и пр.  
Буи [RedBASE](RedBASE_Specification_en.md) оснащены световой индикацией. Так при включении лампы световой индикации постоянно горят до того момента, пока не произойдет первое уточнение географического местоположение буя встроенным **GPS/GLONASS** приемником. После чего они гаснут и через некоторое время (в среднем 1-2 минуты) буй переходит в рабочий режим. При этом лампы световой индикации вспыхивают раз в четыре секунды (число коротких вспышек соответствует номеру буя). А если встроенная батарея буя сильно разряжена, то лампы вспыхивает каждую секунду. В этом случае буй должен быть немедленно поставлен на зарядку, иначе это может привести к выходу из строя встроенной батареи.  
Типичное время перехода буя в рабочий режим (время до того как сигнальная лампа перестанет гореть постоянно) в условиях открытой воды составляет не более 2-3 минут. Если лампа не гаснет более длительное время следует сменить местоположение буя. Многократное повторение данной ситуации на явно открытом пространстве, где ничего не может мешать прохождению спутникового навигационного сигнала, является поводом для обращения к производителю.

### 3.3. Обеспечение прямой видимости между буями и навигационными приемниками
Третье условие определяется физическими принципами работы длинной навигационной акустической базы. Так как вычисление собственного положения навигационными приемниками производится по оценке времен прихода акустических сигналов от буев [RedBASE](RedBASE_Specification_Подводная акустическая навигационная система **RedWAVE** предназначена для обеспечения навигационными данными (абсолютными географическими 
координатами и глубиной) различных подводных объектов в погруженном состоянии: 
- телеуправляемых необитаемых подводных аппаратов (**ТНПА**);
- обитаемых подводных аппаратов (**ОПА**);
- автономных необитаемых подводных аппаратов (**АНПА**);
- дайверов, технических водолазов (в случае использования приборов в водолазном исполнении)..md) до самих приемников, то для их правильной работы требуется постоянная прямая видимость между акустическими передатчиками всех четырех буев [RedBASE](RedBASE_Specification_en.md) и работающими навигационными приемниками (имеется в виду прямая видимость через толщу воды).  
Оптимальным расположением буев в акватории считается выпуклый четырехугольник, ограничивающий место проведения работ. При этом расстояния между буями не должны превышать **700 метров** и не быть менее **30 метров**. Работа с навигационными приемниками вне фигуры длинной базы возможна, но в виду ее физической природы, наибольшую точность и надежность навигационных данных возможно получить внутри фигуры длинной базы.  
Наиболее плохим, с точки зрения длинной навигационной базы, является такое расположение, при котором три или более буев располагаются в линию.
При расстановки и планировании расстановки буев также стоит избегать таких расположений, при которых глубина места (расстояние от поверхности воды до дна) у буев значительно отличается от глубины места позиционируемых объектов. Например, когда работа предполагается в узком месте реки с одним пологим берегом. В таких случаях буи стоит располагать в глубокой части реки.  
Однако, при этом стоит помнить, что слишком маленькая фигура навигационной базы (меньше **30 метров**) и/или сильная ее вытянутость (соотношение сторон четырехугольника более 4-5) приводит к снижению точности и/или меньшей чувствительности в некоторых направлениях соответственно.  
Допускается расположение буев в прорубях, при условии обеспечения несдавливания корпуса устройства льдом и обеспечения достаточной осадки акустической антенны (излучающая антенна буя должна находится глубже нижней кромки льда, как минимум на 0.5 метра).  
Не рекомендуется длительная работа акустической антенны на воздухе. Также следует обеспечить свободное положение акустической антенны в рабочем положении без касаний якорной веревки или каких-либо иных объектов.

## 4. Возможные неисправности, их диагностика и устранение

| № | Симптомы | Возможная причина | Устранение |
| :---: | :--- | :--- | :--- |
| 1 | При установке на зарядную площадку не включается сервисный режим, хотя индикатор питания горит (питание подается на зарядную площадку) | 1. Зарадная площадка прилегает не плотно <br/> 2. Зарядная площадка неисправна | 1. Наити оптимальное положение зарядной площадки <br/>  2. Заменить зарядную площадку |
| 2 | В навигационном режиме не происходит определение местоположения, хотя все буи принимаются | Системе неудается определить местоположение с достаточной точностью в виду неудачного взаимного расположения буев и навигационного приемника или неблагоприятных гидрологических условий | 1. Убедиться, что буи образуют выпуклый четырехугольник и начать навигацию внутри фигуры буев, избегая близости к буям |
| 3 | В навигационном режиме не происходит определение местоположения из-за того что прием буев неустойчивый | 1. Один из буев не работает <br/> 2. Устойчивому приему сигналов буев препятствуют гидрологические условия <br/> 3. Между передатчиками буев и навигационным приемником нет прямой видимости | 1. Проверить работоспособность всех буев <br/> 2 и 3. Попробовать начать навигацию из другого места, убедившись, что прохождению сигнала ничего не мешает (элементы подводного ландшафта и портовой инфраструктуры, густые заросли водорослей и т.п.) |

<div style="page-break-after: always;"></div>

## 5. Обязательства и отказ от ответственности
### 5.1 Условия замены и бесплатного гарантийного обслуживания
Гарантия производителя распространяется только на заводские дефекты, выявивщиеся при эксплуатации устройства в соответствие с настоящим руководством в течении гарантийного срока (2 года с момента покупки).  

Производитель гарантирует бесплатный ремонт или замену неисправного оборудования из комплекта поставки, вышедшего из строя по причине заводского дефекта.  

К поводам для отказа от бесплатного гарантийного обслуживания, бесплатного ремонта и замены относятся:
- любые **механические повреждения** оборудования из комплекта поставки, в т.ч. нарушение изоляции проводов и кабелей;
- любые **повреждения, вызванные воздействием влаги и загрязнейний**, вследствие неправильной эксплуатации оборудования из комплекта поставки;
- любые **электрические повреждения**, вызванные **использованием некомплектных аксессуаров**; к некомплектным не отностятся аксессуары, поставленные производителем или его представителем в замен неисправных или утраченых;
- любые **следы самостоятельного ремонта и/или вскрытия** оборудования из комплекта поставки.

<div style="page-break-after: always;"></div>

### 5.2 Ограничение ответственности производителя

_____________

_**ЛЮБАЯ ИЗ ЧАСТЕЙ КОМПЛЕКТА ПОСТАВКИ В ОТДЕЛЬНОСТИ И В СОСТАВЕ СИСТЕМЫ, ИМЕНУЕМЫЕ ДАЛЕЕ "ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ":**_

_**- НЕ РАЗРАБАТЫВАЛОСЬ КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ТЕСТИРОВАЛОСЬ, КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ЯВЛЯЕТСЯ СРЕДСТВОМ СПАСЕНИЯ**_  
_**- ПРОИЗВОДИТЕЛЬ ЗАЯВЛЯЕТ, ЧТО ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ БЕЗОПАСНО ПРИ ЭКСПЛУАТАЦИИ СОГЛАСНО НАСТОЯЩЕЙ ИНСТРУКЦИИ И НЕ ОТВЕЧАЕТ ЗА ЛЮБЫЕ ПОСЛЕДСТВИЯ ИСПОЛЬЗОВАНИЯ ПОСТАВЛЯЕМОГО ОБОРУДОВАНИЯ**_
  
______________

[Вернуться к содержанию](#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
