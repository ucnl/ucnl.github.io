[Главная](/README_RU) ❯ [Голосовая подводная связь (водолазная телефония)](/underwater_wireless_voice_systems_ru) ❯ **Спецификация устройства: RedPhone-DX**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![RedPhone-DX](/documentation/redphone_dx_qr_ru.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **RedPhone-DX** <br/> Водолазная станция беспроводной голосовой связи <br/> Спецификация устройства |


## ОСОБЕННОСТИ

* **Совместима с большинством подобных устройств (OTS, Oceanreef, etc.)**
* **Полностью литой неразборный и необслуживаемый полиуретановый корпус**
* **Встроенная функция трекинга водолаза<sup>[1](#footnote1)</sup>**
* **Дальность связи до 1000<sup>[2](#footnote2)</sup> м**
* **До 30 часов работы в режиме приема**
* **Автоматически включается при погружении в воду**
* **Встроенный детектор речи / автоматический сквелч**

## ОПИСАНИЕ

Беспроводная телефонная водолазная станция связи **RedPhone-DX** обеспечивает передачу голосовых сообщений между водолазами и/или от водолаза на надводный пункт. Устройство поддерживает стандартые диапазоны частот и совместимо с большинством подобных систем. Встроенная функция пингера навигационной системы [RWLT](/documentation/RU/RWLT/RWLT_DataBrief_ru) позволяет фиксировать географическое положение водолаза по завершении им голосовой передачи. 
В качестве тангенты может применяться [uPress](https://docs.unavlab.com/documentation/RU/Accessories/uPress_Specification_ru.html), не содержащая корродирующих элементов.

<div style="page-break-after: always;"></div>

## ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ

| ПАРАМЕТР | ЗНАЧЕНИЕ |
| :--- | :--- |
| ГАБАРИТЫ<sup>[3](#footnote3)</sup> (д х ш х в) | 106 x 95 x 55 мм |
| ВЕС<sup>[4](#footnote4)</sup> (сухой) | 0.6 кг |
| МАКСИМАЛЬНАЯ ГЛУБИНА ПОГРУЖЕНИЯ | 100 м |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ АКУСТИЧЕСКОЙ СВЯЗИ<sup>[2](#footnote2)</sup> | 1000 м |
| МАКСИМАЛЬНОЕ АКУСТИЧЕСКОЕ ДАВЛЕНИЕ | 150 дБ re 1 мкПа @ 1 м |
| ПОЛОСА ГОЛОСОВОГО СИГНАЛА<sup>[5](#footnote5)</sup> | 300 .. 4300 Гц |
| ЧИСЛО ПОДДЕРЖИВАЕМЫХ КАНАЛОВ | 8 |
| МАКСИМАЛЬНОЕ ВРЕМЯ АВТОНОМНОЙ РАБОТЫ В РЕЖИМЕ ПРИЕМА<sup>[6](#footnote6)</sup> | до 20 часов |
| МАКСИМАЛЬНОЕ ВРЕМЯ АВТОНОМНОЙ РАБОТЫ В СМЕШАННОМ РЕЖИМЕ (20%)<sup>[6](#footnote6),[7](#footnote7)</sup> | до 8 часов |
| МАКСИМАЛЬНОЕ ВРЕМЯ АВТОНОМНОЙ РАБОТЫ В СМЕШАННОМ РЕЖИМЕ (50%)<sup>[6](#footnote6),[8](#footnote8)</sup> | до 2.5 часов |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | 0 .. 50° С |
| ПРИМЕНЯЕМЫЕ ИСТОЧНИКИ ПИТАНИЯ<sup>[9](#footnote9)</sup> | 28 Вт\*ч, LiFePO4, до 3000 циклов заряд-разряд |
| ПЕРЕКЛЮЧЕНИЕ КАНАЛОВ СВЯЗИ | Беспроводное, при помощи [радиодонгла](RedPhone_RF_Dongle_Specification_ru.md) |
| МАТЕРИАЛ КОРПУСА | Полиуретан |
| МАТЕРИАЛ ИЗОЛЯЦИИ КАБЕЛЕЙ | Полиуретан |
| НЕСУЩАЯ ЧАСТОТА НАВИГАЦИОННОГО СИГНАЛА | 20050 Гц |
| ТИП МОДУЛЯЦИИ НАВИГАЦИОННОГО СИГНАЛА | BPSK |
| ДЛИТЕЛЬНОСТЬ НАВИГАЦИОННОГО СИГНАЛА | 200 мсек |

<div style="page-break-after: always;"></div>

## КАНАЛЫ И ПОЛОСЫ ЧАСТОТ

| НОМЕР КАНАЛА | НЕСУЩАЯ ЧАСТОТА, Гц | БОКОВАЯ ПОЛОСА | ПОЛОСА ЧАСТОТ, Гц |
| :---: | :---: | :---: | :---: |
| 1 | 32768 | Нижняя | 28468 .. 32468 |
| 2 | 32768 | Верхняя | 33068 .. 37068 |
| 3 | 31250 | Нижняя | 26950 .. 30950 |
| 4 | 31250 | Верхняя | 31550 .. 35550 |
| 5 | 28500 | Нижняя | 24200 .. 28200 |
| 6 | 28500 | Верхняя | 28800 .. 32800 |
| 7 | 25000 | Нижняя | 20700 .. 24700 |
| 8 | 25000 | Верхняя | 25300 .. 29300 |

## ДОПОЛНИТЕЛЬНО
[Паспорт безопасности для встроенного источника питания, Material Safety Data Sheet (MSDS)](/documentation/RU/Misc/RedPhone_DX_MSDS_ru)

________________
<a name="footnote1"><sup>1</sup></a> Функция обеспечивается буями навигационной системы [RWLT](/documentation/RU/RWLT/RWLT_DataBrief_ru).  
<a name="footnote2"><sup>2</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде и уровня гидроакустических помех.  
<a name="footnote3"><sup>3</sup></a> С учетом гидроакустической антенны.  
<a name="footnote4"><sup>4</sup></a> С тангентой и разъемом для масок, в зависимости от разъема значение может отличаться на вес разъема.  
<a name="footnote5"><sup>5</sup></a> Фактический диапазон воспроизводимых частот зависит от характеристик применяемой гарнитуры.  
<a name="footnote6"><sup>6</sup></a> С новым, полностью заряженным АКБ, при температуре окружающей среды 20° С.  
<a name="footnote7"><sup>7</sup></a> В режиме 2 минуты передачи 8 минут приема.  
<a name="footnote8"><sup>8</sup></a> В режиме 5 минут передачи 5 минут приема.  
<a name="footnote9"><sup>9</sup></a> Аккумулятор встроен в прибор.

<div style="page-break-after: always;"></div>
