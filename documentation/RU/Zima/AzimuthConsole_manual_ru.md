[Главная](/README_RU) ❯ [Гидроакустические навигационные и трекинговые системы](/navigation_and_tracking_systems_ru) ❯ **AzimuthConsole: Руководство пользователя**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **AzimuthConsole** - Кросплатформенное приложение для работы с системой Zima2 USBL <br/> Руководство пользователя |

# AzimuthConsole <br/> Руководство пользователя

<div style="page-break-after: always;"></div>

## Содержание


<div style="page-break-after: always;"></div>

## 1. Введение

### 2. Команды управления

### 2.1. Аргументы командной строки


### 2.2. Команды терминала


### 2.3. Команды управления по протоколу UDP


## 3. Выходные данные

### 3.1. AZMLOC - локальные параметры

Сообщение передается ~1 раз в секунду, когда открыто соединение с пеленгационной антенной.

Формат сообщения:
```@AZMLOC,stPressure_mBar,stDepth_m,waterTemp_C,stPitch_deg,stRoll_deg,age,lat_deg,lon_deg,course_deg,speed_mps,age,heading_deg,age,```

| № | Наименование парамера  | Тип | Единицы измерения | Диапазон значений | Описание | Источник |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | stPressure_mBar | f32 | мБар | 0 .. 30 | Внешнее давление | Встроенный сенсор |
| 2 | stDepth_m | f32 | м | 0 .. 300 | Глубина погружения устройства | Встроенный сенсор |
| 3 | waterTemp_C | f32 | °С | -4 .. 40 | Температура окружающей среды | Встроенный сенсор |
| 4 | stPitch_deg | f32 | ° | -180 .. 180 | Крен | Встроенный сенсор |
| 5 | stRoll_deg | f32 | ° | -180 .. 180 | Дифферент | Встроенный сенсор |
| 6 | age | f32 | сек | 0 .. | Возраст предыдущих значений | Системные часы |
| 7 | lat_deg | f32 | ° | -90 .. 90 | Географическая широта | Внешний источник AUX1 или значение, заданное командой [LHOV]() |
| 8 | lon_deg | f32 | ° | -180 .. 180 | Географическая долгота | Внешний источник AUX1 или значение, заданное командой [LHOV]() |
| 9 | course_deg | f32 | ° | 0 .. 360 | Курс движения | Внешний источник AUX1 |
| 10 | speed_mps | f32 | м/c | 0 .. | Скорость движения | Внешний источник AUX1 |
| 11 | age | f32 | сек | 0 ..  | Возраст предыдущих значений | Системные часы |
| 12 | heading_deg | f32 | ° | 0 .. 360 | Азимутальный угол | Внешний источник AUX1 или AUX2 или значение, заданное командой [LHOV]() |
| 13 | age | f32 | сек | 0 .. | Возраст предыдущего значения | Системные часы |


### 3.2. AZMREM - данные маяка-ответчика

@AZMREM,rem_addr,SRange_m,Azimuth_deg,PTime_s,MSR_dB,age,Depth_m,age,SRangeProjection_m,age,ADistance_m,age,AAzimuth_deg,age,Elevation_deg,age,VCC_V,age,WaterTemp_C,age,Lat_deg,Lat_deg,age,RAzimuth_deg,age,Message,age,IsTimeout




<div style="page-break-after: always;"></div>
