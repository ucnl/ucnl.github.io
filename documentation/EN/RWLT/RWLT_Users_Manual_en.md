[Main](/../../) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **RWLT: User’s manual**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RWLT** - Underwater acoustic tracking system <br/> User's manual |

# RWLT <br/> User's manual

<div style="page-break-after: always;"></div>

## Contents


<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1. Purpose

Underwater Acoustic Tracking System **RWLT** is designed for:

- determining the geographic location and depth of an underwater object (**AUV**, **ROV**, **ROU**, divers, etc.) equipped with an autonomous pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md). In this system configuration, it is possible to track the position of **one** object equipped with an autonomous pinger beacon.
- determining the geographic location of divers equipped with wireless voice diving transceivers [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html). In this system configuration, it is possible to track the position of 255 divers in one water area.

### 1.2. Peculiarities

The **RWLT** system uses state-of-the-art digital broadband noise-immune hydroacoustic communication, and the applied signal is specially designed for difficult hydrological conditions, including those found in shallow waters.

The **RWLT** System is the **Easiest to Use** yet Accurate Subsea Tracking Solution. The system **does not require any calibrations** and integration: it is enough to place an autonomous pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md) on an underwater object (ROV, AUV, diver, etc.), and four navigation buoys on the water surface [RWLT GIB](RWLT_GIB_Specification_en.md). This configuration allows you to monitor the movement of an underwater object in real time in 3D: absolute geographic coordinates + depth.
A distinctive feature of the system is the ability to work with wireless diver's telephones [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_EN_Specification_en.html) as a pinger, thus combining two-way voice communication and navigation.

### 1.3. System Composition

The minimum composition of the system includes:

- **Four sonobuoys** [RWLT GIB](RWLT_GIB_Specification_en.md):

| ![RWLT GIB](/documentation/RWLT_GIB.png) |
| :---: |
| [RWLT GIB](RWLT_GIB_Specification_en.md) <br/> Navigation sonobuoy receiver |

- Radio modem [RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md), for receiving navigation information from buoys:

| ![RWLT RF Dongle](/documentation/RWLT_RF_Dongle.png) |
| :---: |
| [RWLT RF Dongle](RWLT_RF_Dongle_Specification_en.md) <br/> Digital Radio |

And, depending on the user task:
* If it is required to determine the location of divers simultaneously with voice communication, then **up to 255** wireless diver's telephone stations [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) are used;

| ![RedPhone-DX](/documentation/redphone_dx.png) |
| :---: |
| [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) <br/> Wireless voice communication diver's station |

In this configuration, divers will be located at the moment they release the PTT button, i.e. completing the transmission of the voice message; the transmission of voice messages must take place in turn.

* If you want to determine the location of a remotely operated vehicle (ROV, ROV), or a diver without the need for voice communication, then **1** pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md) is used. The pinger works autonomously and the geolocation of the object on which the pinger is attached will be updated every two seconds.

| ![RWLT Pinger](/documentation/RWLT_Pinger.png) |
| :---: |
| [RWLT Pinger](RWLT_Pinger_Specification_en.md) <br/> Pinger beacon |


## 2. Working with the RWLT system

### 2.0. Before work
Depending on whether you are working with a pinger or tracking divers, you will need different versions of specialized software.

- To track an underwater object equipped with an autonomous pinger [RWLT Pinger](RWLT_Pinger_Specification_en.md), the application [🐠 uTrack](https://github.com/ucnl/uTrack/releases/download/beta1/uTrack) must be installed on the operator's PC .zip)

- To track the position of divers equipped with [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html) wireless voice communication diving stations, the [🤿 uTrackDiver](https://github.com/ucnl/uTrack/releases/download/beta/uTrackDiver.zip) application must be installed on the operator's PC 

Download the necessary software in advance. Installation is not required - just unzip the contents of the archive to a location convenient for you.

Whether you are using underwater equipment such as wireless voice communication diving stations or a stand-alone pinger beacon, make sure that all equipment is fully charged before entering the water and charge all devices if necessary.

Particular attention should be paid to wireless voice communication diving stations and pinger beacons: in view of the fact that these devices have built-in power supplies based on **LiFePO4**, they have a very flat discharge characteristic and it is difficult to determine the state of charge of the built-in power source. Therefore, it is recommended to charge all devices no earlier than 1-2 days before use.

We use **LiFePO4** based batteries as they are the most durable and withstand the maximum number of charge-discharge cycles compared to **Li-ion** and **Li-Po** batteries, and can also operate at low temperatures. temperatures.

### 2.1. Preparing for work and checking equipment

#### 2.1.1. Choosing a location for the operator's place 

Select the location where the system operator's station will be located. Since the receiving antenna of the radio modem is located in this place, there must be a direct line of sight to each of the buoys from this place. For normal operation of the system, the operator's console must be able to receive navigation data via radio from all four buoys.
Place the radio modem at the highest possible height away from any bulky objects that shield radio waves (metal, reinforced concrete, etc.).

Connect the radio modem to the USB port of the PC. Launch the application appropriate for your task and press the **🔌 LINK** button in the top toolbar - the application will start searching for a port for communication with the radio modem, which will be reflected in the status bar.

#### 2.1.2. Checking the set of buoys

- Check the integrity of the rubber caps of the toggle switches. If any defects are found that violate the moisture-proof functions of the caps, the use of buoys is **strictly prohibited**.
- Make sure that the charging port caps on all buoys are screwed on tightly.
- Turn on all buoys by moving the toggle switches on their cover to the **ON** position.
- Verify that all buoys are operational and that their built-in power supplies are sufficiently charged, as described in the warning lights below:

> _**WARNING!**_
> Almost all known buoy failures are due to the user using a buoy with an unscrewed cap of the charging connector!
> Operation of buoys with an unscrewed cap of the connector is prohibited and may result in water ingress into the device.
> Failure of buoys due to water ingress through an open charging port is _**out of warranty**_!

The location of the controls and indications on the buoy cover is shown below.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_cover_scheme.png)|
| Location of controls and indications on the cover of the buoy |
| _1 - power switch, 2 - light indication lamps, 3 - charging connector (Radio antenna not shown)_ |

The buoys in each set have different addresses from 1 to 4. When the buoy is turned on using toggle switch 1, the buoy reports its number in the set using indicator 2: the number of flashes corresponds to the buoy number.

After reporting its number, the buoy goes into operation mode. If the buoy's battery is charged, the indicator will remain lit until the built-in GNSS receiver detects signals from the satellites of the global navigation satellite system. After that, it will flash 1 time in 4 seconds. The number of flashes in this case also corresponds to the number of the buoy in the set.

If the battery of the buoy is in a state where the charge is less than 20%, the indicator will flash 1 time per second. The number of flashes in this case also corresponds to the number of the buoy in the set.

> If the user notices flashes 1 time per second, the buoy should be turned off and put on charge as soon as possible.
> Long-term operation with a discharged power supply is not permitted.

If the battery is in a state of critical discharge, then after reporting its number, the buoy will automatically turn off, in this case the indicator will also be off. The buoy must be immediately put on charge to avoid failure of the built-in power source.

If everything is done correctly, and the tops of the buoys have a good view of the celestial hemisphere, then after a while (usually no more than 1-2 minutes) you will be able to see the positions of the buoys in the main application window.

After that, you can place the buoys on the surface of the water.

If you need a significant amount of time to equip the buoys with anchor lines and place them on the surface of the water, you can turn off the buoys to save power and turn them on just before placing them on the water.

#### 2.1.3. Location of buoys on the surface of the water

The buoys are placed in the water area on the surface of the water, their position is fixed with the help of anchors.

> It is worth remembering that although the buoys have a slight positive buoyancy, they are not intended for direct attachment to an anchor line. To unload the buoy from the weight of the anchor rope, fenders (or floats) corresponding to the weight of the rope should be used.

The figure below<sup>[1](#footnote1)</sup> shows the recommended scheme for installing a buoy on a body of water.

| |
| :---: |
| ![deployment scheme](/documentation/def_redbase_dep_scheme.png)|
| Recommended buoy installation scheme |
| _1 - sonobuoy, 2 - extra weight<sup>[2](#footnote2)</sup>, 3 - float, 4 - anchor line, 5 - anchor_ |

__________
<a name="footnote1"><sup>1</sup></a> Images may vary slightly from actual product,
as the manufacturer is constantly working to improve performance and make changes to the design.
<a name="footnote2"><sup>2</sup></a> The extra weight is only applied to the underloaded version.

The buoys should be located in a convex quadrilateral covering the entire proposed work area with a small margin. It is important to observe a few simple conditions for the effective operation of the system:

- buoys are located no closer than 40 and no further than 1500 meters from each to each
- from each buoy there must be direct visibility to the receiving radio modem of the operator's console
- from each sonoacoustic receiver of the buoy there must be a direct line of sight to the positioned underwater object
- it is not recommended to place buoys close to the shore, port infrastructure facilities, ships
- the size of the navigation base (the average size of the rectangle formed by buoys on the surface of the water) should not be less than the maximum depth of the positioned object
- the size of the navigation base should be slightly larger than the intended area of work

> _**WARNING!**_
> Buoys are not underwater devices and are designed to operate on the surface of the water. Although the protection class implies a short-term overlap of the device with a wave, it is worth remembering that the built-in radio equipment (GNSS module and radio modem) cannot work in such conditions!

It is not recommended to throw buoys overboard. It is necessary to carefully lower them to the surface of the water, at the same time making sure that the length of the anchor rope is sufficient and its weight is perceived by the unloading fender, and the buoy is located vertically on the surface of the water and does not experience any additional loads.

#### 2.1.4. Preparation of underwater equipment

Subsea equipment preparation varies for different system configurations:

- For location-tracking configuration of divers equipped with  wireless voice diving stations [RedPhone-DX](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Specification_en.html), refer to the [RedPhone-DX diving stations instruction manual](https://docs.unavlab.com/documentation/EN/RedPhone/RedPhone_DX_Users_Manual_en.html);
It should be remembered that:
  - the **RWLT Pinger** mode must be enabled on the stations (setting **RWLT Pinger enabled**);
  - when using several voice communication stations in one body of water, they must be given **different** addresses (**RWLT Diver's ID**).

- To configure a system with a stand-alone pinger beacon [RWLT Pinger](RWLT_Pinger_Specification_en.md), no preliminary steps are required other than pre-charging the built-in power source (battery pack). For versions with a detachable connection between the pinger beacon and the battery pack, you must first make sure that the connector is tightly closed and serviced (for threaded connectors, make sure that the sealing rings are lubricated with silicone grease, for SUBCONN and similar connectors, make sure that both parts of the connector are grease recommended by the connector manufacturer).

The pinger beacon turns on automatically when it gets into the water (contacts for switching on from water are located on the battery pack). It should be remembered that immediately after switching on, the pinger beacon determines atmospheric pressure for **5** seconds for more accurate depth measurement. Therefore, it is recommended to submerge the battery pack first and wait 5 seconds before submerging the pinger beacon itself.

The pinger beacon must be fastened only to a special groove with a soft clamp in such a way as to exclude any uneven loading of the beacon body, excessive squeezing and shading/shielding of the beacon body. The figure below shows the basic requirements for mounting the acoustic part of the pinger beacon on the vessel:

| |
| :---: |
| ![0](/documentation/uWave_mounting_en.png)|
| Requirements for mounting the acoustic part of the pinger beacon on the vessel|
| _It is not allowed to shield the spatial hemisphere or parts of the antenna located above the mounting groove; the pressure in the area under the fastening must be balanced with the external pressure_ |

The performance of the pinger beacon is easy to check by lowering it into the water: when submerged more than 1 meter, it starts emitting a navigation signal with a period of 2 seconds.

## 2.2. Работа с системой

### 2.2.1. Конфигурация с водолазными станциями связи

#### 2.2.1.1. Интерфейс и функции приложения

Знакомство с приложением предлагаем начать с его настроек. На рисунке ниже представлен общий вид окна настроек, его можно вызвать, нажав на кнопку **'⚙ SETTINGS'** на главной панели инструментов главного окна приложения.

| |
| :---: |
| ![1](/documentation/uTrackDiver_settingswindow_1.png)|
| Элементы управления окна настроек |
| _1 - Признак использования дополнительного источника навигационных данных (GNSS-приемника), 2 - Выпадающий список скорости порта дополнительного источника навигационных данных, 3 - Признак использования первого буя в качестве дополнительного источника навигационных данных, 4 - Список серверов-источников тайлов карты, 5 - Кнопка сброса настроек в настройки по умолчанию, 6 - Признак автоматического выбора солености (из базы данных), 7 - Поле ввода солености, 8 - Признак автовычисления скорости звука, 9 - Поле ввода скорости звука, 10 - Поле ввода температуры воды, 11 - Количество точек трека для отображения, 12 - Поле ввода порога радиальной ошибки, 13 - Выпадащий список выбора размера тайлов карты, 14 - Кнопки принятия настроек и отмены_ |

Приемный радиомодем подключается к ПК через порт USB. Приложение само производит поиск виртуального последовательного порта и это не требует от пользователя задания каких-либо настроек.

- В некоторых ситуациях оператору удобно видеть на карте собственное местоположение, это можно обеспечить двумя способами: первый состоит в подключении дополнительного GNSS-приемника к ПК. В этом случае приложению нужно указать, что такой способ используется, поставив галочку в окошке 1 **Use AUX GNSS**. Так же в этом случае требуется указать скорость последовательного порта, на которой работает внешний GNSS-приемник. Сам порт указывать не требуется, приложение обнаружит его само.

- Если внешнего GNSS-приемника нет, но оператору желательно видеть собственное местоположение на карте, можно воспользоваться вторым способом: в качестве внешнего GNSS может быть использован буй №1. Этот способ имеет некоторые ограничения, например, не всегда есть возможность расположить оператора рядом с буем, от буев идет ограниченный по сравнению с внешним GNSS-приемником набор навигационной информации. Если такой способ применим в текущей задаче, то следует поставить галочку в окошко 3 **Base 1 as AUX GNSS Source**. В этом случае галочка в окошке 1 будет автоматически снята.

- Приложение позволяет отображать треки поверх карты, тайлы которой могут скачиваться по протоколу HTTPS. На данный момент поддерживаются сервис Open Street Maps. В поле 4 **Tile servers** указываются адреса серверов, а в поле 13 **Tile size** указывается размер тайлов в пикселях. Для загрузки тайлов приложению нужен доступ к сети Интернет.

- Кнопка 5 **SET DEFAULTS** позволяет сбросить настройки в состояние по умолчанию.

- Установленная галочка 6 **Auto salinity** означает, что приложение будет пытаться определить соленость из базы данных по текущим географическим координатам. Приложение содержит базу солености поверхности мирового океана с шагом в 1 градус по широте и долготе. Используйте эту настройку только в крупных водоемах: морях и океанах. Если вы работает в небольших внутренних водоемах рекомендуется снять галочку 6 и задать соответствующее значение солености воды в поле 7 **Salinity, PSU**. В большинстве случаев, для внутренних пресных водоемов значение 0 PSU является адекватным. Если у вас есть точные данные о солености водоема или она может быть непосредственно измерена, вы также можете задать ее в поле 7. Значение солености используется для рассчета скорости звука.

- Снятая галочка 7 **Auto speed of sound** и соответствующее поле 9 **Speed of sound, m/s** позволяет задать приложению известное значение скорости звука. Если у вас есть прямое измерение, в противном случае рекомендуется установить галочку 7.

- Поле 10 **Water temperature, °C** позволяет указать приложению релевантное значение температуры воды. Температура воды участвтует в расчете скорости звука, если галочка 9 **Auto speed of sound** установлена. Если вы измеряете температуру воды, рекомендуется брать пробы на некотором расстоянии от поверхности.

- Поле 11 **Track points to show** указывает приложению сколько точек (вычисленных положений) для каждого трека следует одновременно отображать. Данный параметр влияет только на отображение. Приложение дополнительно хранит все полученные точки, которые затем могут быть сохранены.

- Поле 12 **Radial error threshold, m** указывает порог радиальной ошибки (значения функции невязки в конце решения навигационной задачи), выше которого вычисленное местоположение считается ошибочным и отбрасывается. Рекомендуется задавать это значение в пределах 10 метров.

- Копки 14 **OK** и **CANCEL** отвечают за сохранение настроек и отмену изменений соответственно. После изменения и сохранения настроек приложение запросит перезапуск для того, чтобы настройки вступили в силу.

Рассмотрим теперь главное окно приложения. Его общий вид с указанием основных элементов управления представлен на рисунке ниже.

| |
| :---: |
| ![1](/documentation/uTrackDiver_mainwindow_1.png)|
| Основные элементы главного окна приложения |
| _1 - Главная панель инструментов, 2 - Панель инструментов карты, 3 - Поле карты, 4 - Поле дополнительной информации, 5 - Поле журнала, 6 - Панель инструментов списка водолазов, 7 - Список водолазов, 8 - Поле обозначений треков, 9 - Линейка масштаба, 10 - Панель переключателей отображаемых параметров водолазов, 11 - Строка статуса_ |

- 1 - Главная панель инструментов располагается в верхней части окна и содержит следующие элементы:
  - Кнопка **🔌 LINK** - управляет соединением с приемным радиомодемом и внешним GNSS-приемником. 
  - Кнопка **⚙ SETTINGS** - вызов редактора настроек. Данная кнопка недоступна при включенном соединении или при проигрывании файла журнала
  - Меню **📖 LOG** - содержит функции для работы с файлами журналов
    - Пункт **👀 View current** - открыть текущий файл журнала в приложении, ассоциированном с расширением 'log' (как правило это Notepad)
    - Пункт **▶ Playback...** - выбор файла журнала для воспроизведения в реальном масштабе времени. Данная функция позволяет практически полностью восстановить ход проведенных работ и, к примеру, восстановить трек, который не был сохранен.
    - Пункт **🧹 Remove empty entries** - очистка директории LOG в папке приложения: будут удалены все файлы журналов, размером менее 2 килобайт и все пустые папки
    - Пункт **🗜 Archive all entries...** - упаковка всей папки с файлами журналов в Zip-архив.
    - Пункт **🗑 Clear all** - удаление всех файлов журналов приложения. **Будьте внимательны! Все файлы будут удалены без возможности восстановления!!!**
    - Пункт **🧹+🗜+🗑 Do them all...** - Удаление всех пустых папок, файлов журналов меньше 2 килобайт, упаковка остальных файлов журналов в Zip-архим и удаление оригиналов в папке LOG приложения.
  - Меню **🛠 UTILS** - содержит дополнительные функции
    - Подменю **🗺 TRACKS** - функции для работы с треками
      - Пункт **💾 Export...** - сохранение треков в одном из поддерживаемых форматов через системный диалог
      - Пункт **🗑 Clear** - очистка треков, содержащихся в памяти приложения
  - Поле ввода и кнопка **📝 ADD NOTE** служат для ввода комментариев в файл журнала. Вы можете просто набирать текстовый комментарий и нажимать клавишу **Enter** независимо от того, на каком элементе управления находится фокус. Комментарии сохраняются с временной меткой, и в дальнейшем, при проигрывании файла журнала комментарии будут отображаться в соответствующий момент времени. Данная функция позволяет быстро сохранить какие-либо текстовые заметки о ходе работы.
  - Кнопка **ℹ INFO** - вызывает диалог с информацией о приложении и ссылками на дополнительную информацию по системе.

- 2 - Панель инструментов карты располагается под главной панелью инструментов слева и содержит следующие элементы:
  - Кнопка **⛯** - включение/отключение отображения базовых точек (буев). Иногда может потребоваться отключить отображение положения буев на карте, чтобы увеличить масштаб и иметь возможность рассмотреть треки движения водолазов более детально. Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **📜** - включение/отключение отображения текстового поля журнала (5). Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **⋮** - включение/отключение отображения 'легенды' - списка обозначения треков (8). Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **📑** - включение/отключение отображения поля комментариев (NOTES). Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **👽** - включение/отключение отображения поля дополнительной информации (4). Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **⎙** - служит для сохранения скриншота главного окна приложения. Скриншоты сохраняются в директории **SCREENSHOTS** в папке приложения. Имя последнего сохраненного скриншота отображается в строке статуса (11).
  - Кнопка **♻ RESET VIEW** позволяет сбросить текущий вид и отображаемые треки.
- 3 - Поле карты - служит для отображения треков движения водолазов, положения буев на карте-подложке, а также:
  - вертикальной линейки масштаба (9)
  - журнала приложения (5). В этом поле снизу вверх отображаются последние 4 строки журнала приложения.
  - легенды (8). Легенда дает соответствие цвету и размеру точек и наименованию трека. 
  - комментариев. Для создания комментариев о ходе работы налету, оператору достаточно просто набрать их на клавиатуре, при этом набранный текст будет отображаться в поле ввода на главной панели инструментов. По нажатии клавиши 'Enter' текст сохранится в журнал и будет отображен справа в поле карты (если соотствующий переключатель **'📑'** на панели инструментов карты находится в активном состоянии).
  - дополнительной навигационной информации (4).
- 3 - Панель карты предназначена для отображения карты, местоположений буев, вычисленных местоположений водолазов и некоторой дополнительной информации
- 4 - Поле дополнительной информации располагается в левой верхней части панели карты и служит для отображения дополнительной информации. Отображение этого поля может переключаться при помощи кнопки **👽** на панели инструментов карты (2). Каждый параметр отображается в отдельной строке, начинающейся с трехбуквенного идентификатора параметра и двоеточия, затем отображается значение параметра и единицы измерения. Время в формате (MM:SS), отображаемое рядом с параметром, показывает как давно значение параметра было обновлено. Ниже в таблице представлен список всех возможных идентификаторов и их описание:

| Идентификатор | Описание | Единицы измерения | Диапазон | 
| :--- | :--- | :--- | :--- |
| CRS | Курс по данным внешнего GNSS | ° | 0 .. 360 |
| SPD | Скорость по данным внешнего GNSS | km/h (m/s) | >= 0 | 
| LAT | Широта по данным внешнего GNSS | ° | -90 .. 90 |
| LON | Долгота по данным внешнего GNSS  | ° | -180 .. 180 |
| STY | Значение солености (из настроек или из базы данных) | PSU | 0 .. 40 |
| WTM | Занчение температуры воды (из настроек) | °C | -10 .. +40 |
| SOS | Значение скорости звука (из настроек или вычисленное) | m/s | 1300 .. 1600 |
| B1V | Напряжение встроенного АКБ буя №1 | V | 10 .. 13 |
| B2V | Напряжение встроенного АКБ буя №2 | V | 10 .. 13 |
| B3V | Напряжение встроенного АКБ буя №3 | V | 10 .. 13 |
| B4V | Напряжение встроенного АКБ буя №4 | V | 10 .. 13 |
| B1M | Уровень сигнала на буе №1 | dB | 14 .. 36 |
| B2M | Уровень сигнала на буе №2 | dB | 14 .. 36 |
| B3M | Уровень сигнала на буе №3 | dB | 14 .. 36 |
| B4M | Уровень сигнала на буе №4 | dB | 14 .. 36 |

- 5 - Поле журнала располагается в нижней части панели карты и отображает последние 4 строки журнала приложения. Видимость этого поля переключается кнопкой **📜** на панели инструментов карты (2).
- 6 - Панель инструментов списка водолазов **DIVERS** расположена над списком водолазов в левой части главного окна приложения. Панель содержит следующие элементы:
  - Кнопка **🎢** - сортировка списка водолазов по номеру.
  - Кнопка **▼** - свернуть все элементы списка.
  - Кнопка **▲** - развернуть все элементы списка.
- 7 - Список водолазов **DIVERS** расположен в левой части главного окна приложения. Список имеет древовидную структуру, узлы верхнего уровня имеются в формате **Diver #N**, где N - это идентификатор водолаза, который задается в настройках водолазной станции связи [RedPhone-DX](https://docs.unavlab.com/documentation/RU/RedPhone/RedPhone_DX_Specification_ru.html) (настройка **RWLT Diver's ID**, за более подробной информацией обратитесь к [инструкции по эксплуатации водолазных станций RedPhone-DX](https://docs.unavlab.com/documentation/RU/RedPhone/RedPhone_DX_Users_Manual_ru.html)). Дочерние узлы содержат известную системе информацию о данном водолазе. Каждый отдельный параметр представлен строчкой, которая начинается с идентификатора параметра, через двоеточие следует значение параметра. Если значение данного параметра было обновлено более 3-х секунд назад, то в скобках указывается время, прошедшее с момента обновления параметра в формате (MM:SS). Ниже представлен список возможных параметров:

| Идентификатор | Описание | Единицы измерения | Диапазон | 
| :--- | :--- | :--- | :--- |
| LAT | Вычисленная широта | ° | -90 .. 90 |
| LON | Вычисленная долгота | ° | -180 .. 180 |
| RER | Радиальная ошибка | м | 0 .. 99 |
| DOP | Геометрический фактор снижения точности | - | - |
| TBA | Качество взаимного расположения позиционируемого объекта и опорных точек | - | - |
| DST | Дистанция до водолаза от положения по данным внешнего GNSS | м | 0 .. 1500 |
| AZM | Направление (курс) на водолаза из положения по данным внешнего GNSS | ° | 0 .. 360 |
| RAZ | Обратное направление (курс) от водолаза на положение по данным внешнего GNSS | ° | 0 .. 360 |

Наиболее важными параметрами здесь являются **AZM**, **DST** и **RAZ**: по азимуту и дистанции оператор всегда может понять где относительно него располагается тот или иной водолаз, а параметр **RAZ** он может сообщить водолазу по голосовой связи, для того, чтобы тот, придерживаясь данного курса, смог осуществить привод.

Отображение различных параметров переключается кнопками на панели (10). Следует понимать, что параметры, связанные с взаимным расположением водолаза и надводного пункта (дальность, прямой и обратный курс) могут быть определены только при наличии внешнего источника навигационных данных - внешнего GNSS-приемника, задающего системе местоположение надводного пункта слежения за водолазами или при включенной настройке **Base 1 as AUX GNSS** - когда все параметры определяются относительно буя №1.

- 8 - Поле легенды. Отображается в правом верхнем углу поля карты. В нем отображется список треков с примерами точек треков.
- 9 - Линейка масштаба отображается в нижнем правом углу поля карты и показывает масштаб карты в метрах.
- 10 - Панель переключателей отображаемых параметров водолазов расположена под списком водолазов и переключает видимость параметров в списке:
  - Кнопка **DST** - включает/выключает отображение дистанции до водолаза. Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **AZM** - включает/выключает отображение направления **на** водолаза. Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **RAZ** - включает/выключает отображение направления **от** водолаза на положение согласно внешнему GNSS-приемнику. Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **LOC** - включает/выключает отображение местоположения водолаза (широты и долготы). Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **RER** - включает/выключает отображение радиальной ошибки - значения функции невязки, на котором закончилось решение задачи об определении местоположения водолаза. Изменение состояния этой кнопки автоматически сохраняется и воспроизводится при проигрывании файлов журнала.
  - Кнопка **DOP** - включает/отключает отображение параметров **DOP** и **TBA**.
- 11 - Строка статуса. В строке отображаются статусы портов радиомодема и внешнего источника навигационных данных (внешнего GNSS-приемника), имя последнего сохраненного скриншота или Zip-архива, в который были упакованы файлы журнала.


#### 2.2.1.2. Взаимодействие с системой

Определение местоположения водолазов, оснащенных водолазными станциями беспроводной голосовой связи [RedPhone-DX](https://docs.unavlab.com/documentation/RU/RedPhone/RedPhone_DX_Specification_ru.html) возможно тогда, когда соблюдаются следующие условия (подразумевается, что станции правильно сконфигурированы для работы с системой RWLT, а на водоеме установлены навигационные буи):

- на всех буях есть прием GNSS, а на пульте оператора есть прием радиосигналов от всех буев. Т.е. в приложении отображаются положения всех четырех буев;
- специальный навигационный сигнал, воспроизводимый водолазной станцией после завершения водолазом голосовой передачи (отпускании кнопки **PTT**), принимается всеми четырьмя буями системы **RWLT**;
- сигналы от разных водолазов не накладываются друг на друга, и между сигналами от разных водолазов есть временной промежуток не менее 2-х секунд;

Следует помнить о факторах, снижающих эффективность работы системы:
- гидрологические условия: шум природный и техногенный может ухудшать и полностью исключать нормальную работу системы; неблагоприятный подводный ландшафт и донная растительность могут способствовать возникновению акустического затенения и т.п.
- выход водолазов за пределы навигационной базы (фигуры, образуемой буями на водной поверхности): наиболее устойчивая работа системы достигается внутри навигационной базы. В некотором приближении взаимное расположение водолаза и навигационной базы оценивается параметрами **DOP** и **TBA**. Положение в непосредственной близости от одного из буев или прямо за ним также является неблагоприятным.
- крупные суда, особенно с большой осадкой, могут препятствовать прохождению акустического сигнала.

### 2.2.2. Конфигурация с маяком-пингером

**ДАННЫЙ РАЗДЕЛ НАХОДИТСЯ В РАЗРАБОТКЕ**

## 2.3. По завершении работ

**Навигационные буи** должны быть:
- сняты с якорей;
- выключены;
- очищены от загрязнений (ил, грязь, водоросли и тп);
- опреснены без погружения верхней части, если работа проводилась не в пресной воде;
- перед помещением в транспортировочный кейс протерты мягкой тканью от влаги;

Не допускается:
- Хранение в неопресненном виде;
- Хранение буев вместе с влажными якорными веревками;
- Развешивание буев для просушки за грузонесущие проушины;

**Маяк-пингер** должен быть:
- демонтирован с носителя;
- промыт от загрязнений (ил, грязь, водоросли и тп);
- опреснен, если работа проводилась не в пресной воде;
- аккуратно протерт мягкой тканью и просушен на воздухе в течение не менее 30 минут;

Не допускается:
- механическое воздействие на отверстие датчика давления;
- хранение с присутствием влаги (особенно морской);
- замерзание воды в отверстии датчика давления;

**Водолазные станции беспроводной голосовой связи**  
По завершении работ не требуют каких-либо дополнительных манипуляций и отключается автоматически в воздушной среде. Перед укладкой в транспортировочную тару необходимо выполнить промывку и/или опреснение в пресной воде с последующем обтиранием впитывающей тканью и просушкой не менее 30 минут на воздухе.

Для дополнительной и актуальной информации обратитесь к [Инструкции по эксплуатации водолазных станций беспроводной голосовой связи]().

<div style="page-break-after: always;"></div>

## 3. Обязательства и отказ от ответственности
### 3.1. Условия замены и бесплатного гарантийного обслуживания
Гарантия производителя распространяется только на заводские дефекты, выявивщиеся при эксплуатации устройства в соответствие с настоящим руководством в течении гарантийного срока (2 года с момента покупки).  

Производитель гарантирует бесплатный ремонт или замену неисправного оборудования из комплекта поставки, вышедшего из строя по причине заводского дефекта.  

К основаниям для отказа от бесплатного гарантийного обслуживания, бесплатного ремонта и замены относятся:
- любые **механические повреждения** оборудования из комплекта поставки, в т.ч. нарушение изоляции проводов и кабелей;
- любые **повреждения, вызванные воздействием влаги и загрязнений**, вследствие неправильной эксплуатации оборудования из комплекта поставки;
- любые **электрические повреждения**, вызванные **использованием некомплектных аксессуаров** (зарядного устройства), применением некачественных и/или вышедших из строя аккумуляторов; к некомплектным не отностятся аксессуары, поставленные производителем или его представителем взамен неисправных или утраченых;
- любые **следы самостоятельного ремонта и/или вскрытия** оборудования из комплекта поставки.

<div style="page-break-after: always;"></div>

### 3.2. Ограничение ответственности производителя

_____________

_**ЛЮБАЯ ИЗ ЧАСТЕЙ КОМПЛЕКТА ПОСТАВКИ В ОТДЕЛЬНОСТИ И В СОСТАВЕ СИСТЕМЫ, ИМЕНУЕМЫЕ ДАЛЕЕ "ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ":**_

_**- НЕ РАЗРАБАТЫВАЛОСЬ КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ТЕСТИРОВАЛОСЬ, КАК СРЕДСТВО СПАСЕНИЯ**_  
_**- НЕ ЯВЛЯЕТСЯ СРЕДСТВОМ СПАСЕНИЯ**_  
_**- ПРОИЗВОДИТЕЛЬ ЗАЯВЛЯЕТ, ЧТО ПОСТАВЛЯЕМОЕ ОБОРУДОВАНИЕ БЕЗОПАСНО ПРИ ЭКСПЛУАТАЦИИ СОГЛАСНО НАСТОЯЩЕЙ ИНСТРУКЦИИ И НЕ ОТВЕЧАЕТ ЗА ЛЮБЫЕ ПОСЛЕДСТВИЯ ИСПОЛЬЗОВАНИЯ ПОСТАВЛЯЕМОГО ОБОРУДОВАНИЯ**_

______________

_**ПРОИЗВОДИТЕЛЬ ГАРАНТИРУЕТ, ЧТО ГИДРОАКУСТИЧЕСКАЯ ТРЕКИНГОВАЯ СИСТЕМА RWLT (ДАЛЕЕ - СИСТЕМА):**_  
_**- ПРЕДНАЗНАЧЕНА ТОЛЬКО ДЛЯ РАБОТЫ С МАЯКАМИ-ПИНГЕРАМИ ИЛИ ВОДОЛАЗНЫМИ СТАНЦИЯМИ СВЯЗИ, РАССЧИТАНЫМИ НА СОВМЕСТНУЮ РАБОТУ С СИСТЕМОЙ**_  
_**- КОНСТРУКТИВНО НЕ МОЖЕТ БЫТЬ ИСПОЛЬЗОВАНА ДЛЯ СЛЕЖЕНИЯ ЗА ОБЪЕКТАМИ, НЕ ОСНАЩЕННЫМИ МАЯКАМИ-ПИНГЕРАМИ ИЛИ ВОДОЛАЗНЫМИ СТАНЦИЯМИ СВЯЗИ, НЕ РАССЧИТАНЫМИ НА СОВМЕСТНУЮ РАБОТУ С СИСТЕМОЙ**_  
_**- СОДЕРЖИТ ТОЛЬКО ГРАЖДАНСКИЕ И НЕ ПОДЛЕЖАЩИЕ ЛИЦЕНЗИРОВАНИЮ РАДИОЧАСТОТНЫЕ МОДУЛИ: GNSS-ПРИЕМНИКИ И РАДИОМОДЕМЫ**_  
_**ВЫШЕУКАЗАННЫЕ ОГРАНИЧЕНИЯ НЕ МОГУТ БЫТЬ СНЯТЫ НИКАКИМИ МАНИПУЛЯЦИЯМИ С НАСТРОЙКАМИ И/ИЛИ ОРГАНАМИ УПРАВЛЕНИЯ ПРИБОРОВ СИСТЕМЫ И/ИЛИ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ПРЕДНАЗНАЧЕННОГО ДЛЯ РАБОТЫ С СИСТЕМОЙ**_

______________





[Вернуться к содержанию](#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)




