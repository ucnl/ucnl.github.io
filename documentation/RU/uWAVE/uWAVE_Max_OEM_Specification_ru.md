| ![logo](/documentation/sm_logo.png) | ![logo](/documentation/utro_pcb_rt_1_524525_1_2.png) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWAVE Max OEM** - Гидроакустический модем <br/> Спецификация устройства |

## КЛЮЧЕВЫЕ ОСОБЕННОСТИ

* **Предельно малые габариты и масса**
* **Надежная передача данных со скоростью 78 бит/с**
* **Дальность связи до 3000<sup>[1](#footnote1),[2](#footnote2)</sup> м**
* **Кодовое разделение абонентов**
* **Измерение времени распространения сигнала**
* **Высоконадежная технология цифровой широкополосной гидроакустической связи**
* **Низкое энергопотребление (Rx/Tx) 0.33/15 Вт**
* **Открытый протокол сопряжения**
* **Пакетный режим с гарантированной доставкой (ALO - At-least-once)**

## ОПИСАНИЕ

**uWAVE Max OEM** базируется на платформе **UTRO** и поставляется в виде модуля печатной платы с гидроакустической антенной [RT-1.524525-1](/documentation/RU/Transducers/RT-1.524525-1_specification_ru.md).

При помощи модемов **uWAVE Max OEM** пользователь может:
* передавать произвольные цифровые данные между устройствами [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_ru.md), **uWAVE Max** и [uWAVE](uWAVE_Specification_ru.md) в любой комбинации;
* передавать до 9 кодовых пользовательских команд телеуправления;
* запрашивать у удаленных устройств [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_ru.md), **uWAVE Max** и [uWAVE](uWAVE_Specification_ru.md) их глубину, температуру и напряжение питания;
* передавать данные в пакетном режиме с уведомлением о доставке (ALO - At-least-once)
* измерять собственное напряжение питания;

Устройства [семейства uWAVE](uWAVE_Family_ru.md) используют простой открытый [NMEA-подобный протокол настройки](uWAVE_Protocol_Specification_ru.md), а поставляемая библиотека 
[**uWAVELib**](https://github.com/ucnl/uWAVELib) с открытым исходным кодом позволяет осуществлять максимально быструю и простую 
интеграцию устройств в пользовательские решения.

Отличия от базовой версии [uWAVE](/documentation/RU/uWAVE/uWAVE_Specification_ru.md):
* Увеличенная до 3000<sup>[1](#footnote1),[2](#footnote2)</sup> м максимальная дальность связи
* OEM-исполнение
* Отсутствие встроенного датчика глубины/температуры

## ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ

| ПАРАМЕТР | ЗНАЧЕНИЕ |
| :--- | :--- |
| ГАБАРИТЫ (Плата, д х ш х в) | 80 х 43 х 29 мм |
| ВЕС | 54 г |
| ГАБАРИТЫ (Антенна, Ф х h | 64 x 62 мм |
| ВЕС (Антенна, сухой) | 360 г |
| МАКСИМАЛЬНАЯ ГЛУБИНА (Антенна) | 400 м |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ АКУСТИЧЕСКОЙ СВЯЗИ<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000 м |
| СКОРОСТЬ ПЕРЕДАЧИ ДАННЫХ | 78 бит/с |
| ЭНЕРГОПОТРЕБЛЕНИЕ Rx/Tx | 0.33/15 Вт |
| НАПРЯЖЕНИЕ ПИТАНИЯ | 5-13 В |
| НАПРЯЖЕНИЕ ЛИНИИ ДАННЫХ | 0 .. 3.3 В |
| ПОЛОСА ЧАСТОТ | 10 .. 30 кГц |
| МАКСИМАЛЬНОЕ АКУСТИЧЕСКОЕ ДАВЛЕНИЕ (В полосе) | 175 дБ re 1 мкПа @ 1 м |
| BIT ERROR RATE | 10<sup>-6</sup> |
| SNR<sup>[3](#footnote3)</sup></sup> | -2 дБ |
| МАКСИМАЛЬНАЯ ОТНОСИТЕЛЬНАЯ СКОРОСТЬ | +/- 1 м/с |
| ВРЕМЯ СТАРТА | 100 мсек |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | -5 .. 50 °C |
| ИНТЕРФЕЙС СОПРЯЖЕНИЯ<sup>[4](#footnote4)</sup> | UART 9600 бит/с |
| ПРОТОКОЛ СОПРЯЖЕНИЯ | NMEA 0183 [PUWV](uWAVE_Protocol_Specification_ru.md) |
| ДЛИНА КАБЕЛЯ АНТЕННЫ<sup>[4](#footnote4)</sup> | 1 м |
| СХЕМА РАЗДЕЛЕНИЯ АБОНЕНТОВ | 20 кодовых каналов |
| РАЗМЕР БУФЕРА ПЕРЕДАТЧИКА | 127 байт |
| КОМАНДНЫЙ РЕЖИМ| 16 предустановленных сообщений (9 для пользовательских приложений) |
| РАЗРЕШЕНИЕ ПРИ ИЗМЕРЕНИИ ВРЕМЕНИ РАСПРОСТРАНЕНИЯ СИГНАЛА | 0.0001 c |
| ПАКЕТНЫЙ РЕЖИМ | 254 адреса с уведомлением о получении, широковещательные сообщения, размер пакета до 64 байт |
  
________________
<a name="footnote1"><sup>1</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде и уровня гидроакустических помех.  
<a name="footnote2"><sup>2</sup></a> При работе с другим **uWAVE Max/uWAVE Max OEM** или при работе с модемами [uWAVE USBL Modem](uWAVE_USBL_Modem_Specification_ru.md). Максимальная дальность связи со стандартными модемами [uWAVE](uWAVE_Specification_ru.md) составляет 1000 метров.  
<a name="footnote3"><sup>3</sup></a> Значение получено без учета эффекта многолучевого распространения в лабораторном статическом эксперименте.  
<a name="footnote4"><sup>4</sup></a> Значение может быть изменено по запросу.  