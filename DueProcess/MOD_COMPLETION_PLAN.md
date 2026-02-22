# Operation: Due Process — Mod Completion Plan

**Philosophy:** Lowest effort. Reuse everything. Modify, don't rebuild. Texture swaps over new models.

---

## 1. MISSIONS & LOCATIONS (Map Reuse)

| Mission | Story | SWAT 4 Map | Fit Quality | Notes |
|---------|-------|------------|-------------|-------|
| **01: Quinceañera** | Birthday party at community center. 40–60 guests, DJ, piñata, cake. Sofia Reyes turning 15. | `SP-ABomb` | Good | Event space = party venue. Rename "Adelaide Community Center" in briefings. |
| **02: Hospital** | ER waiting room. Sick patients, chemo, dialysis, broken arms, pregnant woman. St. Michael's Medical Center. | `SP-Hospital` | Perfect | Map already matches. No changes needed. |
| **03: School Play** | Lincoln Elementary. Peter Pan performance. Kevin Chen's niece is Tinkerbell. Maria Rodriguez (lunch lady) as Captain Hook. | `SP-RedLibrary` | Acceptable | Library → auditorium. **Sync:** Missions.ini says "Wizard of Oz" but scripts say "Peter Pan"—use Peter Pan for Kevin Chen storyline. |
| **04: Taco Truck** | Taqueria Los Primos in municipal parking lot. Ramón/Lupe operator. Carmen Reyes = customer. Construction workers. | `SP-ConvenienceStore` | Acceptable | Store → parking lot with food truck. Exterior focus. |
| **05: Debrief** | ICE HQ sensitivity training / "Excellence Through Compliance" | `SP-Training` | Good | Already configured. |

---

## 2. STORYLINES (From Scripts — Don't Miss)

### Mission 1: Quinceañera
- **Sofia Reyes** — 15, quinceañera, wants to be a vet, grandmother's dress
- **Elena "Abuela" Reyes** — Grandmother, 56, tailor, tamales, 32 years in neighborhood
- **Miguel Reyes** — Father, 49, construction foreman, coached soccer, World's Best Dad mug
- **Party Guests** — ~47: teachers, nurse, small business owners, Marine vet, soccer team, DJ
- **Anonymous 911 caller** — Nervous woman, "they're speaking Spanish," "concerned citizen"

### Mission 2: Hospital
- **Maria Santos** — Mother, 39, son Diego has broken arm from bike
- **Diego Santos** — 8, third grade, bike tricks, arm hurts
- **Rosa Gutierrez** — 72, retired teacher, heart condition, 23-year patient
- **David Whitehorse** — Lakota, 40s, here for mother's diabetes appointment. Deadpan. *Voice: dw_*
- **Marcus Williams** — 30s, sprained ankle. ICE approaches by mistake. Enthusiastically wants "deportation." *Voice: mw_*
- **Waiting room** — Chemo patient, pregnant woman, dialysis patient, construction worker (lacerated hand), toddler with fever, elderly with chest pains

### Mission 3: School Play (Peter Pan)
- **Kevin Chen** — Late 20s, Queens, niece is Tinkerbell. Officer Mandarin speaks bad Mandarin at him. Columbia Law, Sullivan & Cromwell. *Voice: kc_*
- **Officer Mandarin** — White ICE agent, bad college Mandarin, condescending. Thinks Kevin is pretending not to understand. *Voice: om_*
- **Maria Rodriguez** — Lunch lady 15 years, Captain Hook costume, outstanding deportation order from 2019
- **Isabella Moreno** — 8, Dorothy in scripts OR Tinkerbell (Kevin's niece). **Sync:** Use Tinkerbell for Kevin's family; Isabella can be separate or rename.
- **Parents** — Carlos & Ana Moreno; Kevin Chen (uncle); protective, confused, outraged
- **Principal** — Attempts to intervene

### Mission 4: Taco Truck
- **Ramón Gutierrez** — 58, operator, claims veteran, 30 years here, built truck with his own hands
- **Lupe Hernandez** — In Missions.ini as owner; could be Ramón's wife or same person. Citizen since 2003.
- **Carmen Reyes** — Puerto Rican woman, 40s–50s, customer, furious. Jones Act, 1917, paper towels. *Voice: cr_*
- **Daughter/Assistant** — Ramón's daughter, 20s–30s, protective
- **Construction workers** — Customers, lunch break
- **City councilwoman** — Doesn't want to be photographed

---

## 3. CHARACTERS — Base Model Mapping (Lowest Effort)

**Rule:** Map each mod character to an existing SWAT 4 archetype. Change only textures/skins—no new meshes.

| Mod Character | Base SWAT 4 Model | Outfit Modification | Voice Prefix |
|---------------|-------------------|---------------------|--------------|
| **Sofia Reyes** | FemaleHostage1 (young) | Quinceañera dress texture: white/pastel, lace, simple overlay on existing dress mesh | (TBD) |
| **Elena Reyes** | FemaleHostage2 or 3 (older) | Abuela: grey hair, apron or shawl texture overlay | (TBD) |
| **Miguel Reyes** | MaleHostage1 | Party shirt (guayabera-style recolor of casual shirt) | (TBD) |
| **David Whitehorse** | MaleHostage2 | Modern casual; add subtle tribal ID/bracelet texture if possible; else no change | dw_ |
| **Marcus Williams** | MaleHostage2 | Construction/casual; slight limp idle if possible; else no change | mw_ |
| **Maria Santos** | FemaleHostage1 | Hospital gown or casual; distressed | (TBD) |
| **Kevin Chen** | MaleHostage1 | Business casual (suit texture); Asian features if base allows | kc_ |
| **Officer Mandarin** | OfficerBlueOne or RedOne | Standard tactical; no change | om_ |
| **Maria Rodriguez** | FemaleHostage2 | Lunch lady: hairnet texture, apron overlay, Captain Hook costume (dark coat) | (TBD) |
| **Carmen Reyes** | FemaleHostage2 or 3 | Nuyorican professional; blouse, assertive pose | cr_ |
| **Ramón Gutierrez** | MaleHostage1 | Apron overlay, older face texture | (TBD) |

**Texture swap workflow:**
1. Locate original texture in `Content/Textures/` or character package
2. Create mod copy in `DueProcess/Content/Textures/`
3. Recolor/overlay: dress, apron, guayabera, etc.
4. Reference in `CharacterTypes.ini` or `HostageArchetypes.ini`

---

## 4. VOICE INTEGRATION (Wiring)

| Task | File(s) | Effort |
|------|---------|--------|
| Map dw_, mw_, kc_, cr_, om_ to game events | `SoundEffects.ini`, `Speakers.ini`, `Conversations.ini` | Medium |
| Create speaker IDs: dw, mw, kc, cr, om | `Speakers.ini` | Low |
| Replace or add conversation triggers | `Conversations.ini` + map triggers in SwatEd | Medium |
| Mission briefings (audio) | Record 4; add to `SoundEffects.ini` event `PlayerControllerUIMissionBriefing_Level_*` | Low |
| 911 calls (audio) | Record 4; wire to mission selection | Low |
| Loading dispatcher | Record 4; wire to loading events | Low |
| News Anchor (tv1) | Record ~25 lines; add Conv* triggers at key map points | Medium |

---

## 5. AUDIO STILL NEEDED

| Category | Count | Status |
|----------|-------|--------|
| TOC | 28 lines | Not recorded |
| News Anchor | 25 lines | Not recorded |
| Dispatcher | 4 | Not recorded |
| Mission Briefings | 4 (~90 sec each) | Not recorded |
| 911 Callers | 4 | Not recorded |
| Officers | 51 | Not recorded |
| Quinceañera civilians | Mother, Grandmother, Girl, Father | Not recorded |
| Hospital civilians | Female patient, Elderly male, Pregnant | Not recorded |
| School civilians | Parents, Teacher | Not recorded |
| Taco civilians | Operator, Daughter, Customer | Not recorded |
| **Custom characters** | **dw, kc, mw, cr, om** | **Recorded** |

---

## 6. INI CONFIGURATION TASKS

| File | Task |
|------|------|
| `SoundEffects.ini` | Add EventResponse entries pointing to `DueProcess/Content/Sounds/` paths |
| `Speakers.ini` | Add dw, mw, kc, cr, om speaker entries |
| `Conversations.ini` | Define conversation lines that trigger our voice files at map volumes |
| `HostageArchetypes.ini` | Add archetypes for Sofia, Elena, Miguel, David, Marcus, Maria S., Kevin, Maria R., Carmen, Ramón |
| `CharacterTypes.ini` | Map archetypes to base models + optional texture overrides |
| `Startup.ini` | Ensure `FilePath` includes mod Content/Sounds before base game |

---

## 7. VISUAL ASSETS (Lowest Effort)

| Asset | Approach | Notes |
|-------|----------|-------|
| Character outfits | Texture overlay on existing meshes | Quinceañera dress, apron, guayabera = recolor existing |
| Loading screens | Replace `loading_*.tga` or equivalent in gui_tex | Parody PSA / recruitment style |
| Mission thumbnails | Recolor or add text overlay to existing thumbs | "OPERATION FELIZ CUMPLEAÑOS" etc. |
| No new 3D models | Use existing hostage/suspect/officer meshes | SWAT 4 has enough variety |

---

## 8. MISSION/SCRIPT SYNC FIXES

- [ ] **School play:** Missions.ini says "Wizard of Oz" / Dorothy. Scripts say "Peter Pan" / Tinkerbell. **Decision:** Use Peter Pan. Kevin Chen's niece = Tinkerbell. Update Missions.ini school section to Peter Pan.
- [ ] **Taco owner:** Missions.ini has "Lupe Hernandez" (Female, 59, citizen 2003). Scripts have "Ramón Gutierrez" (Male, 58). **Decision:** Ramón = operator; Lupe = wife/partner or rename Lupe to Ramón. Or: Lupe runs truck, Ramón works it—pick one for primary character.

---

## 9. IMPLEMENTATION ORDER

1. **Sync missions** — Fix Wizard of Oz → Peter Pan; resolve Lupe/Ramón
2. **Speakers.ini** — Add 5 custom speakers (dw, mw, kc, cr, om)
3. **SoundEffects.ini** — Wire custom voice files to appropriate events (start with 1–2 as test)
4. **SwatEd test** — Place one conversation volume, trigger one line
5. **Character archetypes** — Add HostageArchetypes for key characters; map to base models
6. **Texture swaps** — Create 3–5 outfit variants (quinceañera, apron, etc.)
7. **Remaining audio** — TOC, News Anchor, briefings, 911, loading in priority order

---

## 10. FILES REFERENCE

| Purpose | Location |
|---------|----------|
| Voice scripts | `DueProcess/SCRIPTS/NEW_CHARACTERS.txt`, `LINES_BY_VOICE.txt`, `ALL_DIALOGUE_SCRIPTS.md` |
| Mission config | `DueProcess/System/SwatMissions.ini`, `DueProcess_Missions.ini` |
| Objectives | `DueProcess/System/DueProcess_Objectives.ini`, `MissionObjectives.ini` |
| Voice files | `DueProcess/Content/Sounds/CivilianHospital/`, `CivilianSchool/`, `CivilianTaco/`, `OfficerDueProcess/` |
| Convert script | `DueProcess/convert_mp3_to_ogg.sh` |
