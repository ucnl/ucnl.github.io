<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Инструкция по обновлению прошивки модемов uWave  |

<div style="page-break-after: always;"></div>

# Обновление внутреннего программного обеспечения модемов uWave

> Мы постоянно работаем над улучшением продуктов, учитываем мнения и пожелания пользователей и устраняем обнаруженные недоработки. С историей версий, добавлением  новых функций и исправлениями ошибок вы можете ознакомиться на странице [uWave: История версий и изменений](uWAVE_version_history_ru.md).

## Шаг 1 

Скачайте демо-приложение [uWave Host](https://github.com/ucnl/uWAVE_Host/releases/download/1.0/uWAVE_Host.zip) для работы с модемами uWave. Приложение работает на ПК под управлением ОС Windiws (Версии 8 и выше).

Скачайте утилиту для обновления прошивки [UCNL_FW_Update](https://github.com/ucnl/UCNL_FW_Update/releases/download/1.1/UCNL_FW_Update.zip). Утилита работает на ПК под управлением OC Windows (Версии 8 и выше).

Оба приложения не требуют установки. Просто распакуйте скачанные архивы в удобные для вас папки.

## Шаг 2
Подключите ваш модем к ПК посредством преобразователя UART<->USB. Назначение жил кабеля по цветам представлено ниже:  

![uWAVE_wiring_diagram_en](/documentation/uWAVE_wiring_diagram_ru.png)

Напряжение на линиях данных **НЕ ДОЛЖНО** превышать 3.3 V. 
Для первоначального переключения модема в командный режим необходимо предусмотреть возможность подтяжки жилы SVC/CMD к напряжению 3.3 или 5 Вольт. Это удобно сделать при помощи джампера, например так:

![uwave_and_uart_usb_converter](/documentation/uwave_and_uart_usb_converter.png)

![uwave_and_uart_usb_converter2](/documentation/uwave_and_uart_usb_converter2.png)

При таком подключении командный режим включается путем установки джампера.

## Шаг 3
Убедитесь, что командый режим не включен (джампер снят) и подключите модем к USB-порту ПК при помощи преобразователя:

![uwave_and_uart_usb_converter3](/documentation/uwave_and_uart_usb_converter3.png)

## Шаг 4
Запустите приложение uWave Host и нажмите кнопку "SETTINGS" на верхней панели инструментов. В открывшемся окне настроек
выберите нужный порт и нажмите кнопку "OK". 

![uwave_host1](/documentation/uwave_host1.png)

Приложение предложит перезапуститься для применения новых настроек. 












