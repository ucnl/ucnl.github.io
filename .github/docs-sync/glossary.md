# RU → EN glossary for docs.unavlab.com

Authoritative terminology for every RU → EN sync task (CLAUDE.md section 5). Built in Phase 1 from the existing RU/EN document pairs (breadcrumbs, header-table phrases, titles, table header cells, parameter rows paired by matching values, section headings paired by number) with `.github/docs-sync/docsync.py terms`, then curated by the orchestrator.

## How to use

1. Precedence: the fixed terms (section 1) → the canonical rows of sections 3–9 → the term already used in EN documents of the same family → the standard industry term.
2. `CONFLICT` rows list every EN variant found in the repository; the **bold** variant is canonical. Use only the canonical variant in new or updated text; Phase 4 aligns the remaining EN files.
3. Letter case: where the RU text writes a heading, table header or parameter label in ALL CAPS, the EN text keeps ALL CAPS (`ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ` → `TECHNICAL SPECIFICATIONS`). Everywhere else headings are in sentence case (`Подготовка к работе` → `Preparation for work`). Product names keep their own case.
4. `МАКСИМАЛЬНЫЙ / МАКСИМАЛЬНАЯ / МАКСИМАЛЬНОЕ` → `MAXIMUM` spelled out (the style of the most recent EN files); `MAX.` only where RU abbreviates (`МАКС.`). The same for `МИНИМАЛЬНЫЙ` → `MINIMUM`, `НОМИНАЛЬНЫЙ` → `NOMINAL`.
5. The adjective `гидроакустический` is `underwater acoustic` (or just `acoustic` when the context is already underwater), never `hydroacoustic`.
6. Cyrillic look-alikes are errors in EN text: `°С` with a Cyrillic `С` → `°C`, the Cyrillic `х` used as a multiplication sign → `x`, `Ф` as the diameter sign → `Ø`, `№` → `No.`. `docsync.py check` reports them as Cyrillic residue.
7. New terms decided during a batch are appended under `## Added in batch <slug>` at the end of this file. Never edit or reorder earlier rows in Phase 2; conflicts found later are resolved in Phase 4.

Column `Source EN file`: the EN document(s) where the variant occurs (paths relative to `documentation/EN/`, or root pages); `(+n)` = n more files. `CLAUDE.md` = fixed by the sync rules.

## 1. Fixed terms

| RU | EN | Source EN file | Note |
|---|---|---|---|
| маяк-ответчик | responder-beacon | CLAUDE.md | CONFLICT: **responder-beacon** (85 hits in 9 files) / responder beacon (90 hits in 9 files) / responder. Always hyphenated; plural `responder-beacons` |
| пеленгационная антенна | direction-finding antenna | CLAUDE.md | CONFLICT: **direction-finding** (11 files) / direction finding (8 files) |
| Спецификация устройства | Device specification | CLAUDE.md | CONFLICT: **Device specification** / Device Specification (60, header cells) / Device specifications (5). Sentence case in breadcrumbs, titles and header cells |
| Руководство пользователя | User's manual | CLAUDE.md | CONFLICT: **User's manual** (ASCII apostrophe) / User’s manual (typographic apostrophe, 7 files) |
| Инструкция по эксплуатации | User's manual | RedPhone/RedPhone_OS_Users_manual_en.md | Same document type as `Руководство пользователя` |
| Краткое описание | Data brief | CLAUDE.md | CONFLICT: **Data brief** / Databrief (2) / Data Brief (1) / Brief description (2) |
| Протокол информационного сопряжения | Communication protocol specification | CLAUDE.md | CONFLICT: **Communication protocol specification** / Interfacing protocol specification (4) / Communication protocol (2) / Protocol specification (1) |
| Описание протокола сопряжения; Спецификация протокола сопряжения | Communication protocol specification | uWAVE/uWAVE_Protocol_Specification_en.md (+2) | RU index pages use these as synonyms of `Протокол информационного сопряжения`; variant `Communication protocol description` (RedWAVE) |
| Схема подключения; Схема включения устройства | Wiring diagram | CLAUDE.md | CONFLICT: **Wiring diagram** / Device wiring diagram (4) / Wirind diagram (typo, index page) |
| Пультовое приложение | Host application | CLAUDE.md | |
| Технический паспорт; Паспорт изделия | Product passport | CLAUDE.md | `(шаблон)` → `(template)` |
| История версий и изменений | Version history & changes | CLAUDE.md | CONFLICT: **Version history & changes** / Versions & changes (index page) |
| История версий и список изменений | Version history & list of changes | uWAVE/uWAVE_Protocol_Specification_en.md | Variants: Version history / Changes and versions |
| Быстрый старт | Quick start | CLAUDE.md | |
| гидроакустический модем | underwater acoustic modem | CLAUDE.md | |
| ультракороткобазисная (УКБ) система | ultra-short baseline (USBL) system | CLAUDE.md | |
| длиннобазисная (ДБ) система | long baseline (LBL) system | CLAUDE.md | |
| дальномерная система | ranging system | CLAUDE.md | |
| гидроакустическая антенна, излучатель | transducer | CLAUDE.md | `Антенна гидроакустическая приемопередающая` → `Underwater acoustic transducer`; fix typo `acostic` |
| гидрофон | hydrophone | CLAUDE.md | |
| водолазная телефония, подводный телефон | underwater telephone | CLAUDE.md | |
| медиаматериалы | media | CLAUDE.md | |
| Главная | Main | CLAUDE.md | CONFLICT: **Main** (82) / Home (2) |
| Параметр / Значение | Parameter / Value | CLAUDE.md | ALL CAPS in spec tables: `PARAMETER` / `VALUE` |
| Примечание / Внимание / Важно | Note / Caution / Important | CLAUDE.md | |
| курс / крен / тангаж | heading / roll / pitch | CLAUDE.md | |
| наклонная дальность | slant range | CLAUDE.md | |
| азимут / пеленг | azimuth / bearing | CLAUDE.md | |
| датчик давления | pressure sensor | CLAUDE.md | |
| ГНСС | GNSS | CLAUDE.md | |
| техподдержка | support | CLAUDE.md | `Техподдержка support@unavlab.com` → `Support support@unavlab.com`; variant Tech support (4) |

## 2. Do not translate

Keep verbatim, including letter case as written in the RU sentence at hand (the RU text itself mixes `uWAVE`/`uWave`, `RedWAVE`/`RedWave`, `RedBASE`/`RedBase`; keep what RU has, but in breadcrumbs, titles and header cells use the spelling of the product family: `uWave`, `RedWAVE`, `RedBASE`, `RedNODE`, `RedNAV`, `RedLINE`).

**Systems and devices:** Zima, Zima USBL, Zima-B, Zima-R, Zima-R 1000, Zima2, Zima2 USBL, Zima2 LBL, Zima2-B, Zima2-R, Zima2-uR, Zima2-L, Zima2-LX, Zima2-SL, Zima2-B35, Zima2-R35, Zima2-BK, Zima2-RK, Zima2K, Zima2-35, Zima2-OEM35, Bat&Link Box, uWave (uWAVE), uWave Max, uWave Max OEM, uWave USBL Modem, uSwitch, RedLINE (RedLine), RedGTR, RedWAVE, RedBASE, RedNODE, RedNAV, Aquatab S, RedPhone, RedPhone-OS, RedPhone-DX, RedPhone-D, RedPhone-MOS, RedPhone-MDX, RedPhone RF Dongle, Phone-T, Phone-S, RWLT, RWLT Pinger, RWLT Pinger-K, RWLT GIB, uNav RWLT Radio dongle, uNav WAYU Radio dongle, WAYU, WAYU Pinger, WAYU GIB, ACubes A<sup>3</sup>S (A3S), A³R (ACubes AR), A³T (ACubes AT), F4105, F4105-SU, F4105-BU, F4105-AU, uPress, uSpeak, uWire, uClamp, uClamp-S, uBat, Crimea-300, Crimea-300 OS.

**Model codes and part numbers:** SB-23-64-LI, SB-24-48-LF, RT-1.332820-1, RT-1.332820-2, RT-2.332820-1, RT-2.332820-2, RT-1.524525-1, RT-1.524525-1-FF, RT-1.524525-2, R-1.d3505-1, PMVR.134097.002, PMVR.134098.002, patent numbers (`RU2659299C1`), connector designators (`XS1`, `XP2`), and every other alphanumeric code exactly as in RU.

**Software:** AzimuthSuite, AzimuthConsole, AzimuthConsole v1.x, AzimuthWebSuite, ZHost, uGPSHub (repository and release `UGPSHub`), RedBASE_Config, RedNAV Host (repository `RedNavHost`), uNav, uNav application, uTrackDiver, uWaver, uBear, uWaveCommander, uWAVE_ALib, uWAVE_Arduino, uConsole, uGNSS-Monitor, RedPhoneDXConfig, RedPhoneDXConfig-Web, RedLINE_Host, WAYU (host application).

**Protocols and identifiers:** NMEA 0183 / NMEA0183 (as written in RU); proprietary sentence prefixes `$PAZM`, `$PZMA`, `$PUWV`, `$PTNT`, `$PRPH`, `$PUNV`, `$PRWL`, `$PNTN`, `$PAPL`, `$PUNA`; standard sentences (`GGA`, `RMC`, `MTW`, `HDT`, `HDG`, …); command systems `AZM`, `ZMA`, `UWV`, `UNV`, `RPH`, `TNT`; every command mnemonic (`IC_D2H_ACK`, `IC_H2D_SETTINGS_WRITE`, …), field name, enum value, error code, hex value and code block content; firmware version strings (`uWave [JULY] 1.34`).

**UI strings that are already English in RU:** tab and button names such as `❗ CONNECTION`, `🛸 EXTRA`, `🧪 PHYSICS`, menu labels in the original software language. When RU quotes a Russian UI label of software that has an English UI (AzimuthSuite, AzimuthConsole, uNav, RedNAV Host, ZHost), use the real English UI string; if it is unknown, translate literally in bold and record a question.

**Organization:** the brand is UC&NL, Underwater Communication & Navigation Laboratory (`Лаборатория подводной связи и навигации` in running text). The official English legal name is **UCNL LLC**: `ООО "Лаборатория подводной связи и навигации"`, `OOO "Лаборатория подводной связи и навигации"` (the RU sources also spell `ООО` with Latin `O`) and `ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛАБОРАТОРИЯ ПОДВОДНОЙ СВЯЗИ И НАВИГАЦИИ"` all become `UCNL LLC`.

**Personal names** are transliterated as in the authors' own English publications: Дикарев → Dikarev, Дмитриев → Dmitriev, Кубкин → Kubkin, Василенко → Vasilenko, Абеленцев → Abelentsev; initials keep their order (`А. В. Дикарев` → `A. V. Dikarev`).

## 3. Sections, breadcrumbs and document types

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Гидроакустические навигационные и трекинговые системы; Навигационные и трекинговые системы | Navigation & tracking systems | navigation_and_tracking_systems_en.md (+30) | Breadcrumb section, index `/navigation_and_tracking_systems_en` |
| Гидроакустические модемы | Underwater acoustic modems | underwater_acoustic_modems_en.md (+13) | Index `/underwater_acoustic_modems_en` |
| Голосовая подводная связь (водолазная телефония) | Underwater wireless voice systems | underwater_wireless_voice_systems_en.md (+6) | CONFLICT: **Underwater wireless voice systems** (CLAUDE.md breadcrumb) / Underwater Wireless voice systems (Underwater telephone) (index page heading) |
| Гидрофоны и гидроакустические антенны | Hydrophones & transducers | underwater_acoustic_antennas_en.md (+6) | CONFLICT: **Hydrophones & transducers** / Hydrophones and Underwater Acoustic Antennas (1, 2026-03) |
| Аксессуары | Accessories | accessories_en.md (+5) | |
| Специализированное оборудование | Other equipment | underwater_bespoke_systems_en.md (+4) | |
| Медиа | Media | media_videos_en.md | |
| Наши проекты для образования; Образовательные проекты | Educational projects | educational_projects_en.md (+3) | Breadcrumb section. Variant Our educational projects (index page title). The WAYU and A3S RU documents use this breadcrumb; existing EN WAYU documents point to Navigation & tracking systems instead — mirror RU |
| Дополнительные материалы | Miscellaneous info | misc_en.md (+9) | |
| Online утилиты | Online utilities | online_utilities_en.md | |
| Документация | Products documentation | README.md | Site index section |
| Техподдержка и соцсети | Support & social media | README.md | |
| Прочее | Media, educational projects and other things | README.md | Site index section; fix `educational project` |
| На главную | Back to main | accessories_en.md (+3) | CONFLICT: **Back to main** / To main (1) |
| Вернуться к содержанию | Back to contents | RedWAVE/RedWAVE_Protocol_Specification_en.md | |
| К общему списку медиаматериалов | Back to all media | Zima/media.md (+2) | CONFLICT: **Back to all media** / To all media (3) / Back (1) |
| Содержание | Contents | Zima/Zima2_Users_manual_en.md (+15) | CONFLICT: **Contents** / Content (2) |
| Таблица сравнения гидроакустических модемов; Сравнение гидроакустических модемов | Modems comparison table | modems_comparison_en.md | |
| Таблица сравнения навигационных систем | Comparison table of navigation systems | navigation_systems_comparison_en.md | |
| Сравнительная таблица модемов семейства uWave; Сравнение модемов семейства uWave | uWave family modems comparison table | uWAVE/uWAVE_Modems_comparison_en.md | |
| Краткое описание семейства устройств uWave | uWave devices family: Data brief | uWAVE/uWAVE_Family_en.md | |
| Руководство по обновлению прошивки; Инструкция по обновлению прошивки модемов uWave | Firmware update guide | uWAVE/uWAVE_FW_Updating_en.md | CONFLICT: **Firmware update guide** / Instructions for firmware updating (index) / Instructions for updating the firmware of uWave modems (header) |
| Обновление внутреннего программного обеспечения модемов uWave | Updating the firmware of uWave modems | uWAVE/uWAVE_FW_Updating_en.md | Title |
| Программа и методики испытаний | Test program and procedures | — | New (RedPhone_PM, RedNAV_PM) |
| Программа и методики испытаний (Водолазный вариант) | Test program and procedures (diver version) | — | New |
| медиаматериалы, видео испытаний, треки и т.п. | media, test videos, tracks, etc. | RWLT/media.md (+3) | Variant tracks, videos, tutorials, etc. (drops `испытаний`) |
| Вкладыш с QR кодами ссылок | QR links sheet | Misc/l2c.md | |
| Стикер на упаковку малый | Small package sticker | Misc/package_sticker.md | Variant Package sticker small / Small box sticker |
| Брошюра | Brochure | — | |
| (шаблон) | (template) | — | Passports in the RU index |
| (В разработке) | (In development) | underwater_bespoke_systems_en.md | Variant (COMING SOON) |
| Поставляется с 06.2022 г. | Available since June 2022 | CLAUDE.md | Pattern for `Поставляется с MM.YYYY г.` |
| Поставлялась с 05.2016 по 05.2022 г. | Supplied from May 2016 to May 2022 | navigation_and_tracking_systems_en.md | Variant May 2016 - May 2022 |
| Предыдущие версии | Previous versions | — | Variant Discontinued (index page) |
| Исходный код / Скачать релиз / Релизы / Репозиторий | Source code / Download release / Releases / Repository | navigation_and_tracking_systems_en.md | Fix typo `dowload` |
| 3D-модель (STEP) | 3D model (STEP) | navigation_and_tracking_systems_en.md | Variant 3D-model |
| Кронштейн плоский / Кронштейн на баллон | Flat bracket / Tank bracket | navigation_and_tracking_systems_en.md | Variants Bracket flat / Bracket on tank / tank holder |

## 4. Device descriptions (header cells and breadcrumbs)

| RU | EN | Source EN file | Note |
|---|---|---|---|
| гидроакустическая навигационная система | underwater acoustic navigation system | Zima/Zima_Users_manual_en.md (+2) | CONFLICT: **underwater acoustic navigation system** / Underwater acoustic tracking system (2) / Underwater tracking system (1) |
| гидроакустическая трекинговая система | underwater acoustic tracking system | WAYU/WAYU_Users_Manual_en.md (+1) | |
| станция пеленгования; гидроакустическая станция пеленгования | direction-finding station | Zima/Zima_B_Specification_en.md | Variants direction finding antenna / base station / Hydroacoustic direction-finding base station |
| маяк-ответчик навигационной системы Zima2 USBL | Zima2 USBL responder-beacon | Zima/Zima2R_Specification_en.md | |
| микро маяк-ответчик | micro responder-beacon | — | Zima2-uR |
| маяк-ответчик на глубину до 1000 м | responder-beacon rated to 1000 m | navigation_and_tracking_systems_en.md | Variant 1000 m depth rating responder-beacon |
| LBL-трансивер | LBL transceiver | — | Zima2-L, Zima2-LX |
| решатель (Solver) | solver | — | Zima2-SL |
| блок питания и коммутации | power supply and switching unit | — | Bat&Link Box. Variant Autonomous power supply (index pages) |
| источник питания и преобразователь интерфейса | power supply and interface converter | Zima/Bat_n_link_box_Users_manual_en.md | CONFLICT: **power supply and interface converter** / Autonomous power supply and interfacing unit |
| Автономный источник питания и преобразователь RS422/485⮀USB | Autonomous power supply and RS422/485⮀USB converter | — | accessories index |
| семейство устройств гидроакустической связи; семейство устройств гидроакустической цифровой связи | family of underwater acoustic (digital) communication devices | uWAVE/uWAVE_Family_en.md | CONFLICT: **family of underwater acoustic communication devices** / underwater communication system / underwater acoustic modem |
| Гидроакустический модем кодовой связи; модем кодовой гидроакустической связи | underwater acoustic code communication modem | RedGTR/RedGTR_Specifications_en.md (+1) | Variant code communication underwater acoustic modem |
| гидроакустический модем начального уровня | entry-level underwater acoustic modem | — | uSwitch |
| Буй-ретранслятор; Навигационный гидроакустический буй | GNSS-equipped sonobuoy | RedWAVE/RedBASE_Specification_en.md | RedBASE; established EN product description |
| Навигационный буй | Navigation buoy | WAYU/WAYU_GIB_Specification_en.md (+1) | GIB |
| Навигационный приемник для ТНПА/АНПА; Универсальный навигационный приемник | navigation receiver for ROVs and AUVs; universal navigation receiver | RedWAVE/RedNODE_Specification_en.md | RedNODE |
| Навигационный приемник для водолазов; Водолазный навигационный приемник | diver's navigation receiver | RedWAVE/RedNAV_Specification_en.md | RedNAV |
| Навигационный планшет водолаза; Водолазный планшет | diver's navigation tablet; diver's tablet | RedWAVE/Aquatab_s_specification_en.md | Aquatab S |
| Приемник сигнала навигационных буев | navigation buoy signal receiver | WAYU/WAYU_RF_Dongle_Specification_en.md | Variant Navigation receiver |
| Навигационный маяк - пингер | navigation pinger beacon | RWLT/RWLT_Pinger_Specification_en.md | CONFLICT: **navigation pinger beacon** / Pinger beacon / Underwater pinger beacon |
| навигационный приемник для трекинговых систем RWLT/WAYU | navigation receiver for RWLT/WAYU tracking systems | RWLT/uNav_protocol_specification_en.md | Variant navigation solver/radio modem |
| радиодонгл; Radio dongle | radio dongle | RWLT/RWLT_RF_Dongle_en.md | CONFLICT: **radio dongle** in prose / RF dongle. Product names keep their RU form: `uNav RWLT Radio dongle`, `RedPhone RF Dongle` |
| Радиодонгл для настройки приборов RedPhone-DX | radio dongle for configuring RedPhone-DX devices | RedPhone/RedPhone_RF_Dongle_Specification_en.md | Variant RedPhone-DX configuration tool |
| Надводная станция (водолазной беспроводной / голосовой гидроакустической) связи | surface station (of the wireless diver voice communication system) | RedPhone/RedPhone_OS_Specification_en.md (+4) | CONFLICT: **surface station** / Underwater telephone. Surface unit / Underwater telephone (surface station) |
| Водолазная станция (беспроводной / голосовой гидроакустической) связи | diver station (of the wireless voice communication system) | RedPhone/RedPhone_DX_Specification_en.md (+2) | CONFLICT: **diver station** / Underwater telephone. Diver's unit / Wireless telephone for divers |
| с увеличенной дальностью | extended-range | — | RedPhone-MOS, RedPhone-MDX |
| Система беспроводной гидроакустической голосовой связи | wireless underwater acoustic voice communication system | — | |
| Система связи дайверов | diver communication system | — | Phone-T / Phone-S kits |
| Модуль управления гидроакустическими размыкателями | Acoustic release control unit | F4105/F4105_SU_Specification_en.md | |
| Актуатор-размыкатель | Release unit | F4105/F4105_BU_Specification_en.md | |
| Гидроакустический пробудитель | Acoustic wake-up unit | F4105/F4105_AU_Specification_en.md | CONFLICT: **Acoustic wake-up unit** / Acoustic awakening unit (existing) |
| Гидроакустический размыкатель | Acoustic release | underwater_bespoke_systems_en.md | |
| Подводная кнопка; Кнопка подводная | underwater button | Accessories/uPress_Specification_en.md | |
| Микрофон для водолазных масок | microphone for diving masks | — | uSpeak |
| Удлинительный кабель (с преобразователем) UART-RS422 | extension cable (with UART-RS422 converter) | Accessories/RS422_extension_cable_en.md | |
| Кронштейн фланцевый; Фланцевый кронштейн | flange rod mount | Accessories/Flange_rod_mound_Specification_en.md | |
| Подводные аккумуляторные сборки; Подводные аккумуляторы; Сборка аккумуляторная подводная | underwater battery packs; submersible battery pack | Accessories/Sub_batteries_en.md (+3) | `Сборка аккумуляторная подводная SB-…` → `Submersible battery pack SB-…` |
| конформная аккумуляторная сборка | conformal battery pack | — | Batpacks |
| Датчик абсолютного давления | absolute pressure sensor | — | Crimea-300 |
| Интерфейсный модуль | interface module | — | Crimea-300 OS |
| Приемопередающая антенна | Transducer | Transducers/RT_1_332820_1_Specification_en.md (+3) | `Приемопередающая антенна RT-…` → `Transducer RT-…` |
| с полосовым фильтром | with band-pass filter | — | |
| Приемная антенна; Антенна гидроакустическая приемная | receiving transducer | Transducers/R_1.d3505_1_Specification_en.md | CONFLICT: **receiving transducer** (consistent with the fixed term `гидроакустическая антенна` → transducer) / Receiving antenna / Underwater Acoustic Receiving Antenna |
| модуль одночастотного приемника | single-frequency receiver module | A3S/A3R_Datasheet_en.md | A³R |
| модуль импульсного одночастотного передатчика | single-frequency pulse transmitter module | A3S/A3T_Datasheet_en.md | A³T |
| Стандартные комплекты и что с ними можно сделать | Standard kits and what you can build with them | — | A3S packages |
| Приложение для трекинга водолазов | diver tracking application | RWLT/uTrackDiver_Users_Manual_en.md | |
| Кроссплатформенное приложение для работы с системой Zima2 USBL | Cross-platform application for the Zima2 USBL system | — | AzimuthConsole |
| Консольное пультовое приложение | Console host application | — | AzimuthConsole |
| Пультовое онлайн приложение | Online host application | — | AzimuthWebSuite |
| Демонстрационное приложение | Demo application | underwater_acoustic_modems_en.md | Variant demo host application |
| Информационный лист по совместимости для систем определения положения и курса | Compatibility data sheet for positioning and heading systems | — | Zima_GNSS_requirements (index wording) |
| Требования по совместимости для GNSS | GNSS compatibility requirements | Zima/Zima_GNSS_requirements_en.md | Variant Compatibility Requirements for Heading and Positioning |

## 5. Common section headings

| RU | EN | Source EN file | Note |
|---|---|---|---|
| КЛЮЧЕВЫЕ ОСОБЕННОСТИ | KEY FEATURES | Zima/Zima2B_Specification_en.md (+27) | |
| ОСОБЕННОСТИ | FEATURES | Accessories/Sub_batteries_en.md (+2) | CONFLICT: **FEATURES** / KEY FEATURES (6; RU has no `КЛЮЧЕВЫЕ` there) / Distinctive features |
| Отличительные черты; Особенности | Distinctive features; Features | Zima/Zima_DataBrief_en.md (+3) | |
| ОПИСАНИЕ | DESCRIPTION | A3S/A3R_Datasheet_en.md (+36) |  |
| ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ | TECHNICAL SPECIFICATIONS | Zima/Zima2RK_Specification_en.md (+33) | CONFLICT: **TECHNICAL SPECIFICATIONS** (34, newest) / TECHNICAL SPECIFICATION (2) / TECHNICAL FEATURES (2, Zima2-B) / Specifications (1) |
| ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ | ADDITIONAL PARAMETERS | Transducers/RT_1_524525_1_FF_Specification_en.md (+4) | CONFLICT: **ADDITIONAL PARAMETERS** / ADDITIONAL FEATURES (2) |
| ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ | ADDITIONAL INFORMATION | Misc/BatLinkBox_MSDS_en.md (+11) |  |
| ГАБАРИТНЫЙ ЧЕРТЕЖ | DIMENSIONAL DRAWING | Transducers/R_1.d3505_1_Specification_en.md (+7) | CONFLICT: **DIMENSIONAL DRAWING** / DRAWINGS (7) |
| НАЗНАЧЕНИЕ ЖИЛ КАБЕЛЯ | CABLE WIRE ASSIGNMENT | Transducers/R_1.d3505_1_Specification_en.md (+7) | CONFLICT: **CABLE WIRE ASSIGNMENT** / WIRING DIAGRAM (4, reserved for `Схема подключения`) / Wire functions (3) |
| НАЗНАЧЕНИЕ ЖИЛ КАБЕЛЯ И РАСПИНОВКА | CABLE WIRE ASSIGNMENT AND PINOUT | Accessories/Sub_batteries_en.md (+1) | Variants ADDITIONAL SPECIFICATIONS / PINOUT (misaligned) |
| Назначение жил кабеля и габариты | Cable wire assignment and dimensions | Zima/ZimaR_wiring_diagram_en.md | Header cell; variant Wiring diagram and drawings |
| РАСПИНОВКА И ПОДКЛЮЧЕНИЕ | PINOUT AND CONNECTION | A3S/A3R_Datasheet_en.md (+2) |  |
| РАСПИНОВКА РАЗЪЕМА; Распиновки разъемов | CONNECTOR PINOUT; Connector pinouts | F4105/F4105_AU_Specification_en.md (+2) |  |
| РАЗЪЕМ XS1 | CONNECTOR XS1 | A3S/A3R_Datasheet_en.md (+1) | Same pattern for every connector designator |
| ТРЕБОВАНИЯ ПО УСТАНОВКЕ | INSTALLATION REQUIREMENTS | uWAVE/uWAVE_wiring_diagram_en.md | |
| ВАРИАНТЫ АВТОНОМНОГО ИСПОЛНЕНИЯ | STANDALONE VERSIONS | WAYU/WAYU_Pinger_Specification_en.md | Variant AUTONOMOUS OPTIONS |
| КАНАЛЫ И ПОЛОСЫ ЧАСТОТ | CHANNELS AND FREQUENCY BANDS | RedPhone/RedPhone_Specification_en.md | |
| Введение | Introduction | Zima/Bat_n_link_box_Users_manual_en.md (+15) | CONFLICT: **Introduction** / Introducation (typo, 2) |
| Назначение | Purpose | RWLT/RWLT_Users_Manual_en.md (+10) | Heading. In pinout tables the column `Назначение` is `Function` |
| Общие сведения; Общие данные; Общие положения | General information | RWLT/RWLT_DataBrief_en.md (+7) | Variants General info / Brief description |
| Состав системы | System composition | Zima/Zima2_Users_manual_en.md (+8) | Variant Composition of the system |
| Комплект поставки | Delivery set | RedPhone/RedPhone_DX_Users_Manual_en.md (+2) | CONFLICT: **Delivery set** / Equipment set (2) / Contents of the standard delivery set (1) |
| Исполнения; Варианты исполнения | Versions; Configuration options | Zima/Zima_Users_manual_en.md | `Стандартное исполнение` → `Standard version`, `Исполнение 35` → `Version 35` |
| в интегрируемом / автономном исполнении | integrated / standalone version | — | |
| Решаемые задачи | Tasks to be solved | WAYU/WAYU_DataBrief_en.md (+4) | Variants Solved problems / Tasks that the system solves |
| Схемы сопряжения | Interfacing schemes | Zima/Zima2_DataBrief_en.md | Variants Pairing schemes / Working options |
| Геометрические ограничения | Geometric limitations | RWLT/RWLT_DataBrief_en.md (+4) | Variants Geometric restrictions / Geometrical limitations / Geometric Constraints |
| Системные требования | System requirements | Zima/Zima_Users_manual_en.md | |
| До проведения работ | Before operation | Zima/Zima2_Users_manual_en.md (+2) | Variants Before work / Before start |
| Подготовка к работе | Preparation for operation | RedPhone/RedPhone_OS_Users_manual_en.md | |
| Подготовка к работе и проверка оборудования | Preparation for operation and equipment check | Zima/Zima2_Users_manual_en.md (+2) | Variants differ in each manual |
| Непосредственно перед работой | Immediately before operation | RedPhone/RedPhone_OS_Users_manual_en.md | |
| Работа с системой / устройством | Working with the system / the device | RWLT/RWLT_Users_Manual_en.md (+1) | Variants Work with the device / Using the device |
| Работа с ПО | Using the software | RedWAVE/RedNAV_Host_Users_Manual_en.md | |
| По завершении работ; Завершение работы | After operation; Shutdown | RedPhone/RedPhone_DX_Users_Manual_en.md (+4) |  |
| Хранение и обслуживание; Условия хранения и обслуживания | Storage and maintenance; Storage and maintenance conditions | Zima/Bat_n_link_box_Users_manual_en.md (+5) |  |
| Возможные неисправности, их диагностика и устранение | Troubleshooting | RedPhone/RedPhone_Users_Manual_en.md | Existing: Possible malfunctions, their diagnosis and elimination |
| Известные проблемы | Known issues | uWAVE/uWAVE_version_history_en.md | |
| Коды ошибок | Error codes | RedLINE/RedLINE_Protocol_Specifications_en.md (+5) | Variant Error messages |
| Предварительные проверки; Проверочные мероприятия | Preliminary checks; Test procedures | RedPhone/RedPhone_OS_Users_manual_en.md | |
| Внешняя визуальная проверка | External visual inspection | RedPhone/RedPhone_OS_Users_manual_en.md | |
| Проверка работоспособности устройства | Functional check of the device | RedPhone/RedPhone_OS_Users_manual_en.md | |
| Органы управления и разъемы | Controls and connectors | RedPhone/RedPhone_OS_Users_manual_en.md (+1) |  |
| Звуковые сигналы | Sound signals | RedPhone/RedPhone_OS_Users_manual_en.md (+2) | Variant Sound alerts |
| Заряд / Зарядка встроенного источника питания | Charging the built-in power supply | RWLT/RWLT_Users_Manual_en.md (+2) | |
| Замена аккумуляторов | Battery replacement | RedPhone/RedPhone_Users_Manual_en.md | |
| Обязательства и отказ от ответственности | Obligations and disclaimer | RWLT/RWLT_Users_Manual_en.md (+8) | CONFLICT: **Obligations and disclaimer** (literal) / Liability and disclaimer (7) |
| Ограничение ответственности производителя | Limitation of the manufacturer's liability | Zima/Zima2_Users_manual_en.md (+8) | CONFLICT: **Limitation of the manufacturer's liability** / Disclaimer of the manufacturer (5) / Manufacturer disclaimer / Manufacturer Liability Limitation / Disclamer (typo) |
| Условия замены и бесплатного гарантийного обслуживания | Terms of replacement and free warranty service | Zima/Bat_n_link_box_Users_manual_en.md (+8) | Variant Conditions for replacement and free warranty service |
| Медиаматериалы | Media | RedPhone/media.md | |
| Шаг 1 | Step 1 | RedPhone/RedPhone_DX_Users_Manual_en.md (+1) | Same pattern for `Шаг 1.1` etc. |
| Рецепт 1; Готовые рецепты | Recipe 1; Recipes | uWAVE/uWAVE_Protocol_Specification_en.md | |
| Приложения | Appendices | uWAVE/uWAVE_Protocol_Specification_en.md | Variant Appendix; single `Приложение А` → `Appendix A` |
| Замечания | Remarks | Misc/RedPhone_OS_MSDS_en.md (+6) | CONFLICT: **Remarks** / Notes (6). `Примечание` stays `Note` |

## 6. Specification tables

| RU | EN | Source EN file | Note |
|---|---|---|---|
| ПАРАМЕТР / ЗНАЧЕНИЕ | PARAMETER / VALUE | A3S/A3R_Datasheet_en.md (+42) |  |
| НАИМЕНОВАНИЕ | NAME | Accessories/Flange_rod_mound_Specification_en.md (+6) |  |
| ФУНКЦИЯ | FUNCTION | A3S/A3R_Datasheet_en.md (+7) |  |
| ОБОЗНАЧЕНИЕ | DESIGNATION | uSwitch/uSwitch_Specification_en.md | |
| НОМЕР КОНТАКТА; № КОНТАКТА; № КОНТАКТА РАЗЪЕМА; Номер пина | PIN NUMBER; PIN No.; CONNECTOR PIN No.; Pin number | A3S/A3R_Datasheet_en.md (+5) | Variant PIN # / № Pin |
| ЦВЕТ ЖИЛЫ (КАБЕЛЯ) | WIRE COLOR | WAYU/WAYU_Pinger_Specification_en.md | CONFLICT: **WIRE COLOR** / CORE COLOR. US spelling `color`, never `colour` |
| АКТИВНОЕ СОСТОЯНИЕ | ACTIVE STATE | A3S/A3R_Datasheet_en.md (+2) |  |
| ГАБАРИТЫ | DIMENSIONS | A3S/A3R_Datasheet_en.md (+3) | Fix typo DIMENSTIONS |
| ГАБАРИТЫ (Ф х h); (д х ш х в) | DIMENSIONS (Ø x h); (L x W x H) | Zima/Zima2B_Specification_en.md | Keep the RU symbol order; `Ф` → `Ø` |
| ВЕС; ВЕС (сухой) | WEIGHT; WEIGHT (dry) | A3S/A3R_Datasheet_en.md (+16) | Fix typo WIGHT |
| МАКСИМАЛЬНАЯ ГЛУБИНА | MAXIMUM DEPTH | uWAVE/uWAVE_Max_Specification_en.md (+2) | CONFLICT: **MAXIMUM DEPTH** / DEPTH RATING (2) / MAX. OPERATING DEPTH / MAXIMAL DEPTH |
| МАКСИМАЛЬНАЯ РАБОЧАЯ ГЛУБИНА | MAXIMUM OPERATING DEPTH | — | |
| МАКСИМАЛЬНАЯ ГЛУБИНА ПОГРУЖЕНИЯ | MAXIMUM IMMERSION DEPTH | WAYU/WAYU_Pinger_Specification_en.md (+5) | CONFLICT: **MAXIMUM IMMERSION DEPTH** / DEPTH RATING (4) / MAX. DEPTH / MAXIMUM DIVE DEPTH |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ АКУСТИЧЕСКОЙ СВЯЗИ; МАКСИМАЛЬНАЯ АКУСТИЧЕСКАЯ ДАЛЬНОСТЬ СВЯЗИ | MAXIMUM ACOUSTIC COMMUNICATION RANGE | A3S/A3R_Datasheet_en.md (+13) | CONFLICT: **MAXIMUM ACOUSTIC COMMUNICATION RANGE** (newest) / MAX. ACOUSTIC RANGE / MAX. OPERATING RANGE / MAX. ACOUSTIC COMMUNICATION RANGE / ACOUSTIC RANGE (ENEGRY) |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ РАДИОСВЯЗИ | MAXIMUM RADIO COMMUNICATION RANGE | WAYU/WAYU_RF_Dongle_Specification_en.md (+2) | Variants MAX. RF RANGE / COMMUNICATION RANGE |
| МАКСИМАЛЬНОЕ АКУСТИЧЕСКОЕ ДАВЛЕНИЕ (В полосе) | MAXIMUM ACOUSTIC SOURCE LEVEL (in band) | A3S/A3T_Datasheet_en.md (+3) | CONFLICT: **MAXIMUM ACOUSTIC SOURCE LEVEL** (standard term for dB re 1 μPa @ 1 m) / ACOUSTIC SOURCE LEVEL / MAXIMUM ACOUSTIC PRESSURE / ACOUSTIC POWER SOURCE / ACOUSIC (typo) |
| МАКСИМАЛЬНАЯ ОТНОСИТЕЛЬНАЯ СКОРОСТЬ | MAXIMUM RELATIVE VELOCITY | A3S/A3R_Datasheet_en.md (+4) |  |
| МАКСИМАЛЬНАЯ СКОРОСТЬ ОТНОСИТЕЛЬНО БУЕВ | MAXIMUM VELOCITY RELATIVE TO BUOYS | WAYU/WAYU_Pinger_Specification_en.md (+3) | Variants MAX. RELATIVE VELOCITY / MAX. RELATIVE SPEED |
| МАКСИМАЛЬНЫЙ РАЗМЕР РАБОЧЕЙ ОБЛАСТИ | MAXIMUM WORKING AREA SIZE | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| МАКСИМАЛЬНОЕ ВРЕМЯ АВТОНОМНОЙ РАБОТЫ (В РЕЖИМЕ ПРИЕМА / В СМЕШАННОМ РЕЖИМЕ …) | MAXIMUM BATTERY LIFE (RX MODE / MIXED MODE …) | RedPhone/RedPhone_OS_Specification_en.md (+7) | Keep the RU qualifiers, e.g. `(20% TX, 80% RX)`; variant BATTERY LIFE / MAXIMUM TIME OF OPERATION |
| МАКСИМАЛЬНОЕ ВНЕШНЕЕ ГИДРОСТАТИЧЕСКОЕ ДАВЛЕНИЕ | MAXIMUM EXTERNAL HYDROSTATIC PRESSURE | Transducers/R_1.d3505_1_Specification_en.md | |
| НОМИНАЛЬНАЯ ПОГРЕШНОСТЬ ПО ГЛУБИНЕ | NOMINAL DEPTH ACCURACY | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ ГОРИЗОНТАЛЬНОГО УГЛА ПРИХОДА СИГНАЛА | NOMINAL HORIZONTAL ANGLE OF ARRIVAL ACCURACY | Zima/Zima2B_Specification_en.md | RU source spells `СИНГНАЛА`; existing HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.) |
| НОМИНАЛЬНАЯ ГОРИЗОНТАЛЬНАЯ ПОГРЕШНОСТЬ (2DRMS) | NOMINAL HORIZONTAL ACCURACY (2DRMS) | RedWAVE/RedNAV_Specification_en.md (+1) | Variant NOMINAL 2D-ACCURACY |
| НОМИНАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ ГЕОГРАФИЧЕСКОГО ПОЛОЖЕНИЯ | NOMINAL POSITION UPDATE RATE | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| НОМИНАЛЬНОЕ ВРЕМЯ ДО ПЕРВОГО УТОЧНЕНИЯ МЕСТОПОЛОЖЕНИЯ | NOMINAL TIME TO FIRST FIX | RedWAVE/RedNAV_Specification_en.md (+1) | CONFLICT: **NOMINAL TIME TO FIRST FIX** / MINIMAL TIME TO FIRST POSITION FIX (wrong qualifier) |
| НОМИНАЛЬНОЕ ВРЕМЯ СТАРТА; ВРЕМЯ СТАРТА | NOMINAL STARTUP TIME; STARTUP TIME | uWAVE/uWAVE_Max_Specification_en.md (+3) | Variants RATED STARTUP TIME / RATE STARTUP TIME (typo) |
| РАЗРЕШЕНИЕ ПО ГЛУБИНЕ; РАЗРЕШЕНИЕ ДАТЧИКА ГЛУБИНЫ (локально / удаленно) | DEPTH RESOLUTION; DEPTH SENSOR RESOLUTION (local / remote) | RWLT/RWLT_Pinger_K_Specification_en.md |  |
| РАЗРЕШЕНИЕ ПРИ ИЗМЕРЕНИИ ВРЕМЕНИ РАСПРОСТРАНЕНИЯ СИГНАЛА | SIGNAL PROPAGATION TIME MEASUREMENT RESOLUTION | uWAVE/uWAVE_Max_Specification_en.md (+1) |  |
| РАЗРЕШЕНИЕ ПРИ ИЗМЕРЕНИИ НАКЛОННОЙ ДАЛЬНОСТИ | SLANT RANGE MEASUREMENT RESOLUTION | Zima/Zima2B_Specification_en.md | Existing SLANT RANGE RESOLUTION |
| ТОЧНОСТЬ ВСТРОЕННОГО ДАТЧИКА ТЕМПЕРАТУРЫ | BUILT-IN TEMPERATURE SENSOR ACCURACY | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | OPERATING TEMPERATURE RANGE | A3S/A3R_Datasheet_en.md (+17) | CONFLICT: **OPERATING TEMPERATURE RANGE** (newest files, industry standard) / WORKING TEMPERATURE RANGE (39 files, older) / WORKING TEMPERATURES |
| НАПРЯЖЕНИЕ ПИТАНИЯ | SUPPLY VOLTAGE | A3S/A3R_Datasheet_en.md (+7) | Variant POWER SUPPLY |
| ДИАПАЗОН РАБОЧИХ НАПРЯЖЕНИЙ | OPERATING VOLTAGE RANGE | — | |
| НАПРЯЖЕНИЕ ЛИНИИ (ЛИНИЙ) ДАННЫХ | DATA LINE VOLTAGE | uWAVE/uWAVE_Specification_en.md (+5) |  |
| ВЫХОДНОЕ СОПРОТИВЛЕНИЕ ЛИНИЙ ДАННЫХ | DATA LINE OUTPUT IMPEDANCE | RedWAVE/RedNODE_Specification_en.md (+2) |  |
| ЭНЕРГОПОТРЕБЛЕНИЕ (Rx/Tx); ПОТРЕБЛЯЕМАЯ МОЩНОСТЬ | POWER CONSUMPTION (Rx/Tx) | A3S/A3R_Datasheet_en.md (+2) |  |
| ПОТРЕБЛЯЕМЫЙ ТОК | CURRENT CONSUMPTION | WAYU/WAYU_RF_Dongle_Specification_en.md |  |
| НЕСУЩАЯ ЧАСТОТА; НЕСУЩАЯ | CARRIER FREQUENCY; CARRIER | A3S/A3R_Datasheet_en.md (+5) |  |
| НЕСУЩАЯ ЧАСТОТА, Гц / ПОЛОСА ЧАСТОТ, Гц / БОКОВАЯ ПОЛОСА / НОМЕР КАНАЛА | CARRIER FREQUENCY, Hz / BANDWIDTH, Hz / SIDEBAND / CHANNEL NUMBER | RedPhone/RedPhone_DX_Specification_en.md (+3) |  |
| ПОЛОСА ЧАСТОТ; РАБОЧАЯ ПОЛОСА ЧАСТОТ; ЧАСТОТНЫЙ ДИАПАЗОН | BANDWIDTH; OPERATING BANDWIDTH; FREQUENCY RANGE | uSwitch/uSwitch_Specification_en.md (+2) |  |
| ПОЛОСА ГОЛОСОВОГО СИГНАЛА | VOICE BANDWIDTH | RedPhone/RedPhone_OS_Specification_en.md (+2) |  |
| ЧИСЛО ПОДДЕРЖИВАЕМЫХ КАНАЛОВ | NUMBER OF SUPPORTED CHANNELS | RedPhone/RedPhone_OS_Specification_en.md (+2) |  |
| ПЕРЕКЛЮЧЕНИЕ КАНАЛОВ (СВЯЗИ) | CHANNEL SWITCHING | RedPhone/RedPhone_Specification_en.md |  |
| СКОРОСТЬ ПЕРЕДАЧИ ДАННЫХ | DATA RATE | uSwitch/uSwitch_Specification_en.md (+3) | Variants PAYLOAD DATA RATE / DATA TRANSFER RATE |
| ПРЕДЕЛЬНОЕ СООТНОШЕНИЕ СИГНАЛ/ШУМ (В ПОЛОСЕ) | MINIMUM SIGNAL-TO-NOISE RATIO (IN BAND) | RedWAVE/RedWAVE_DataBrief_en.md (+1) | Existing SNR; `предельное` = limiting value |
| СХЕМА РАЗДЕЛЕНИЯ АБОНЕНТОВ | MULTIPLE ACCESS SCHEME | uWAVE/uWAVE_Max_Specification_en.md (+1) | Existing SUBSCRIBERS DIVISION; `кодовое разделение абонентов` → `code division multiple access` |
| ДЛИТЕЛЬНОСТЬ НАВИГАЦИОННОГО СИГНАЛА; ДЛИТЕЛЬНОСТЬ ИМПУЛЬСА | NAVIGATION SIGNAL DURATION; PULSE DURATION | A3S/A3T_Datasheet_en.md (+3) |  |
| ПЕРИОД ИЗЛУЧЕНИЯ АКУСТИЧЕСКОГО СИГНАЛА | ACOUSTIC SIGNAL EMISSION PERIOD | WAYU/WAYU_Pinger_Specification_en.md (+1) |  |
| НЕСУЩАЯ ЧАСТОТА НАВИГАЦИОННОГО СИГНАЛА; ТИП МОДУЛЯЦИИ НАВИГАЦИОННОГО СИГНАЛА | NAVIGATION SIGNAL CARRIER FREQUENCY; NAVIGATION SIGNAL MODULATION TYPE | RedPhone/RedPhone_Specification_en.md (+1) |  |
| РЕФЕРЕНСНЫЙ ЭЛЛИПСОИД | REFERENCE ELLIPSOID | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| ИНТЕРФЕЙС; ИНТЕРФЕЙС СОПРЯЖЕНИЯ | INTERFACE | RedWAVE/RedNODE_Specification_en.md (+5) |  |
| ПРОТОКОЛ; ПРОТОКОЛ СОПРЯЖЕНИЯ; ИНФОРМАЦИОННЫЙ ПРОТОКОЛ | PROTOCOL; COMMUNICATION PROTOCOL | RWLT/RWLT_RF_Dongle_en.md (+4) |  |
| ПОДКЛЮЧЕНИЕ; РАДИОСВЯЗЬ | CONNECTION; RADIO COMMUNICATION | RWLT/RWLT_RF_Dongle_en.md (+2) |  |
| ВСТРОЕННЫЙ GNSS-модуль | BUILT-IN GNSS MODULE | RedWAVE/RedNAV_Specification_en.md (+1) | RU source spells `ВТСРОЕННЫЙ` |
| ДЛИНА КАБЕЛЯ; ДИАМЕТР КАБЕЛЯ; ТИП КАБЕЛЯ | CABLE LENGTH; CABLE DIAMETER; CABLE TYPE | Transducers/R_1.d3505_1_Specification_en.md (+7) |  |
| ДЛИНА КАБЕЛЯ ГИДРОАКУСТИЧЕСКОЙ АНТЕННЫ | TRANSDUCER CABLE LENGTH | F4105/F4105_SU_Specification_en.md (+1) |  |
| МАТЕРИАЛ ИЗОЛЯЦИИ КАБЕЛЯ (КАБЕЛЕЙ) | CABLE INSULATION MATERIAL | Transducers/R_1.d3505_1_Specification_en.md (+1) |  |
| МАТЕРИАЛ КОРПУСА | HOUSING MATERIAL | RedWAVE/RedBASE_Specification_en.md | CONFLICT: **HOUSING MATERIAL** (industry standard, newest) / BODY MATERIAL (7 files) |
| МАТЕРИАЛ ЗАЩИТНОГО КОМПАУНДА; ТОЛЩИНА ЗАЩИТНОГО СЛОЯ КОМПАУНДА | POTTING COMPOUND MATERIAL; POTTING COMPOUND THICKNESS | Accessories/RS422_extension_cable_en.md | Existing PROTECTIVE COATING MATERIAL |
| ИСПОЛНЕНИЕ (пыле-/влагозащита) | PROTECTION CLASS | RedPhone/RedPhone_Specification_en.md (+1) | Variant DUST/WATERPROOF |
| ТИП (ВСТРОЕННОГО) АКБ; ЕМКОСТЬ ВСТРОЕННОГО АКБ | (BUILT-IN) BATTERY TYPE; BUILT-IN BATTERY CAPACITY | F4105/F4105_SU_Specification_en.md | `АКБ` → battery |
| ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ | ELECTRICAL CAPACITANCE (transducers) / ENERGY CAPACITY (batteries, W·h) | Transducers/R_1.d3505_1_Specification_en.md | Decide by the unit |
| ЗАЩИТНЫЙ ИНТЕРВАЛ ПОСЛЕ ДЕТЕКТИРОВАНИЯ СИГНАЛА | LOCKOUT INTERVAL AFTER SIGNAL DETECTION | A3S/A3R_Datasheet_en.md | |
| КРЕПЛЕНИЕ | MOUNTING | RedPhone/RedPhone_RF_Dongle_Specification_en.md |  |
| ЦВЕТ КОРПУСА | HOUSING COLOR | Accessories/uPress_Specification_en.md | |
| Единицы измерения | Units | uWAVE/uWAVE_Family_en.md (+1) |  |
| Диапазон / Разрешение | Range / Resolution | RWLT/uTrackDiver_Users_Manual_en.md (+1) |  |
| Поле/Параметр | Field/Parameter | RedWAVE/RedWAVE_Protocol_Specification_en.md | Protocol tables |
| Идентификатор | ID | RWLT/uNav_application_Users_manual_en.md (+1) | Protocol tables |
| Тип устройства | Device type | RedGTR/RedGTR_Protocol_Specifications_en.md |  |
| Версия встроенного ПО; Актуальная версия ПО | Firmware version; Current firmware version | uWAVE/uWAVE_version_history_en.md | Variant Actual FW version (false friend) |
| Дата / Статус / Количество | Date / Status / Quantity | uWAVE/uWAVE_version_history_en.md (+1) |  |
| Индикатор; Режим/состояние | Indicator; Mode/state | WAYU/WAYU_Users_Manual_en.md | |
| Распространяется на устройства / Документ | Applies to / Document | misc_en.md | Variant Devices / File |
| Сайт технической документации / Техническая поддержка | Technical documentation website / Technical support | — | Passports |

## 7. Protocol documents

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Протокол физического уровня | Physical layer protocol | Zima/Zima2_Protocol_Specification_en.md (+4) | CONFLICT: **Physical layer protocol** (literal) / Physical layer (4) / Physical protocol |
| Стандарт протокола диалогового уровня NMEA0183 | NMEA0183 dialog layer protocol standard | Zima/Zima2_Protocol_Specification_en.md | CONFLICT: **NMEA0183 dialog layer protocol standard** / NMEA0183 Protocol standard (5, drops `диалогового уровня`) |
| Система команд AZM | AZM command system | Zima/Zima2_Protocol_Specification_en.md | Same pattern for ZMA, UWV, UNV, RPH, TNT; variant AZM Protocol |
| сообщение (NMEA) | sentence | RedWAVE/RedWAVE_Protocol_Specification_en.md | `Дополнительные сообщения` → `Additional sentences`; `Основные и часто употребляемые сообщения` → `Main and frequently used sentences` |
| Таблицы идентификаторов; Идентификаторы | Identifier tables; Identifiers | uWAVE/uWAVE_Protocol_Specification_en.md (+5) |  |
| Идентификаторы локальных данных | Local data identifiers | RedGTR/RedGTR_Protocol_Specifications_en.md (+3) |  |
| Идентификаторы адресных / широковещательных / удаленных команд | Addressed / broadcast / remote command identifiers | Zima/Zima2_Protocol_Specification_en.md (+1) | |
| Идентификаторы ответов | Response identifiers | Zima/Zima2_Protocol_Specification_en.md | |
| Идентификаторы (сервисных) операций | Service action identifiers | RedWAVE/RedWAVE_Protocol_Specification_en.md (+1) |  |
| Идентификаторы устройств | Device type identifiers | RedGTR/RedGTR_Protocol_Specifications_en.md | |
| Типы датчиков давления | Pressure sensor types | Zima/Zima2_Protocol_Specification_en.md | |
| Типы уточнений географического положения | Fix types | RedWAVE/RedWAVE_Protocol_Specification_en.md | |
| реакция устройства | device response | uWAVE/uWAVE_Protocol_Specification_en.md | `IC_D2H_ACK - реакция устройства` |
| запрос / ответ / удаленный абонент | request / response / remote subscriber | uWAVE/uWAVE_Protocol_Specification_en.md | |
| превышен интервал ожидания ответа | response timeout | uWAVE/uWAVE_Protocol_Specification_en.md | |
| Командный режим / Пакетный режим / Режим прозрачного канала / Сервисный режим / Навигационный режим | Command mode / Packet mode / Transparent channel mode / Service mode / Navigation mode | uWAVE/uWAVE_Family_en.md (+5) |  |
| Режимы работы устройства | Device operating modes | uWAVE/uWAVE_Protocol_Specification_en.md | Variant Working modes |
| Скоростные режимы | Data rate modes | uWAVE/uWAVE_Modems_comparison_en.md | |
| Удаленные команды | Remote commands | uWAVE/uWAVE_Protocol_Specification_en.md | |
| Требования к протоколу | Protocol requirements | Zima/Zima_GNSS_requirements_en.md | |
| кодовое разделение | code division | Zima/Zima2B_Specification_en.md | |
| многолучевое распространение | multipath propagation | — | |
| угол прихода (сигнала) | angle of arrival | Zima/Zima2B_Specification_en.md | |
| уточнение местоположения | position fix | — | |

## 8. Software user's manuals

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Интерфейс и функции приложения | Application interface and functions | RWLT/uNav_application_Users_manual_en.md (+1) |  |
| Настройки приложения | Application settings | RWLT/uNav_application_Users_manual_en.md (+1) |  |
| Главное окно (приложения) | Main (application) window | RWLT/uTrackDiver_Users_Manual_en.md |  |
| Главная панель инструментов / Панель инструментов карты / Панель инструментов | Main toolbar / Map toolbar / Toolbar | RWLT/uNav_application_Users_manual_en.md (+2) |  |
| Панель карты / Поле легенды / Линейка масштаба / Строка статуса | Map panel / Legend field / Scale bar / Status line | RWLT/uNav_application_Users_manual_en.md (+1) |  |
| Панель журнала; Поле журнала | Log panel; Log field | RWLT/uNav_application_Users_manual_en.md (+1) |  |
| Панель / Поле дополнительной информации | Additional information panel / field | RWLT/uTrackDiver_Users_Manual_en.md |  |
| Вкладка | tab | RWLT/uNav_application_Users_manual_en.md | `Вкладка ❗ CONNECTION` → `❗ CONNECTION tab` |
| Пункт (меню) | menu item | Zima/Zima_Users_manual_en.md | `Пункт НАСТРОЙКИ` → `SETTINGS menu item` (use the real UI label) |
| Список водолазов | Diver list | RWLT/uTrackDiver_Users_Manual_en.md | |
| Работа в абсолютных / относительных координатах | Working in absolute / relative coordinates | Zima/Zima2_DataBrief_en.md (+1) |  |
| Подготовка подводного оборудования | Preparing the underwater equipment | WAYU/WAYU_Users_Manual_en.md (+1) |  |
| Подготовка к работе радиодонгла | Preparing the radio dongle for operation | WAYU/WAYU_Users_Manual_en.md (+1) |  |
| Расположение буев на поверхности воды | Positioning the buoys on the water surface | WAYU/WAYU_Users_Manual_en.md (+1) |  |
| Выбор места для расположения пульта оператора | Selecting a location for the operator console | WAYU/WAYU_Users_Manual_en.md (+1) |  |
| Расположение и настройка пеленгационной антенны | Positioning and setting up the direction-finding antenna | — | |
| Расположение маяка на носителе | Mounting the responder-beacon on the carrier | Zima/Zima2_Users_manual_en.md | |
| Калибровка углового расхождения | Angular misalignment calibration | Zima/Zima2_Users_manual_en.md | Existing EN heading at this number is a different section (misaligned) |
| Запуск в качестве службы Windows | Running as a Windows service | — | AzimuthConsole |
| Обновление приложения | Updating the application | — | |
| Скрипты / Примеры скриптов | Scripts / Script examples | — | |
| носитель | carrier (vehicle) | Zima/Zima2_Users_manual_en.md | The vehicle or vessel carrying a beacon |
| ТНПА / АНПА | ROV / AUV | RedWAVE/RedNODE_Specification_en.md | |
| ПО / ПК | software / PC | — | `ПО ZHost` → `ZHost software` |
| сервисный кабель | service cable | RWLT/RWLT_Users_Manual_en.md | |
| сросток | splice | — | Cable splice |
| неопресненный | not rinsed with fresh water | — | Storage instructions |

## 9. Product passports, warranty and safety data sheets

### 9.1 Product passports (templates)

| RU | EN | Source EN file | Note |
|---|---|---|---|
| ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛАБОРАТОРИЯ ПОДВОДНОЙ СВЯЗИ И НАВИГАЦИИ"; ООО "Лаборатория подводной связи и навигации" | UCNL LLC | — | Official English legal name; passport title block, approval block, MSDS supplier details |
| УТВЕРЖДАЮ | APPROVED | — | Approval block of the passport form |
| Руководитель R&D OOO "Лаборатория подводной связи и навигации" | Head of R&D, UCNL LLC | — | |
| Главный инженер OOO "Лаборатория подводной связи и навигации" | Chief Engineer, UCNL LLC | — | |
| `"____" ______________ 20 ___ г.` | `"____" ______________ 20 ___` | — | Keep the blank form exactly; drop only the Russian `г.` |
| ОСНОВНЫЕ СВЕДЕНИЯ ОБ ИЗДЕЛИИ | GENERAL INFORMATION ABOUT THE PRODUCT | — | |
| Технические характеристики и документация | Specifications and documentation | — | |
| КОМПЛЕКТНОСТЬ. ЗАВОДСКИЕ И СЕРИЙНЫЕ (РЕГИСТРАЦИОННЫЕ) НОМЕРА. СВИДЕТЕЛЬСТВО О ПРОИЗВОДСТВЕ, УПАКОВЫВАНИИ | DELIVERY SET. FACTORY AND SERIAL (REGISTRATION) NUMBERS. CERTIFICATE OF MANUFACTURE AND PACKING | — | |
| Дата производства комплекта / Упаковано и проверено по составу комплекта / Упаковщик | Kit production date / Packed and checked against the delivery set / Packer | — | |
| Расположение заводских и серийных (регистрационных) номеров | Location of factory and serial (registration) numbers | — | |
| Состав комплекта. Перечень заводских и серийных номеров изделий в составе комплекта | Delivery set contents. List of factory and serial numbers of the items in the set | — | |
| заводской номер / серийный (регистрационный) номер | factory number / serial (registration) number | — | |
| горячее клеймение | hot stamping | — | |
| ГАРАНТИИ ИЗГОТОВИТЕЛЯ. СРОК СЛУЖБЫ ИЗДЕЛИЯ | MANUFACTURER'S WARRANTY. SERVICE LIFE | — | |
| срок гарантийных обязательств / гарантийный срок | warranty period | — | |
| скрытые недостатки | latent defects | — | |
| акт сдачи-приемки / акт передачи продукции в ремонт | acceptance certificate / certificate of transfer for repair | — | |
| Поставщик / Заказчик | Supplier / Customer | — | Capitalized as in RU |
| ЗАМЕТКИ ПО ЭКСПЛУАТАЦИИ И ХРАНЕНИЮ | NOTES ON OPERATION AND STORAGE | — | |
| Сведения о взаимозаменяемости | Interchangeability | — | |
| Особые требования к хранению | Special storage requirements | — | |
| Перечень особых мер безопасности при работе | Special safety precautions during operation | — | |
| Межотраслевые правила по охране труда при проведении водолазных/подводных работ | Intersectoral occupational safety rules for diving/underwater operations | — | Russian regulation: keep and record per rule 6 |
| средство спасения и средство жизнеобеспечения | rescue or life-support equipment | — | |

### 9.2 Material safety data sheets

Section headings follow the standard 16-section layout of GHS/REACH Annex II safety data sheets. Several existing EN MSDS headings are non-standard; the canonical column gives the standard wording.

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Паспорт безопасности химической продукции (MSDS) | Material safety data sheet (MSDS) | Misc/BatLinkBox_MSDS_en.md (+10) | CONFLICT: **Material safety data sheet** / Material safety datasheet (existing) |
| MSDS (Паспорта безопасности) | MSDS (Material safety data sheets) | misc_en.md | |
| ИДЕНТИФИКАЦИЯ ХИМИЧЕСКОЙ ПРОДУКЦИИ И СВЕДЕНИЯ О ПРОИЗВОДИТЕЛЕ ИЛИ ПОСТАВЩИКЕ | IDENTIFICATION OF THE PRODUCT AND OF THE COMPANY OR SUPPLIER | Misc/*_MSDS_en.md (6) | |
| ИДЕНТИФИКАЦИЯ ОПАСНОСТИ (ОПАСНОСТЕЙ) | HAZARD(S) IDENTIFICATION | Misc/*_MSDS_en.md (6) | Existing Identification of danger(s) |
| СОСТАВ (ИНФОРМАЦИЯ О КОМПОНЕНТАХ) | COMPOSITION (INFORMATION ON INGREDIENTS) | Misc/*_MSDS_en.md (6) | |
| МЕРЫ ПО ОКАЗАНИЮ ПЕРВОЙ ПОМОЩИ | FIRST-AID MEASURES | Misc/*_MSDS_en.md (6) | Existing MEASURES FOR FIRST AID |
| МЕРЫ И СРЕДСТВА ОБЕСПЕЧЕНИЯ ПОЖАРОВЗРЫВОБЕЗОПАСНОСТИ | FIRE AND EXPLOSION SAFETY MEASURES AND EQUIPMENT | Misc/*_MSDS_en.md (6) | Existing MEASURES AND FIRE-FIGHTING |
| МЕРЫ ПО ПРЕДОТВРАЩЕНИЮ И ЛИКВИДАЦИИ АВАРИЙНЫХ И ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ И ИХ ПОСЛЕДСТВИЙ | MEASURES TO PREVENT AND ELIMINATE ACCIDENTS AND EMERGENCIES AND THEIR CONSEQUENCES | Misc/*_MSDS_en.md (6) | Existing MEASURES FOR THE PREVENTION AND ELIMINATION OF ACCIDENTAL AND THEIR CONSEQUENCES (word missing) |
| ПРАВИЛА ХРАНЕНИЯ ХИМИЧЕСКОЙ ПРОДУКЦИИ И ОБРАЩЕНИЯ С НЕЙ ПРИ ПОГРУЗОЧНО-РАЗГРУЗОЧНЫХ РАБОТАХ | RULES FOR STORAGE AND HANDLING OF THE CHEMICAL PRODUCT DURING LOADING AND UNLOADING | Misc/*_MSDS_en.md (6) | |
| СРЕДСТВА КОНТРОЛЯ ЗА ОПАСНЫМ ВОЗДЕЙСТВИЕМ И СРЕДСТВА ИНДИВИДУАЛЬНОЙ ЗАЩИТЫ | EXPOSURE CONTROLS AND PERSONAL PROTECTION | Misc/*_MSDS_en.md (6) | Existing CONTROLS EXPOSURE AND PERSONAL PROTECTION |
| ФИЗИКО-ХИМИЧЕСКИЕ СВОЙСТВА | PHYSICAL AND CHEMICAL PROPERTIES | Misc/*_MSDS_en.md (6) | Existing PHYSIOCHEMICAL PROPERTIES (typo) |
| СТАБИЛЬНОСТЬ И РЕАКЦИОННАЯ СПОСОБНОСТЬ | STABILITY AND REACTIVITY | Misc/*_MSDS_en.md (6) | |
| ИНФОРМАЦИЯ О ТОКСИЧНОСТИ | TOXICOLOGICAL INFORMATION | Misc/*_MSDS_en.md (6) | |
| ИНФОРМАЦИЯ О ВОЗДЕЙСТВИИ НА ОКРУЖАЮЩУЮ СРЕДУ | ECOLOGICAL INFORMATION | Misc/*_MSDS_en.md (6) | Existing INFORMATION ON ECOLOGICAL |
| РЕКОМЕНДАЦИИ ПО УДАЛЕНИЮ ОТХОДОВ (ОСТАТКОВ) | DISPOSAL CONSIDERATIONS | Misc/*_MSDS_en.md (6) | Existing DISPOSAL CONSIDERATIONS (EWC); keep `(EWC)` only if RU has it |
| ИНФОРМАЦИЯ ПРИ ПЕРЕВОЗКАХ (ТРАНСПОРТИРОВАНИИ) | TRANSPORT INFORMATION | Misc/*_MSDS_en.md (6) | Existing INFORMATION (AIR TRANSPORT) |
| ИНФОРМАЦИЯ О НАЦИОНАЛЬНОМ И МЕЖДУНАРОДНОМ ЗАКОНОДАТЕЛЬСТВЕ | INFORMATION ON NATIONAL AND INTERNATIONAL LEGISLATION | Misc/*_MSDS_en.md (6) | Existing INFORMATION ON NATIONAL AND INTERNATIONAL LAW |
| Безопасность, здоровье и экологическая законодательство/регламенты характерные для данного вещества или смеси | Safety, health and environmental regulations/legislation specific for the substance or mixture | Misc/*_MSDS_en.md (6) | |
| Транспортировка емкостей в соответствии с Приложением II из MARPOL 73/78 и Кодексом КСГМГ | Transport in bulk according to Annex II of MARPOL 73/78 and the IBC Code | Misc/*_MSDS_en.md (6) | `КСГМГ` → `IBC Code` |
| Другая информация | Other information | Misc/*_MSDS_en.md (6) | |
| Торговое наименование / Номер статьи / Номер регистрации (REACH) / Номер ЕС / Номер CAS | Trade name / Article number / Registration number (REACH) / EC number / CAS number | Misc/*_MSDS_en.md (9) | `Эта информация не доступна` → `This information is not available` |
| Установленные применения | Identified uses | Misc/*_MSDS_en.md (3) | Existing Installed applications (wrong) |
| Соответствующие установленным применения вещества или смеси и противопоказания к применению | Relevant identified uses of the substance or mixture and uses advised against | Misc/*_MSDS_en.md (6) | Existing The corresponding set of the substance or mixture and contraindications |
| Подробная информация о поставщике в паспорте безопасности | Details of the supplier of the safety data sheet | Misc/*_MSDS_en.md (6) | |
| Номер телефона экстренных служб | Emergency telephone number | Misc/*_MSDS_en.md (3) | Existing Emergency numbers |
| Электронная почта / Веб-сайт / Факс | E-mail / Website / Fax | Misc/*_MSDS_en.md (3) | Existing Fax machine (wrong) |
| Классификация вещества или смеси / Элементы маркировки / Другие опасности | Classification of the substance or mixture / Label elements / Other hazards | Misc/*_MSDS_en.md (6) | |
| Вещества | Substances | Misc/*_MSDS_en.md (6) | |
| Используемые элементы (ячейки) | Cells used | Misc/*_MSDS_en.md (3) | Existing Cell Configuration |
| Описание мер первой помощи | Description of first-aid measures | Misc/*_MSDS_en.md (6) | |
| Наиболее важные симптомы и воздействия, как острые, так и замедленные | Most important symptoms and effects, both acute and delayed | Misc/*_MSDS_en.md (6) | |
| Указание на необходимость немедленной медицинской помощи и специального лечения | Indication of any immediate medical attention and special treatment needed | Misc/*_MSDS_en.md (6) | |
| Средства пожаротушения / Особые опасности, создаваемые веществом или смесью / Рекомендации для пожарных | Extinguishing media / Special hazards arising from the substance or mixture / Advice for firefighters | Misc/*_MSDS_en.md (6) | |
| Меры личной безопасности, защитное снаряжение и чрезвычайные меры | Personal precautions, protective equipment and emergency procedures | Misc/*_MSDS_en.md (6) | |
| Экологические меры предосторожности / Методы и материалы для локализации и очистки | Environmental precautions / Methods and material for containment and cleaning up | Misc/*_MSDS_en.md (6) | |
| Меры предосторожности по безопасному обращению / Условия для безопасного хранения с учетом любых несовместимостей / Специфическое(ие) конечное(ые) применение(ия) | Precautions for safe handling / Conditions for safe storage, including any incompatibilities / Specific end use(s) | Misc/*_MSDS_en.md (6) | |
| Инженерно-технические средства контроля / Средства индивидуальной защиты | Engineering controls / Personal protective equipment | Misc/*_MSDS_en.md (6) | |
| Информация об основных физических и химических свойств | Information on basic physical and chemical properties | Misc/*_MSDS_en.md (6) | RU source has the ungrammatical `свойств` |
| Агрегатное состояние / Запах / Порог запаха / рН (значение) | Physical state / Odor / Odor threshold / pH (value) | Misc/*_MSDS_en.md (3) | US spelling `odor`; existing Smell |
| Точка плавления/замерзания / Начальная температура кипения и интервал кипения / Температура вспышки в закрытом тигле | Melting point/freezing point / Initial boiling point and boiling range / Flash point (closed cup) | Misc/*_MSDS_en.md (3) | |
| Интенсивность испарения / Воспламеняемость (твердое вещество, газ) / Пределы взрываемости | Evaporation rate / Flammability (solid, gas) / Explosive limits | Misc/*_MSDS_en.md (3) | Existing lammability (typo) |
| верхний предел взрыва (ВПВ) / нижний предел взрывоопасности (НПВ) | upper explosive limit (UEL) / lower explosive limit (LEL) | Misc/*_MSDS_en.md (3) | |
| Давление паров / Плотность пара / Относительная плотность / Объемная плотность | Vapor pressure / Vapor density / Relative density / Bulk density | Misc/*_MSDS_en.md (3) | |
| Растворимость(и) / Растворимость в воде / Коэффициент распределения / н-октанол / вода (log KOW) | Solubility(ies) / Solubility in water / Partition coefficient / n-octanol/water (log KOW) | Misc/*_MSDS_en.md (3) | Existing Solubility (u), Distribution factor (wrong) |
| Температура самовоспламенения / Температура разложения / Вязкость / Окисляющие свойства | Auto-ignition temperature / Decomposition temperature / Viscosity / Oxidizing properties | Misc/*_MSDS_en.md (3) | US spelling `oxidizing` |
| Химическая активность / Несовместимость с другими веществами / Условия, действия которых следует избегать | Reactivity / Incompatibility with other substances / Conditions to avoid | Misc/*_MSDS_en.md (6) | Existing The conditions of action that should be avoided |
| Токсичность / Оценка химической безопасности | Toxicity / Chemical safety assessment | Misc/*_MSDS_en.md (6) | |
| Методы утилизации отходов | Waste treatment methods | Misc/*_MSDS_en.md (6) | |
| Номер ООН / Собственное транспортное наименование ООН / Класс(ы) опасности при транспортировке / Группа упаковки / Экологические опасности / Специальные меры предосторожности для пользователя | UN number / UN proper shipping name / Transport hazard class(es) / Packing group / Environmental hazards / Special precautions for user | Misc/*_MSDS_en.md (3) | Existing Packaging group |
| Информация по каждому из Типовых Регламентов ООН | Information for each of the UN Model Regulations | Misc/*_MSDS_en.md (6) | |
| ДОПОГ / МПОГ / ВОПОГ / МКМПОГ / ИКАО / СГС | ADR / RID / ADN / IMDG / ICAO / GHS | Misc/*_MSDS_en.md (3) | |
| Отказ от ответственности | Disclaimer | Misc/*_MSDS_en.md (6) | Existing Renunciation (wrong) |
| Описания используемых сокращений / Сокр. | Abbreviations used / Abbr. | Misc/*_MSDS_en.md (3) | |
| отсутствует | not applicable | Misc/*_MSDS_en.md (3) | Existing is absent |
| Литий / Фосфат железа | Lithium / Iron phosphate | Misc/*_MSDS_en.md (3) | |
| Аккумулятор высокотоковый литий-железофосфатный | High-current lithium iron phosphate (LiFePO4) battery | Misc/RedBase_v3_LiFEPO4_msds_en.md | Header cell |

## Added in batch redwave-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Буй-ретранслятор; Навигационный гидроакустический буй (RedBase) | GNSS-equipped sonobuoy; relay sonobuoy | RedWAVE/RedBASE_Specification_en.md, RedWAVE/RedNAV_Specification_en.md | RedBase header cell keeps `GNSS-equipped sonobuoy`; `буи-ретрансляторы` in running text = `relay sonobuoys` |
| Водолазный навигационный приемник (RedNav) | diver's navigation receiver | RedWAVE/RedNAV_Specification_en.md | Header cell; `Водолазный навигатор` = `diver's navigator` |
| Универсальный (интегрируемый) навигационный приемник (RedNode) | universal (integrated) navigation receiver | RedWAVE/RedWAVE_DataBrief_en.md | |
| плавучая длинная (навигационная) база | floating long (navigation) base | RedWAVE/RedWAVE_DataBrief_en.md (+2) | |
| ВЫНОСНОЙ БЛОК; ИНТЕРФЕЙСНЫЙ БЛОК | REMOTE UNIT; INTERFACE UNIT | RedWAVE/RedNAV_Specification_en.md | |
| СИНХРОНИЗАЦИЯ С ПК | SYNCHRONIZATION WITH PC | RedWAVE/RedNAV_Specification_en.md | |
| МАРШРУТНЫЕ ФУНКЦИИ; загружаемые точки | ROUTE FUNCTIONS; uploadable points | RedWAVE/RedNAV_Specification_en.md | |
| ПРЕДЕЛЬНОЕ СООТНОШЕНИЕ СИГНАЛ/ШУМ В ПОЛОСЕ | MINIMUM SIGNAL-TO-NOISE RATIO (IN BAND) | RedWAVE/RedNAV_Specification_en.md | |
| МАКСИМАЛЬНАЯ СКОРОСТЬ ОТНОСИТЕЛЬНО ПРИЕМНИКОВ | MAXIMUM VELOCITY RELATIVE TO RECEIVERS | RedWAVE/RedBASE_Specification_en.md | |
| ДЛИНА КАБЕЛЯ ГИДРОАКУСТИЧЕСКОГО ПЕРЕДАТЧИКА | UNDERWATER ACOUSTIC TRANSMITTER CABLE LENGTH | RedWAVE/RedBASE_Specification_en.md | |
| ВРЕМЯ ПОЛНОЙ ЗАРЯДКИ ОТ СЕТИ 220 В / 50 Гц | FULL CHARGE TIME FROM 220 V / 50 Hz MAINS | RedWAVE/RedBASE_Specification_en.md | |
| блоки дополнительной плавучести; якорная веревка; батарейный блок | additional buoyancy blocks; anchor line; battery block | RedWAVE/RedBASE_Specification_en.md | |
| залитый в полиуретановый компаунд | potted in a polyurethane compound | RedWAVE/RedBASE_Specification_en.md | |
| Свинцово-кислотный (АКБ) | Lead-acid | RedWAVE/RedBASE_old_Specification_en.md | |
| зарядная площадка | charging pad | RedWAVE/RedNAV_Host_Users_Manual_en.md | |
| RedNav Host UI | Search in base, Search, OK, Save, Download, Upload to device, Waypoints, Right-handed device, State: connected | RedWAVE/RedNAV_Host_Users_Manual_en.md | Real English strings (`MainForm.resx`, `MainFormStrings.resx` of github.com/ucnl/RedNavHost); RU "Переворот экрана" = `Right-handed device` |
| Windows 10 Bluetooth UI | Start -> Settings -> Devices, On, + Add Bluetooth or other device, Pair, Next, Connected | RedWAVE/RedNAV_Host_Users_Manual_en.md | |
| Управление выдачей сообщений | Sentence output control | RedWAVE/RedWAVE_Protocol_Specification_en.md | |
| Превышен интервал ожидания | Waiting interval exceeded | RedWAVE/RedWAVE_Protocol_Specification_en.md | |
| Ускорение свободного падения | Gravitational acceleration | RedWAVE/RedWAVE_Protocol_Specification_en.md | As in the uWave protocol |
