[Main](/) ❯ [Underwater acoustic modems](/underwater_acoustic_modems_en) ❯ **uWave family: Modems comparison table**

<details>
  <summary><b>ℹ Recommendations for printing / saving as PDF</b></summary>
  <br>
  <ol>
    <li>Press <b>Ctrl+P</b> (macOS: <b>Cmd+P</b>)</li>
    <li>Select <b>"Save as PDF"</b> (Microsoft Print to PDF) as the printer</li>
    <li>In <b>"Pages"</b>, enter a range that excludes the first and the last page</li>
    <li>Disable <b>headers and footers</b> (title, URL, page numbers)</li>
    <li>In <b>Chrome/Edge</b>: More settings → "Margins" → <b>None</b> | in <b>Firefox</b>: "Margins & Header/Footer" → <b>None</b></li>
    <li>Click <b>Print</b> and choose where to save the PDF</li>
  </ol>
</details>

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | **uWave** family modems comparison |

<div style="page-break-after: always;"></div>

## Main device parameters

|  | [uWave](uWAVE_Specification_en.md) | [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md) | [uWave Max](uWAVE_Max_Specification_en.md) | [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) | 
| :--- | :---: | :---: | :---: | :---: | 
|      | ![](/documentation/RT_1_332820_1.png) | ![](/documentation/utro_pcb_rt_1_524525_1_2.png) | ![](/documentation/def_modem_black.png) | ![](/documentation/zima_b.png) |
| Current status | **Available** | **Available** | **Available** | **Available** |
| Maximum communication range, m | 1000<sup>[1](#footnote1)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 3000<sup>[1](#footnote1),[2](#footnote2)</sup> |
| Data rate, bit/s | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> | 78 / 156<sup>[3](#footnote3)</sup> / 314<sup>[3](#footnote3)</sup> / 634<sup>[3](#footnote3)</sup> |
| Dimensions, mm | **Ø41 x 45** | 80 x 43 x 29 (PCB) <br/> Ø64 x 62 (transducer) |  Ø64 x 62 | Ø64 x 128 |
| Weight (dry), g | **160** | 54 (PCB) <br/> 360 (transducer) | 360 | 440 |
| Maximum operating depth, m | 300 | **400 / 1000** <sup>[4](#footnote4),[5](#footnote5)</sup> | 300 | 300 |
| Power consumption (RX/TX), W | **0.33/6** | 0.33/15 | 0.33/15 | 0.33/15 |
| Maximum acoustic source level (in band), dB re 1 μPa @ 1 m | 169 | 175 | 175 | 175 |
| Supply voltage measurement module | **✓** | **✓** | **✓** | **✘** |
| Depth/temperature sensor | **✓** | **✘** | **✓** | **✓** |
| Two-axis inclinometer | **✘** | **✘** | **✘** | **✓** |
| Horizontal angle of arrival determination | **✘** | **✘** | **✘** | **✓** |

## Data rate modes

All devices of the family can work with alternative firmware supporting different data rate modes of communication.
The modes are not compatible with each other. The mode is changed by [re-flashing the device](uWAVE_FW_Updating_en.md).

|      | STRONG | EASY   | LITE   | HASTE |
| :--- | :---:  | :---:  | :---:  | :---:  |
| Data rate, bit/s | 78 | 156 | 314 | 634 |
| Maximum range, m | 1000/3000<sup>[1](#footnote1),[2](#footnote2)</sup> | 800<sup>[1](#footnote1)</sup> | 700<sup>[1](#footnote1)</sup> | 500<sup>[1](#footnote1)</sup> |
| Number of code channels | 20 | 14 | 7 | 3 |


<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> A parameter that determines the maximum range at which a signal can be received, based on the electro-acoustic parameters of the transmitter and receiver, the spatial decrease in the intensity of sound energy, attenuation in the medium and the level of acoustic noise.   
<a name="footnote2"><sup>2</sup></a> When [uWave Max OEM](uWAVE_Max_OEM_Specification_en.md), [uWave Max](uWAVE_Max_Specification_en.md) and [uWave USBL Modem](uWAVE_USBL_Modem_Specification_en.md) are operated in any combination. The maximum communication range with standard [uWave](uWAVE_Specification_en.md) modems is 1000 meters. The parameter is specified for the standard data rate mode - 78 bit/s.  
<a name="footnote3"><sup>3</sup></a> The standard data rate mode of 78 bit/s provides the maximum communication range and noise immunity. Other modes are provided by [re-flashing the devices](uWAVE_FW_Updating_en.md).  
<a name="footnote4"><sup>4</sup></a> The maximum depth is determined by the transducer. The modem's printed circuit board must be located in the user's one-atmosphere (normobaric) housing.  
<a name="footnote5"><sup>5</sup></a> Operating depth of 1000 meters is provided when working with the [RT-1.524525-1-FF](/documentation/EN/Transducers/RT_1_524525_1_FF_Specification_en) transducer.   

  
<div style="page-break-after: always;"></div>

<!-- docs-sync: source=documentation/RU/uWAVE/uWAVE_Modems_comparison_ru.md commit=5e5766e3d53d20c67730cbadfd0ac0e2d4f33a9b date=2026-06-10 -->
