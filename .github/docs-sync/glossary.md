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

Keep verbatim. **Maintainer decision (2026-10-09): product names are always written in mixed case in EN text** — `uWave`, `uWave Max`, `uWave Max OEM`, `uWave USBL Modem`, `RedWave`, `RedBase`, `RedNode`, `RedNav`, `RedLine`, `Zima`, `Zima-B` — never `uWAVE`, `RedWAVE`, `RedBASE`, `RedNODE`, `RedNAV`, `RedLINE`, `ZIMA`, even where RU writes them in capitals (running text, link texts, breadcrumbs, titles, header cells). Acronym names stay as they are (`RWLT`, `WAYU`, `A3S`, `F4105`, `RedGTR`, `GIB`). File names, directory names, link targets, URLs, image paths, code blocks and identifiers (`uWAVE_ALib`, `uWAVELib`, `RedBASE_Config`) are not changed. Labels that RU writes entirely in ALL CAPS stay ALL CAPS. `docsync.py check` reports violations as `product name case`.

**Systems and devices:** Zima, Zima USBL, Zima-B, Zima-R, Zima-R 1000, Zima2, Zima2 USBL, Zima2 LBL, Zima2-B, Zima2-R, Zima2-uR, Zima2-L, Zima2-LX, Zima2-SL, Zima2-B35, Zima2-R35, Zima2-BK, Zima2-RK, Zima2K, Zima2-35, Zima2-OEM35, Bat&Link Box, uWave, uWave Max, uWave Max OEM, uWave USBL Modem, uSwitch, RedLine, RedGTR, RedWave, RedBase, RedNode, RedNav, Aquatab S, RedPhone, RedPhone-OS, RedPhone-DX, RedPhone-D, RedPhone-MOS, RedPhone-MDX, RedPhone RF Dongle, Phone-T, Phone-S, RWLT, RWLT Pinger, RWLT Pinger-K, RWLT GIB, uNav RWLT Radio dongle, uNav WAYU Radio dongle, WAYU, WAYU Pinger, WAYU GIB, ACubes A<sup>3</sup>S (A3S), A³R (ACubes AR), A³T (ACubes AT), F4105, F4105-SU, F4105-BU, F4105-AU, uPress, uSpeak, uWire, uClamp, uClamp-S, uBat, Crimea-300, Crimea-300 OS.

**Model codes and part numbers:** SB-23-64-LI, SB-24-48-LF, RT-1.332820-1, RT-1.332820-2, RT-2.332820-1, RT-2.332820-2, RT-1.524525-1, RT-1.524525-1-FF, RT-1.524525-2, R-1.d3505-1, PMVR.134097.002, PMVR.134098.002, patent numbers (`RU2659299C1`), connector designators (`XS1`, `XP2`), and every other alphanumeric code exactly as in RU.

**Software:** AzimuthSuite, AzimuthConsole, AzimuthConsole v1.x, AzimuthWebSuite, ZHost, uGPSHub (repository and release `UGPSHub`), RedBASE_Config, RedNav Host (repository `RedNavHost`), uNav, uNav application, uTrackDiver, uWaver, uBear, uWaveCommander, uWAVE_ALib, uWAVE_Arduino, uConsole, uGNSS-Monitor, RedPhoneDXConfig, RedPhoneDXConfig-Web, RedLINE_Host, WAYU (host application).

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
| Буй-ретранслятор; Навигационный гидроакустический буй | GNSS-equipped sonobuoy | RedWAVE/RedBASE_Specification_en.md | RedBase; established EN product description |
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

## Added in batch zima-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| штанга; опускная штанга | pole; deployment pole | Zima/Zima2_DataBrief_en.md (+1) | Antenna mounting pole over the side of a vessel; not `rod`/`boom` |
| точка топопривязки | position reference point | Zima/Zima2_DataBrief_en.md (+1) | |
| угловое смещение нуля антенны и GNSS-компаса | angular offset between the antenna zero and the GNSS compass | Zima/Zima2_DataBrief_en.md | |
| Базовая станция пеленгования | direction-finding base station | Zima/Zima2_DataBrief_en.md | |
| удлинитель UART-RS422 | UART-RS422 extension cable | Zima/Zima2_DataBrief_en.md | |
| провис (кабеля) | slack | Zima/Zima2_Users_manual_en.md | Not `sag` |
| струи движетелей | thruster/propeller wash | Zima/Zima2_Users_manual_en.md | |
| обитаемые подводные аппараты (ОПА) | human-occupied vehicles (HOVs) | Zima/Zima2_Users_manual_en.md | |
| дайверы и технические водолазы | recreational and technical divers | Zima/Zima2_Users_manual_en.md | |
| нормобарический корпус | one-atmosphere (normobaric) housing | Zima/Zima2_Users_manual_en.md | |
| антенна маяка | transducer (of the beacon) | Zima/Zima2_Users_manual_en.md | The direction-finding antenna stays `antenna` |
| надводный / подводный разъем | topside / underwater connector | Zima/Zima2_Users_manual_en.md | |
| состыковать / разомкнуть разъем | mate / unmate the connector | Zima/Zima2_Users_manual_en.md | |
| литьевой шов | molding seam | Zima/Zima2_Users_manual_en.md | |
| выборка (на кронштейне) | cutout | Zima/Zima2_Users_manual_en.md | |
| транспортировочные заглушки | transport plugs | Zima/Zima2_Users_manual_en.md | |
| транспортировочная тара | transport case | Zima/Zima2_Users_manual_en.md | |
| самостоятельный ремонт | unauthorized repair | Zima/Zima2_Users_manual_en.md | Warranty wording |
| круговое вероятное отклонение | circular error probable | Zima/Zima2_Users_manual_en.md | RU uses it to define DRMS; translated as written, question raised |
| угловая поправка | angular correction | Zima/Zima2_Users_manual_en.md | AzimuthSuite field label, not confirmed against the English UI |
| Взаимодействие с системой | Interacting with the system | Zima/Zima2_Users_manual_en.md | |
| Ручное задание координат и направления | Manual setting of coordinates and direction | Zima/Zima2_Users_manual_en.md | |
| (устаревшее) приложение | obsolete application | Zima/Zima2_Users_manual_en.md | AzimuthSuite |
| РАБОЧИЙ КОНУС (ОТНОСИТЕЛЬНО ГОРИЗОНТАЛИ) | OPERATING CONE (RELATIVE TO THE HORIZONTAL) | Zima/Zima2B_Specification_en.md | Other Zima EN files still say WORKING VERTICAL ANGLES |
| РАЗВИВАЕМОЕ АКУСТИЧЕСКОЕ ДАВЛЕНИЕ | ACOUSTIC SOURCE LEVEL | Zima/Zima2B_Specification_en.md | RU has no `МАКСИМАЛЬНОЕ` here |
| ВРЕМЯ АВТОНОМНОЙ РАБОТЫ | BATTERY LIFE | Zima/Zima2B_Specification_en.md | |
| (КРЕН/ДИФФЕРЕНТ) | (ROLL/PITCH) | Zima/Zima2B_Specification_en.md | `дифферент` = pitch (trim) |
| МАКСИМАЛЬНЫЙ КОМПЕНСИРУЕМЫЙ ВСТРОЕННЫМ ИНКЛИНОМЕТРОМ НАКЛОН ПРИБОРА ОТНОСИТЕЛЬНО ВЕРТИКАЛИ | MAXIMUM DEVICE TILT RELATIVE TO THE VERTICAL COMPENSATED BY THE BUILT-IN INCLINOMETER | Zima/Zima2B_Specification_en.md | |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ИЗМЕРЕНИЯ НАКЛОННОЙ ДАЛЬНОСТИ | NOMINAL SLANT RANGE MEASUREMENT ACCURACY | Zima/Zima2B_Specification_en.md | RU spells `ТОЧНСТЬ` |
| мсек | ms | Zima/Zima2B_Specification_en.md | SI symbol |
| Раздел документации по системе | Documentation section for the … system | Zima/Zima2_fast_start_en.md | |
| Браузерное приложение | Browser-based application | Zima/Zima2_fast_start_en.md | AzimuthWebSuite |

## Added in batch zima-2

| RU | EN | Source EN file | Note |
|---|---|---|---|
| ДОПОЛНИТЕЛЬНО (heading) | ADDITIONAL INFORMATION | Zima/Zima2R_Specification_en.md (+2) | Same as `ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ` |
| ПЕРИОД ОПРОСА, сек / ВРЕМЯ РАБОТЫ, ч / ПРИМЕЧАНИЕ | POLLING PERIOD, s / OPERATING TIME, h / NOTE | Zima/Zima2R_Specification_en.md (+2) | Battery life tables |
| Без опроса, в режиме приема / Минимально возможный период опроса | Without polling, in receiving mode / Shortest possible polling period | Zima/Zima2R_Specification_en.md (+2) | |
| опрос / опрашивать (маяки-ответчики) | polling / poll; interrogation / interrogate | Zima/Zima2R_Specification_en.md, Zima/Zima2_LBL_DataBrief_en.md | `polling` for USBL polling periods and cycles; `interrogation` for the LBL transceiver interrogating the navigation base. Both are standard |
| общий (широковещательный) запрос / последовательный опрос | common (broadcast) request / sequential interrogation | Zima/Zima2_LBL_DataBrief_en.md | Zima2-L vs Zima2-LX modes |
| U<sub>пит.</sub> | U<sub>supply</sub> | Zima/Zima2R_Specification_en.md (+3) | Wire assignment tables |
| Экран (жила кабеля) | Shield | Zima/Zima2R_Specification_en.md (+3) | |
| до 16 изолирующих адресов | up to 16 isolating addresses | Zima/Zima2R_Specification_en.md (+3) | Literal; meaning queried with the maintainer |
| навигационная база | navigation base | Zima/Zima2L_Specification_en.md (+1) | LBL |
| опорные маяки-ответчики / опорные точки | reference responder-beacons / reference points | Zima/Zima2_LBL_DataBrief_en.md (+1) | |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ МЕСТОПОЛОЖЕНИЯ (СКО) | NOMINAL POSITIONING ACCURACY (RMS) | Zima/Zima2L_Specification_en.md | `СКО` → RMS |
| МАКСИМАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ МЕСТОПОЛОЖЕНИЯ | MAXIMUM POSITION UPDATE RATE | Zima/Zima2L_Specification_en.md | |
| натурный (статический) эксперимент | full-scale (static) experiment | Zima/Zima2L_Specification_en.md | |
| РАЗЪЕМЫ | CONNECTORS | Zima/Zima2RK_Specification_en.md | `(Питание и данные)` → `(Power and data)`, `(Антенна)` → `(Transducer)` |
| Рабочая глубина до … / Глубина погружения до … | Operating depth up to … / Immersion depth up to … | Zima/Zima2RK_Specification_en.md, Zima/Zima2R35_Specification_en.md | Key features |
| РАЗРЕШЕНИЕ ПО ГЛУБИНЕ МАЯКОВ-ОТВЕТЧИКОВ | DEPTH RESOLUTION OF RESPONDER-BEACONS | Zima/Zima2B35_Specification_en.md | |
| мембрана (датчика давления) | diaphragm | Zima/Zima2R35_Specification_en.md | Consistent with the Zima2 user's manual |
| Самый маленький маяк-ответчик в мире | The world's smallest responder-beacon | Zima/Zima2uR_Specification_en.md | |
| миниатюрная версия | miniature version | Zima/Zima2uR_Specification_en.md | |
| Варианты построения системы | System configuration options | Zima/Zima2_LBL_DataBrief_en.md | |
| Сравнение режимов / Схема опроса / Расчет положения / Выход | Comparison of modes / Interrogation scheme / Position calculation / Output | Zima/Zima2_LBL_DataBrief_en.md | |
| энергетическая дальность акустической связи | acoustic communication range determined by the link budget | Zima/Zima2_LBL_DataBrief_en.md | |
| единая аппаратная платформа | single hardware platform | Zima/Zima2_LBL_DataBrief_en.md | |

## Added in batch zima-3

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Идентификаторы адресных запросов | Addressed request identifiers | Zima/Zima2_Protocol_Specification_en.md | The section 7 row "адресных … команд" covers a different phrase; RU table entries are `CDS_REQ_*` |
| управляющая система (Host) | control system (Host) | Zima/Zima2_Protocol_Specification_en.md | Prefixes: D2H = Device to Host, H2D = Host to Device |
| LBL-решатель | LBL solver | Zima/Zima2_Protocol_Specification_en.md | |
| пользовательский параметр | user parameter | Zima/Zima2_Protocol_Specification_en.md | H2D_CREQ / H2D_CSET |
| сглаживающий фильтр | smoothing filter | Zima/Zima2_Protocol_Specification_en.md | |
| датчик глубины | depth sensor | Zima/Zima2_Protocol_Specification_en.md | |
| телеуправление | remote control | Zima/Zima2_Protocol_Specification_en.md (+1) | |
| интервал ожидания ответа маяка-ответчика | responder-beacon response waiting interval | Zima/Zima2_Protocol_Specification_en.md | Timeout |
| Элемент / Дескриптор | Element / Descriptor | Zima/Zima2_Protocol_Specification_en.md | NMEA sentence structure table |
| См. Таблица 3.x | See Table 3.x | Zima/Zima2_Protocol_Specification_en.md | |
| вещественное значение | real (floating-point) value | Zima/Zima2_Protocol_Specification_en.md | |
| Дата релиза / Устройство / Истории версий по устройствам | Release date / Device / Version histories by device | Zima/Zima2_version_history_en.md | |
| мелкие доработки | minor improvements | Zima/Zima2_version_history_en.md | |
| авторасчет скорости звука | automatic speed of sound calculation | Zima/Zima2_version_history_en.md | |
| уровень солености | salinity level | Zima/Zima2_technical_passport_en.md (+2) | |
| энергетически сопрягаются с носителем | are power-interfaced with the carrier | Zima/Zima2_technical_passport_en.md (+2) | |
| Моноблочные устройства | monoblock devices | Zima/Zima2_technical_passport_en.md (+2) | |
| Поставщик за свой счет устраняет | the Supplier shall eliminate … at its own expense | Zima/Zima2_technical_passport_en.md (+2) | Contractual `shall` |
| за счет сил и средств Заказчика | using the Customer's own resources | Zima/Zima2_technical_passport_en.md (+2) | |
| Гарантийные обязательства не распространяются на … | The warranty obligations do not apply to … | Zima/Zima2_technical_passport_en.md (+2) | |
| Не допускается хранение в неопресненном и влажном виде | Storage of the devices without rinsing in fresh water or while damp is not allowed | Zima/Zima2_technical_passport_en.md (+2) | |
| (опция) | (optional) | Zima/Zima2-OEM35_technical_passport_en.md | |
| Бар | bar | Zima/Zima2_technical_passport_en.md (+2) | Lowercase unit symbol |
| метров водного (водяного) столба | meters of water column | Zima/Zima2_technical_passport_en.md (+2) | |
| сборка печатных плат | printed circuit board assembly | Zima/Zima2-OEM35_technical_passport_en.md | |
| полимерная самоклеящаяся бирка | polymer self-adhesive tag | Zima/Zima2-OEM35_technical_passport_en.md | |
| Версия ПО (в паспорте) | Firmware version | Zima/Zima2_technical_passport_en.md (+2) | Device firmware, consistent with the version history |

## Added in batch zima-4

| RU | EN | Source EN file | Note |
|---|---|---|---|
| опорный маяк | reference beacon | Zima/AzimuthConsole_manual_en.md | `RBADD`/`RBLST`; see also "опорные маяки-ответчики" |
| Режим по опорным маякам | Reference beacon mode | Zima/AzimuthConsole_manual_en.md | `AMODE,mode=beacon_referenced` |
| искомые (не опорные) маяки | target (non-reference) beacons | Zima/AzimuthConsole_manual_en.md | |
| Запрос маяков | Beacon interrogation | Zima/AzimuthConsole_manual_en.md | Command group `Interrogation` in AzimuthConsole |
| поворотное устройство | rotator | Zima/AzimuthConsole_manual_en.md | Radant rotator (RDT port) |
| калибровка на поворотном устройстве | rotator calibration | Zima/AzimuthConsole_manual_en.md | `SCAL`; angular calibration = `ACAL` |
| возраст / давность данных | age of the data | Zima/AzimuthConsole_manual_en.md | `age` fields |
| угол места | elevation angle | Zima/AzimuthConsole_manual_en.md | `Elevation_deg` |
| Курс движения | Course (direction of motion) | Zima/AzimuthConsole_manual_en.md | `course_deg`; heading = `heading_deg` |
| Азимутальный угол | Azimuth angle | Zima/AzimuthConsole_manual_en.md | |
| Наименование параметра | Parameter name | Zima/AzimuthConsole_manual_en.md | Output data tables |
| Диапазон значений | Value range | Zima/AzimuthConsole_manual_en.md | |
| Встроенный сенсор | Built-in sensor | Zima/AzimuthConsole_manual_en.md | |
| Внешний источник | External source | Zima/AzimuthConsole_manual_en.md | |
| Расчетное значение | Calculated value | Zima/AzimuthConsole_manual_en.md | |
| Заданное пользователем | Set by the user | Zima/AzimuthConsole_manual_en.md | |
| веб-интерфейс | web interface | Zima/AzimuthConsole_manual_en.md | Lowercase in running text |
| инициализирующий скрипт | initialization script | Zima/AzimuthConsole_manual_en.md | `init.cmd` |
| DH-фильтр | DH filter | Zima/AzimuthConsole_manual_en.md | |
| мБар | mbar | Zima/AzimuthConsole_manual_en.md | Unit column; identifiers such as `stPressure_mBar` unchanged |
| Запуск от имени администратора | Run as administrator | Zima/AzimuthConsole_manual_en.md | Real Windows UI string |
| UI labels of AzimuthConsole | as in `src/wwwroot/i18n.js` (`en:` block) | Zima/AzimuthConsole_manual_en.md | e.g. Zoom In, Auto Scale, Interrogate/Pause, Apply & Restart, Save as default settings |

## Added in batch zima-5

| RU | EN | Source EN file | Note |
|---|---|---|---|
| коммутационный хаб | switching hub | Zima/Bat_n_link_box_Specification_en.md (+1) | Bat&Link Box |
| Выключатель питания | Power switch | Zima/Bat_n_link_box_Users_manual_en.md | Front panel legend |
| Индикатор заряда / Индикатор питания | Charge indicator / Power indicator | Zima/Bat_n_link_box_Users_manual_en.md | |
| сетевой адаптер (зарядное устройство) | mains adapter (charger) | Zima/Bat_n_link_box_Users_manual_en.md | |
| горит постоянно / мигает | on continuously / blinking | Zima/Bat_n_link_box_Users_manual_en.md | Indicator states |
| Ударопрочное исполнение | Impact-resistant design | Zima/Bat_n_link_box_Specification_en.md | Also "ударопрочный кейс" = impact-resistant case |
| РАЗЪЕМЫ И ИНТЕРФЕЙСЫ | CONNECTORS AND INTERFACES | Zima/Bat_n_link_box_Specification_en.md | |
| РАЗЪЕМ ЗАРЯДКИ | CHARGING CONNECTOR | Zima/Bat_n_link_box_Specification_en.md | |
| MSDS ВСТРОЕННОГО ИСТОЧНИКА ПИТАНИЯ | MSDS OF THE BUILT-IN POWER SUPPLY | Zima/Bat_n_link_box_Specification_en.md | |
| ЭЛЕКТРОННАЯ ВЕРСИЯ ЭТОГО ДОКУМЕНТА | ELECTRONIC VERSION OF THIS DOCUMENT | Zima/Bat_n_link_box_Specification_en.md | Also in RedBASE, RWLT GIB, WAYU GIB |
| технология одновременной навигации | simultaneous navigation technology | Zima/Zima_B_Specification_en.md (+2) | Patent RU156897U1 |
| информационно сопрягается (маяк с носителем) | data-interfaced (beacon with the carrier) | Zima/Zima_DataBrief_en.md | "энергетически и информационно" = for both power and data |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ ГОРИЗОНТАЛЬНОГО УГЛА | NOMINAL HORIZONTAL ANGLE DETERMINATION ACCURACY | Zima/Zima_R_Specification_en.md (+1) | Without "ПРИХОДА СИГНАЛА" |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ ДИСТАНЦИИ | NOMINAL DISTANCE DETERMINATION ACCURACY | Zima/Zima_R_Specification_en.md (+1) | |
| ИСПОЛНЕНИЕ ДО 350 М | VERSION UP TO 350 m | Zima/Zima2-35_technical_passport_en.md | Passport title |
| специализированное ПО | specialized software | Zima/Zima_GNSS_requirements_en.md | |
| стороны света | cardinal directions | Zima/Zima_GNSS_requirements_en.md | |
| частота обновления | update rate | Zima/Zima_GNSS_requirements_en.md | |
| Требования по совместимости для систем определения курса и положения | Compatibility requirements for heading and position determination systems | Zima/Zima_GNSS_requirements_en.md (+1) | Breadcrumb: "Compatibility information sheet for positioning and heading systems" |

## Added in batch zima-6

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Пультовое ПО ZHost | ZHost host software | Zima/Zima_Users_manual_en.md | First-generation Zima |
| UI labels of ZHost | as in `ZHost/MainForm.resx` and `ZHost/CustomUI/SettingsEditor.resx` (neutral = English) | Zima/Zima_Users_manual_en.md | e.g. CONNECTION, RESPONDER, AUTOQUERY, AUTOSNAPSHOT, PPI, SET DEFAULTS, Responders in use |
| Панель статуса | Status panel | Zima/Zima_Users_manual_en.md | |
| лимб (индикатора) | dial | Zima/Zima_Users_manual_en.md | PPI panel |
| курсовой угол | relative bearing | Zima/Zima_Users_manual_en.md | |
| опреснение | desalination (soaking and rinsing in fresh water) | Zima/Zima_Users_manual_en.md | |
| ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ (А·ч) | CAPACITY | Zima/Zima_Users_manual_en.md | W·h → ENERGY CAPACITY; transducers → CAPACITANCE |
| КОЛИЧЕСТВО ЭЛЕМЕНТОВ В СБОРКЕ | NUMBER OF CELLS IN THE PACK | Zima/Zima_Users_manual_en.md | |
| Симптомы / Возможная причина / Устранение | Symptoms / Possible cause / Remedy | Zima/Zima_Users_manual_en.md | Troubleshooting table |
| Гидрология | Hydrological conditions | Zima/Zima_Users_manual_en.md | |
| курс (VTG) | course over ground | Zima/Zima_Users_manual_en.md | NMEA VTG |
| решатель | solver | Zima/Zima2SL_Specification_en.md | Zima2-SL |
| потребитель (навигационных данных) | data consumer | Zima/Zima2SL_Specification_en.md | |
| ОЖИДАЕТСЯ | PENDING | Zima/Zima2SL_Specification_en.md | Placeholder for images and values not yet published |

## Added in batch zima-7

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Идентификаторы удаленных команд | Remote command identifiers | Zima/Zima_Protocol_Specification_en.md | First-generation Zima protocol |
| настроечное поле | configuration field | Zima/Zima_Protocol_Specification_en.md | |
| акустическое ядро | acoustic core | Zima/Zima_Protocol_Specification_en.md | |
| Управление энергосберегающим режимом | Power-saving mode control | Zima/Zima_Protocol_Specification_en.md | |
| «Теплая» перезагрузка | 'Warm' reboot | Zima/Zima_Protocol_Specification_en.md | |
| Глубина … от поверхности | depth below the surface | Zima/Zima_Protocol_Specification_en.md | |
| Доступно: (командная строка / терминал / удаленный терминал) | Available via: (command line / terminal / remote terminal (UDP)) | Zima/AzimuthConsole_v1x_en.md | |
| перегрузка (координат и курса) | override | Zima/AzimuthConsole_v1x_en.md | LHO?/LHOV = location and heading override |
| ACHOD-фильтр | ACHOD filter | Zima/AzimuthConsole_v1x_en.md | Not the DH filter of 2.x |
| длинная навигационная база | long navigation base | Zima/AzimuthConsole_v1x_en.md | SRC3 |
| МАКСИМАЛЬНОЕ ЧИСЛО МАЯКОВ В БАЗЕ | MAXIMUM NUMBER OF BEACONS IN THE BASE | Zima/Zima2LX_Specification_en.md | |
| МАКСИМАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ ДАЛЬНОСТЕЙ | MAXIMUM RANGE UPDATE RATE | Zima/Zima2LX_Specification_en.md | Cf. MAXIMUM POSITION UPDATE RATE (Zima2-SL) |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ИЗМЕРЕНИЯ ДАЛЬНОСТИ (СКО) | NOMINAL RANGE MEASUREMENT ACCURACY (RMS) | Zima/Zima2LX_Specification_en.md | |

## Added in batch zima-8

| RU | EN | Source EN file | Note |
|---|---|---|---|
| UI labels of AzimuthSuite | as in `MainForm.resx`, `SettingsEditor.resx`, `Dialogs/*.resx` of AzimuthSuite (neutral = English) | Zima/AzimuthSuite_manual_en.md | RU already quotes most labels in English |
| Угловая поправка (настройки AzimuthSuite) | Angular correction | Zima/AzimuthSuite_manual_en.md | Real UI label: "Antenna angle adjust, °" (`SettingsEditor.resx`, `groupBox6`) |
| Поле карты | Map field | Zima/AzimuthSuite_manual_en.md | |
| Текстовое поле дополнительных параметров | Additional parameters text field | Zima/AzimuthSuite_manual_en.md | |
| привод носителя (на маяк) | homing of the carrier | Zima/AzimuthSuite_manual_en.md | RAZ parameter |
| точка привязки | reference point | Zima/AzimuthSuite_manual_en.md | |
| Пункт (меню) **X** - … | The **X** item/menu … | Zima/AzimuthSuite_manual_en.md | Sentence pattern for menu items and buttons |

## Added in batch uwave-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Устройства семейства | Devices of the family | uWAVE/uWAVE_Family_en.md | |
| Оснащение устройств | Device equipment | uWAVE/uWAVE_Family_en.md | |
| Диапазоны измеряемых значений | Ranges of measured values | uWAVE/uWAVE_Family_en.md | |
| Основные параметры устройств | Main device parameters | uWAVE/uWAVE_Modems_comparison_en.md | |
| Текущий статус / Поставляется | Current status / Available | uWAVE/uWAVE_Modems_comparison_en.md | |
| Модуль измерения напряжения питания | Supply voltage measurement module | uWAVE/uWAVE_Modems_comparison_en.md | |
| Двухосевой инклинометр | Two-axis inclinometer | uWAVE/uWAVE_Family_en.md (+1) | |
| Отличия от базовой версии | Differences from the base version of | uWAVE/uWAVE_Max_Specification_en.md (+1) | |
| НЕСУЩАЯ | CARRIER | uWAVE/uWAVE_Specification_en.md | |
| РАЗМЕР БУФЕРА ПЕРЕДАТЧИКА | TRANSMITTER BUFFER SIZE | uWAVE/uWAVE_Specification_en.md (+3) | |
| ПАКЕТНЫЙ РЕЖИМ | PACKET MODE | uWAVE/uWAVE_Specification_en.md (+3) | ALO = At-least-once |
| КОМАНДНЫЙ РЕЖИМ | COMMAND MODE | uWAVE/uWAVE_Specification_en.md (+3) | |
| кОм | kΩ | uWAVE/uWAVE_Specification_en.md (+3) | |
| Передача данных совмещенная с УКБ навигацией | Data transmission combined with USBL navigation | uWAVE/uWAVE_USBL_Modem_Specification_en.md | |
| Упоминания об устройствах uWave; Научные публикации | Mentions of uWave devices; Scientific publications | uWAVE/uWave_publications_en.md | Russian-language citations are quoted verbatim |

## Added in batch uwave-3

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Инструкция по обновлению прошивки модемов uWave | Firmware update guide for uWave modems | uWAVE/uWAVE_FW_Updating_en.md | Header cell; breadcrumb: Firmware update guide |
| Рисунок N / рис. N | Figure N / Fig. N | uWAVE/uWAVE_FW_Updating_en.md | |
| перепрошивка | reflashing | uWAVE/uWAVE_FW_Updating_en.md | |
| выпадающий список | drop-down list | uWAVE/uWAVE_FW_Updating_en.md | |
| Запустите приложение/утилиту | Launch the application/utility | uWAVE/uWAVE_FW_Updating_en.md | "Press **X**" is reserved for buttons |
| медиаматериалы: видео с испытаний, видеоинструкции | media: test videos, video tutorials | uWAVE/media.md | |
| Волгодонской судоходный канал | Volga-Don Shipping Canal | uWAVE/media.md | |

## Added in batch uwave-2

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Система команд UWV | UWV command system | uWAVE/uWAVE_Protocol_Specification_en.md | |
| канал передачи / приема | transmit / receive channel | uWAVE/uWAVE_Protocol_Specification_en.md | |
| параметры среды и питания | ambient and power supply parameters | uWAVE/uWAVE_Protocol_Specification_en.md | |
| уведомление о получении | receipt notification | uWAVE/uWAVE_Protocol_Specification_en.md | Packet mode |
| режим пакетной передачи | packet transmission mode | uWAVE/uWAVE_Protocol_Specification_en.md | |
| превышен интервал ожидания ответа | response timeout | uWAVE/uWAVE_Protocol_Specification_en.md | |
| НЕУСТРАНИМАЯ и НЕ ГАРАНТИЙНАЯ поломка | IRREPARABLE damage … NOT COVERED BY THE WARRANTY | uWAVE/uWAVE_Protocol_Specification_en.md | Caution notes |
| жила … притянута к | wire … pulled to | uWAVE/uWAVE_Protocol_Specification_en.md | SVC/CMD |
| Рецепт N | Recipe N | uWAVE/uWAVE_Protocol_Specification_en.md | |
| через толщу воды | through the water column | uWAVE/uWave_technical_passport_en.md | |
| встроенная схема измерения напряжения питания | built-in supply voltage measurement circuit | uWAVE/uWave_technical_passport_en.md | |

## Added in batch redphone-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| тангента | PTT button; PTT handset | RedPhone/RedPhone_OS_Users_manual_en.md, RedPhone/Phone_T_package_tech_passport_en.md | `Микрофон с тангентой` → `Microphone with PTT button`; a separate surface-station handset → `PTT handset`. Never "tangent" |
| п. N.N (ссылка на раздел) | section N.N | RedPhone/RedPhone_OS_Users_manual_en.md | Not `p.` (reads as "page") |
| Прием! (конец голосового сообщения) | Over! | RedPhone/RedPhone_OS_Users_manual_en.md | Radio procedure word; maintainer question open for all three RedPhone manuals |
| полудуплексная схема связи | half-duplex | RedPhone/RedPhone_OS_Users_manual_en.md | `Связь работает по полудуплексной схеме` → `communication is half-duplex` |
| Верхняя / Нижняя (боковая полоса) | Upper / Lower | RedPhone/RedPhone_OS_Specification_en.md (+3) | Old EN `High` / `Low` |
| Хорошее / Удовлетворительное / Отличное (соответствие тракту) | Good / Satisfactory / Excellent | RedPhone/RedPhone_OS_Users_manual_en.md | Table 1 column `Match with the characteristics of the transceiver path` |
| однополосная амплитудная модуляция | single-sideband amplitude modulation (SSB) | RedPhone/RedPhone_OS_Users_manual_en.md | |
| детектор речи; автоматический сквелч | voice activity detector; automatic squelch | RedPhone/RedPhone_DX_Specification_en.md (+1) | |
| неразборный и необслуживаемый (корпус, конструкция) | one-piece, maintenance-free | RedPhone/RedPhone_DX_Specification_en.md (+1) | `моноблочная неразборная конструкция` → `one-piece monoblock design` |
| приборная панель | front panel; control panel | RedPhone/RedPhone_OS_Users_manual_en.md, RedPhone/RedPhone_OS_Specification_en.md | |
| надводный пункт контроля за (водолазными) спусками | surface dive control point; surface dive monitoring point | RedPhone/RedPhone_OS_Users_manual_en.md, RedPhone/Phone_T_package_tech_passport_en.md | |
| головной телефон (наушники); головные телефоны | headphones | RedPhone/RedPhone_OS_Users_manual_en.md (+1) | Do not add "(earphones)" |
| гермомешок; транспортировочный мешок | waterproof bag; transport bag | RedPhone/RedPhone_OS_Users_manual_en.md | |
| громкоговоритель; динамик | speaker | RedPhone/RedPhone_OS_Users_manual_en.md | Matches the panel label **"Speaker"** |
| грузонесущая проушина | load-bearing eye | RedPhone/RedPhone_OS_Users_manual_en.md | `фиксация кабеля за грузонесущую проушину` → `secured by its load-bearing eye` |
| ЗАПРЕЩАЕТСЯ | PROHIBITED | RedPhone/RedPhone_OS_Users_manual_en.md | |
| зарядное шасси | charging chassis | RedPhone/Phone_T_package_tech_passport_en.md | Literal; the delivery-set table says `Зарядное устройство` = charger |
| герморазъем | watertight connector | RedPhone/Phone_T_package_tech_passport_en.md | |
| баллон | tank | RedPhone/Phone_T_package_tech_passport_en.md | As `Кронштейн на баллон` → `Tank bracket` |
| спортивный дайвинг | recreational diving | RedPhone/Phone_T_package_tech_passport_en.md | |
| Приемник телеметрии RWLT RF Dongle | RWLT RF Dongle telemetry receiver | RedPhone/Phone_T_package_tech_passport_en.md | |
| Система команд RPH | RPH command system | RedPhone/RedPhone-DX_protocol_specification_en.md | |
| Протокол диалогового уровня | dialog layer protocol | RedPhone/RedPhone-DX_protocol_specification_en.md | Same as the Zima2 and uWave protocols |
| Поле/Параметр / Описание | Field/Parameter / Description | RedPhone/RedPhone-DX_protocol_specification_en.md | |

## Added in batch rwlt-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Курс (движения) в навигационных сообщениях (tCrs, gnssCrs, crs2rp, crs4rp, RMC) | Course | RWLT/uNav_protocol_specification_en.md | Course over ground / direction to a point; the fixed `курс` → `heading` applies to vessel/antenna orientation |
| сообщение (протокол NMEA) | sentence | RWLT/uNav_protocol_specification_en.md (+2) | As in the Zima2 and RedPhone-DX protocols |
| сглаживающий фильтр | smoothing filter | RWLT/uNav_protocol_specification_en.md | Old EN "anti-aliasing filter" was wrong |
| буфер-классификатор | classifier buffer | RWLT/uNav_protocol_specification_en.md | |
| определитель курса движения | course estimator | RWLT/uNav_protocol_specification_en.md | |
| опорная точка | reference point | RWLT/uNav_protocol_specification_en.md | |
| нумерованный объект / цель | numbered object / target | RWLT/uNav_protocol_specification_en.md | |
| Возраст навигационных данных | Navigation data age | RWLT/uNav_protocol_specification_en.md | |
| Радиальная ошибка | Radial error | RWLT/uNav_protocol_specification_en.md | |
| навигационный гидроакустический буй (RWLT GIB) | navigation sonobuoy | RWLT/RWLT_GIB_Specification_en.md | Header cell keeps `Navigation buoy`; consistent with RWLT_DataBrief_en and RWLT_Users_Manual_en |
| плавучая (длинная) навигационная база | floating (long) navigation base | RWLT/RWLT_GIB_Specification_en.md, RWLT/RWLT_tech_pass_en.md | |
| схема поплавок-перо | float-and-spar (spar buoy) design | RWLT/RWLT_GIB_Specification_en.md | |
| ИЗБЫТОЧНАЯ ПЛАВУЧЕСТЬ | EXCESS BUOYANCY | RWLT/RWLT_GIB_Specification_en.md | |
| ОСАДКА; ВЫСОТА НАД ВОДОЙ | DRAFT; HEIGHT ABOVE WATER | RWLT/RWLT_GIB_Specification_en.md | |
| МАКСИМАЛЬНАЯ СКОРОСТЬ ОТНОСИТЕЛЬНО ПИНГЕРА / БУЕВ | MAXIMUM VELOCITY RELATIVE TO PINGER / BUOYS | RWLT/RWLT_GIB_Specification_en.md, RWLT/RWLT_Pinger_K_Specification_en.md | |
| МАКСИМАЛЬНО / МИНИМАЛЬНО ДОПУСТИМОЕ РАССТОЯНИЕ ДО ДРУГИХ БУЕВ КОМПЛЕКТА | MAXIMUM / MINIMUM PERMISSIBLE DISTANCE TO OTHER BUOYS OF THE SET | RWLT/RWLT_GIB_Specification_en.md | |
| ТИП ВСТРОЕННОГО РАДИОМОДУЛЯ; МАКСИМАЛЬНАЯ МОЩНОСТЬ РАДИОМОДУЛЯ | BUILT-IN RADIO MODULE TYPE; MAXIMUM RADIO MODULE POWER | RWLT/RWLT_GIB_Specification_en.md | |
| РЕФЕРЕНСНЫЙ ЭЛЛИПСОИД | REFERENCE ELLIPSOID | RWLT/RWLT_GIB_Specification_en.md | |
| ПЕРИОД ИЗЛУЧЕНИЯ АКУСТИЧЕСКОГО СИГНАЛА | ACOUSTIC SIGNAL EMISSION PERIOD | RWLT/RWLT_Pinger_K_Specification_en.md | |
| ТЕЛЕМЕТРИЧЕСКАЯ ИНФОРМАЦИЯ | TELEMETRY INFORMATION | RWLT/RWLT_Pinger_K_Specification_en.md | RWLT_Pinger_Specification_en (OK in master) says `TELEMETRY`; align in Phase 4 |
| носитель (ТНПА, АНПА) | carrier (ROV, AUV) | RWLT/RWLT_Pinger_K_Specification_en.md, RWLT/RWLT_tech_pass_en.md | Old EN "media" was wrong |
| Исполнение IP68 | IP68 protection class | RWLT/RWLT_RF_Dongle_en.md | |
| Эмуляция протокола GNSS-приемников | GNSS receiver protocol emulation | RWLT/RWLT_RF_Dongle_en.md | |
| только прием (радиосвязь) | receive only | RWLT/RWLT_RF_Dongle_en.md | |
| Автономный блок питания и коммутации Bat&Link Box | Bat&Link Box autonomous power supply and switching unit | RWLT/RWLT_tech_pass_en.md | |
| батарейная сборка | battery pack | RWLT/RWLT_tech_pass_en.md | |
| сростки (аксессуары) | splices | RWLT/RWLT_tech_pass_en.md | |
| хранение в неопресненном и влажном виде | storage without rinsing in fresh water or while damp | RWLT/RWLT_tech_pass_en.md | |

## Added in batch redphone-2

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Устройство (раздел руководства) | Device design | RedPhone/RedPhone_DX_Users_Manual_en.md | Section heading describing the construction |
| Настройка станции | Station configuration | RedPhone/RedPhone_DX_Users_Manual_en.md | |
| № Контакта; Общий (контакт) | Pin No.; Common | RedPhone/RedPhone_DX_Users_Manual_en.md | Pinout tables |
| ремень; резиновый жгут | strap; rubber bungee cord | RedPhone/RedPhone_DX_Users_Manual_en.md | Mounting on the tank; "belt" is the diver's belt |
| металлическая скоба | metal clamp | RedPhone/RedPhone_DX_Users_Manual_en.md | |
| мокрая салфетка | wet wipe | RedPhone/RedPhone_DX_Users_Manual_en.md | |
| транспортировочная тара | transport case | RedPhone/RedPhone_DX_Users_Manual_en.md | |
| сервисный кабель | USB service cable | RedPhone/RedPhone_DX_Users_Manual_en.md | |
| с увеличенной дальностью связи (RedPhone-MDX, RedPhone-MOS) | Extended-range … | RedPhone/RedPhone_MDX_Specification_en.md, RedPhone/RedPhone_MOS_Specification_en.md | `Extended-range diver station …`, `Extended-range surface station …` |
| В надводном положении (переключение каналов) | In the surface position | RedPhone/RedPhone_Specification_en.md | As in the Zima2 user's manual |
| USB-радиодонгл | USB radio dongle | RedPhone/RedPhone_Specification_en.md | |
| ВСТРОЕННЫЙ ИСТОЧНИК ПИТАНИЯ | BUILT-IN POWER SUPPLY | RedPhone/RedPhone_Specification_en.md | |
| RedPhone DX Config UI (web tool) | Connection, Connect, Device type, Serial number, Firmware version, SETS2 Settings, RWLT Mode, RWLT Diver ID, Flags, Bit 0 (PinsPrevail), Bit 7 (CH Indicator), Save Settings, Write to Flash | RedPhone/RedPhone_DX_Users_Manual_en.md | Real English strings from `i18n.js` of github.com/ucnl/RedPhoneDXConfig-Web |

## Added in batch redphone-4

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Комплект ЗИП | Spare parts and tools kit | RedPhone/RedPhone_Users_Manual_en.md | Old EN "SPTA kit" |
| кредл; зарядный кредл (шасси) | cradle; charging cradle (chassis) | RedPhone/RedPhone_Users_Manual_en.md | |
| наживить (гайки, винты) | hand-thread | RedPhone/RedPhone_Users_Manual_en.md | Not "tighten" |
| Выбор канала связи - бит N | Communication channel selection - bit N | RedPhone/RedPhone_Users_Manual_en.md | DIP-switch table |
| Станция RedPhone с креплением на ремень | RedPhone station with a strap mount | RedPhone/RedPhone_Users_Manual_en.md | |
| ПРИМЕНЯЕМЫЕ ИСТОЧНИКИ ПИТАНИЯ | POWER SOURCES USED | RedPhone/RedPhone_Users_Manual_en.md, RedPhone/RedPhone_DX_Specification_en.md | |
| Испытания в мелководном водоеме | Tests in a shallow body of water | RedPhone/media.md | |
| при отсутствии прямой видимости | without a direct line of sight | RedPhone/media.md | |
| Фиксация (кабеля антенны) при помощи карабина | Securing the transducer with a carabiner | RedPhone/media.md | US spelling `carabiner` |
| Проверка исправности | Checking the serviceability | RedPhone/media.md | |

## Added in batch redphone-3

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Программа и методики испытаний | Test program and procedures | RedPhone/RedPhone_PM_en.md | |
| Объект испытаний / Цель испытаний | Test object / Test objective | RedPhone/RedPhone_PM_en.md | |
| Комплект оборудования (КО) | equipment set (ES) | RedPhone/RedPhone_PM_en.md | Distinct from `Комплект поставки` = delivery set |
| Комплект ЗИП | Spare parts and tools kit | RedPhone/RedPhone_PM_en.md, RedPhone/RedPhone_Users_Manual_en.md | |
| Приборный состав | Instrument composition | RedPhone/RedPhone_PM_en.md | |
| Частота проведения испытаний | Frequency of testing | RedPhone/RedPhone_PM_en.md | |
| полигон (испытательный) | test site | RedPhone/RedPhone_PM_en.md | |
| натурные испытания | full-scale tests | RedPhone/RedPhone_PM_en.md | |
| сдаточные испытания / приемочные испытания | delivery tests / acceptance tests | RedPhone/RedPhone_PM_en.md | |
| волнение (моря) … баллов | sea state … | RedPhone/RedPhone_PM_en.md | Bare code number, no "points" |
| разборчивость; процент разборчивости | intelligibility; intelligibility percentage | RedPhone/RedPhone_PM_en.md | |
| артикуляционные списки | articulation lists | RedPhone/RedPhone_PM_en.md | The Russian word lists themselves are kept in Cyrillic (phonetically balanced test material) |
| Испытание на автономность | battery life test | RedPhone/RedPhone_PM_en.md | |
| надводный пост | surface post | RedPhone/RedPhone_PM_en.md | |
| станция связи (надводная / водолазная) | (surface / diver) communication station | RedPhone/RedPhone_PM_en.md | |
| Кранец (буек) | Fender (small buoy) | RedPhone/RedPhone_PM_en.md | |
| Как меня поняли? Прием | How do you read me? Over | RedPhone/RedPhone_PM_en.md | Radio check; `Слышу вас на X баллов из 10` → `I hear you X out of 10` |
| по телефонной связи (повторить слово) | over the underwater telephone link | RedPhone/RedPhone_PM_en.md | |
| Н/п | N/A | RedPhone/RedPhone_PM_en.md | |
