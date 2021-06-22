<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** modems comparison |

<div style="page-break-after: always;"></div>

## Main features

|  | [uWave](uWAVE_Specification_en.md) | [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) | [uWave Max](uWAVE_Max_Specification_en.md) | [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) | 
| :--- | :---: | :---: | :---: | :---: | 
|      | ![](https://raw.githubusercontent.com/ucnl/ucnl.github.io/master/documentation/RT_1_332820_1.png) | ![](https://raw.githubusercontent.com/ucnl/ucnl.github.io/master/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](https://raw.githubusercontent.com/ucnl/ucnl.github.io/master/documentation/def_modem_black.png) | ![](https://raw.githubusercontent.com/ucnl/ucnl.github.io/master/documentation/def_zima_b_ant.png) |
| Status | **Active** | **Active** | **Planned for 20222** | **Planned for 2022** |
| Max. acoustic range | 1000<sup>[1](#footnote1)</sup> m | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> m | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> m | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> m |
| Baudrate | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> bps | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> bps | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> bps | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> bps |
| Dimensions | **Ф41 x 45 mm** | 80 х 43 х 29 mm (PCB) <br/> Ф64 x 62 mm (transducer) | Ф64 x 62 mm | Ф64 х 128 mm |
| Weight (dry) | **160 g** | (PCB) 54 г <br/> (transducer) 360 g | 360 g | 440 g |
| Depth rating | 300 m | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> m | 300 m | 300 m |
| Supply voltage measurement | **✓** | **✓** | **✓** | **✓** |
| Depth/temperature sensor | **✓** | **✘** | **✓** | **✓** |
| 2-Axis inclinometer | **✘** | **✘** | **✘** | **✓** |

## Data transmission speed options

All devices of the family can work with alternative firmware supporting different communication speed modes.
The modes are not compatible with each other. Mode change is made by flashing the device.

|      | STRONG | EASY   | LITE   |
| :--- | :---:  | :---:  | :---:  |
| Baudrate, bps | 78 | 156 | 314 |
| Max. acoustic range, m | 1000/3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 700<sup>[1](#footnote1)</sup> | 500<sup>[1](#footnote1)</sup> |
| Number of code channels | 20 | 14 | 7 | 


<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> When communicating [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) in any combination. The maximum communication range with standard modems [uWave](uWAVE_Specification_ru.md) is 1000 meters. The parameter is specified for the standard speed mode - 78 bps.  
<a name="footnote3"><sup>3</sup></a> Standard speed mode 78 bps provides maximum communication range and noise immunity. Other modes are available by re-flashing devices.  
<a name="footnote4"><sup>4</sup></a> The maximum depth is determined by the transducer. The modem's printed circuit board must be located in the user's normobaric enclosure.  
<a name="footnote5"><sup>5</sup></a> Working depth of 1000 meters is ensured when working with [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en.md) transducer.   

  
<div style="page-break-after: always;"></div>
