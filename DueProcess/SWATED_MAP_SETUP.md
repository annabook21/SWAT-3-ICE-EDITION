# SwatEd Map Setup — Operation: Due Process

This guide explains how to place Due Process characters and conversations in maps using SwatEd (Windows only).

---

## Prerequisites

- SwatEd installed (comes with SWAT 4 SDK)
- Due Process mod loaded
- Maps: SP-Hospital, SP-RedLibrary, SP-ConvenienceStore

---

## 1. Place Hostage NPCs

### Hospital (SP-Hospital)

In the ER waiting room area, place:

| Archetype | Speaker Tag | Notes |
|-----------|-------------|-------|
| DueProcess_DavidWhitehorse | `dw` | Waiting for mother's appointment |
| DueProcess_MarcusWilliams | `mw` | Sprained ankle, sitting |

### School (SP-RedLibrary)

In the auditorium/audience area:

| Archetype | Speaker Tag | Notes |
|-----------|-------------|-------|
| DueProcess_KevinChen | `kc` | Uncle of Tinkerbell |
| (Officer) | `om` | Officer Mandarin — use OfficerBlueOne or OfficerRedOne with custom placement if needed |

### Taco Truck (SP-ConvenienceStore)

Near the store / parking lot area:

| Archetype | Speaker Tag | Notes |
|-----------|-------------|-------|
| DueProcess_CarmenReyes | `cr` | Customer getting lunch |
| DueProcess_RamonGutierrez | (optional) | Truck operator |
| DueProcess_LupeGutierrez | (optional) | Wife/co-owner |

---

## 2. Assign Speaker Tags

In SwatEd, when placing or editing a Hostage/Suspect:

1. Select the actor
2. Find the **Tag** or **SpeakerId** / **Speaker** property (exact name varies by editor)
3. Set it to match the conversation Speaker: `dw`, `mw`, `kc`, `cr`, or `om`

The game's `LocateAvailableSpeaker()` finds actors by this tag when playing conversations.

---

## 3. Place ConversationVolumes

ConversationVolumes are triggers that start a conversation when the player enters.

### Hospital

- **ConvDPHosp1** — Near David Whitehorse (`dw`)
- **ConvDPHosp2** — Near David (alternate line)
- **ConvDPHosp3** — Near Marcus Williams (`mw`)
- **ConvDPHosp4** — Near Marcus (alternate line)

### School

- **ConvDPSchool1** — Near Kevin Chen (`kc`)
- **ConvDPSchool2** — Near Officer Mandarin (`om`)
- **ConvDPSchool3** — Covers both (Kevin/Officer exchange)

### Taco Truck

- **ConvDPTaco1** — Near Carmen Reyes (`cr`)
- **ConvDPTaco2** — Alternate line
- **ConvDPTaco3** — Alternate line

### How to add a ConversationVolume

1. In SwatEd, add a **Trigger** or **ConversationVolume** actor (class name may be `ConversationVolume` or similar)
2. Set its **ConversationName** or **TriggerConversation** property to one of:  
   `ConvDPHosp1`, `ConvDPHosp2`, `ConvDPHosp3`, `ConvDPHosp4`,  
   `ConvDPSchool1`, `ConvDPSchool2`, `ConvDPSchool3`,  
   `ConvDPTaco1`, `ConvDPTaco2`, `ConvDPTaco3`
3. Resize/position the volume so the player enters it when approaching the relevant NPC

---

## 4. Verify

1. Save the map
2. Launch the mod and play the mission
3. Walk into each ConversationVolume — the corresponding dialogue should play from the nearby NPC
4. If no dialogue plays: confirm the NPC has the correct speaker tag and is inside (or near) the ConversationVolume

---

## Reference: Conversation → Speaker mapping

| Conversation | Speaker | Speech |
|--------------|---------|--------|
| ConvDPHosp1 | dw | dw_01 |
| ConvDPHosp2 | dw | dw_02 |
| ConvDPHosp3 | mw | mw_01 |
| ConvDPHosp4 | mw | mw_02 |
| ConvDPSchool1 | kc | kc_01 |
| ConvDPSchool2 | om | om_01 |
| ConvDPSchool3 | om, kc | om_02, kc_02, kc_05 |
| ConvDPTaco1 | cr | cr_01 |
| ConvDPTaco2 | cr | cr_02 |
| ConvDPTaco3 | cr | cr_03 |
