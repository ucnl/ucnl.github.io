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

| № | Наименование парамера  | Тип | Единицы измерения | Диапазон значений | Описание |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | stPressure_mBar | f32 | мБар | 0 .. 30 | Давление по встроенному датчику |
| 1 | stDepth_m | f32 | м | 0 .. 300 | Глубина погружения устройства |



### 3.2. AZMREM - данные маяка-ответчика

@AZMREM,rem_addr,SRange_m,Azimuth_deg,PTime_s,MSR_dB,age,Depth_m,age,SRangeProjection_m,age,ADistance_m,age,AAzimuth_deg,age,Elevation_deg,age,VCC_V,age,WaterTemp_C,age,Lat_deg,Lat_deg,age,RAzimuth_deg,age,Message,age,IsTimeout




<div style="page-break-after: always;"></div>
