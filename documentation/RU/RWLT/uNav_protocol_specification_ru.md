[Главная](/README_RU) ❯ [Гидроакустические навигационные и трекинговые системы](/navigation_and_tracking_systems_ru) ❯ **Описание протокола сопряжения: uNav**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uNav** - навигационный приемник для трекинговых систем RWLT/WAYU <br/> Протокол информационного сопряжения |
  
# uNav <br/> протокол информационного сопряжения

<div style="page-break-after: always;"></div>

## Содержание
- [0. История версий и список изменений](#0-%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9-%D0%B8-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9)
- [1. Введение](#1-%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5)  
  - [1.1. Протокол физического уровня](#11-%D0%BF%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB-%D1%84%D0%B8%D0%B7%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F)
  - [1.2. Стандарт протокола диалогового уровня NMEA0183](#12-%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB%D0%B0-%D0%B4%D0%B8%D0%B0%D0%BB%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-nmea0183)
- [2. Система команд UNA]()  
   
- [3. Приложения](#5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
 
 - [5.2. Готовые рецепты](#52-%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D1%8B%D0%B5-%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B)
   
<div style="page-break-after: always;"></div>

## 0. История версий и список изменений
[История версий и изменений](uNav_version_history_ru.md)

<div style="page-break-after: always;"></div>

## 1. Введение
### 1.1. Протокол физического уровня
   
Устройства uNav поддерживают информационное сопряжение при помощи последовательного интерфейса.

Настройки порта подключения по умолчанию<sup>[1](#footnote1)</sup>:  
> _Baudrate: 9600 bit/s_  
> _Data bits: 8_  
> _Stop bits: 1_  
> _Parity: No_  
> _Hardware flow control: No_  


### 1.2. Стандарт протокола диалогового уровня NMEA0183
Стандарт NMEA0183 описывает формат текстовых (ASCII) сообщений диалогового уровня.  

Пример сообщения:  **`$PUNA0,1,0*hh<СR><LF>`**  

Основные элементы посылки (сообщения, sentence) NMEА0183:
* '$' - начало сообщения,
* 'P' - Proprietary, проприетарный код
* 'UNA' - трехбуквенный идентификатор
* '0' - идентификатор сообщения
* ',' - запятая (разделитель параметров)  
* '*' - разделитель контрольной суммы
* 'hh' - контрольная сумма в шестнадцатеричном формате (например FF, 01). Рассчитывается как побитовый XOR всех байт между '$' и '*'.
* \<CR\>\<LF\> - конец сообщения (перевод строки)
________
<a name="footnote1"><sup>1</sup> Указанные параметры могут быть изменены по запросу</a>

<div style="page-break-after: always;"></div>

## 2. Система команд UWV для ГА модемов uWAVE
Префикс **D2H** в наименовании сообщений означает, что оно передается от устройства (Device) к управляющей системе (Host).
Префикс **H2D** в наименовании сообщений означает, что оно передается от управляющей системы (Host) к устройству (Device).

### 2.1. IC_D2H_ACK
Сообщение IC_D2H_ACK - реакция устройства на поступивший от управляющей системы запрос  

Формат сообщения: **`$PUWV0,x,x*hh<CR><LF>`**  

| Поле/Параметр |	Описание |
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV	| UWV |
| 0	| Идентификатор сообщения |
| cmdID	| Идентификатор обрабатываемой команды (на которую устройство отреагировало) |
| errCode	| Error code \([см. 4.1](#41-%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA)\) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.2. IC_H2D_SETTINGS_WRITE
Запись новых настроек
 
Формат сообщения: **`$PUWV1,x,x,x.x,x,x,x.x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 1 | Идентификатор сообщения |
| txChID | идентификатор канала передачи |
| rxChID | идентификатор канала приема |
| STY | Соленость, PSU |
| isCmdMode | '0' - командный режим управляется service pin, '1' - командный режим по умолчанию |
| isACKOnTXFinished | ‘1’ - модем будет посылать сообщение [IC_D2H_ACK](#21-ic_d2h_ack) с параметром [LOC_ACK_TX_FINISHED](#41-error-codes) при завершении отправки сообщения (при опустошении буфера акустического передатчика), ‘0’ - модем не будет оповещать о завершении передачи |
| gravityAcc | Ускорение свободного падения (для более точного определения глубины), в м/с<sup>2</sup> в диапазоне от 9.77 до 9.84 |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.3. IC_H2D_RC_REQUEST
Кодовый запрос удаленному абоненту

Формат сообщения: **`$PUWV2,x,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 2 | Идентификатор сообщения | 
| txChID | Идентификатор канала передачи |
| rxChID | Идентификатор канала приема (ожидания ответа) |
| rcCmdID | Command ID \([см. 4.2](#42-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B)\) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.4. IC_D2H_RC_RESPONSE
Принята реакция удаленного абонента на кодовый запрос  

Формат сообщения: **`$PUWV3,x,x.x,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 3 | Идентификатор сообщения |
| txChID | Идентификатор канала передачи, в котором был выполнен запрос |
| rcCmdID | Идентификатор команды \([см. 4.2](#42-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B)\) |
| propTime | Время распространения сигнала, сек |
| MSR | Mean main lobe to side-peak ratio, дБ |
| Value | Запрошенное значение | 
| Azimuth | Горизонтальный угол прихода сигнала \(Только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md), иначе поле пустое\) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.5. IC_D2H_RC_TIMEOUT
Удаленный абонент не ответил за запрос

Формат сообщения: **`$PUWV4,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 4 | Идентификатор сообщения |
| txChID | Идентификатор канала передачи, в котором был выполнен запрос |
| rcCmdID | Идентификатор команды \([см. 4.2](#42-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B)\) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.6. IC_D2H_RC_ASYNC_IN
Входящее  кодовое сообщение от удаленного абонента  

Формат сообщения: **`$PUWV5,x,x.x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 5 | Идентификатор сообщения |
| rcCmdID | Command ID \([see 4.2](#42-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B)\) |
| MSR | Mean main lobe to side-peak ratio, дБ |
| Azimuth | Горизонтальный угол прихода сигнала \(Только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md), иначе поле пустое\) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.7. IC_H2D_AMB_DTA_CFG
Настройка выдачи параметров среды и питания
Данное сообщение конфигурирует вывод модемом показаний встроенного датчика давления/температуры и напряжения питания. После настройки 
модем может передавать эти показания при помощи сообщения [IC_D2H_AMB_DTA](#28-ic_h2d_amb_dta)

Формат сообщения: **`$PUWV6,x,x,x,x,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 6 | Идентификатор сообщения |
| IsSaveToFlash | 1 - сохранить настройки во Flash, 0 - не сохранять |
| PeriodMs | Период выдачи информации в миллисекундах, <br/>0 - вывод показаний отключен, <br/> 1 - тандемный вывод (сразу после любого исходящего сообщения от устройства управляющей системе) <br/> или значение от 500 до 60000 (0.5 - 60 секунд) |
| IsPressure | 1 - выводить показания датчика давления, 0 - не выводить |
| IsTemperature | 1 - выводить показания датчика температуры, 0 - не выводить |
| IsDepth | 1 - выводить глубину, 0 - не выводить |
| IsVCC | 1 - выводить напряжение питания, 0 - не выводить |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

Если параметр **PeriodMs** равен нулю, но как минимум один из признаков **IsPressure/IsTemperature/IsDepth/IsVCC** установлен, устройство однократно передаст указанные параметры.

### 2.8. IC_H2D_AMB_DTA
Параметры среды и питания.  

Формат сообщения: **`$PUWV7,x.x,x.x,x.x,x.x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
7 | Идентификатор сообщенияentifier |
Pressure_mBar | давление в мБар |
Temperature_C | температура в °C |
Depth_m | Глубина в метрах |
VCC_V | Напряжение питания в вольтах |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.9. IC_H2D_DINFO_GET
Получить информацию об устройстве. На это сообщение устройство отвечает сообщением [IC_D2H_DINFO](#210-ic_d2h_dinfo).

Формат сообщения: **`$PUWV?,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
? | Идентификатор сообщения |
Reserved | Reserved |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.10. IC_D2H_DINFO
Информация об устройстве  

Формат сообщения: **`$PUWV!,c--c,с--с,x,c--c,x,x.x,x,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| ! | Идентификатор сообщения |
| Serial number | Серийный номер устройства |
| System moniker | Наименование системы |
| System version | Версия |
| Core moniker | Подсистема связи |
| Core version | Версия подсистемы связи |
| acBaudrate | Скорость передачи данных, бод |
| rxChID | Идентификатор канала приема |
| txChID | Идентификатор канала передачи |
| maxChannels | Общее число доступных идентификаторов каналов |
| styPSU | Соленость, PSU (задется пользователем) |
| isPTS | ‘1’ - устройство имеет встроенный датчик давления/температуры, ‘0’ - не имеет |
| isCmdMode | ‘1’ - командный режим по умолчанию, ‘0’ - командный режим управляется по сервисной жиле. |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.11. IC_H2D_PT_SETTINGS_READ
Прочитать настройки пакетного режима. На этот запрос устройство отвечает сообщением [IC_D2H_PT_SETTINGS](#212-ic_d2h_pt_settings).

Формат сообщения: **`$PUWVD,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| D | Идентификатор сообщения |
| reserved | Поле должно содержать '0' |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.12. IC_D2H_PT_SETTINGS
Настройки пакетного режима.

Формат сообщения: **`$PUWVE,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| E | Идентификатор сообщения |
| isPTMode | '0' - пакетный режим неактивен, '1' - пакетный режим активен. **Начиная с версии прошивки 1.20 не используется - для передачи в пакетном режиме модему достаточно быть в командном режиме, а прием пакетного сообщения возможнен независимо от режима, в котором находится модем** |
| ptLocalAddress | Адрес локального модема в пакетном режиме, 0 .. 254 |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.13. IC_H2D_PT_SETTINGS_WRITE
Настройки пакетного режима. На этот запрос устройство отвечает сообщением [IC_D2H_PT_SETTINGS](#212-ic_d2h_pt_settings).

Формат сообщения: **`$PUWVF,x,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| F | Идентификатор сообщения |
| isSaveInFlash | '0' - не сохранять настройки во флеш, '1' - сохранять настройки во флеш |
| isPTMode | '0' - пакетный режим неактивен, '1' - пакетный режим активен. **Начиная с версии прошивки 1.20 не используется - для передачи в пакетном режиме модему достаточно быть в командном режиме, а прием пакетного сообщения возможнен независимо от режима, в котором находится модем** |
| ptLocalAddress | Адрес локального модема в пакетном режиме 0 .. 254 |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.14. IC_H2D_PT_SEND
Послать пакет данных.

Формат сообщения: **`$PUWVG,x,x,h--h*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| G | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254, 255 - широковещательное сообщение без уведомления о получении |
| maxTries | Максимальное число попыток, 0 .. 255. Если поле пустое, то будет использовано максимальное число попыток по умолчанию - 255 |
| dataPacket | массив байт в HEX-формате с префиксом '0x', например для строки '123' 0x313233. Максимальный размер пакета 64 байта. Если поле пустое, то текущая передача будет отменена. |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.15. IC_D2H_PT_FAILED
Передача пакета данных не увенчалась успехом.

Формат сообщения: **`$PUWVH,x,x,h--h*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| H | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254 |
| maxTries | Предпринятое число попыток |
| dataPacket | Массив байт в HEX-формате с префиксом '0x', например для строки '123' 0x313233. Максимальный размер пакета 64 байта. |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.16. IC_D2H_PT_DLVRD
Пакет данных успешно передан.

Формат сообщения: **`$PUWVI,x,x,x.x,h--h*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| I | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254 |
| maxTries | Предпринятое число попыток |
| azimuth | Горизонтальный угол прихода сигнала, только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md), в остальных случаях поле пустое |
| dataPacket | Массив байт в HEX-формате с префиксом '0x', например для строки '123' 0x313233. Максимальный размер пакета 64 байта. |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.17. IC_D2H_PT_RCVD
Принят пакет данных.

Формат сообщения: **`$PUWVJ,x,x.x,,h--h*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| J | Идентификатор сообщения |
| sender_ptAddress | Адрес удаленного модема (отправителя), 0 .. 254 |
| azimuth | Горизонтальный угол прихода сигнала, только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md), в остальных случаях поле пустое |
| dataPacket | Массив байт в HEX-формате с префиксом '0x', например для строки '123' 0x313233. Максимальный размер пакета 64 байта. |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.18. IC_H2D_PT_ITG
Запрос удаленного абонента с логической адресацией.

Формат сообщения: **`$PUWVK,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| K | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254 |
| dataID | Идентификатор запрашиваемого параметра (0 - глубина, 1 - температура, 2 - напряжение питания) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.19. IC_D2H_PT_ITG_TMO 
Превышение интервала ожидания ответа на запрос с логической адресацией.

Формат сообщения: **`$PUWVL,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| L | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254 |
| dataID | Идентификатор запрошенного параметра (0 - глубина, 1 - температура, 2 - напряжение питания) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |

### 2.20. IC_D2H_PT_ITG_RESP
Ответ удаленного абонента с логической адресацией.

Формат сообщения: **`$PUWVM,x,x,x.x,x.x,x.x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| M | Идентификатор сообщения |
| target_ptAddress | Адрес удаленного модема, 0 .. 254 |
| dataID | Идентификатор запрошенного параметра (0 - глубина, 1 - температура, 2 - напряжение питания) |
| dataValue | Значение запрошенного параметра |
| pTime | Время распространения сигнала, сек |
| azimuth | Горизонтальный угол прихода сигнала, °. Только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md), в остальных случаях поле пустое |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |


### 2.21. IC_H2D_INC_DTA_CFG
> Только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md)
Настройка вывода данных о крене и дифференте.

Формат сообщения: **`$PUWV8,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 8 | Идентификатор сообщения |
| IsSaveToFlash | 1 - сохранить настройки во Flash, 0 - не сохранять |
| PeriodMs | Период выдачи информации в миллисекундах, <br/>0 - вывод показаний отключен, <br/> 1 - тандемный вывод (сразу после любого исходящего сообщения от устройства управляющей системе) <br/> или значение от 500 до 60000 (0.5 - 60 секунд) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |


### 2.22. IC_D2H_INC_DTA
> Только для устройств [uWAVE USBL](uWAVE_USBL_Modem_Specification_ru.md)
Данные о крене и дифференте.

Формат сообщения: **`$PUWV9,x.x,x.x,x.x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| 9 | Идентификатор сообщения |
| reserved | Поле зарезервировано и оставлено пустым |
| Pitch | Значение крена в градусах |
| Roll | Значение дифферента в градусах |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |


### 2.23. IC_H2D_AQPNG_SETTINGS_READ
> Поддерживается с версии 1.30

Запрос настроек режима AUTO QUERY / PINGER.

Формат сообщения: **`$PUWVN,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| N | Идентификатор сообщения |
| reserved | Поле зарезервировано и оставлено пустым |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |


### 2.24. IC_HDH_AQPNG_SETTINGS
> Поддерживается с версии 1.30
Сообщения для задания настроек режима AUTO QUERY / PINGER. Это же сообщение используется устройством для уведомления пользователя об успешном изменении настроек данного режима.

Настройка периода относится только к режиму пингер. Идентификаторы кодовых каналов приема и передачи используются только если IsPT = 0. PTTargetAddress используется только в режиме мастера и если IsPT = 1.

Формат сообщения: **`$PUWVO,x,x,x,x,x,x,x,x*hh<CR><LF>`**

| Поле/Параметр |	Описание|
| :--- | :--- |
| $	| Начало сообщения '$' |
| PUWV | UWV |
| O | Идентификатор сообщения |
| IsSaveToFlash | 1 - сохранить настройки во Flash, 0 - не сохранять |
| AQPNG_Mode | 0 - Режим неактивен, 1 - пингер, 2 - мастер (автозапрос) |
| PeriodMs | Период для режима пингера в миллисекундах, <br/> значение от 2000 до 300000 (2 секунды - 5 минут) |
| RcTxID | Идентификатор канала передачи для командного режима |
| RcRxID | Идентификатор канала приема для командного режима |
| DataID | 0 - глубина, 1 - температура, 2 - напряжение питания, 3 - все три в цикле |
| IsPT | 0 - работа в командном режиме, 1 - работа с пакетными запросами |
| PTTargetAddress | Адрес целевого абонента в пакетном режиме (для режима Мастер) |
| *	| Разделитель контрольной суммы NMEA |
| hh	| Контрольная сумма NMEA |
| \<CR\>\<LF\> | Конец сообщения |




<div style="page-break-after: always;"></div>

## 3. Режимы работы устройства

### 3.1. Режим прозрачного канала

В режиме прозрачного канала устройства не анализируют приходящие от управляющей системы данные и без изменений транслируют их в гидроакустический канал, где они могут быть приняты любым другим модемом **uWave**, ведущим прием в таком же кодовом канале, в каком производилась передача. При условии, что у принимающего модема не активирован [режим пакетной передачи](#32-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC).

<div style="page-break-after: always;"></div>

### 3.2. Командный режим
Модемы **uWave** предоставляют пользователю т.н. "прозрачный канал", когда все данные, подаваемые устройству на вход, без изменений 
и их анализа передаются в гидроакустический канал, после чего принимаются другим модемом и в неизменном виде отдаются пользователю на 
приемной стороне. В связи с этим, для того, чтобы иметь возможность производить настройку модемов, а также измерять время распространения 
до удаленных абонентов существует командный режим. Модемы анализируют входные данные только в командном режиме. Для перехода в командный 
режим, жила **SVC/CMD** должна быть притянута к +3.3 V. После этого, для выхода из командного режима жила "service" должна быть притянута 
к земле. Также командный режим может быть включен по умолчанию при помощи сообщения [IC_H2D_SETTINGS_WRITE](#22-ic_h2d_settings_write), 
когда параметр **isCmdMode = 1**, при этом, начиная с версии прошивки 1.30 жила **SVC/CMD** становится выходной цифровой линией, переходящей в высокое логическое состояние синхронно с началом излучения сигнала модемом и через 500 мс после обнаружения начала входящего сообщения. Для возврата к управлению по уровню на жиле service, также можно воспользоваться сообщением [IC_H2D_SETTINGS_WRITE](#22-ic_h2d_settings_write) с параметром **isCmdMode = 0**.

В командном режиме устройства позволяют передавать короткие кодовые запросы другим устройствам: запрашивать глубину, температуру, напряжение питания удаленного модема и передавать 8 пользовательских команд.
Кодовые запросы имеют фиксированные длины запросных и ответных сигналов, что позволяет запрашивающей системе определять время распространения (и наклонную дальность) до запрашиваемой системы. Удаленный модем принимает и обрабатывает кодовый запрос независимо от того, в каком режиме он находится, что снимает с пользовательской системы необходимость контролировать состояние удаленного модема.

> **ВНИМАНИЕ!** Жила **SVC/CMD** притягивается ТОЛЬКО к 3-5 V или земле, подключение ее к более высокому напряжению вызовет **НЕУСТРАНИМУЮ** и **НЕ ГАРАНТИЙНУЮ** поломку устройства.

> **ВНИМАНИЕ!** Перед включением устройства, жила **SVC/CMD** должна быть притянута к земле, иначе устройство войдет в режим обновления программного обеспечения.

Ниже представлены схемы включения и выключения командного режиме при помощи жилы **SVC/CMD** в случае сопряжения модема с ПК посредством преобразователя интерфейса UART-USB.

| ![uwave_usb_cmd_mode_off](/documentation/uwave_usb_cmd_mode_off.png) |
| :---: |
| Подключение модема к USB-порту ПК при помощи конвертера интерфейса. **Командный режим выключен** |

| ![uwave_usb_cmd_mode_on](/documentation/uwave_usb_cmd_mode_on.png) |
| :---: |
| Подключение модема к USB-порту ПК при помощи конвертера интерфейса. **Командный режим включен** |

<div style="page-break-after: always;"></div>

### 3.3. Пакетный режим
Пакетный режим предоставляет пользователю возможность осуществлять передачу данных пакетами размером до 64 байт с гарантированной доставкой (**ALO - at-least-once**, гарантируется, что сообщение будет передано как минимум 1 раз) и уведомлением о получении а также запросы параметров с одномременным измерением времени распространения сигнала. Так как взаимодействие модема с пользовательской системой в пакетном режиме реализовано при помощи сообщений в формате **NMEA0183**, то для работы в этом режиме и предающее и принимающее устройства должны быть переведены в [командный режим](#32-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D1%8B%D0%B9-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC).
В пакетном режиме адресуется до 255 устройств (адреса от 0 до 254, адрес 255 назначен для передачи широковещательных сообщений без уведомления).
Пользователю доступны следующие функции:  
- задание адреса локального модема  
- адресная передача пакета данных удаленному устройству  
- получение уведомления об успешной доставке пакета и число потребовавшихся попыток  
- получение уведомления об превышении интервала попыток в случае несостоявшейся передачи  
- получение входящего пакетного сообщения с адресом отправителя  
- запрос параметров удаленного абонента (глубина, температура, напряжение питания) с измерением времени распространения
- получение уведомления об превышении интервала ожидания ответа
- получение ответа удаленного абонента с запрошенным параметров и измеренным временем распространения сигнала

Для взаимодействия с модемом в пакетном режиме предназначены команды с [2.11. IC_H2D_PT_SETTINGS_READ](#211-ic_h2d_pt_settings_read) по [2.17. IC_D2H_PT_RCVD](#217-ic_d2h_pt_rcvd).

После передачи данных в пакетном режиме, отправляющий модем ожидает от адресата короткое кодовое сообщение [ACK](#42-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B), при получении такового уведомляет пользователя об успешной передаче или повторяет передачу до тех пор, пока не будет получен ответ от адресата или не будет превышено число попыток.

<div style="page-break-after: always;"></div>


## 4. Идентификаторы
### 4.1. Коды ошибок

| Ошибка | Значение | Описание |
| :--- | :--- | :--- |
| LOC_ERR_NO_ERROR | 0 | Запрос принят |
| LOC_ERR_INVALID_SYNTAX | 1 | Ошибка синтаксиса |
| LOC_ERR_UNSUPPORTED | 2 | Запрос не поддерживается |
| LOC_ERR_TRANSMITTER_BUSY | 3 | Передатчик занят |
| LOC_ERR_ARGUMENT_OUT_OF_RANGE | 4 | Указанный параметр вне допустимого диапазона |
| LOC_ERR_INVALID_OPERATION | 5 | Неверный запрос |
| LOC_ERR_UNKNOWN_FIELD_ID | 6 | Неизвестный идентификатор |
| LOC_ERR_VALUE_UNAVAILIBLE | 7 | Запрошенный параметр недоступен в данный момент |
| LOC_ERR_RECEIVER_BUSY | 8 | Приемник занят (ожидается ответ удаленной системы) |
| LOC_ERR_TX_BUFFER_OVERRUN | 9 | Буфер передатчика полон |
| LOC_ERR_CHKSUM_ERROR | 10 | Ошибка контрольной суммы |
| LOC_ACK_TX_FINISHED | 11 | Акустический передатчик закончил передачу сообщения |
| LOC_ACK_BEFORE_STANDBY | 12 | Устройство переходит в режим STAND-BY |
| LOC_ACK_AFTER_WAKEUP | 13 | Устройство вышло из режима STAND-BY |
| LOC_ERR_SVOLTAGE_TOO_HIGH | 14 | Напряжение питание слишком высоко (более 13 вольт) и усилитель мощности не будет использоваться во избежание его выхода из строя |

### 4.2 Удаленные команды  

| Команда | Значение | Описание|
| :--- | :--- | :--- |
| RC_PING | 0 | Ping |
| RC_PONG | 1 | Pong |
| RC_DPT_GET | 2 | Запрос глубины удаленного абонента |
| RC_TMP_GET | 3 | Запрос температуры Value удаленного абонента |
| RC_BAT_V_GET | 4 | Запрос напряжения питания удаленного абонента |
| RC_ERR_NSUP | 5 | Удаленная система ответила - запрос не поддерживается |
| RC_ACK | 6 | Удаленная система ответила - запрос принят |
| RC_USR_CMD_000 | 7 | Пользовательская команда |
| RC_USR_CMD_001 | 8 | Пользовательская команда |
| RC_USR_CMD_002 | 9 | Пользовательская команда |
| RC_USR_CMD_003 | 10 | Пользовательская команда |
| RC_USR_CMD_004 | 11 | Пользовательская команда |
| RC_USR_CMD_005 | 12 | Пользовательская команда |
| RC_USR_CMD_006 | 13 | Пользовательская команда |
| RC_USR_CMD_007 | 14 | Пользовательская команда |
| RC_USR_CMD_008 | 15 | Пользовательская команда |
| RC_MSG_ASYNC_IN | 16 | Входящее сообщение в режиме прозрачного канала |

<div style="page-break-after: always;"></div>

## 5. Приложения
### 5.1. Примеры работы с устройством в командном режиме
В приведенных примерах, перед командами, посылаемыми **в** устройство, располагается префикс `<<`, а перед командами, приходящими **из**
устройства - префикс `>>`.     
Подразумевается, что устройство подключено к управляющей системе и включен командный режим.  

#### 5.1.2. Пример 1 - запрос информации об устройстве
```
<< $PUWV?,0*27<CR><LF>
```
PUWV? = [IC_H2D_DINFO_GET](#29-ic_h2d_dinfo_get)
```
>> $PUWV!,3A001E000E51363437333330,STRONG,256,uWAVE [JULY],257,78.27,0,0,28,0.0,1,0*18<CR><LF>
```
PUWV! = [IC_D2H_DINFO](#210-ic_d2h_dinfo)  
3A001E000E51363437333330 = серийный номер,  
STRONG = наименование системы  
256 = 0x0100 версия системы 01.00  
uWAVE \[JULY\] = наименование подсистемы связи,  
257 = 0x0101 версия подсистемы связи 01.01  
78.27 = скорость передачи данных по гидроакустическому каналу, бит/с  
0 = идентификатор канала передачи  
0 = идентификатор канала приема  
28 = общее число доступных кодовых каналов  
0.0 = соленость, PSU  
1 = встроенный датчик давления/температуры присутствует и исправен  
0 = командный режим по умолчанию отключен  


#### 5.1.3. Пример 2 - кодовый запрос удаленному абоненту
```
<< $PUWV2,0,0,2*28
```
PUWV2 = [IC_H2D_RC_REQUEST](#23-ic_h2d_rc_request)  
0 = Идентификатор канала передачи (идентификатор канала приема адресата)  
0 = Идентификатор канала приема (идентификатор канала передачи адресата)  
2 = Request ID = [RC_DPT_GET](#42-remote-commands)  
```
>> $PUWV0,2,0*36
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
2 = ACK на запрос PUWV2  
0 = Error code = [LOC_ERR_NO_ERROR](#41-%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA)  
```
>> $PUWV3,0,2,0.00020,22.75,0.000,*1B
```
PUWV3 = [IC_D2H_RC_RESPONSE](#24-ic_d2h_rc_response)  
0 = идентификатор канала приема удаленного абонента  
2 = Request ID = [RC_DPT_GET](#42-remote-commands)  
0.00020 = время распространения сигнала, сек  
22.75 = MSR (Main lobe to side-peak ratio), дБ  
0.000 = принятое значение (в данном случае глубина удаленного модема в метрах)  
```
<< $PUWV2,0,0,3*29
```
PUWV2 = [IC_H2D_RC_REQUEST](#23-ic_h2d_rc_request)  
0 = Идентификатор канала передачи (идентификатор канала приема адресата)  
0 = Идентификатор канала приема (идентификатор канала передачи адресата)   
3 = Request ID = [RC_TMP_GET](#42-remote-commands)  
```
>> $PUWV0,2,0*36
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
2 = ACK на запрос PUWV2  
0 = Error code = [LOC_ERR_NO_ERROR](#41-%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA)  
```
>> $PUWV3,0,3,0.00030,26.31,27.300,*29
```
PUWV3 = [IC_D2H_RC_RESPONSE](#24-ic_d2h_rc_response)  
0 = идентификатор канала приема удаленного абонента  
2 = Request ID = [RC_TMP_GET](#42-remote-commands)  
0.00030 = вермя распространения, сек  
26.31 = MSR (Main lobe to side-peak ratio), дБ  
27.300 = принятое значение (в данном случае температура удаленного абонента в °C)  

#### 5.1.4. Пример 3 - установка выдачи данных о параметрах окружающей среды
```
<< $PUWV6,0,1000,1,1,1,1*03<CR><LF>
```
PUWV6 = [IC_H2D_AMB_DTA_CFG](#27-ic_h2d_amb_dta_cfg)  
0 = isSaveToFlash = false  
1000 = передавать данные каждый 1000 мсек  
1 = isPressure = true  
1 = isTemperature = true  
1 = isDepth = true  
1 = isVCC = true  
```
>> $PUWV0,6,0*32<CR><LF>
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
6 = ACK на запрос PUWV6  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
```
>> $PUWV7,1025.2,29.9,-0.014,5.0*18
. . .
>> $PUWV7,1026.3,29.9,-0.002,5.0*1D
```
PUWV7 = [IC_D2H_AMB_DTA](#28-ic_h2d_amb_dta)   
1026.3 = давление, мБар  
29.9 = температура, °C  
-0.002 = глубина, m  
5.0 = напряжение питания, V  
```
<< $PUWV6,0,0,0,0,0,0*32
```
PUWV6 = [IC_H2D_AMB_DTA_CFG](#27-ic_h2d_amb_dta_cfg)  
0 = isSaveToFlash = false  
0 = не передавать данные
0 = isPressure = false  
0 = isTemperature = false  
0 = isDepth = false  
0 = isVCC = false  
```
>> $PUWV0,6,0*32
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
6 = ACK на запрос PUWV6  
0 = Код ошибки = [LOC_ERR_NO_ERROR](#41-%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA)  

#### 5.1.5. Пример 4 - Включение пакетного режима

```
<< $PUWVF,1,1,0*5E<CR><LF>
```
PUWVF = [IC_H2D_PT_SETTINGS_WRITE](#213-ic_h2d_pt_settings_write)  
1 = Сохранить настройки во флеш = true  
1 = Пакетный режим включен = true  
0 = Адрес локального устройства = 0  
```
>> $PUWVE,1,0*40
```
PUWVE = [IC_D2H_PT_SETTINGS](#212-ic_d2h_pt_settings)  
1 = Пакетный режим включен  
0 = Адрес локального устройства  

#### 5.1.6. Пример 5 - Передача в пакетном режиме и получени уведомления о доставке

```
<< $PUWVG,0,8,0x313233*2C
```
PUWVG = [IC_H2D_PT_SEND](#214-ic_h2d_pt_send)  
0 = Целевой адрес  
8 = Максимальное число попыток  
0x313233 = массив их трех байт ('123')  
```
>> $PUWV0,G,0*43
```
PUWV0 = [IC_D2H_ACK](#21-ic_d2h_ack)  
G = ACK на запрос PUWVG  
0 = Error code = [LOC_ERR_NO_ERROR](#41-error-codes)  
```
$PUWVI,0,1,,0x313233*07
```  
PUWVI = [IC_D2H_PT_DLVRD](#216-ic_d2h_pt_dlvrd)  
0 = адресат  
1 = число предпринятых попыток  
пустое поле - устройство не поддерживает определение горизонтального угла прихода сигнала  
0x313233 = массив их трех байт ('123')  

### 5.2. Готовые рецепты
Подразумевается, что устройство подключено к управляющей системе и включен командный режим. Сообщения можно скопировать и послать в модем, дополнив символами <CR><LF> (New line, Hex: 0x0D 0x0A, Dec: 13 10, или \\r\\n).

#### Рецепт 1
Задание основных настроек по умолчанию
- Идентификаторы каналов приема и передачи - **0**
- Командный режим по умолчанию **выключен**
- ACK по завершению передачи **выключен**
- Соленость **0.0 PSU**
- Ускорение свободного падения **9.8067 м/с<sup>2</sup>**

```
$PUWV1,0,0,0.,0,0,9.8067*35
```

#### Рецепт 2
Отключение автоматической передачи всех параметров среды и напряжения питания с сохранением настроек во флеш.

```
$PUWV6,0,0,0,0,0,0*32
```

#### Рецепт 3
Включение автоматической передачи всех параметров среды и напряжения питания 1 раз в секунду без сохранения этих настроек во флеш.

```
$PUWV6,0,1000,1,1,1,1*03
```

#### Рецепт 4
Включение автоматической передачи всех параметров среды и напряжения питания после любого исходящего от модема сообщения без сохранения настроек во флеш.

```
$PUWV6,0,1,1,1,1,1*33
```

#### Рецепт 5
Включение автоматической передачи только глубины локального модема после любого исходящего от модема сообщения без сохранения настроек во флеш.

```
$PUWV6,0,1,0,0,1,0*32
```

#### Рецепт 6
Запросить глубину удаленного модема с идентификаторами приемного и передающего каналов 0.

```
$PUWV2,0,0,2*28
```
________

<div style="page-break-after: always;"></div>
  
[Вернуться к содержанию](#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5)
