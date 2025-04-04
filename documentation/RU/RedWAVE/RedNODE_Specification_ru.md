[Главная](/README_RU) ❯ [Гидроакустические навигационные и трекинговые системы](/navigation_and_tracking_systems_ru) ❯ **Спецификация устройства: RedNode - Навигационный приемник для ТНПА/АНПА**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/def_modem_black.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedNode** - Универсальный навигационный приемник <br/> Спецификация устройства |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **3D-позиция в абсолютных географических координатах**
* **Эмуляция протокола простых GNSS-приемников**
* **Частота обновления 3D-позиции до 1 Гц**
* **Полностью акустически пассивное устройство**
* **Минимальные габариты и масса**
* **Одновременная работа неограниченного числа устройств<sup>[*](#footnote_a1)</sup>**
* **Надежная и помехоустойчивая технология цифровой широкополосной гидроакустической связи**
* **Патентованная<sup>[**](#footnote_a2)</sup> моноблочная конструкция**

## ОПИСАНИЕ

**[RedNWave](RedWAVE_DataBrief_ru.md)** - единственная на сегодняшний день система, созданная по запатентованной<sup>[**](#footnote_a1)</sup> технологии, реализующая т.н. "подводный GPS": в точности повторяя 
идеологию GPS и других спутниковых систем, позволяет неограниченному числу подводных объектов определять свое географическое положение 
одновременно.  
 
При поддержке четырех плавучих гидроакустических навигационных буев [RedBase](RedBASE_Specification_ru.md), в одной акватории возможна 
одновременная работа неограниченного числа устройств **RedNode** и [RedNav](RedNAV_Specification_ru.md).  

**RedNode** - универсальный навигационный приемник системы **[RedWave](RedWAVE_DataBrief_ru.md)**, принимающий гидроакустические 
навигационные сигналы от буев, определяет собственные географические координаты, которые передает по последовательному интерфейсу (**UART**)
 упрвляющей системе. При этом эмулируется формат сообщений, применяющихся в обычных GNSS-приемниках, что обеспечивает максимальную простоту 
 интеграции.
 
_________
<a name="footnote_a1"><sup>*</sup></a> Патенты US10989815B2, WO2017044012A1, EP3349040A4, RU2599902C1.  
<a name="footnote_a2"><sup>**</sup></a> Патент RU2659299C1.  

<div style="page-break-after: always;"></div>

## ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ

| ПАРАМЕТР | ЗНАЧЕНИЕ |
| :--- | :--- |
| ГАБАРИТЫ (ВЫНОСНОЙ БЛОК, Ф х h) | 64 x 62 мм |
| ВЕС (сухой) | 0.3 кг |
| НАПРЯЖЕНИЕ ПИТАНИЯ<sup>[1](#footnote1)</sup> | 12 В |
| НАПРЯЖЕНИЕ ЛИНИЙ ДАННЫХ | 3.3 В |
| ВЫХОДНОЕ СОПРОТИВЛЕНИЕ ЛИНИЙ ДАННЫХ | 1 кОм |
| ПОТРЕБЛЯЕМАЯ МОЩНОСТЬ | 0.35 Вт |
| МАКСИМАЛЬНАЯ СКОРОСТЬ ОТНОСИТЕЛЬНО БУЕВ | +/- 1.8 м/с  |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | -5 .. 50 °С |
| МАКСИМАЛЬНАЯ ГЛУБИНА ПОГРУЖЕНИЯ | 300 м |
| МАКСИМАЛЬНЫЙ РАЗМЕР РАБОЧЕЙ ОБЛАСТИ | 700 х 700 метров внутри фигуры буев |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ АКУСТИЧЕСКОЙ СВЯЗИ<sup>[2](#footnote2)</sup> | 3000 м |
| НЕСУЩАЯ ЧАСТОТА | 20100 Гц |
| ПРЕДЕЛЬНОЕ СООТНОШЕНИЕ СИГНАЛ/ШУМ В ПОЛОСЕ<sup>[3](#footnote3)</sup> | -6 дБ |
| РЕФЕРЕНСНЫЙ ЭЛЛИПСОИД | WGS-84 |
| НОМИНАЛЬНАЯ ГОРИЗОНТАЛЬНАЯ ПОГРЕШНОСТЬ<sup>[4](#footnote4)</sup> (2DRMS) | 0.84 м |
| НОМИНАЛЬНАЯ ПОГРЕШНОСТЬ ПО ГЛУБИНЕ<sup>[5](#footnote5)</sup>  | 0.1 м |
| НОМИНАЛЬНОЕ ВРЕМЯ ДО ПЕРВОГО УТОЧНЕНИЯ МЕСТОПОЛОЖЕНИЯ | 28 c |
| НОМИНАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ ГЕОГРАФИЧЕСКОГО ПОЛОЖЕНИЯ | 1 Гц |
| НОМИНАЛЬНОЕ ВРЕМЯ СТАРТА | 100 мсек |
| ТОЧНОСТЬ ВСТРОЕННОГО ДАТЧИКА ТЕМПЕРАТУРЫ | 0.1 °C |
| ДЛИНА КАБЕЛЯ | 1 м |
| ДИАМЕТР КАБЕЛЯ | 5 мм |
| ИНТЕРФЕЙС СОПРЯЖЕНИЯ<sup>[6](#footnote6)</sup> | UART, 9600  |
| ИНФОРМАЦИОННЫЙ [ПРОТОКОЛ](RedWAVE_Protocol_Specification_ru.md) | NMEA0183 (RMC, GGA, WTW) <br/> + расширенный набор сообщений |

________________
<a name="footnote1"><sup>1</sup></a> Для устройств, выпущенных после июня 2020 года. Для устройств, выпущенных ранее напряжение питания 5 В.  
<a name="footnote2"><sup>2</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из 
электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде 
и уровня гидроакустических помех.  
<a name="footnote3"><sup>3</sup></a> Величина получена без учета эффекта многолучевого распространения.  
<a name="footnote4"><sup>4</sup></a> Величина получена путем измерения в реальном водоеме при неподвижно закрепленных буях и навигационном
приемнике в течение 60 минут.  
<a name="footnote5"><sup>5</sup></a> Величина может зависеть от правильности задания пользователем солености воды, в котором производятся
работа.  
<a name="footnote6"><sup>6</sup></a> По договоренности возможна поставка с преобразователем интерфейса RS422, монтируемым на кабель в необслуживаемый уретановый корпус.  

<div style="page-break-after: always;"></div>
