# Operation: Due Process — Mod Completion Plan

**Philosophy:** Lowest effort. Reuse everything. Modify, don't rebuild. Texture swaps over new models.

---

## 1. MISSIONS & LOCATIONS (Map Reuse)

| Mission | Story | SWAT 4 Map | Fit Quality | Notes |
|---------|-------|------------|-------------|-------|
| **01: The Nightclub** | Eastern European nightclub raid. Andriy Kovalenko (Ukrainian defense contractor) at friend Tomek's birthday. | `SP-ABomb` | Good | Nightclub setting fits naturally. Andriy voiced (ak_01-10). **Needs SwatEd** for ConvDPNightclub volumes. |
| **02: The Waiting Room** | ER waiting room. Sick patients, chemo, dialysis, broken arms, pregnant woman. St. Michael's Medical Center. | `SP-Hospital` | Perfect | Map already matches. No changes needed. |
| **03: The School Play** | Lincoln Elementary. Peter Pan performance. Kevin Chen's niece is Tinkerbell. Maria Rodriguez (lunch lady) as Captain Hook. | `SP-RedLibrary` | Acceptable | Library = auditorium. Kevin/Officer Mandarin voiced (kc_, om_). |
| **04: The Taco Truck** | Taqueria Los Primos in municipal parking lot. Ramon/Lupe operator. Carmen Reyes = customer. | `SP-ConvenienceStore` | Acceptable | Store = parking lot with food truck. Carmen voiced (cr_). |
| **Training: The Debrief** | ICE HQ sensitivity training / "Excellence Through Compliance" | `SP-Training` | Good | Already configured. First in campaign order. |
| **05: The Shelter** | Asylum seeker shelter in tenement building. Jean-Pierre Baptiste (Haitian journalist). Sarah Morrison (retired immigration judge). | `SP-Tenement` | Excellent | 12 ConvTen volumes baked in map = dialogue works without SwatEd. Jean-Pierre voiced (jp_01-12). Audio recorded and wired. |

---

## 2. STORYLINES

### Mission 1: The Nightclub (SP-ABomb)
- **Andriy Kovalenko** — Ukrainian, 36, defense contractor, TS/SCI clearance, green card holder. *Voice: ak_* (10 lines, recorded)
- **Tomasz "Tomek" Wojcik** — Polish, 37, structural engineer, US citizen. It's his birthday.
- **Club Patrons** — ~30: nurses, Uber driver, retired Lithuanian math teacher, people who just like the music

### Mission 2: The Waiting Room (SP-Hospital)
- **David Whitehorse** — Lakota, 40s, here for mother's diabetes appointment. Deadpan. *Voice: dw_* (11 lines, recorded)
- **Marcus Williams** — Black American, 30s, sprained ankle. Enthusiastically wants "deportation." *Voice: mw_* (17 lines, recorded)
- **Maria Santos** — Mother, 39, son Diego has broken arm
- **Waiting room patients** — Chemo patient, pregnant woman, elderly with chest pains, etc.

### Mission 3: The School Play (SP-RedLibrary)
- **Kevin Chen** — Chinese-American, late 20s, Queens, niece is Tinkerbell. Columbia Law. *Voice: kc_* (14 lines, recorded)
- **Officer Mandarin** — White ICE agent, bad college Mandarin. *Voice: om_* (9 lines, recorded)
- **Maria Rodriguez** — Lunch lady 15 years, Captain Hook costume, outstanding deportation order

### Mission 4: The Taco Truck (SP-ConvenienceStore)
- **Carmen Reyes** — Puerto Rican, 40s-50s, customer, furious. Jones Act, 1917. *Voice: cr_* (19 lines, recorded)
- **Ramon Gutierrez** — Operator, 58, claims veteran, 30 years in US
- **Lupe Hernandez** — Owner, citizen since 2003

### Training: Excellence Through Compliance (SP-Training)
- **DAD Garrett Stokes** — Career bureaucrat, 50s, 23 years ICE. Instructor. *Voice: icetr_* (Stokes lines, 89 lines)
- **Agt. Vasquez** — 42-day Academy graduate, 2 weeks on the job. *Voice: icetr_09_03, icetr_55-58* (5 lines)
- **Agt. Dawson** — CBP veteran transfer, 15 years, uneasy. *Voice: icetr_59-62* (4 lines)
- **Agent Banter** — Fields, Jackson, Reynolds, Girard. *Voice: icetr_21, icetr_23, icetr_73* (11 lines)
- 12 acts, 121 total lines. References: Todd Lyons memo, Renee Good killing, Abrego Garcia, Pine Tree Riots, whistleblower testimony, Minneapolis operation, Homan quotes.

### Mission 5: The Shelter (SP-Tenement)
- **Jean-Pierre Baptiste** — Haitian journalist, late 30s, asylum seeker. TPS, work permit. Fled Port-au-Prince after death threats. *Voice: jp_* (12 lines, recorded)
- **Sarah Morrison** — Retired immigration judge, 66, volunteer coordinator. Left the bench because she couldn't stomach the system.
- **Building Residents** — ~30 asylum seekers from Haiti, Guatemala, Syria, Venezuela, Honduras. All have pending court dates.

---

## 3. VOICE INTEGRATION STATUS

### Recorded & Wired
| Character | Prefix | Lines | SoundEffects.ini | Speakers.ini | Conversations.ini | Preloader |
|-----------|--------|-------|------------------|--------------|-------------------|-----------|
| David Whitehorse | dw_ | 11 | Done | Done | Done | m02 (Hospital) |
| Marcus Williams | mw_ | 17 | Done | Done | Done | m02 (Hospital) |
| Kevin Chen | kc_ | 14 | Done | Done | Done | m03 (School) |
| Officer Mandarin | om_ | 9 | Done | Done | Done | m03 (School) |
| Carmen Reyes | cr_ | 19 | Done | Done | Done | m07 (Taco) |
| Andriy Kovalenko | andk/ak_ | 10 | Done | Done | Needs SwatEd volumes | m04 (ABomb) |
| Jean-Pierre Baptiste | jpb/jp_ | 12 | Done | Done | Done (ConvTen1-13) | m09 (Tenement) |
| DAD Stokes (Training) | icetr_ | 89 | Done | Done (u1) | Done (Train1-74) | m00 (Training) |
| Agt. Vasquez (Training) | icetr_ | 5 | Done | Done (vaz) | Done (Train9,55-58) | m00 (Training) |
| Agt. Dawson (Training) | icetr_ | 4 | Done | Done (daw) | Done (Train59-62) | m00 (Training) |
| Training Officers | icetr_ | 11 | Done | Done (b1/b2/r1/r2) | Done (Train21,23,73) | m00 (Training) |

### Audio Still Needed
| Category | Count | Status |
|----------|-------|--------|
| Training - DAD Stokes | ~89 | Wired, not recorded |
| Training - Agt. Vasquez | 5 | Wired, not recorded |
| Training - Agt. Dawson | 4 | Wired, not recorded |
| Training - Officer banter | 11 | Wired, not recorded |
| TOC lines | ~28 | Not recorded |
| News Anchor | ~25 | Not recorded |
| Dispatcher | ~6 | Not recorded |
| Mission Briefings (audio) | 6 | Not recorded |
| 911 Callers | ~6 | Not recorded |
| Officer chatter | ~51 | Not recorded |
| Hospital civilians (non-DW/MW) | ~10 | Not recorded |
| School civilians (non-KC) | ~10 | Not recorded |
| Taco civilians (non-CR) | ~10 | Not recorded |
| Nightclub civilians (non-AK) | ~10 | Not recorded |
| Tenement civilians (non-JP) | ~10 | Not recorded |
| Sarah Morrison | TBD | Not recorded |

---

## 4. CRITICAL REMAINING TASKS

### Map Editing (Requires SwatEd on Windows/CrossOver)
- [ ] **SP-ABomb (Mission 1):** Add ConvDPNightclub1-5 ConversationVolumes for Andriy's dialogue. Currently, the 7 existing ConvAbomb1-7 play bomb-plot dialogue that clashes with the nightclub narrative.
- [ ] **SP-Tenement (Mission 5):** No map editing needed! All 12 ConvTen volumes are baked into the map and have been redefined to play Jean-Pierre's dialogue via INI.

### INI Configuration
- [x] Mission briefings (DueProcess_Missions.ini) — All 5 missions + training configured
- [x] SwatMissions.ini — All 5 missions + training configured
- [x] Conversations.ini — ConvTen1-13 redefined for Jean-Pierre
- [x] Speakers.ini — All 7 custom speakers added (dw, mw, kc, cr, om, andk, jpb)
- [x] SoundEffects.ini — All custom voice specs wired, preloaders updated
- [x] HostageArchetypes.ini — Custom archetypes for all characters + tenement archetypes repurposed

### Visual Assets (Low Priority)
- [ ] Character texture swaps (nightclub outfits, etc.)
- [ ] Loading screens (parody PSA / recruitment style)
- [ ] Mission thumbnails

---

## 5. IMPLEMENTATION ORDER

1. [x] **Mission sync** — All 5 missions + training configured with briefings, hostages, suspects, timelines
2. [x] **Speakers** — All 9 custom speakers in Speakers.ini (+ vaz, daw for training)
3. [x] **Voice wiring** — All recorded characters wired in SoundEffects.ini + Conversations.ini
4. [x] **Character archetypes** — All custom + tenement archetypes configured
5. [x] **SP-Training narrative** — 121-line "Excellence Through Compliance" training rewrite (12 acts, icetr_ prefix)
6. [ ] **SwatEd map editing** — ConvDPNightclub volumes for SP-ABomb (Windows/CrossOver)
7. [ ] **Remaining audio recording** — Training (121 lines), TOC, News Anchor, briefings, 911, officers, civilians
8. [ ] **Texture swaps** — Character outfits, loading screens, thumbnails

---

## 6. FILES REFERENCE

| Purpose | Location |
|---------|----------|
| Voice scripts | `DueProcess/SCRIPTS/NEW_CHARACTERS.txt` |
| Mission config | `DueProcess/System/SwatMissions.ini`, `DueProcess_Missions.ini` |
| Objectives | `DueProcess/System/DueProcess_Objectives.ini`, `MissionObjectives.ini` |
| Conversations | `DueProcess/System/Conversations.ini` |
| Speakers | `DueProcess/System/Speakers.ini` |
| Sound specs | `DueProcess/System/SoundEffects.ini` |
| Archetypes | `DueProcess/System/HostageArchetypes.ini` |
| Voice files | `DueProcess/Content/Sounds/CivilianHospital/`, `CivilianSchool/`, `CivilianTaco/`, `CivilianNightclub/`, `CivilianTenement/`, `OfficerDueProcess/`, `ScriptedVO/` (training icetr_) |
| Convert script | `DueProcess/convert_mp3_to_ogg.sh` |

---

## 7. TECHNICAL NOTES

### SP-Tenement Map Architecture (Confirmed via reverse-engineering)
- **12 ConversationVolumes** baked in: ConvTen1-11, ConvTen13 (no ConvTen12)
- **4 hostage archetypes** baked in: Tenement_MaleHostage1-3, Tenement_FemaleHostage1
- All redefinable via INI without map editing
- Conversation trigger chain: TriggerVolume → Script → ActionStartConversation → ConversationManager → reads [ConvTenX] from Conversations.ini

### Campaign Structure (SwatMissions.ini Order)
Missions reordered so DP content plays first, stock missions after:
1. SP-Training (DP Debrief)
2. SP-ABomb (DP Mission 01 - The Nightclub)
3. SP-Hospital (DP Mission 02 - The Waiting Room)
4. SP-RedLibrary (DP Mission 03 - The School Play)
5. SP-ConvenienceStore (DP Mission 04 - The Taco Truck)
6. SP-Tenement (DP Mission 05 - The Shelter)
7-15. Stock missions (FoodWall, Fairfax, AutoGarage, Casino, JewelryHeist, ArmsDeal, Hotel, DNA, ObjBallistics)

### SP-ABomb Map Architecture
- **7 ConvAbomb volumes** baked in (bomb-plot dialogue — clashes with nightclub narrative)
- **5 ConvDPNightclub sections** defined in Conversations.ini but NO matching volumes in map
- **Requires SwatEd** to add ConvDPNightclub TriggerVolumes
