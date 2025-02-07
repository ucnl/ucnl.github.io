[Main](/../../) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **Modems comparison table**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) |  |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Modems comparison table |

<div style="page-break-after: always;"></div>

## Modems comparison table

|  | [uSwitch](/documentation/EN/uSwitch/uSwitch_Specification_en.md) | [uWave](/documentation/EN/uWAVE/uWAVE_Specification_en.md) | [uWave Max OEM](/documentation/EN/uWAVE/uWAVE_Max_OEM_Specification_en.md) | [uWave Max](/documentation/EN/uWAVE/uWAVE_Max_Specification_en.md) | [uWave USBL Modem](/documentation/EN/uWAVE/uWAVE_USBL_Modem_Specification_en.md) | 
| :--- | :---: | :---: | :---: | :---: | :---: | 
|      | ![image](https://github.com/user-attachments/assets/7ec2e40f-854d-4fee-96d5-8fc714a8de52) | ![](/documentation/RT_1_332820_1.png) | ![](/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](/documentation/def_modem_black.png) | ![](/documentation/zima_b.png) |
| Status | **Active** | **Active** | **Active** | **Active** | **Active** |
| Max. acoustic range, m | 300<sup>[1](#footnote1) | 1000<sup>[1](#footnote1)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> |
| Baudrate, bps | 32 | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> |
| Dimensions, mm | 100 x 19 х 25 (плата) <br/> Ф41 x 45 (антенна)  | **Ф41 x 45** | 80 х 43 х 29 (плата) <br/> Ф64 x 62 (антенна) |  Ф64 x 62 | Ф64 х 128 |
| Weight (dry), g | 30 (плата) <br/> 150 (антенна) | **160** | 54 (плата) <br/> 360 (aнтенна) | 360 | 440 |
| Depth rating, m | 400<sup>[4](#footnote4)</sup> | 300 | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> | 300 | 300 |
| Supply voltage<sup>[6](#footnote6)</sup>, В |  7 .. 13 | 5 .. 12 | 5 .. 12 | 5 .. 12 | 5 .. 12 |
| Power consumption (RX/TX), W | 0.36/24 | **0.33/6** | 0.33/15 | 0.33/15 | 0.33/15 |
| Acoustic source level (in band), dB re 1 uPa @ 1 m | 165 | 169 | 175 | 175 | 175 |
| Interface | UART | UART | UART | UART | UART |
| Supscribers code division | **✘** | **✓** | **✓** | **✓** | **✓** |
| Logical addressing | **✘** | **✓** | **✓** | **✓** | **✓** |
| Packet mode with guaranteed delivery | **✘** | **✓** | **✓** | **✓** | **✓** |
| Propagation time measurement | **✓** | **✓** | **✓** | **✓** | **✓** |
| Supply voltage measurement circuit | **✘** | **✓** | **✓** | **✓** | **✘** |
| Depth/Temperature sensor | **✘** | **✓** | **✘** | **✓** | **✓** |
| Dual axis inclinometer | **✘** | **✘** | **✘** | **✘** | **✓** |
| Determining the horizontal angle of arrival | **✘** | **✘** | **✘** | **✘** | **✓** |

________________

<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electro-acoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and acoustic noise level.  
<a name="footnote2"><sup>2</sup></a> When communicating [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) in any combination. The maximum communication range with standard modems [uWave](uWAVE_Specification_en.md) is 1000 meters. The parameter is specified for the standard speed mode - 78 bps.  
<a name="footnote3"><sup>3</sup></a> Standard speed mode 78 bps provides maximum communication range and noise immunity. Other modes are available by [re-flashing devices](uWAVE_FW_Updating_en.md).  
<a name="footnote4"><sup>4</sup></a> The maximum depth is determined by the transducer. The modem's printed circuit board must be located in the user's normobaric enclosure.  
<a name="footnote5"><sup>5</sup></a> Working depth of 1000 meters is ensured when working with [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en) transducer.   
<a name="footnote6"><sup>6</sup></a> Maximum power and communication range is provided at a supply voltage of 12 V.

<div style="page-break-after: always;"></div>
