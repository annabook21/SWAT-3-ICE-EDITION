# Voice File Wiring — Operation: Due Process

## Completed wiring (Feb 2025)

### PlayerControllerConversationsDummy (mission random dialogue pool)
Due Process voice lines added to the mission-specific conversation pools:
- **m03 (ConvenienceStore / Taco truck):** cr_01 … cr_05
- **m06 (RedLibrary / School):** kc_01, kc_02, kc_05, kc_11, om_01, om_02, om_06
- **m10 (Hospital):** dw_01, dw_02, dw_06, mw_01, mw_02, mw_15

### SoundEffects.ini
All custom character voice lines are registered as `StreamSoundEffectSpecification` entries:
- **dw_01–dw_11** → `CivilianHospital/dw_01.ogg` … `dw_11.ogg` (David Whitehorse)
- **mw_01–mw_17** → `CivilianHospital/mw_01.ogg` … `mw_17.ogg` (Marcus Williams)
- **kc_01–kc_14** → `CivilianSchool/kc_01.ogg` … `kc_14.ogg` (Kevin Chen)
- **om_01–om_09** → `OfficerDueProcess/om_01.ogg` … `om_09.ogg` (Officer Mandarin)
- **cr_01–cr_19, cr_13b** → `CivilianTaco/cr_01.ogg` … `cr_19.ogg` (Carmen Reyes)

### Conversations.ini
Conversation definitions added for in-mission dialogue:
- **ConvDPHosp1–4** — Hospital (David Whitehorse, Marcus Williams)
- **ConvDPSchool1–3** — School / Red Library (Kevin Chen, Officer Mandarin)
- **ConvDPTaco1–3** — Taco truck (Carmen Reyes)

### Speakers.ini
Speaker IDs: `dw`, `mw`, `kc`, `cr`, `om` (already present).

### HostageArchetypes.ini
Archetypes: DueProcess_DavidWhitehorse, DueProcess_MarcusWilliams, DueProcess_KevinChen, DueProcess_CarmenReyes, etc.

---

## File locations

Paths are relative to `DueProcess/Content/Sounds/`:

| Folder             | Files                | Character(s)    |
|--------------------|----------------------|-----------------|
| CivilianHospital/  | dw_01.ogg … dw_11.ogg, mw_01.ogg … mw_17.ogg | David, Marcus |
| CivilianSchool/    | kc_01.ogg … kc_14.ogg | Kevin Chen     |
| CivilianTaco/      | cr_01.ogg … cr_19.ogg, cr_13b.ogg | Carmen Reyes |
| OfficerDueProcess/ | om_01.ogg … om_09.ogg | Officer Mandarin |

### Audio format
- **Format:** OGG Vorbis
- **Sample rate:** 44100 Hz
- **Channels:** Mono

### Converting MP3 → OGG
From the mod root, run:
```bash
./convert_mp3_to_ogg.sh Content/Sounds/CivilianHospital
./convert_mp3_to_ogg.sh Content/Sounds/CivilianSchool
./convert_mp3_to_ogg.sh Content/Sounds/CivilianTaco
./convert_mp3_to_ogg.sh Content/Sounds/OfficerDueProcess
```
Requires: `ffmpeg`, `oggenc` (vorbis-tools: `brew install vorbis-tools`).

---

## Map setup (SwatEd)

To hear these lines in-game:

1. Place hostage NPCs using DueProcess archetypes (e.g. DueProcess_DavidWhitehorse).
2. Assign speaker tags: `dw`, `mw`, `kc`, `cr`, `om` (exact tag names depend on SwatEd/level format).
3. Add ConversationVolumes that trigger: ConvDPHosp1, ConvDPHosp2, ConvDPHosp3, ConvDPHosp4, ConvDPSchool1, ConvDPSchool2, ConvDPSchool3, ConvDPTaco1, ConvDPTaco2, ConvDPTaco3.
