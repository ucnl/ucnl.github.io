# RU → EN glossary for docs.unavlab.com

Authoritative terminology for every RU → EN sync task (CLAUDE.md section 5). Built in Phase 1 from the existing RU/EN document pairs (breadcrumbs, header-table phrases, titles, table header cells, parameter rows paired by matching values, section headings paired by number) with `.github/docs-sync/docsync.py terms`, then curated by the orchestrator.

## How to use

1. Precedence: the fixed terms (section 1) → the canonical rows of sections 3–9 → the term already used in EN documents of the same family → the standard industry term.
2. The EN column gives the canonical term. Apply it consistently in new and updated documents, using the context specified in the RU column and notes.
3. Letter case: where the RU text writes a heading, table header or parameter label in ALL CAPS, the EN text keeps ALL CAPS (`ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ` → `TECHNICAL SPECIFICATIONS`). Everywhere else headings are in sentence case (`Подготовка к работе` → `Preparation for work`). Product names keep their own case.
4. `МАКСИМАЛЬНЫЙ / МАКСИМАЛЬНАЯ / МАКСИМАЛЬНОЕ` → `MAXIMUM` spelled out (the style of the most recent EN files); `MAX.` only where RU abbreviates (`МАКС.`). The same for `МИНИМАЛЬНЫЙ` → `MINIMUM`, `НОМИНАЛЬНЫЙ` → `NOMINAL`.
5. The adjective `гидроакустический` is `underwater acoustic` (or just `acoustic` when the context is already underwater), never `hydroacoustic`.
6. Cyrillic look-alikes are errors in EN text: `°С` with a Cyrillic `С` → `°C`, the Cyrillic `х` used as a multiplication sign → `x`, `Ф` as the diameter sign → `Ø`, `№` → `No.`. `docsync.py check` reports them as Cyrillic residue.
7. Add new terms under `## Added in batch <slug>`. Preserve existing terminology unless the maintainer approves a change or a final terminology review resolves a recorded variant.

Column `Source EN file`: the EN document(s) where the variant occurs (paths relative to `documentation/EN/`, or root pages); `(+n)` = n more files. `CLAUDE.md` = fixed by the sync rules.

## 1. Fixed terms

| RU | EN | Source EN file | Note |
|---|---|---|---|
| маяк-ответчик | responder-beacon | CLAUDE.md | |
| пеленгационная антенна | direction-finding antenna | CLAUDE.md | |
| Спецификация устройства | Device specification | CLAUDE.md | |
| Руководство пользователя | User's manual | CLAUDE.md | |
| Инструкция по эксплуатации | User's manual | RedPhone/RedPhone_OS_Users_manual_en.md | Same document type as `Руководство пользователя` |
| Краткое описание | Data brief | CLAUDE.md | |
| Протокол информационного сопряжения | Communication protocol specification | CLAUDE.md | |
| Описание протокола сопряжения; Спецификация протокола сопряжения | Communication protocol specification | uWAVE/uWAVE_Protocol_Specification_en.md (+2) | RU index pages use these as synonyms of `Протокол информационного сопряжения`; variant `Communication protocol description` (RedWAVE) |
| Схема подключения; Схема включения устройства | Wiring diagram | CLAUDE.md | |
| Пультовое приложение | Host application | CLAUDE.md | |
| Технический паспорт; Паспорт изделия | Product passport | CLAUDE.md | `(шаблон)` → `(template)` |
| История версий и изменений | Version history & changes | CLAUDE.md | |
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
| Главная | Main | CLAUDE.md | |
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

**UI strings that are already English in RU:** tab and button names such as `❗ CONNECTION`, `🛸 EXTRA`, `🧪 PHYSICS`, menu labels in the original software language. When RU quotes a Russian UI label of software that has an English UI (AzimuthSuite, AzimuthConsole, uNav, RedNAV Host, ZHost), use the real English UI string; if it is unknown, use a faithful literal translation in bold and send any unresolved interpretation to the controller privately.

**Organization:** the brand is UC&NL, Underwater Communication & Navigation Laboratory (`Лаборатория подводной связи и навигации` in running text). The official English legal name is **UCNL LLC**: `ООО "Лаборатория подводной связи и навигации"`, `OOO "Лаборатория подводной связи и навигации"` (the RU sources also spell `ООО` with Latin `O`) and `ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ЛАБОРАТОРИЯ ПОДВОДНОЙ СВЯЗИ И НАВИГАЦИИ"` all become `UCNL LLC`.

**Personal names** are transliterated as in the authors' own English publications: Дикарев → Dikarev, Дмитриев → Dmitriev, Кубкин → Kubkin, Василенко → Vasilenko, Абеленцев → Abelentsev; initials keep their order (`А. В. Дикарев` → `A. V. Dikarev`).

## 3. Sections, breadcrumbs and document types

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Гидроакустические навигационные и трекинговые системы; Навигационные и трекинговые системы | Navigation & tracking systems | navigation_and_tracking_systems_en.md (+30) | Breadcrumb section, index `/navigation_and_tracking_systems_en` |
| Гидроакустические модемы | Underwater acoustic modems | underwater_acoustic_modems_en.md (+13) | Index `/underwater_acoustic_modems_en` |
| Голосовая подводная связь (водолазная телефония) | Underwater wireless voice systems | underwater_wireless_voice_systems_en.md (+6) | |
| Гидрофоны и гидроакустические антенны | Hydrophones & transducers | underwater_acoustic_antennas_en.md (+6) | |
| Аксессуары | Accessories | accessories_en.md (+5) | |
| Специализированное оборудование | Other equipment | underwater_bespoke_systems_en.md (+4) | |
| Медиа | Media | media_videos_en.md | |
| Наши проекты для образования; Образовательные проекты | Educational projects | educational_projects_en.md (+3) | Breadcrumb section. Variant Our educational projects (index page title). The WAYU and A3S RU documents use this breadcrumb; existing EN WAYU documents point to Navigation & tracking systems instead — mirror RU |
| Дополнительные материалы | Miscellaneous info | misc_en.md (+9) | |
| Online утилиты | Online utilities | online_utilities_en.md | |
| Документация | Products documentation | README.md | Site index section |
| Техподдержка и соцсети | Support & social media | README.md | |
| Прочее | Media, educational projects and other things | README.md | Site index section; fix `educational project` |
| На главную | Back to main | accessories_en.md (+3) | |
| Вернуться к содержанию | Back to contents | RedWAVE/RedWAVE_Protocol_Specification_en.md | |
| К общему списку медиаматериалов | Back to all media | Zima/media.md (+2) | |
| Содержание | Contents | Zima/Zima2_Users_manual_en.md (+15) | |
| Таблица сравнения гидроакустических модемов; Сравнение гидроакустических модемов | Modems comparison table | modems_comparison_en.md | |
| Таблица сравнения навигационных систем | Comparison table of navigation systems | navigation_systems_comparison_en.md | |
| Сравнительная таблица модемов семейства uWave; Сравнение модемов семейства uWave | uWave family modems comparison table | uWAVE/uWAVE_Modems_comparison_en.md | |
| Краткое описание семейства устройств uWave | uWave devices family: Data brief | uWAVE/uWAVE_Family_en.md | |
| Руководство по обновлению прошивки; Инструкция по обновлению прошивки модемов uWave | Firmware update guide | uWAVE/uWAVE_FW_Updating_en.md | |
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
| гидроакустическая навигационная система | underwater acoustic navigation system | Zima/Zima_Users_manual_en.md (+2) | |
| гидроакустическая трекинговая система | underwater acoustic tracking system | WAYU/WAYU_Users_Manual_en.md (+1) | |
| станция пеленгования; гидроакустическая станция пеленгования | direction-finding station | Zima/Zima_B_Specification_en.md | Variants direction finding antenna / base station / Hydroacoustic direction-finding base station |
| маяк-ответчик навигационной системы Zima2 USBL | Zima2 USBL responder-beacon | Zima/Zima2R_Specification_en.md | |
| микро маяк-ответчик | micro responder-beacon | — | Zima2-uR |
| маяк-ответчик на глубину до 1000 м | responder-beacon rated to 1000 m | navigation_and_tracking_systems_en.md | Variant 1000 m depth rating responder-beacon |
| LBL-трансивер | LBL transceiver | — | Zima2-L, Zima2-LX |
| решатель (Solver) | solver | — | Zima2-SL |
| блок питания и коммутации | power supply and switching unit | — | Bat&Link Box. Variant Autonomous power supply (index pages) |
| источник питания и преобразователь интерфейса | power supply and interface converter | Zima/Bat_n_link_box_Users_manual_en.md | |
| Автономный источник питания и преобразователь RS422/485⮀USB | Autonomous power supply and RS422/485⮀USB converter | — | accessories index |
| семейство устройств гидроакустической связи; семейство устройств гидроакустической цифровой связи | family of underwater acoustic (digital) communication devices | uWAVE/uWAVE_Family_en.md | |
| Гидроакустический модем кодовой связи; модем кодовой гидроакустической связи | underwater acoustic code communication modem | RedGTR/RedGTR_Specifications_en.md (+1) | Variant code communication underwater acoustic modem |
| гидроакустический модем начального уровня | entry-level underwater acoustic modem | — | uSwitch |
| Буй-ретранслятор; Навигационный гидроакустический буй | GNSS-equipped sonobuoy | RedWAVE/RedBASE_Specification_en.md | RedBase; established EN product description |
| Навигационный буй | Navigation buoy | WAYU/WAYU_GIB_Specification_en.md (+1) | GIB |
| Навигационный приемник для ТНПА/АНПА; Универсальный навигационный приемник | navigation receiver for ROVs and AUVs; universal navigation receiver | RedWAVE/RedNODE_Specification_en.md | RedNODE |
| Навигационный приемник для водолазов; Водолазный навигационный приемник | diver's navigation receiver | RedWAVE/RedNAV_Specification_en.md | RedNAV |
| Навигационный планшет водолаза; Водолазный планшет | diver's navigation tablet; diver's tablet | RedWAVE/Aquatab_s_specification_en.md | Aquatab S |
| Приемник сигнала навигационных буев | navigation buoy signal receiver | WAYU/WAYU_RF_Dongle_Specification_en.md | Variant Navigation receiver |
| Навигационный маяк - пингер | navigation pinger beacon | RWLT/RWLT_Pinger_Specification_en.md | |
| навигационный приемник для трекинговых систем RWLT/WAYU | navigation receiver for RWLT/WAYU tracking systems | RWLT/uNav_protocol_specification_en.md | Variant navigation solver/radio modem |
| радиодонгл; Radio dongle | radio dongle | RWLT/RWLT_RF_Dongle_en.md | |
| Радиодонгл для настройки приборов RedPhone-DX | radio dongle for configuring RedPhone-DX devices | RedPhone/RedPhone_RF_Dongle_Specification_en.md | Variant RedPhone-DX configuration tool |
| Надводная станция (водолазной беспроводной / голосовой гидроакустической) связи | surface station (of the wireless diver voice communication system) | RedPhone/RedPhone_OS_Specification_en.md (+4) | |
| Водолазная станция (беспроводной / голосовой гидроакустической) связи | diver station (of the wireless voice communication system) | RedPhone/RedPhone_DX_Specification_en.md (+2) | |
| с увеличенной дальностью | extended-range | — | RedPhone-MOS, RedPhone-MDX |
| Система беспроводной гидроакустической голосовой связи | wireless underwater acoustic voice communication system | — | |
| Система связи дайверов | diver communication system | — | Phone-T / Phone-S kits |
| Модуль управления гидроакустическими размыкателями | Acoustic release control unit | F4105/F4105_SU_Specification_en.md | |
| Актуатор-размыкатель | Release unit | F4105/F4105_BU_Specification_en.md | |
| Гидроакустический пробудитель | Acoustic wake-up unit | F4105/F4105_AU_Specification_en.md | |
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
| Приемная антенна; Антенна гидроакустическая приемная | receiving transducer | Transducers/R_1.d3505_1_Specification_en.md | |
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
| ОСОБЕННОСТИ | FEATURES | Accessories/Sub_batteries_en.md (+2) | |
| Отличительные черты; Особенности | Distinctive features; Features | Zima/Zima_DataBrief_en.md (+3) | |
| ОПИСАНИЕ | DESCRIPTION | A3S/A3R_Datasheet_en.md (+36) |  |
| ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ | TECHNICAL SPECIFICATIONS | Zima/Zima2RK_Specification_en.md (+33) | |
| ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ | ADDITIONAL PARAMETERS | Transducers/RT_1_524525_1_FF_Specification_en.md (+4) | |
| ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ | ADDITIONAL INFORMATION | Misc/BatLinkBox_MSDS_en.md (+11) |  |
| ГАБАРИТНЫЙ ЧЕРТЕЖ | DIMENSIONAL DRAWING | Transducers/R_1.d3505_1_Specification_en.md (+7) | |
| НАЗНАЧЕНИЕ ЖИЛ КАБЕЛЯ | CABLE WIRE ASSIGNMENT | Transducers/R_1.d3505_1_Specification_en.md (+7) | |
| НАЗНАЧЕНИЕ ЖИЛ КАБЕЛЯ И РАСПИНОВКА | CABLE WIRE ASSIGNMENT AND PINOUT | Accessories/Sub_batteries_en.md (+1) | Variants ADDITIONAL SPECIFICATIONS / PINOUT (misaligned) |
| Назначение жил кабеля и габариты | Cable wire assignment and dimensions | Zima/ZimaR_wiring_diagram_en.md | Header cell; variant Wiring diagram and drawings |
| РАСПИНОВКА И ПОДКЛЮЧЕНИЕ | PINOUT AND CONNECTION | A3S/A3R_Datasheet_en.md (+2) |  |
| РАСПИНОВКА РАЗЪЕМА; Распиновки разъемов | CONNECTOR PINOUT; Connector pinouts | F4105/F4105_AU_Specification_en.md (+2) |  |
| РАЗЪЕМ XS1 | CONNECTOR XS1 | A3S/A3R_Datasheet_en.md (+1) | Same pattern for every connector designator |
| ТРЕБОВАНИЯ ПО УСТАНОВКЕ | INSTALLATION REQUIREMENTS | uWAVE/uWAVE_wiring_diagram_en.md | |
| ВАРИАНТЫ АВТОНОМНОГО ИСПОЛНЕНИЯ | STANDALONE VERSIONS | WAYU/WAYU_Pinger_Specification_en.md | Variant AUTONOMOUS OPTIONS |
| КАНАЛЫ И ПОЛОСЫ ЧАСТОТ | CHANNELS AND FREQUENCY BANDS | RedPhone/RedPhone_Specification_en.md | |
| Введение | Introduction | Zima/Bat_n_link_box_Users_manual_en.md (+15) | |
| Назначение | Purpose | RWLT/RWLT_Users_Manual_en.md (+10) | Heading. In pinout tables the column `Назначение` is `Function` |
| Общие сведения; Общие данные; Общие положения | General information | RWLT/RWLT_DataBrief_en.md (+7) | Variants General info / Brief description |
| Состав системы | System composition | Zima/Zima2_Users_manual_en.md (+8) | Variant Composition of the system |
| Комплект поставки | Delivery set | RedPhone/RedPhone_DX_Users_Manual_en.md (+2) | |
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
| Обязательства и отказ от ответственности | Obligations and disclaimer | RWLT/RWLT_Users_Manual_en.md (+8) | |
| Ограничение ответственности производителя | Limitation of the manufacturer's liability | Zima/Zima2_Users_manual_en.md (+8) | |
| Условия замены и бесплатного гарантийного обслуживания | Terms of replacement and free warranty service | Zima/Bat_n_link_box_Users_manual_en.md (+8) | Variant Conditions for replacement and free warranty service |
| Медиаматериалы | Media | RedPhone/media.md | |
| Шаг 1 | Step 1 | RedPhone/RedPhone_DX_Users_Manual_en.md (+1) | Same pattern for `Шаг 1.1` etc. |
| Рецепт 1; Готовые рецепты | Recipe 1; Recipes | uWAVE/uWAVE_Protocol_Specification_en.md | |
| Приложения | Appendices | uWAVE/uWAVE_Protocol_Specification_en.md | Variant Appendix; single `Приложение А` → `Appendix A` |
| Замечания | Remarks | Misc/RedPhone_OS_MSDS_en.md (+6) | |

## 6. Specification tables

| RU | EN | Source EN file | Note |
|---|---|---|---|
| ПАРАМЕТР / ЗНАЧЕНИЕ | PARAMETER / VALUE | A3S/A3R_Datasheet_en.md (+42) |  |
| НАИМЕНОВАНИЕ | NAME | Accessories/Flange_rod_mound_Specification_en.md (+6) |  |
| ФУНКЦИЯ | FUNCTION | A3S/A3R_Datasheet_en.md (+7) |  |
| ОБОЗНАЧЕНИЕ | DESIGNATION | uSwitch/uSwitch_Specification_en.md | |
| НОМЕР КОНТАКТА; № КОНТАКТА; № КОНТАКТА РАЗЪЕМА; Номер пина | PIN NUMBER; PIN No.; CONNECTOR PIN No.; Pin number | A3S/A3R_Datasheet_en.md (+5) | Variant PIN # / № Pin |
| ЦВЕТ ЖИЛЫ (КАБЕЛЯ) | WIRE COLOR | WAYU/WAYU_Pinger_Specification_en.md | |
| АКТИВНОЕ СОСТОЯНИЕ | ACTIVE STATE | A3S/A3R_Datasheet_en.md (+2) |  |
| ГАБАРИТЫ | DIMENSIONS | A3S/A3R_Datasheet_en.md (+3) | Fix typo DIMENSTIONS |
| ГАБАРИТЫ (Ф х h); (д х ш х в) | DIMENSIONS (Ø x h); (L x W x H) | Zima/Zima2B_Specification_en.md | Keep the RU symbol order; `Ф` → `Ø` |
| ВЕС; ВЕС (сухой) | WEIGHT; WEIGHT (dry) | A3S/A3R_Datasheet_en.md (+16) | Fix typo WIGHT |
| МАКСИМАЛЬНАЯ ГЛУБИНА | MAXIMUM DEPTH | uWAVE/uWAVE_Max_Specification_en.md (+2) | |
| МАКСИМАЛЬНАЯ РАБОЧАЯ ГЛУБИНА | MAXIMUM OPERATING DEPTH | — | |
| МАКСИМАЛЬНАЯ ГЛУБИНА ПОГРУЖЕНИЯ | MAXIMUM IMMERSION DEPTH | WAYU/WAYU_Pinger_Specification_en.md (+5) | |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ АКУСТИЧЕСКОЙ СВЯЗИ; МАКСИМАЛЬНАЯ АКУСТИЧЕСКАЯ ДАЛЬНОСТЬ СВЯЗИ | MAXIMUM ACOUSTIC COMMUNICATION RANGE | A3S/A3R_Datasheet_en.md (+13) | |
| МАКСИМАЛЬНАЯ ДАЛЬНОСТЬ РАДИОСВЯЗИ | MAXIMUM RADIO COMMUNICATION RANGE | WAYU/WAYU_RF_Dongle_Specification_en.md (+2) | Variants MAX. RF RANGE / COMMUNICATION RANGE |
| МАКСИМАЛЬНОЕ АКУСТИЧЕСКОЕ ДАВЛЕНИЕ (В полосе) | MAXIMUM ACOUSTIC SOURCE LEVEL (in band) | A3S/A3T_Datasheet_en.md (+3) | |
| МАКСИМАЛЬНАЯ ОТНОСИТЕЛЬНАЯ СКОРОСТЬ | MAXIMUM RELATIVE VELOCITY | A3S/A3R_Datasheet_en.md (+4) |  |
| МАКСИМАЛЬНАЯ СКОРОСТЬ ОТНОСИТЕЛЬНО БУЕВ | MAXIMUM VELOCITY RELATIVE TO BUOYS | WAYU/WAYU_Pinger_Specification_en.md (+3) | Variants MAX. RELATIVE VELOCITY / MAX. RELATIVE SPEED |
| МАКСИМАЛЬНЫЙ РАЗМЕР РАБОЧЕЙ ОБЛАСТИ | MAXIMUM WORKING AREA SIZE | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| МАКСИМАЛЬНОЕ ВРЕМЯ АВТОНОМНОЙ РАБОТЫ (В РЕЖИМЕ ПРИЕМА / В СМЕШАННОМ РЕЖИМЕ …) | MAXIMUM BATTERY LIFE (RX MODE / MIXED MODE …) | RedPhone/RedPhone_OS_Specification_en.md (+7) | Keep the RU qualifiers, e.g. `(20% TX, 80% RX)`; variant BATTERY LIFE / MAXIMUM TIME OF OPERATION |
| МАКСИМАЛЬНОЕ ВНЕШНЕЕ ГИДРОСТАТИЧЕСКОЕ ДАВЛЕНИЕ | MAXIMUM EXTERNAL HYDROSTATIC PRESSURE | Transducers/R_1.d3505_1_Specification_en.md | |
| НОМИНАЛЬНАЯ ПОГРЕШНОСТЬ ПО ГЛУБИНЕ | NOMINAL DEPTH ACCURACY | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| НОМИНАЛЬНАЯ ТОЧНОСТЬ ОПРЕДЕЛЕНИЯ ГОРИЗОНТАЛЬНОГО УГЛА ПРИХОДА СИГНАЛА | NOMINAL HORIZONTAL ANGLE OF ARRIVAL ACCURACY | Zima/Zima2B_Specification_en.md | RU source spells `СИНГНАЛА`; existing HORIZONTAL ANGLE OF ARRIVAL ESTIMATION ACCURACY (typ.) |
| НОМИНАЛЬНАЯ ГОРИЗОНТАЛЬНАЯ ПОГРЕШНОСТЬ (2DRMS) | NOMINAL HORIZONTAL ACCURACY (2DRMS) | RedWAVE/RedNAV_Specification_en.md (+1) | Variant NOMINAL 2D-ACCURACY |
| НОМИНАЛЬНАЯ ЧАСТОТА ОБНОВЛЕНИЯ ГЕОГРАФИЧЕСКОГО ПОЛОЖЕНИЯ | NOMINAL POSITION UPDATE RATE | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| НОМИНАЛЬНОЕ ВРЕМЯ ДО ПЕРВОГО УТОЧНЕНИЯ МЕСТОПОЛОЖЕНИЯ | NOMINAL TIME TO FIRST FIX | RedWAVE/RedNAV_Specification_en.md (+1) | |
| НОМИНАЛЬНОЕ ВРЕМЯ СТАРТА; ВРЕМЯ СТАРТА | NOMINAL STARTUP TIME; STARTUP TIME | uWAVE/uWAVE_Max_Specification_en.md (+3) | Variants RATED STARTUP TIME / RATE STARTUP TIME (typo) |
| РАЗРЕШЕНИЕ ПО ГЛУБИНЕ; РАЗРЕШЕНИЕ ДАТЧИКА ГЛУБИНЫ (локально / удаленно) | DEPTH RESOLUTION; DEPTH SENSOR RESOLUTION (local / remote) | RWLT/RWLT_Pinger_K_Specification_en.md |  |
| РАЗРЕШЕНИЕ ПРИ ИЗМЕРЕНИИ ВРЕМЕНИ РАСПРОСТРАНЕНИЯ СИГНАЛА | SIGNAL PROPAGATION TIME MEASUREMENT RESOLUTION | uWAVE/uWAVE_Max_Specification_en.md (+1) |  |
| РАЗРЕШЕНИЕ ПРИ ИЗМЕРЕНИИ НАКЛОННОЙ ДАЛЬНОСТИ | SLANT RANGE MEASUREMENT RESOLUTION | Zima/Zima2B_Specification_en.md | Existing SLANT RANGE RESOLUTION |
| ТОЧНОСТЬ ВСТРОЕННОГО ДАТЧИКА ТЕМПЕРАТУРЫ | BUILT-IN TEMPERATURE SENSOR ACCURACY | RedWAVE/RedNAV_Specification_en.md (+1) |  |
| ДИАПАЗОН РАБОЧИХ ТЕМПЕРАТУР | OPERATING TEMPERATURE RANGE | A3S/A3R_Datasheet_en.md (+17) | |
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
| МАТЕРИАЛ КОРПУСА | HOUSING MATERIAL | RedWAVE/RedBASE_Specification_en.md | |
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
| Протокол физического уровня | Physical layer protocol | Zima/Zima2_Protocol_Specification_en.md (+4) | |
| Стандарт протокола диалогового уровня NMEA0183 | NMEA0183 dialog layer protocol standard | Zima/Zima2_Protocol_Specification_en.md | |
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
| Паспорт безопасности химической продукции (MSDS) | Material safety data sheet (MSDS) | Misc/BatLinkBox_MSDS_en.md (+10) | |
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
| круговое вероятное отклонение | circular error probable | Zima/Zima2_Users_manual_en.md |  |
| угловая поправка | angular correction | Zima/Zima2_Users_manual_en.md | AzimuthSuite field label |
| Взаимодействие с системой | Interacting with the system | Zima/Zima2_Users_manual_en.md | |
| Ручное задание координат и направления | Manual setting of coordinates and direction | Zima/Zima2_Users_manual_en.md | |
| (устаревшее) приложение | obsolete application | Zima/Zima2_Users_manual_en.md | AzimuthSuite |
| РАБОЧИЙ КОНУС (ОТНОСИТЕЛЬНО ГОРИЗОНТАЛИ) | OPERATING CONE (RELATIVE TO THE HORIZONTAL) | Zima/Zima2B_Specification_en.md |  |
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
| до 16 изолирующих адресов | up to 16 isolating addresses | Zima/Zima2R_Specification_en.md (+3) |  |
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
| Прием! (конец голосового сообщения) | Over! | RedPhone/RedPhone_OS_Users_manual_en.md | Radio procedure word |
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
| ТЕЛЕМЕТРИЧЕСКАЯ ИНФОРМАЦИЯ | TELEMETRY INFORMATION | RWLT/RWLT_Pinger_K_Specification_en.md |  |
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

## Added in batch wayu-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Наши проекты для образования (раздел) | Educational projects | WAYU/*_en.md | Breadcrumb section of the WAYU documents, index page `/educational_projects_en` |
| Автоматическое включение от воды / в воде | Automatic activation in water | WAYU/WAYU_DataBrief_en.md (+3), RWLT/RWLT_GIB_Specification_en.md | |
| Навигационный гидроакустический маяк-пингер | Underwater acoustic navigation pinger beacon | WAYU/WAYU_DataBrief_en.md | |
| Радиодонгл - приемник навигационных буев | Radio dongle - navigation buoy receiver | WAYU/WAYU_DataBrief_en.md | |
| Решаемые задачи | Tasks to be solved | WAYU/WAYU_DataBrief_en.md, RedWAVE/RedWAVE_DataBrief_en.md | |
| Отличительные черты | Distinctive features | WAYU/WAYU_DataBrief_en.md | |
| От каждого до каждого из буев должно быть не более … | The distance between any two buoys must be no more than … | WAYU/WAYU_DataBrief_en.md | |
| НАЗНАЧЕНИЕ ЖИЛ КАБЕЛЯ И РАСПИНОВКА | CABLE WIRE ASSIGNMENT AND PINOUT | WAYU/WAYU_Pinger_Specification_en.md | |
| № КОНТАКТА РАЗЪЕМА | CONNECTOR PIN No. | WAYU/WAYU_Pinger_Specification_en.md | |
| интегрируемое / автономное исполнение | integrated / standalone version | WAYU/WAYU_Pinger_Specification_en.md | |
| неразделанный кабель | unterminated cable | WAYU/WAYU_Pinger_Specification_en.md | |
| подводные аккумуляторные сборки | underwater battery packs | WAYU/WAYU_Pinger_Specification_en.md | |
| U<sub>пит.</sub> | U<sub>supply</sub> | WAYU/WAYU_Pinger_Specification_en.md | |
| этилвинилацетат (EVA) | ethylene-vinyl acetate (EVA) | WAYU/WAYU_GIB_Specification_en.md | |
| ЗАРЯДКА / ВРЕМЯ ЗАРЯДА ВСТРОЕННОЙ АКБ | CHARGING / CHARGING TIME OF THE BUILT-IN BATTERY | WAYU/WAYU_GIB_Specification_en.md | |
| разгрузочный кранец | relief fender | WAYU/WAYU_Users_Manual_en.md | |
| в акватории | in the operating area | WAYU/WAYU_Users_Manual_en.md | |
| выпуклый четырехугольник | convex quadrilateral | WAYU/WAYU_Users_Manual_en.md | |
| Горит красным / Не горит (индикатор) | Lit red / Off | WAYU/WAYU_Users_Manual_en.md | |
| схема установки | installation layout | WAYU/WAYU_Users_Manual_en.md | |
| шлюз (канала) | lock | WAYU/media.md | Old EN "Gateway" |
| Yandex карты | Yandex Maps | WAYU/media.md | |

## Added in batch redwave-4

| RU | EN | Source EN file | Note |
|---|---|---|---|
| водолазный навигатор; навигатор водолаза | diver's navigator | RedWAVE/RedWave_tech_pass_en.md, RedWAVE/RedWAVE_DataBrief_en.md | RedNav |
| водолазный планшет Aquatab | Aquatab diver's tablet | RedWAVE/RedWave_tech_pass_en.md | |
| в водолазном исполнении | in the diver version | RedWAVE/RedWave_tech_pass_en.md | |
| гидроакустический навигационный приемник RedNode | RedNode underwater acoustic navigation receiver | RedWAVE/RedWave_tech_pass_en.md | |
| методом лазерной гравировки | by laser engraving | RedWAVE/RedWave_tech_pass_en.md | Factory numbers; hot stamping = горячее клеймение |

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

## Added in batch a3s-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Стандартные комплекты и что с ними можно сделать | Standard kits and what you can do with them | A3S/A3S_packages_en.md | Breadcrumb and title |
| КОМПЛЕКТ №N | KIT No. N | A3S/A3S_packages_en.md | |
| гидроакустическая приемопередающая антенна | underwater acoustic transceiving transducer | A3S/A3S_packages_en.md (+2) | |
| модуль одночастотного приемника / импульсного одночастотного передатчика | single-frequency receiver module / single-frequency pulse transmitter module | A3S/A3S_packages_en.md | |
| приемная решетка (N-элементная) | (N-element) receiving array | A3S/A3S_packages_en.md | |
| разностно-дальномерная система | range-difference system | A3S/A3S_packages_en.md | |
| донная дальномерная база | seabed ranging base | A3S/A3S_packages_en.md | |
| метод "запрос-ответ"; по предварительной синхронизации | "request-response" method; by prior synchronization | A3S/A3S_packages_en.md | |
| режим ответчика | responder mode | A3S/A3R_Datasheet_en.md | Old EN "Transponder mode" |
| Вход / Выход антенны | Transducer input / output | A3S/A3R_Datasheet_en.md, A3S/A3T_Datasheet_en.md | |
| Строб (приемника); Общий строб приемников | (receiver) strobe; common receiver strobe | A3S/A3R_Datasheet_en.md | |
| Инициация передачи импульса | Pulse transmission trigger | A3S/A3T_Datasheet_en.md, A3S/A3R_Datasheet_en.md | |
| Адрес на шине; перемычка; объединяются в стек | bus address; jumper; stackable | A3S/A3R_Datasheet_en.md | |
| МИНИМАЛЬНАЯ ПАУЗА МЕЖДУ ИМПУЛЬСАМИ | MINIMUM PAUSE BETWEEN PULSES | A3S/A3T_Datasheet_en.md | |

## Added in batch transducers-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Антенна гидроакустическая приемопередающая (header cell); Приемопередающая антенна (breadcrumb) | Underwater acoustic transducer; Transducer | Transducers/RT_1_332820_1_Specification_en.md (+4) | As in the fixed-term note of `гидроакустическая антенна` |
| РАЗМЕР (Ф х h) | SIZE (Ø x h) | Transducers/RT_1_332820_1_Specification_en.md (+4) | Old EN: DIMENSIONS (Ф х h) with Cyrillic letters |
| МАКСИМАЛЬНОЕ ПОДВОДИМОЕ НАПРЯЖЕНИЕ (ПИКОВОЕ) | MAXIMUM INPUT VOLTAGE (PEAK) | Transducers/RT_1_332820_1_Specification_en.md (+4) | Old EN: MAX. INPUT VOLTAGE (peak) |
| ДИАМЕТР СЕЧЕНИЯ КАБЕЛЯ | CABLE DIAMETER | Transducers/RT_1_524525_1_FF_Specification_en.md (+4) | |
| ДИАГРАММА НАПРАВЛЕННОСТИ (… кГц) | BEAM PATTERN (… kHz) | Transducers/RT_1_332820_1_Specification_en.md (+3) | |
| Тор, соосный с цилиндром | Torus coaxial with the cylinder | Transducers/RT_1_332820_1_Specification_en.md (+3) | |
| УГОЛ РАСТВОРА ДИАГРАММЫ (… кГц) | BEAM ANGLE (… kHz) | Transducers/RT_1_332820_1_Specification_en.md (+3) | |
| АЧХ 3 дБ; АЧХ < 3 дБ | frequency response 3 dB; frequency response < 3 dB | Transducers/RT_1_332820_2_Specification_en.md (+3) | Literal; RT-1.524525-1 and RT-2.332820-1 EN (not in this batch) have only "(3 dB)" in the beam angle row |
| РАБОЧАЯ ПОЛОСА (прием) / (излучение) | OPERATING BANDWIDTH (receive) / (transmit) | Transducers/RT_1_332820_2_Specification_en.md (+2) | RU writes `(изучение)`, a typo |
| НАПРЯЖЕНИЕ ПИТАНИЯ (прием) | SUPPLY VOLTAGE (receive) | Transducers/RT_1_332820_2_Specification_en.md (+1) | |
| + 5 В питание предусилителя | + 5 V preamplifier power supply | Transducers/RT_1_332820_2_Specification_en.md (+2) | |
| Встроенный полосовой фильтр | Built-in band-pass filter | Transducers/RT_1_332820_2_Specification_en.md (+2) | |
| активный полосовой фильтр 4 порядка на приеме и пассивный LC-фильтр второго порядка на излучение | 4th-order active band-pass filter for reception and a second-order passive LC filter for transmission | Transducers/RT_1_332820_2_Specification_en.md (+2) | Digit and word kept as in RU |
| Необслуживаемая моноблочная конструкция, выполняемая по запатентованной технологии | Maintenance-free monoblock design made using a patented technology | Transducers/RT_1_332820_1_Specification_en.md (+3) | |
| Полное отсутствие корродирующих элементов | Complete absence of corroding elements | Transducers/RT_1_332820_1_Specification_en.md (+4) | Old EN: corrosive |
| Высококачественный экранированный кабель в полиуретановой изоляции | High-quality shielded cable with polyurethane insulation | Transducers/RT_1_332820_1_Specification_en.md (+4) | |
| Миниатюрная и легкая антенна на основе одного цилиндрического пьезоэлемента | Miniature and lightweight transducer based on a single cylindrical piezoelectric element | Transducers/RT_1_332820_1_Specification_en.md (+1) | |
| Одноэлементная антенна - баланс между чувствительностью в режимах приема и передачи, массой и габаритами | Single-element transducer - a balance between sensitivity in receiving and transmitting modes, weight and dimensions | Transducers/RT_1_524525_1_FF_Specification_en.md (+1) | |
| Антенна на основе двух цилиндрических элементов, соединенных параллельно | Transducer based on two cylindrical elements connected in parallel | Transducers/RT_2_332820_2_Specification_en.md | |
| Водозаполняемая центральная часть для компенсации давления | Free-flooded center section for pressure compensation | Transducers/RT_1_524525_1_FF_Specification_en.md | |
| Паз для крепления | Mounting groove | Transducers/RT_1_332820_1_Specification_en.md (+3) | |
| 3D-модель антенны (STEP) | 3D model of the transducer (STEP) | Transducers/RT_1_524525_1_FF_Specification_en.md | |
| № / Цвет / Назначение (cable table) | No. / Color / Function | Transducers/RT_1_332820_1_Specification_en.md (+4) | |
| Оплетка / Экран | Braid / Shield | Transducers/RT_1_332820_2_Specification_en.md (+2) | |
| Общий (выход) / Сигнал (вход) / Сигнал (выход) | Common (output) / Signal (input) / Signal (output) | Transducers/RT_1_332820_2_Specification_en.md (+2) | |

## Added in batch redwave-3

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Программа и методика испытаний (RedWave) | test program and procedures | RedWAVE/RedNAV_PM_en.md | As in RedPhone/RedPhone_PM_en.md |
| Методика N | Procedure N | RedWAVE/RedNAV_PM_en.md | |
| Выход на заданную точку / на сохраненную точку / на заданную точку группой | Reaching a predefined point / a saved point / a predefined point as a group | RedWAVE/RedNAV_PM_en.md | |
| Полевые испытания / Испытания надежности | Field tests / Reliability tests | RedWAVE/RedNAV_PM_en.md | |
| Предварительные испытания работоспособности | Preliminary operability tests | RedWAVE/RedNAV_PM_en.md | |
| Постановка длинной базы / Завершение испытаний | Deployment of the long base / Completion of the tests | RedWAVE/RedNAV_PM_en.md | |
| Проверка времени автономности буя / прибора RedNav | Buoy battery life check / RedNav instrument battery life check | RedWAVE/RedNAV_PM_en.md | |
| Проверка корпуса буя на соответствие IP68 | Checking the buoy housing for IP68 compliance | RedWAVE/RedNAV_PM_en.md | |
| Буй навигационный / Водолазный навигационный прибор / Устройство зарядное | navigation buoy / diver's navigation instrument / charger | RedWAVE/RedNAV_PM_en.md | Product name first: `[RedBase](…) navigation buoy` |
| плавсредство | watercraft | RedWAVE/RedNAV_PM_en.md | |
| якорная веревка / канаты | anchor line / lines | RedWAVE/RedNAV_PM_en.md | |
| разрывное усилие | breaking strength | RedWAVE/RedNAV_PM_en.md | |
| буек на якоре | anchored marker buoy | RedWAVE/RedNAV_PM_en.md | |
| путевая точка / маршрутная точка / сохраненная точка | waypoint / route point / saved point | RedWAVE/RedNAV_PM_en.md | |
| топопривязка | position referencing | RedWAVE/RedNAV_PM_en.md | |
| водолазная консоль | diving console | RedWAVE/RedNAV_PM_en.md | |
| внешние признаки разгерметизации | external signs of seal failure | RedWAVE/RedNAV_PM_en.md | |
| Образцы считаются работоспособными | Units are considered operable | RedWAVE/RedNAV_PM_en.md | |
| Google Планета Земля; GoogleEarth | Google Earth | RedWAVE/RedNAV_PM_en.md, RedWAVE/uGPSHub_Users_manual_en.md | |
| Главная панель инструментов / Панель инструментов карты / Панель дополнительной информации / Панель легенды (caption) | Main toolbar / Map toolbar / Additional information panel / Legend panel | RedWAVE/uGPSHub_Users_manual_en.md | The headings keep `Legend field` (RU: Поле легенды) |
| рулетка (измерение расстояний на карте) | tape measure | RedWAVE/uGPSHub_Users_manual_en.md | `ruler` is the scale bar |
| функция невязки | residual function | RedWAVE/uGPSHub_Users_manual_en.md | |
| исполнение (сведения об устройстве) | device version | RedWAVE/uGPSHub_Users_manual_en.md | |
| горячие клавиши | keyboard shortcuts | RedWAVE/uGPSHub_Users_manual_en.md | |
| по часовой стрелке от направления на север | clockwise from north | RedWAVE/uGPSHub_Users_manual_en.md | |
| взаимное расположение (объекта и навигационной базы) | relative position | RedWAVE/uGPSHub_Users_manual_en.md | |
| Track Filter FIFO size; Screenshot names ty time (RU quotes) | Track filter FIFO size; Screenshots names by time | RedWAVE/uGPSHub_Users_manual_en.md | Real strings of the UGPSHub application; labels absent from the application stay as RU quotes them |

## Added in batch redwave-2

| RU | EN | Source EN file | Note |
|---|---|---|---|
| гидроакустический навигационный буй-ретранслятор (heading, captions); буи-ретрансляторы (running text) | GNSS-equipped sonobuoy; relay sonobuoys | RedWAVE/RedWAVE_Users_Manual_en.md | Applies the redwave-1 row |
| порядковый номер (адрес) буя | sequence number (address) | RedWAVE/RedWAVE_Users_Manual_en.md | Not "serial number", which is the device serial number |
| схема установки / постановки буя | installation layout | RedWAVE/RedWAVE_Users_Manual_en.md | As in WAYU/WAYU_Users_Manual_en.md |
| кранцы (или поплавки), соответствующие весу веревки | fenders (or floats) matched to the weight of the line | RedWAVE/RedWAVE_Users_Manual_en.md | As in WAYU/WAYU_Users_Manual_en.md |
| Подготовка к использованию и проверка | Preparation for use and checks | RedWAVE/RedWAVE_Users_Manual_en.md | |
| Требования к интеграции и расположению на носителе | Requirements for integration and placement on the carrier | RedWAVE/RedWAVE_Users_Manual_en.md | |
| Работа с устройством | Working with the device | RedWAVE/RedWAVE_Users_Manual_en.md | |
| световая индикация (лампы, источники света) | indicator lamps; indicator light sources | RedWAVE/RedWAVE_Users_Manual_en.md | |
| зарядная площадка | charging pad | RedWAVE/RedWAVE_Users_Manual_en.md | |
| интерфейсный модуль / интерфейсный блок / интерфейсное устройство | interface module / interface unit / interface device | RedWAVE/RedWAVE_Users_Manual_en.md | RU uses three names for one unit; kept literally |
| выносные GPS-антенны на кабеле | remote GPS antennas on a cable | RedWAVE/RedWAVE_Users_Manual_en.md | As in RedWAVE/RedNAV_Specification_en.md |
| подводно-технические работы | underwater engineering work | RedWAVE/RedWAVE_Users_Manual_en.md | As in RedWAVE/RedNAV_Specification_en.md |
| пиктограмма | icon | RedWAVE/RedWAVE_Users_Manual_en.md | |
| стоячая вода | slack water | RedWAVE/RedWAVE_Users_Manual_en.md | |
| струи движителей | thruster wash | RedWAVE/RedWAVE_Users_Manual_en.md | |
| густые заросли водорослей | dense algae growth | RedWAVE/RedWAVE_Users_Manual_en.md | |
| Следует помнить, что | Keep in mind that | RedWAVE/RedWAVE_Users_Manual_en.md | |

## Added in batch uswitch-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| Наши проекты для образования (breadcrumb) | Educational projects | uSwitch/uSwitch_Specification_en.md | Index page `/educational_projects_en` |
| Функция включения при контакте с водой | Switch-on function upon contact with water | uSwitch/uSwitch_Specification_en.md | |
| Функция измерения времени распространения сигнала | Signal propagation time measurement function | uSwitch/uSwitch_Specification_en.md | |
| сборка печатных плат | printed circuit board assembly | uSwitch/uSwitch_Specification_en.md | |
| контактные площадки | contact pads | uSwitch/uSwitch_Specification_en.md | |
| ОБОЗНАЧЕНИЕ / НАИМЕНОВАНИЕ / АКТИВНОЕ СОСТОЯНИЕ / ФУНКЦИЯ (pinout table) | DESIGNATION / NAME / ACTIVE STATE / FUNCTION | uSwitch/uSwitch_Specification_en.md | |
| Земля/Общий | Ground/Common | uSwitch/uSwitch_Specification_en.md | |
| +U<sub>пит.</sub> | +U<sub>supply</sub> | uSwitch/uSwitch_Specification_en.md | |
| детектор воды | water detector | uSwitch/uSwitch_Specification_en.md | |
| передающий тракт | transmit path | uSwitch/uSwitch_Specification_en.md | |
| перемычка (резистор 0 Ом типоразмера 1206); запайка | jumper (0 Ω resistor, size 1206); soldering | uSwitch/uSwitch_Specification_en.md | |

## Added in batch accessories-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| ОСОБЕННОСТИ (accessories) | FEATURES | Accessories/uPress_Specification_en.md (+6) | |
| Отечественная разработка и производство | Domestic development and production | Accessories/uPress_Specification_en.md (+1) | Market-specific (rule 6), kept |
| Патентованная конструкция; Патент RU… | Patented design; Patent RU… | Accessories/uPress_Specification_en.md (+1) | Patent numbers verbatim |
| Возможно окрашивание в любой цвет по каталогу RAL при заказе от 50 шт. | Painting in any color from the RAL catalog is possible when ordering 50 pcs or more. | Accessories/uPress_Specification_en.md (+2) | |
| С учетом кабеля стандартной длины | Including a cable of standard length | Accessories/uPress_Specification_en.md (+1) | |
| Параметр может быть изменен по договоренности | The parameter can be changed by agreement | Accessories/uPress_Specification_en.md (+1) | |
| СОСТОЯНИЕ ПО УМОЛЧАНИЮ / НОРМАЛЬНО РАЗОМКНУТ | DEFAULT STATE / NORMALLY OPEN | Accessories/uPress_Specification_en.md | |
| ЦВЕТ КОРПУСА / ЦВЕТ НАЖИМНОГО ЭЛЕМЕНТА | HOUSING COLOR / PUSH ELEMENT COLOR | Accessories/uPress_Specification_en.md | |
| ХОД НАЖАТИЯ ДО СРАБАТЫВАНИЯ / УСИЛИЕ СРАБАТЫВАНИЯ / КОЛИЧЕСТВО СРАБАТЫВАНИЙ | TRAVEL TO ACTUATION / ACTUATION FORCE / NUMBER OF ACTUATIONS | Accessories/uPress_Specification_en.md | |
| МАКСИМАЛЬНАЯ КОММУТИРУЕМАЯ МОЩНОСТЬ; ДИАПАЗОН КОММУТИРУЕМЫХ ТОКОВ / НАПРЯЖЕНИЙ | MAXIMUM SWITCHING POWER; SWITCHING CURRENT / VOLTAGE RANGE | Accessories/uPress_Specification_en.md | |
| РОД ТОКА: постоянный, переменный | CURRENT TYPE: DC, AC | Accessories/uPress_Specification_en.md | |
| наработка на отказ | mean time between failures | Accessories/uPress_Specification_en.md | |
| МАТЕРИАЛ ИЗОЛЯЦИИ КАБЕЛЯ | CABLE INSULATION MATERIAL | Accessories/uPress_Specification_en.md (+1) | |
| МАТЕРИАЛ ЗАЩИТНОГО КОМПАУНДА / ТОЛЩИНА ЗАЩИТНОГО СЛОЯ КОМПАУНДА | POTTING COMPOUND MATERIAL / POTTING COMPOUND THICKNESS | Accessories/Sub_batteries_en.md (+2) | |
| Герметичная заливка в полиуретановый компаунд | Hermetic potting in polyurethane compound | Accessories/Sub_batteries_en.md (+1) | |
| ЕМКОСТЬ, Вт·ч; ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ (Вт·ч) | ENERGY CAPACITY | Accessories/Sub_batteries_en.md (+1) | As in the glossary row `ЭЛЕКТРИЧЕСКАЯ ЕМКОСТЬ` |
| ТИП ЭЛЕМЕНТОВ / САМОРАЗРЯД / ДИАПАЗОН ТЕМПЕРАТУР ПРИ ЗАРЯДЕ | CELL TYPE / SELF-DISCHARGE / CHARGING TEMPERATURE RANGE | Accessories/Sub_batteries_en.md | |
| ВЕС (в воде) | WEIGHT (in water) | Accessories/Sub_batteries_en.md | |
| уточняется | to be specified | Accessories/Sub_batteries_en.md | |
| MSDS (Паспорт безопасности химической продукции) | MSDS (Material safety data sheet) | Accessories/Sub_batteries_en.md | |
| ЭЛЕКТРОННАЯ ВЕРСИЯ ЭТОГО ДОКУМЕНТА | ELECTRONIC VERSION OF THIS DOCUMENT | Accessories/Sub_batteries_en.md (+1) | |
| конформная аккумуляторная сборка; приборный кейс | conformal battery pack; instrument case | Accessories/Batpacks_en.md | |
| микрофон защищенный для водолазных масок | protected microphone for diving masks | Accessories/uSpeak_specification_en.md | |
| ДЭМШ | DEMSh | Accessories/uSpeak_specification_en.md | Transliterated Russian microphone type |
| ЧУВСТВИТЕЛЬНОСТЬ, мкВ/Па | SENSITIVITY, μV/Pa | Accessories/uSpeak_specification_en.md | |
| Фланцевый кронштейн | Flange rod mount | Accessories/Flange_rod_mound_Specification_en.md | |
| стакан / крышка / полукольцо; круглая выборка; нулевое направление | cup / cap / half-ring; round recess; zero direction | Accessories/Flange_rod_mound_Specification_en.md | |
| крепеж из нержавеющей стали | stainless steel fasteners | Accessories/Flange_rod_mound_Specification_en.md | |
| КОМПЛЕКТ (heading, parts list) | DELIVERY SET | Accessories/Flange_rod_mound_Specification_en.md | As `Комплект поставки` |
| Датчик абсолютного давления (и температуры) | absolute pressure (and temperature) sensor | Accessories/crimea_300_Datasheet_en.md (+1) | |
| ПРОТОКОЛ СОПРЯЖЕНИЯ | COMMUNICATION PROTOCOL | Accessories/crimea_300_Datasheet_en.md | |
| ПОГРЕШНОСТЬ ИЗМЕРЕНИЯ ДАВЛЕНИЯ / ТЕМПЕРАТУРЫ | PRESSURE / TEMPERATURE MEASUREMENT ACCURACY | Accessories/crimea_300_Datasheet_en.md | |
| РАЗРЕШЕНИЕ ПО ДАВЛЕНИЮ / ПО ТЕМПЕРАТУРЕ | PRESSURE / TEMPERATURE RESOLUTION | Accessories/crimea_300_Datasheet_en.md | |
| ДИАПАЗОН ИЗМЕРЯЕМЫХ ДАВЛЕНИЙ / ТЕМПЕРАТУР | MEASURED PRESSURE / TEMPERATURE RANGE | Accessories/crimea_300_Datasheet_en.md | |
| Система команд TNT; Префикс D2H / H2D | TNT command system; D2H / H2D prefix | Accessories/crimea_300_Datasheet_en.md | |
| Настроечные поля / Идентификаторы сервисных операций / Идентификаторы локальных параметров | Configuration fields / Service action identifiers / Local parameter identifiers | Accessories/crimea_300_Datasheet_en.md | |
| работа по запросу / циклическая передача (без запроса) | operation on request / cyclic transmission (without request) | Accessories/crimea_300_Datasheet_en.md (+1) | |
| ОГРАНИЧЕНИЯ / ДОПОЛНИТЕЛЬНЫЕ МАТЕРИАЛЫ | LIMITATIONS / ADDITIONAL MATERIALS | Accessories/crimea_300_Datasheet_en.md | |
| Интерфейсный модуль | interface module | Accessories/crimea_300_OS_Datasheet_en.md | |
| ЖКИ ЭКРАН: Символьный | LCD SCREEN: Character-based | Accessories/crimea_300_OS_Datasheet_en.md | |
| кнопки без фиксации | non-latching buttons | Accessories/crimea_300_OS_Datasheet_en.md | |
| места пайки | soldering points | Accessories/crimea_300_OS_Datasheet_en.md | |
| Калибровка Z0 (атмосферного давления); задание солености; сброс настроек | Z0 calibration (atmospheric pressure calibration); setting the salinity; resetting the settings | Accessories/crimea_300_OS_Datasheet_en.md | Device menu labels |

## Added in batch f4105-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| стопорная гайка | lock nut | F4105/F4105_DataBrief_en.md (+2) | Maintainer decision |
| исполнительное устройство | actuating device | F4105/F4105_DataBrief_en.md (+2) | Maintainer decision |
| стопорный палец | lock pin | F4105/F4105_Users_manual_en.md (+1) | Maintainer decision; `палец стопорной гайки` is `lock nut pin` |
| Модуль программирования и передачи команд | programming and command transmission unit | F4105/F4105_tech_pass_en.md | Distinct from `Модуль программирования и управления`: programming and control unit |
| задающее устройство | setting device | F4105/F4105_DataBrief_en.md (+1) | F4105-SU role |
| поплавок-катушка; поплавок-стабилизатор | float-reel; stabilizer float | F4105/F4105_Users_manual_en.md | |
| мотор-редуктор; стопорный узел | geared motor; stopper knot | F4105/F4105_Users_manual_en.md | |
| фал; грузонесущая проушина | line; load-bearing eye | F4105/F4105_Users_manual_en.md (+2) | |

## Added in batch redline-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| МИНИМАЛЬНЫЙ РАЗМЕР ПАКЕТА ДЛЯ ПЕРЕДАЧИ | MINIMUM PACKET SIZE FOR TRANSMISSION | RedLINE/RedLine_Specification_en.md | |
| локальная переменная | local variable | RedLINE/RedLINE_Protocol_Specifications_en.md | |
| ретрансляция | relaying | RedLINE/RedLINE_Protocol_Specifications_en.md | isRTX field |
| прямой / обратный канал | forward / reverse channel | RedLINE/RedLINE_Protocol_Specifications_en.md | isRVRS field |
| шина данных | data bus | RedLINE/RedLINE_Protocol_Specifications_en.md | |

## Added in batch misc-1

| RU | EN | Source EN file | Note |
|---|---|---|---|
| герметично закрытые ячейки | hermetically sealed cells | Misc/RedPhone_OS_MSDS_en.md (+1) | |
| водяная струя мелкого разбрызгивания | fine water spray | Misc/RedPhone_OS_MSDS_en.md (+1) | |
| автономный дыхательный аппарат; автономный ВДА | self-contained breathing apparatus; self-contained breathing apparatus (SCBA) | Misc/RedPhone_OS_MSDS_en.md (+1) | |
| статическая электризация | static electricity buildup | Misc/RedPhone_OS_MSDS_en.md (+1) | |
| отслужившие аккумуляторные элементы | spent battery cells | Misc/RedPhone_OS_MSDS_en.md (+1) | |

## Added in batch misc-2

No new terms. This batch reuses the approved MSDS and navigation buoy terminology.

## Added in batch a3s-2

| RU | EN | Source EN file | Note |
|---|---|---|---|
| антенная решетка | transducer array | A3S/A3S_Users_Manual_en.md | |
| кросс-плата | backplane | A3S/A3S_Users_Manual_en.md | |
| статическая ошибка | static error | A3S/A3S_Users_Manual_en.md | |
| послезвучание; реверберация | reverberation | A3S/A3S_Users_Manual_en.md | |
| линейная аппроксимация | linear approximation | A3S/A3S_Users_Manual_en.md | |
| среднеквадратичное отклонение; СКО | standard deviation; SD | A3S/A3S_Users_Manual_en.md | Statistical dispersion of angle-of-arrival measurements |
