[Main](/README.md) ❯ [Navigation & tracking systems](/navigation_and_tracking_systems_en) ❯ **Comparison table of navigation systems**

<div style="page-break-after: always;"></div>

| ![logo](/documentation/sm_logo.png) | |
| :---: | ---: |
| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | Comparison of navigation and tracking systems |

<div style="page-break-after: always;"></div>

## Comparison table of navigation systems

|  | [RedWAVE underwater GPS](/documentation/EN/RedWAVE/RedWAVE_DataBrief_en.md) | [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) | [RWLT](/documentation/EN/RWLT/RWLT_DataBrief_en.md) + <br/> [RedPhone-DX](/documentation/EN/RedPhone/RedPhone_DX_Specification_en.md) | [Zima2 USBL](/documentation/EN/Zima/Zima2_DataBrief_en.md) | [uWAVE USBL](/documentation/EN/uWAVE/uWAVE_USBL_Modem_Specification_en.md) | [WAYU](/documentation/EN/WAYU/WAYU_DataBrief_en.md) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| System configuration | LBL | LBL | LBL | USBL | USBL | LBL |
| Place of generation of navigation information | Submerged <br/> object | Surface <br/> control <br/> point | Surface <br/> control <br/> point | Surface <br/> control <br/> point | Surface <br/> control <br/> point | Surface <br/> control <br/> point |
| Number of positioning objects | **∞** | 1 | up to 255<sup>[1](#footnote1)</sup> | up to 16<sup>[1](#footnote1)</sup> | up to 20<sup>[1](#footnote1)</sup> | 1 | 
| Nominal navigation data update period | 1 sec | 2 sec | at the end of each voice message from a diver | ≥ 1<sup>[2](#footnote2)</sup> sec | ≥ 3.6<sup>[2](#footnote2)</sup> sec | 2 sec |
| Maximum work area size | 700 х 700 m  | 1500 x 1500 m | 1500 x 1500 m | Circle R = 3000 m | Circle R = 1000 m | 300 x 300 m |
| Nominal accuracy | 2DRMS 0.84 m | 2DRMS 0.84 m | 2DRMS 0.84 m | 1° (≈17 m at a distance of 1000 m) | 2° (≈35 m at a distance of 1000 m) | 2DRMS 1.48 m |
| Maximal depth | 300<sup>[3](#footnote3)</sup> m | 300/500<sup>[3](#footnote3),[4](#footnote4)</sup> m | 100 m | 300/350/1000<sup>[4](#footnote4)</sup> m | 300 m | 100 m |
| Navigation data | Latitude, <br/> Longitude, <br/> Depth, <br/> Temperature, <br/> Time UTC<sup>[7](#footnote7)</sup>, <br/> Course | Latitude, <br/> Longitude, <br/> Depth<sup>[5](#footnote5)</sup>, <br/> Temperature<sup>[5](#footnote5)</sup>, <br/> Course | Latitude, <br/> Longitude | Distance, <br/> Azimuth, <br/> Depth, <br/> Battery voltage, <br/> Latitude<sup>[6](#footnote6)</sup>, <br/> Longitude<sup>[6](#footnote6)</sup> | Distance, <br/> Azimuth, <br/> Depth, <br/> Battery voltage, <br/> Latitude<sup>[5](#footnote5)</sup>, <br/> Longitude<sup>[6](#footnote6)</sup> | Latitude, <br/> Longitude, <br/> Course |
| Maximal relative velocity | ±1.8 m/s | ±1.8 m/s | ±1.8 m/s | ±2 m/s | ±1 m/s | ±2 m/s |
| Deployment features | Requires 4 floating buoys to be deployed | Requires 4 floating buoys to be deployed | Requires 4 floating buoys to be deployed | Requires fixing the base station on a rigid rod and connecting an external GPS and compass | Requires fixing the base station on a rigid rod and connecting an external GPS and compass | Requires 4 floating buoys to be deployed |
| Distinctive feature | - Unlimited number of simultaneously positioned devices, <br/> - Ability to connect to [AQUATAB-S](https://duslate.com/products/aquatab-s/) diver's tablet | Divers positioning simultaneously with voice transmission | Divers positioning simultaneously with voice transmission | Automatic tracking | Two-way data transmission | The most affordable solution for amateurs |

<div style="page-break-after: always;"></div>

________________
<a name="footnote1"><sup>1</sup></a> The maximum number of devices supported to be processed sequentially is specified.  
<a name="footnote2"><sup>2</sup></a> The minimum value is indicated when working with one transponder beacon located at a distance of up to 100 meters from the base station  
<a name="footnote3"><sup>3</sup></a> For the diving version, the maximum depth is 70 m  
<a name="footnote4"><sup>4</sup></a> Different maximum depth for different system versions  
<a name="footnote5"><sup>5</sup></a> The parameters are available only when working with the [RWLT pinger](/documentation/EN/RWLT/RWLT_Pinger_Specification_en). When positioning diving telephone devices, these parameters are not available.  
<a name="footnote6"><sup>6</sup></a> These parameters are available only when external sources of navigation data are connected: course and base station geo position  
<a name="footnote7"><sup>7</sup></a> These parameters are not available in the diver's version
  
<div style="page-break-after: always;"></div>
