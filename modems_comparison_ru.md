[Главная](/README_RU) ❯ [Гидроакустические модемы](/underwater_acoustic_modems_ru) ❯ **Таблица сравнения гидроакустических модемов**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/ed467b08-2db4-4997-97c5-9cdc2b30b19f) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Сравнение гидроакустических модемов |

<div style="page-break-after: always;"></div>

## Таблица сравнения гидроакустических модемов

|  | [uSwitch](/documentation/RU/uSwitch/uSwitch_Specification_ru.md) | [uWave](/documentation/RU/uWAVE/uWAVE_Specification_ru.md) | [uWave Max OEM](/documentation/RU/uWAVE/uWAVE_Max_OEM_Specification_ru.md) | [uWave Max](/documentation/RU/uWAVE/uWAVE_Max_Specification_ru.md) | [uWave USBL Modem](/documentation/RU/uWAVE/uWAVE_USBL_Modem_Specification_ru.md) | 
| :--- | :---: | :---: | :---: | :---: | :---: | 
| | ![image](https://github.com/user-attachments/assets/7ec2e40f-854d-4fee-96d5-8fc714a8de52) | ![](/documentation/RT_1_332820_1.png) | ![](/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](/documentation/def_modem_black.png) | ![](/documentation/zima_b.png) |
| Текущий статус | **Поставляется** | **Поставляется** | **Поставляется** | **Поставляется** | **Поставляется** |
| Максимальная дальность связи, м | 300<sup>[1](#footnote1) | 1000<sup>[1](#footnote1)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> |
| Скорость передачи данных, бит/с | 32 | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> |
| Габариты, мм | 100 x 19 х 25 (плата) <br/> Ф41 x 45 (антенна)  | **Ф41 x 45** | 80 х 43 х 29 (плата) <br/> Ф64 x 62 (антенна) |  Ф64 x 62 | Ф64 х 128 |
| Вес (сухой), г | 30 (плата) <br/> 150 (антенна) | **160** | 54 (плата) <br/> 360 (aнтенна) | 360 | 440 |
| Максимальная рабочая глубина, м | 400<sup>[4](#footnote4)</sup> | 300 | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> | 300 | 300 |
| Напряжение питания<sup>[6](#footnote6)</sup>, В |  7 .. 13 | 5 .. 12 | 5 .. 12 | 5 .. 12 | 5 .. 12 |
| Энергопотребление (RX/TX), Вт | 0.36/24 | **0.33/6** | 0.33/15 | 0.33/15 | 0.33/15 |
| Максимальное акустическое давление (в полосе), дБ re 1 мкПа @ 1 м | 165 | 169 | 175 | 175 | 175 |
| Интерфейс подключения | UART | UART | UART | UART | UART |
| Кодовое разделение абонентов | **✘** | **✓** | **✓** | **✓** | **✓** |
| Логическая адресация | **✘** | **✓** | **✓** | **✓** | **✓** |
| Пакетный режим с гарантированной доставкой | **✘** | **✓** | **✓** | **✓** | **✓** |
| Функция измерения времени распространения | **✓** | **✓** | **✓** | **✓** | **✓** |
| Модуль измерения напряжения питания | **✘** | **✓** | **✓** | **✓** | **✘** |
| Датчик глубины/температуры | **✘** | **✓** | **✘** | **✓** | **✓** |
| Двухосевой инклинометр | **✘** | **✘** | **✘** | **✘** | **✓** |
| Определение горизонтального угла прихода сигнала | **✘** | **✘** | **✘** | **✘** | **✓** |

________________
<a name="footnote1"><sup>1</sup></a> Параметр, определяющий максимальную дальность, на которой возможен прием сигнала, исходя из электроакустических параметров передатчика и приемника, пространственного убывания интенсивности звуковой энергии, затухания в среде и уровня гидроакустических помех.   
<a name="footnote2"><sup>2</sup></a> При работе [uWave Max OEM](/documentation/RU/uWAVE/uWAVE_Max_OEM_Specification_ru.md), [uWave Max](/documentation/RU/uWAVE/uWAVE_Max_Specification_ru.md) и [uWave USBL Modem](/documentation/RU/uWAVE/uWAVE_USBL_Modem_Specification_ru.md) в любых сочетаниях. Максимальная дальность связи со стандартными модемами [uWave](uWAVE_Specification_ru.md) составляет 1000 метров. Параметр указан для стандартного скоростного режима - 78 бит/с.  
<a name="footnote3"><sup>3</sup></a> Стандартный скоростной режим 78 бит/с обеспечивает максимальную дальность связи и помехоустойчивость. Другие режимы обеспечиваются [перепрошивкой устройств](/documentation/RU/uWAVE/uWAVE_FW_Updating_ru.md).  
<a name="footnote4"><sup>4</sup></a> Максимальная глубина определяется антенной. Печатная плата модема должна располагаться в нормобарическом корпусе пользователя.  
<a name="footnote5"><sup>5</sup></a> Рабочая глубина 1000 метров обеспечивается при работе с антенной [RT-1.524525-1-FF](/documentation/RU/Transducers/RT_1_524525_1_FF_Specification_ru).  
<a name="footnote6"><sup>6</sup></a> Максимальная мощность и дальность связи обеспечивается при напряжении питания 12 В.   
