[Главная](/README_RU) ❯ [Гидроакустические навигационные и трекинговые системы](/navigation_and_tracking_systems_ru) ❯ **Спецификация устройства: Zima2-B - пеленгационная антенна**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_zima_b_ant.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2-B** - станция пеленгования **Zima2 USBL** <br/> спецификация устройства |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **Предельно малые габариты и масса**
* **Дальность связи до 3000<sup>[1](#footnote1)</sup> метров**
* **Высоконадежная цифровая гидроакустическая связь устойчивая к многолучевому распространению**
* **Кодовое разделение абонентов - до 16 маяков-ответчиков**
* **Низкое энергопотребление (Rx/Tx) 0.33/25 Вт**
* **Патентованная<sup>[*](#footnote_a1)</sup> технология одновременной навигации**
* **Встроенный датчик давления/температуры**
* **Патентованная<sup>[**](#footnote_a2)</sup> моноблочная конструкция**

## ОПИСАНИЕ

**Zima2-B** - пеленгационная станция ультракороткобазисной системы [Zima2 USBL](Zima2_DataBrief_ru.md).

Устройство использует сигнал фиксированной длины с кодовым разделением для обеспечения определения направления, дальности и глубины 
маяков-ответчиков [Zima2-R](Zima2R_Specification_ru.md).

При использовании внешнего приемника **GNSS** и Компаса устройство позволяет определять абсолютные координаты маяков-ответчиков.
Обеспечивается последовательная работа до 16 маяков-ответчиков.
 
Идеальное решение для определения направления и дистанции до **ТНПА**, **АНПА** и **водолазов**.

Предельно малый размер, низкое энергопотребление и простота использования делают пеленгационную систему [Zima2 USBL](Zima2_DataBrief_ru.md) идеальным решением для работы с автономными и телеуправляемыми аппаратами, а также определения относительного местоположения водолазов.

_________
<a name="footnote_a1"><sup>*</sup></a> Патент RU156897U1.  
<a name="footnote_a2"><sup>**</sup></a> Патент RU2659299C1.  

<div style="page-break-after: always;"></div>

## ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ

| ПАРАМЕТР | ЗНАЧЕНИЕ |
| :--- | :--- |
| ГАБАРИТЫ (Ф х h) | 64 x 128 мм |
| ВЕС (сухой)<sup>[2](#footnote2)</sup> | 0.44 кг |
| МАКСИМАЛЬНАЯ ГЛУБИНА | 40 м |
| НОМИНАЛЬНАЯ ПОГРЕШНОСТЬ ПО ГЛУБИНЕ | 0.1 м |
| МАКСИМАЛЬНАЯ АКУСТИЧЕСКАЯ ДАЛЬНОСТЬ СВЯЗИ<sup>[1](#footnote1)</sup> | 3000 м |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ ГОРИЗОНТАЛЬНОГО УГЛА ПРИХОДА СИНГНАЛА<sup>[3](#footnote3)</sup> | 1° |
| МАКСИМАЛЬНЫЙ КОМПЕНСИРУЕМЫЙ ВСТРОЕННЫМ ИНКЛИНОМЕТРОМ НАКЛОН ПРИБОРА ОТНОСИТЕЛЬНО ВЕРТИКАЛИ (КРЕН/ДИФФЕРЕНТ) | +/- 30° |
| РАБОЧИЙ КОНУС (ОТНОСИТЕЛЬНО ГОРИЗОНТАЛИ)<sup>[3](#footnote3)</sup> | 0 .. 85° |
| ПОЛОСА ЧАСТОТ | 10 .. 30 кГц |
| ТОЧНОСТЬ ВСТРОЕННОГО ДАТЧИКА ТЕМПЕРАТУРЫ | 0.1°С |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[2](#footnote2)</sup> | -3 дБ |
| МАКСИМАЛЬНАЯ ОТНОСИТЕЛЬНАЯ СКОРОСТЬ | +/- 2 м/с |
| ВРЕМЯ СТАРТА | 100 мсек |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | -5 .. 50 °C |
| ВРЕМЯ АВТОНОМНОЙ РАБОТЫ<sup>[4](#footnote4)</sup> ПРИ ПИТАНИИ ОТ [BAT&LINK BOX](Bat_n_link_box_Specification_ru.md) | 8 ч |
| ИНТЕРФЕЙС СОПРЯЖЕНИЯ | USB (COM) 9600 бит/с |
| ПРОТОКОЛ СОПРЯЖЕНИЯ | NMEA 0183 [PAZM](Zima2_Protocol_Specification_ru.md) |
| ДЛИНА КАБЕЛЯ<sup>[5](#footnote5)</sup> | 10 м |
| МАКСИМАЛЬНОЕ ЧИСЛО МАЯКОВ-ОТВЕТЧИКОВ | 16 |
  
________________
<a name="footnote1"><sup>1</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде и уровня гидроакустических помех.  
<a name="footnote2"><sup>2</sup></a> Без учета веса преобразователя и кабеля.  
<a name="footnote3"><sup>3</sup></a> Значение получено без учета эффекта многолучевого распространения в лабораторном статическом эксперименте.  
<a name="footnote4"><sup>4</sup></a> При режиме работы станции 1 запрос в 3 секунды.  
<a name="footnote5"><sup>5</sup></a> С учетом преобразователя интерфейса и удлиняющего кабеля до прибора [Bat&Link Box](Bat_n_link_box_Specification_ru.md). Опционально возможно увеличение до 20 метров.  

<div style="page-break-after: always;"></div>
