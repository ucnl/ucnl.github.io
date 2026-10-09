[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave: Version history & changes**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** family of underwater acoustic communication devices <br/> Version history & changes |
  
# uWave <br/> Version history & changes

<div style="page-break-after: always;"></div>

## 0. Versions

| Current firmware version | **uWave [JULY] 1.34** dated 22-NOV-2023 |
| :--- | :--- |
| | |

| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 22-NOV-2023 | System: (all) <br/> Core: uWave [JULY] v1.34 | - BUG FIX: incorrect depth sensor data after prolonged operation in some cases |
| 12-JUN-2023 | System: (all) <br/> Core: uWave [JULY] v1.33 | + 634 bit/s data rate mode <br/> - BUG FIX: fixed a bug in packet processing and the absence of a failed transmission notification in some cases |
| 18-OCT-2022 | System: (all) <br/> Core: uWave [JULY] v1.32 | - BUG FIX: fixed a bug that prevented the device from accepting packets larger than 54 bytes for transmission |
| 31-JAN-2022 | System: (all) <br/> Core: uWave [JULY] v1.31 | - BUG FIX: fixed a bug that caused a packet delivery notification to arrive together with the ACK sentence for the previous command <br/> - Firmware size reduced by almost a factor of 4 through extensive refactoring |
| 10-DEC-2021 | System: (all) <br/> Core: uWave [JULY] v1.30 | From this version onward, when IsCmdModeByDefault is enabled, the command wire becomes an output instead of an input. It carries a digital strobe signal synchronized with transmission and reception. <br/> + AUTO QUERY / PINGER mode introduced: the modem can be configured to automatically query a modem with specified channel parameters, query a specified subscriber in packet mode, or periodically transmit a signal containing its depth, temperature, supply voltage or all three parameters in turn. The signal from such a pinger can now be received by other modems (which are not issuing queries) |
| 27-SEP-2021 | System: (all) <br/> Core: uWave [JULY] v1.24 | - BUG FIX: fixed a bug that made it impossible to interrupt repeated attempts to transmit a packet message |
| 17-SEP-2021 | System: (all) <br/> Core: uWave [JULY] v1.23 | - BUG FIX: fixed a bug that could, in rare cases, cause the modem to freeze while waiting for a remote request |
| 30-AUG-2021 | System: (all), <br/> Core: uWave [JULY] v1.22 | - BUG FIX: fixed a bug that could disrupt the interface in the direction from the modem to the user when working with command requests |
| 08-JUL-2021 | System: (all), <br/> Core: uWave [JULY] v1.21 | - BUG FIX: fixed incorrect transmitter operation in transparent channel mode that could leave new data untransmitted if it arrived via UART at the end of a transmission <br/> +/- Packet mode sentence formats changed: a field for the horizontal angle of arrival added (for uWave USBL devices) <br/> + Range measurement and requests for depth, temperature and supply voltage supported within the logical addressing of packet mode |
| 28-JUN-2021 | System: (all), <br/> Core: uWave [JULY] v1.20 | + Packet mode no longer needs to be enabled separately (it is always enabled). The modem can receive packet mode messages in both transparent channel mode and command mode |
| 21-JUN-2021 | System: --- | + Alternative firmware versions with data rates of: <br/> 156 bit/s (System: Easy) <br/> 314 bit/s (System: Lite) <br/> Alternative modes tested in a real body of water at a distance of 500 m |
| 14-MAY-2021 | System: STRONG 2.0, <br/> Core: uWave [JULY] v1.10 | + Packet mode (guaranteed delivery, ALO - At-least-once, logical addressing) <br/> - Bug fixed: Tx/Rx channel identifiers in code requests |
| 21-DEC-2019 | System: STRONG 1.0, <br/> Core: uWave [JULY] v1.08 | + Gravitational acceleration setting added for more accurate depth determination |    


## 1. Features and complex issues

### 1.1. Switching to command mode and back
A change in the state of the service wire takes priority over data transmission or reception. With some models of interface converters, interference may be induced on the cable during transmission in transparent channel mode if the wire is not pulled to ground. As a result, the modem may switch to command mode during transmission, which may end data transmission prematurely. To prevent this situation, the service wire must not be left unconnected.

### 1.2. Using the same code channel for reception and transmission
Using the same code channel for reception and transmission in some small bodies of water may cause a querying modem working with short code requests to receive its own request signal reflected from the shore or other objects. This is not a modem bug or flaw, but a consequence of the laws of sound propagation in water. It is therefore recommended to use different code channels for reception and transmission.

### 1.3. 'TX Busy' error when attempting to send anything immediately after receiving a message in packet mode
When a modem receives a message in packet mode, it immediately sends a receipt notification, so its transmitter is busy. The user can enable the 'ACK On TX Finished' setting so that the modem notifies them whenever transmission has finished. Alternatively, handle this situation by waiting or retrying transmission after about 500 ms.

### 1.4. Any write to flash saves **all** current settings
The modems support several groups of settings: main settings, ambient parameter output settings, packet mode settings and auto query/pinger mode settings. Since all modem settings are stored in a shared area of nonvolatile memory, any write to flash saves the settings.

### 1.5. Code channel settings take effect after the device is restarted
If you change the code channel settings, you must restart the device for them to take effect (disconnect the power and reapply it after a couple of seconds).

## 2. Known issues

| Description | Status |
| :--- | :--- |
| The devices accept all hexadecimal values only in uppercase. This affects all commands for working with packets | Not fixed |

________  
                    
<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uWAVE/uWAVE_version_history_ru.md commit=9535c84e99f94ede412e371d082de623394e3ac9 date=2025-11-26 -->
