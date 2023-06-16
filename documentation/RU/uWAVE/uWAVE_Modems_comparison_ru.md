[Главная](/README_RU) ❯ [Гидроакустические модемы](/underwater_acoustic_modems_ru) ❯ **Сравнительная таблица модемов семейства uWave**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Сравнение модемов семейства **uWave** |

<div style="page-break-after: always;"></div>

## Основные параметры устройств

|  | [uWave](uWAVE_Specification_ru.md) | [uWave Max OEM](uWAVE_Max_OEM_Specification_ru.md) | [uWave Max](uWAVE_Max_Specification_ru.md) | [uWave USBL Modem](uWAVE_USBL_Modem_Specification_ru.md) | 
| :--- | :---: | :---: | :---: | :---: | 
|      | ![](/documentation/RT_1_332820_1.png) | ![](/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](/documentation/def_modem_black.png) | ![](/documentation/def_zima_b_ant.png) |
| Текущий статус | **Поставляется** | **Поставляется** | **Поставляется** | **Поставляется** |
| Максимальная дальность связи, м | 1000<sup>[1](#footnote1)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> |
| Скорость передачи данных, бит/с | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> |
| Габариты, мм | **Ф41 x 45** | 80 х 43 х 29 (плата) <br/> Ф64 x 62 (антенна) |  Ф64 x 62 | Ф64 х 128 |
| Вес (сухой), г | **160** | 54 (плата) <br/> 360 (aнтенна) | 360 | 440 |
| Максимальная рабочая глубина, м | 300 | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> | 300 | 300 |
| Энергопотребление (RX/TX), Вт | **0.33/6** | 0.33/15 | 0.33/15 | 0.33/15 |
| Максимальное акустическое давление (в полосе), дБ re 1 мкПа @ 1 м | 169 | 175 | 175 | 175 |
| Модуль измерения напряжения питания | **✓** | **✓** | **✓** | **✘** |
| Датчик глубины/температуры | **✓** | **✘** | **✓** | **✓** |
| Двухосевой инклинометр | **✘** | **✘** | **✘** | **✓** |
| Определение горизонтального угла прихода сигнала | **✘** | **✘** | **✘** | **✓** |

## Скоростные режимы

Все устройства семейства могут работать с альтернативными прошивками, поддерживающие разные скоростные режимы связи.
Режимы не совместимы между собой. Смена режима производится путем [перепрошивки устройства](uWAVE_FW_Updating_ru.md).

|      | STRONG | EASY   | LITE   | HASTE |
| :--- | :---:  | :---:  | :---:  | :---:  |
| Скорость передачи, бит/с | 78 | 156 | 314 | 634 |
| Максимальная дальность, м | 1000/3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 800<sup>[1](#footnote1)</sup> | 700<sup>[1](#footnote1)</sup> | 500<sup>[1](#footnote1)</sup> |
| Число кодовых каналов | 20 | 14 | 7 | 3 |


<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде и уровня гидроакустических помех.   
<a name="footnote2"><sup>2</sup></a> При работе [uWave Max OEM](uWAVE_Max_OEM_Specification_ru.md), [uWave Max](uWAVE_Max_Specification_ru.md) и [uWave USBL Modem](uWAVE_USBL_Modem_Specification_ru.md) в любых сочетаниях. Максимальная дальность связи со стандартными модемами [uWave](uWAVE_Specification_ru.md) составляет 1000 метров. Параметр указан для стандартного скоростного режима - 78 бит/с.  
<a name="footnote3"><sup>3</sup></a> Стандартный скоростной режим 78 бит/с обеспечивает максимальную дальность связи и помехоустойчивость. Другие режимы обеспечиваются [перепрошивкой устройств](uWAVE_FW_Updating_ru.md).  
<a name="footnote4"><sup>4</sup></a> Максимальная глубина определяется антенной. Печатная плата модема должна располагаться в нормобарическом корпусе пользователя.  
<a name="footnote5"><sup>5</sup></a> Рабочая глубина 1000 метров обеспечивается при работе с антенной [RT-1.524525-1-FF](/documentation/RU/Transducers/RT_1_524525_1_FF_Specification_ru).   

  
<div style="page-break-after: always;"></div>
