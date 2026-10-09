[Main](/) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Zima2: Version history & changes**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **Zima2** USBL tracking system <br/> Version history & changes |
  
# Zima2 <br/> Version history & changes

<div style="page-break-after: always;"></div>

## 0. Versions

| Device | Current firmware version | Release date |
| :--- | :--- | :--- |
| Zima2B | 2.00 | 10-JAN-2026 |
| Zima2BK | 2.00 | 10-JAN-2026 |
| Zima2R | 2.00 | 10-JAN-2026 |
| Zima2RK | 2.00 | 10-JAN-2026 |
| Zima2uR | 2.00 | 10-JAN-2026 |

## 1. Version histories by device

### 1.1. Zima2B/2BK

| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 10-JAN-2026 | 2.00 | + isolation of uplink channels to increase reliability in challenging conditions. **This version is only partially compatible with previous ones** |
| 26-MAR-2025 | 1.34 | + supply voltage request from the beacon <br/> BUGFIX: error in the automatic speed of sound calculation in the Zima2B station |
| 26-DEC-2023 | 1.33 | + telemetry transmission. Up to 28 integer parameters can be assigned to a beacon, which the station can poll. The fact of polling is passed to the control system to implement the remote control function. For more details, see the protocol commands [H2D_CREQ](Zima2_Protocol_Specification_en.md#210-h2d_creq) and [D2D_CSET](Zima2_Protocol_Specification_en.md#211-h2d_cset) |
| 12-APR-2023 | 1.32 | BUGFIX: fixed an error that could cause the station to continue polling the beacons after the connection was closed |
| 10-DEC-2022 | 1.31 | + minor improvements |
| 10-OCT-2022 | 1.30 | |

### 1.2. Zima2R/RK

| Date | Firmware version | Description |
| :--- | :--- | :--- |
| 10-JAN-2026 | 2.00 | + isolation of uplink channels to increase reliability in challenging conditions. **This version is only partially compatible with previous ones** |
| 26-MAR-2025 | 1.34 | + supply voltage transmission on request from the station |
| 26-DEC-2023 | 1.33 | + telemetry transmission. Up to 28 integer parameters can be assigned to a beacon, which the station can poll. The fact of polling is passed to the control system to implement the remote control function. For more details, see the protocol commands [H2D_CREQ](Zima2_Protocol_Specification_en.md#210-h2d_creq) and [D2D_CSET](Zima2_Protocol_Specification_en.md#211-h2d_cset) |
| 01-MAR-2023 | 1.32 | BUGFIX: fixed an error in depth transmission over the underwater acoustic channel |
| 12-FEB-2022 | 1.31 | - minor improvements and refactoring |
| 08-JAN-2023 | 1.30 | - Zima2RK version |

________  
                    
<div style="page-break-after: always;"></div>
<!-- docs-sync: source=documentation/RU/Zima/Zima2_version_history_ru.md commit=e4a6285a78511bc1f397b9520785830197e0dfc2 date=2026-03-30 -->
