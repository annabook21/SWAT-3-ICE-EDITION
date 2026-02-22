# OPERATION: DUE PROCESS — Complete Voice Line Specification

## Audio Format Requirements

All voice files must be:
- **Format:** OGG Vorbis
- **Sample Rate:** 44100 Hz
- **Channels:** Mono
- **Bitrate:** ~48-96 kbps (variable)

---

## PART 1: SCRIPTED MISSION AUDIO (Highest Priority)

These are the fully custom audio files for your four missions. They replace files in `Content/Sounds/ScriptedVO/`.

### 1A. Mission Briefings (Pre-Mission Screen)

The briefing plays while viewing the mission overview. Each is 60-120 seconds.

| Filename | Description |
|----------|-------------|
| `Quince_briefing.ogg` | Mission 1 - Quinceañera raid briefing |
| `Hospital_briefing.ogg` | Mission 2 - Hospital waiting room briefing |
| `School_briefing.ogg` | Mission 3 - School play briefing |
| `Taco_briefing.ogg` | Mission 4 - Taco truck briefing |

**Style:** Sterile government memo language. Dry, matter-of-fact delivery. Gradually reveals the absurdity.

**Example Script (Quinceañera):**
> "This is a targeted enforcement action briefing for Operation Feliz Cumpleaños. Intelligence indicates a gathering of 40-60 individuals at 1847 Mariposa Lane. The event has been flagged as a potential harboring situation disguised as a cultural celebration. Primary objectives include verifying documentation status of all attendees and securing any catered food items for agricultural inspection. ROE is standard administrative processing. Note: field agents should expect decorative streamers, loud music, and a three-tiered cake. Threat level: Festive."

---

### 1B. 911 Calls (Mission Selection Screen)

These play when selecting the mission. 15-30 seconds each.

| Filename | Description |
|----------|-------------|
| `Quince_call.ogg` | Neighbor complaint about "suspicious party" |
| `Hospital_call.ogg` | Anonymous tip about "non-citizens" in ER |
| `School_call.ogg` | Report of "undocumented performers" |
| `Taco_call.ogg` | Health inspector "concern" about taco truck |

**Style:** Civilian caller, slightly nervous. The tip should be clearly absurd/prejudiced.

**Example Script (Quinceañera):**
> "Yes, hello? I'd like to report a disturbance at 1847 Mariposa Lane. There's a lot of cars, loud music, and... well, they're speaking Spanish. I don't know if they're supposed to be here. It looks like some kind of party? There's a lot of balloons and... I just think someone should check it out. I'm a concerned citizen."

---

### 1C. Loading Screen Dispatcher Audio

Plays during map loading. 20-40 seconds.

| Filename | Description |
|----------|-------------|
| `QuinceLoad_dis.ogg` | Dispatcher briefing en route |
| `HospitalLoad_dis.ogg` | Dispatcher briefing en route |
| `SchoolLoad_dis.ogg` | Dispatcher briefing en route |
| `TacoLoad_dis.ogg` | Dispatcher briefing en route |

**Style:** Radio dispatcher voice, professional but hints at the absurdity.

**Example:**
> "All units, be advised you are approaching the target location. Intel suggests the structure contains party decorations, a DJ, and approximately 45 persons of interest celebrating what appears to be a 15th birthday. Exercise caution near the piñata. Repeat: approach piñata with caution."

---

### 1D. In-Mission Scripted Conversations

These are triggered at specific map locations. Each conversation has multiple parts spoken by different characters.

**Naming Convention:** `Conv[Mission][Number]_[Part]_[Speaker].ogg`

**Speaker codes:**
- `ld` = Team Lead (player)
- `toc` = TOC (command center)
- `b1`, `b2` = Blue team officers
- `r1`, `r2` = Red team officers
- `tv1` = News reporter (your satirical "NewsAnchor")
- `civ` = Civilian (custom)

**Per Mission: Approximately 10-20 conversation files**

Example filenames for Quinceañera mission:
```
ConvQuince1_1_ld.ogg    "TOC, we have visual on the target. Confirming... decorations."
ConvQuince1_2_toc.ogg   "Copy that. Proceed with documentation verification."
ConvQuince2_1_b1.ogg    "Lead, I'm seeing a lot of children. They appear to be... dancing."
ConvQuince3_1_tv1.ogg   "This is Breaking News coverage of KEEPING AMERICA SAFE..."
```

---

## PART 2: TOC (TACTICAL OPERATIONS CENTER)

These are event-triggered radio responses from command. Replace files in `Content/Sounds/TOC/`.

### Mission Events

| Category | Count | Example Line |
|----------|-------|--------------|
| `toc_MissionCompletedSuccess` | 2-3 | "TOC to Element Lead: Operation concluded. Excellent compliance metrics. The Director sends congratulations." |
| `toc_MissionCompletedFailure` | 2-3 | "TOC to all units: Mission outcome sub-optimal. Prepare for administrative review. Remember: processing quotas exist for a reason." |
| `toc_RepliedMissionStart` | 2-3 | "All units, you are cleared for administrative action. Remember your Form I-200s. TOC out." |

### Status Reports

| Category | Count | Example Line |
|----------|-------|--------------|
| `toc_RepliedSuspectReported` | 2-3 | "Copy. One person of enforcement interest secured. Log the encounter for metrics." |
| `toc_RepliedHostageReported` | 2-3 | "Copy. One potential witness to unlawful presence secured. Remind them of civic duty." |
| `toc_RepliedOfficerDown` | 2-3 | "Officer down. Requesting backup and Form WC-1 for workplace injury." |
| `toc_RepliedInjSuspectReported` | 2-3 | "Injured detainee secured. Note: medical costs will be billed to country of origin." |
| `toc_RepliedInjHostageReported` | 2-3 | "Injured civilian secured. Begin documentation of collateral circumstances." |

### Team Contact

| Category | Count | Example Line |
|----------|-------|--------------|
| `toc_ContactedLead` | 2-3 | "TOC to Element Lead, status report requested for congressional briefing. Over." |
| `toc_ContactedRedOne` | 2-3 | "TOC to Red One, what's your Form I-213 count? Over." |
| `toc_ContactedBlueOne` | 2-3 | "TOC to Blue One, confirm all detainees have been issued Notice to Appear. Over." |
| `toc_ContactedEntryTeam` | 2-3 | "TOC to Entry Team, reminder: cameras are rolling. Professional optics. Over." |

**Total TOC lines: ~30-40 files**

---

## PART 3: OFFICER VOICE LINES (AI Squad + Player)

These are the most numerous. Each officer type needs ~200 files for full coverage.

**For a satirical mod, focus on these HIGH-IMPACT categories:**

### Compliance Commands (CRITICAL - Used Constantly)

| Category | Example Satirical Line |
|----------|------------------------|
| `ReassuredPassiveHostage` | "Remain calm. Your cooperation will be noted in your case file." |
| `ReassuredAggressiveHostage` | "Resisting only adds to your processing time. Think of the paperwork." |
| `ArrestedSuspect` | "You are being administratively detained. You have the right to... wait, do you?" |
| `ReportedCivilianRestrained` | "Civilian secured. Beginning documentation protocol." |
| `ReportedSuspectRestrained` | "Suspect restrained. Preparing Form I-200." |
| `ReportedCivilianSecured` | "Lead, one cooperative individual processed. Compliance rate: excellent." |
| `ReportedSuspectSecured` | "Person of enforcement interest secured and ready for transport." |

### Combat/Tactical Callouts

| Category | Example Satirical Line |
|----------|------------------------|
| `ReportedSuspectSpotted` | "Visual on person of enforcement interest. They appear to be... eating lunch." |
| `ReportedCivilianSpotted` | "Civilian spotted. Standby for documentation status assessment." |
| `ReportedSuspectFleeing` | "Suspect fleeing! In violation of... existing in a particular location!" |
| `ReportedCivilianWillNotComply` | "Civilian refusing to comply with voluntary documentation request." |
| `ReportedSuspectWillNotComply` | "Suspect non-compliant. Possibly confused about rights they may not have." |

### Equipment Deployment

| Category | Example Satirical Line |
|----------|------------------------|
| `ReportedDeployingFlashbang` | "Flashbang out. Expediting the compliance process." |
| `ReportedDeployingGas` | "Deploying CS gas. For their own administrative convenience." |
| `ReportedDeployingTaser` | "Taser deployed. Subject will be more compliant momentarily." |
| `ReportedDeployingPepper` | "Pepper spray deployed. Standard processing encouragement." |

### Mission Progress

| Category | Example Satirical Line |
|----------|------------------------|
| `MissionDoneSuccess` | "Mission complete. The Director will be pleased with these numbers." |
| `MissionDoneFailure` | "Mission failed. Someone's getting transferred to a filing desk." |
| `StartedMission` | "Entry team ready. Forms prepared. Let's process some individuals." |

**Recommended: Create ~50-80 officer lines covering the most-used categories**

---

## PART 4: CIVILIAN VOICE LINES (The Humanized Victims)

These are CRITICAL for the satirical contrast. Replace files in `Content/Sounds/FemaleHostage1/`, etc.

### Hostage Behavior Categories

| Category | Generic Context | Satirical Replacement |
|----------|----------------|----------------------|
| `AnnouncedSpottedOfficer` | See SWAT | "Oh no, not again..." / "Please, my children are here!" |
| `AnnouncedSpottedOfficerScared` | Scared reaction | "I have papers! I have papers!" / "This is a birthday party!" |
| `AnnouncedSpottedOfficerSurprised` | Surprised | "What?! We're just celebrating!" / "This is a hospital!" |
| `AnnouncedCompliant` | Surrendering | "Okay, okay, I'll cooperate... just don't hurt my family." |
| `AnnouncedNonCompliant` | Refusing | "I'm not leaving my grandmother!" / "She needs her medication!" |
| `AnnouncedFlee` | Running away | "Run! Get the children out!" |
| `AnnouncedRestrained` | Being cuffed | "This is a mistake... I've lived here for 20 years..." |
| `ReactedBang` | Flashbanged | *screaming* / "The baby! Where's the baby?!" |
| `ReactedPepper` | Pepper sprayed | *coughing, crying* "We didn't do anything!" |
| `ReactedTaser` | Tased | *pain sounds* |
| `ReactedSting` | Stinger | *pain, confusion* |
| `CalledForHelp` | Calling out | "Someone help us! Call a lawyer!" / "This isn't right!" |
| `Screamed` | General fear | *screaming, crying* |
| `PointedToEnemy` | Pointing | "Please, she's just the caterer! She's been here for hours!" |
| `TalkedToEnemy` | Speaking | "Just do what they say... it'll be okay..." |
| `Died` | Death sounds | *This stays as is - injury sounds* |

**Create ~20-30 lines per civilian archetype:**
- Quinceañera guests (family-focused, celebration interrupted)
- Hospital patients (vulnerable, sick, dependent on care)
- School parents (protective, confused, advocating for children)
- Taco truck workers (working-class, dignity, "I just work here")

---

## PART 5: NEWS ANCHOR / CABLE NEWS COMMENTARY

This is your unique satirical voice - the "KEEPING AMERICA SAFE" narrator.

**Integration Option 1: Replace Sierra sniper lines (limited)**
- `s1_spottedcontact` → "And we're seeing movement now, folks..."
- `s1_lostcontact` → "We seem to have lost visual..."

**Integration Option 2: Use scripted conversation system (better)**
Create conversation triggers that play news commentary at key moments:
```
ConvQuince_News1_tv1.ogg  "Breaking news on KEEPING AMERICA SAFE. We're live at what appears to be a residential birthday party..."
ConvQuince_News2_tv1.ogg  "Officers are moving in now. This is exactly the kind of tough enforcement Americans voted for."
ConvQuince_News3_tv1.ogg  "Multiple individuals in custody. Another successful operation keeping our communities safe."
```

**Recommended: 15-25 news commentary lines per mission**

---

## PART 6: PRIORITY RECORDING LIST

### ABSOLUTE MINIMUM (for a playable proof-of-concept):

**Scripted Mission Audio (12 files):**
1. `Quince_briefing.ogg` - 90 sec
2. `Quince_call.ogg` - 20 sec
3. `QuinceLoad_dis.ogg` - 30 sec
4. `Hospital_briefing.ogg` - 90 sec
5. `Hospital_call.ogg` - 20 sec
6. `HospitalLoad_dis.ogg` - 30 sec
7. `School_briefing.ogg` - 90 sec
8. `School_call.ogg` - 20 sec
9. `SchoolLoad_dis.ogg` - 30 sec
10. `Taco_briefing.ogg` - 90 sec
11. `Taco_call.ogg` - 20 sec
12. `TacoLoad_dis.ogg` - 30 sec

**TOC Lines (10 files):**
13. `toc_RepliedMissionStart_1.ogg`
14. `toc_MissionCompletedSuccess_1.ogg`
15. `toc_MissionCompletedFailure_1.ogg`
16. `toc_RepliedSuspectReported_1.ogg`
17. `toc_RepliedHostageReported_1.ogg`
18. `toc_RepliedOfficerDown_1.ogg`
19. `toc_ContactedLead_1.ogg`
20. `toc_ContactedEntryTeam_1.ogg`
21. `toc_RepliedInjSuspectReported_1.ogg`
22. `toc_RepliedInjHostageReported_1.ogg`

**News Commentary (4 files):**
23-26. One news commentary per mission

**TOTAL MINIMUM: ~26 files, ~15 minutes of audio**

---

### RECOMMENDED (for full satirical impact):

| Category | File Count | Total Duration |
|----------|------------|----------------|
| Mission Briefings | 4 | ~6 min |
| 911 Calls | 4 | ~2 min |
| Loading Dispatcher | 4 | ~3 min |
| In-Mission Conversations | 40 | ~8 min |
| TOC Event Lines | 30 | ~5 min |
| Officer Compliance Lines | 50 | ~5 min |
| Civilian Reactions | 60 | ~8 min |
| News Commentary | 40 | ~10 min |
| **TOTAL** | **~232 files** | **~47 min** |

---

## FILE ORGANIZATION

```
DueProcess/
└── Content/
    └── Sounds/
        ├── ScriptedVO/           # Mission briefings, calls, conversations
        │   ├── Quince_briefing.ogg
        │   ├── Quince_call.ogg
        │   ├── QuinceLoad_dis.ogg
        │   ├── ConvQuince1_1_ld.ogg
        │   └── ...
        ├── TOC/                  # Command center responses
        │   ├── toc_RepliedMissionStart_1.ogg
        │   └── ...
        ├── OfficerDueProcess/    # Satirical officer lines
        │   ├── dp_ArrestedSuspect_1.ogg
        │   └── ...
        ├── CivilianQuince/       # Quinceañera civilians
        │   ├── cq_AnnouncedCompliant_1.ogg
        │   └── ...
        ├── CivilianHospital/     # Hospital civilians
        ├── CivilianSchool/       # School civilians
        └── CivilianTaco/         # Taco truck civilians
```

---

## RECORDING TIPS

1. **Record in a quiet space** - closets with clothes work well
2. **Keep consistent distance** from microphone (6-8 inches)
3. **Record each line 2-3 times** - pick the best take
4. **Leave 0.5 sec silence** at start and end of each file
5. **Normalize audio** to -3dB peak
6. **Test in-game** before recording the full set

---

## VOICE CASTING SUGGESTIONS

| Role | Voice Profile |
|------|---------------|
| **TOC** | Dry, bureaucratic, slight boredom. Think DMV employee reading a script. |
| **Officers** | Mix of genuine and robotic. Some lines deadpan professional, others hint at discomfort. |
| **News Anchor** | Performative concern. Fox News energy - urgent, self-important, inflammatory. |
| **Civilians (Quince)** | Mix of ages. Warm family voices. Fear mixed with confusion. Spanish accents authentic. |
| **Civilians (Hospital)** | Sick, tired, vulnerable. Some elderly. Medical anxiety on top of enforcement fear. |
| **Civilians (School)** | Parents. Protective. Disbelief. "This is a school!" energy. |
| **Civilians (Taco)** | Working-class dignity. "I'm just doing my job." Exhaustion, resignation. |

---

## CONVERSION COMMAND

If you have WAV files, convert to OGG:

```bash
# Single file
ffmpeg -i input.wav -c:a libvorbis -q:a 4 -ac 1 -ar 44100 output.ogg

# Batch convert all WAVs in a folder
for f in *.wav; do ffmpeg -i "$f" -c:a libvorbis -q:a 4 -ac 1 -ar 44100 "${f%.wav}.ogg"; done
```

---

## NEXT STEPS

1. **Start with the 26-file minimum** to test the pipeline
2. **Record mission briefings first** - these set the tone
3. **Test integration** before recording the full set
4. **Expand to recommended list** based on playtesting feedback

The original guide missed approximately 200+ potential voice line categories. This version covers the complete scope of what SWAT 4's audio system supports.
