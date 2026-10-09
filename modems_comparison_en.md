[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **Modems comparison table**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | ![image](https://github.com/user-attachments/assets/ed467b08-2db4-4997-97c5-9cdc2b30b19f) |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Modems comparison table |

<div style="page-break-after: always;"></div>

## Modems comparison table

|  | [uSwitch](/documentation/EN/uSwitch/uSwitch_Specification_en.md) | [uWave](/documentation/EN/uWAVE/uWAVE_Specification_en.md) | [uWave Max OEM](/documentation/EN/uWAVE/uWAVE_Max_OEM_Specification_en.md) | [uWave Max](/documentation/EN/uWAVE/uWAVE_Max_Specification_en.md) | [uWave USBL Modem](/documentation/EN/uWAVE/uWAVE_USBL_Modem_Specification_en.md) | 
| :--- | :---: | :---: | :---: | :---: | :---: | 
|      | ![image](https://github.com/user-attachments/assets/7ec2e40f-854d-4fee-96d5-8fc714a8de52) | ![](/documentation/RT_1_332820_1.png) | ![](/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](/documentation/def_modem_black.png) | ![](/documentation/zima_b.png) |
| Current status | **Available** | **Available** | **Available** | **Available** | **Available** |
| Maximum communication range, m | 300<sup>[1](#footnote1) | 1000<sup>[1](#footnote1)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> |
| Data rate, bit/s | 32 | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> |
| Dimensions, mm | 100 x 19 x 25 (PCB) <br/> Ø41 x 45 (transducer)  | **Ø41 x 45** | 80 x 43 x 29 (PCB) <br/> Ø64 x 62 (transducer) |  Ø64 x 62 | Ø64 x 128 |
| Weight (dry), g | 30 (PCB) <br/> 150 (transducer) | **160** | 54 (PCB) <br/> 360 (transducer) | 360 | 440 |
| Maximum operating depth, m | 400<sup>[4](#footnote4)</sup> | 300 | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> | 300 | 300 |
| Supply voltage<sup>[6](#footnote6)</sup>, V |  7 .. 13 | 5 .. 12 | 5 .. 12 | 5 .. 12 | 5 .. 12 |
| Power consumption (RX/TX), W | 0.36/24 | **0.33/6** | 0.33/15 | 0.33/15 | 0.33/15 |
| Maximum acoustic source level (in band), dB re 1 μPa @ 1 m | 165 | 169 | 175 | 175 | 175 |
| Connection interface | UART | UART | UART | UART | UART |
| Code division multiple access | **✘** | **✓** | **✓** | **✓** | **✓** |
| Logical addressing | **✘** | **✓** | **✓** | **✓** | **✓** |
| Packet mode with guaranteed delivery | **✘** | **✓** | **✓** | **✓** | **✓** |
| Propagation time measurement function | **✓** | **✓** | **✓** | **✓** | **✓** |
| Supply voltage measurement module | **✘** | **✓** | **✓** | **✓** | **✘** |
| Depth/temperature sensor | **✘** | **✓** | **✘** | **✓** | **✓** |
| Two-axis inclinometer | **✘** | **✘** | **✘** | **✘** | **✓** |
| Determination of the horizontal angle of arrival of the signal | **✘** | **✘** | **✘** | **✘** | **✓** |

________________

<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received based on the electroacoustic parameters of the transmitter and receiver, spatial decrease in the intensity of sound energy, attenuation in the medium and underwater acoustic noise level.   
<a name="footnote2"><sup>2</sup></a> When [uWave Max OEM](/documentation/EN/uWAVE/uWAVE_Max_OEM_Specification_en.md), [uWave Max](/documentation/EN/uWAVE/uWAVE_Max_Specification_en.md) and [uWave USBL Modem](/documentation/EN/uWAVE/uWAVE_USBL_Modem_Specification_en.md) operate in any combination. The maximum communication range with standard [uWave](documentation/EN/uWAVE/uWAVE_Specification_en.md) modems is 1000 meters. The parameter is specified for the standard data rate mode - 78 bit/s.  
<a name="footnote3"><sup>3</sup></a> The standard data rate mode of 78 bit/s provides maximum communication range and noise immunity. Other modes are available by [reflashing the devices](/documentation/EN/uWAVE/uWAVE_FW_Updating_en.md).  
<a name="footnote4"><sup>4</sup></a> The maximum depth is determined by the transducer. The modem's printed circuit board must be located in the user's one-atmosphere (normobaric) housing.  
<a name="footnote5"><sup>5</sup></a> An operating depth of 1000 meters is achieved when using the [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en) transducer.  
<a name="footnote6"><sup>6</sup></a> Maximum power and communication range are achieved at a supply voltage of 12 V.   

<!-- docs-sync: source=modems_comparison_ru.md commit=82898a3c16d443b8e4f241cb263b9c619d5d1498 date=2025-02-07 -->
