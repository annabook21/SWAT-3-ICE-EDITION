# Running SWAT 4 on Apple Silicon (Wine Plan)

## Background

SWAT 4 is a 32-bit DirectX 9 Windows game. Running it on an Apple Silicon Mac requires translating x86 instructions to ARM (via Rosetta 2) and Windows API calls to macOS (via Wine). The full translation chain is:

**32-bit x86 → wine32on64 → Rosetta 2 → Wine → WineD3D (DX9→OpenGL) → Metal**

Game Porting Toolkit (GPTK), Whisky, and D3DMetal do NOT support DirectX 9 — only DX11/DX12. They are not viable for SWAT 4.

---

## Step 1: Install CrossOver

CrossOver ($24/year) is the only well-tested solution for 32-bit DX9 games on Apple Silicon.

- Download from https://www.codeweavers.com/crossover
- Install and activate license (14-day free trial available)
- CrossOver handles wine32on64, Rosetta 2 bridging, and bottle management automatically

**Free alternative:** Porting Kit (https://portingkit.com) — built on Wine/CrossOver open-source components, more manual setup.

---

## Step 2: Create a Bottle and Install SWAT 4

1. Open CrossOver → **Bottle** → **New Bottle**
2. Name it `SWAT4` (or similar)
3. Bottle type: **Windows 10 32-bit**
4. Install SWAT 4 into the bottle:
   - If using disc/ISO: mount and run `Setup.exe` through CrossOver
   - If using GOG installer: run the GOG `.exe` installer through CrossOver
5. Verify the install completes without errors

---

## Step 3: Install the Mod

1. Locate the SWAT 4 install inside the bottle:
   ```
   ~/Library/Application Support/CrossOver/Bottles/SWAT4/drive_c/Program Files/SWAT 4/
   ```
2. Copy the `DueProcess` mod folder into the SWAT 4 root directory (next to `Content`, `ContentExpansion`, etc.)
3. Verify the folder structure looks like:
   ```
   SWAT 4/
   ├── Content/
   ├── ContentExpansion/
   ├── DueProcess/
   │   ├── Content/
   │   │   └── Sounds/
   │   │       └── CivilianNightclub/
   │   │           ├── ak_01.ogg
   │   │           ├── ak_02.ogg
   │   │           └── ...
   │   ├── System/
   │   │   ├── Conversations.ini
   │   │   ├── DueProcess_Missions.ini
   │   │   ├── Speakers.ini
   │   │   ├── SoundEffects.ini
   │   │   └── SwatMissions.ini
   │   └── SCRIPTS/
   └── System/
   ```

---

## Step 4: Apply INI Tweaks

Edit `SWAT 4/Content/System/Swat4.ini` (the base game config inside the bottle):

### 4a. Disable EAX Audio
Find the `[ALAudio.ALAudioSubsystem]` section and set:
```ini
UseEAX=False
```
EAX 3D positional audio crashes under Wine's OpenAL implementation.

### 4b. Reduce Texture Cache
In the same file or `[Engine.GameEngine]` section, set:
```ini
CacheSizeMegs=128
```
Prevents texture cache overflow that causes visual glitches on the translation layer.

### 4c. Audio Driver Fallback (if needed)
If audio cuts out or is distorted, open `winecfg` in the bottle (CrossOver → Bottle → Open Wine Configuration) and under the **Audio** tab, switch from PulseAudio to **CoreAudio** or the generic driver.

---

## Step 5: Configure Launch Options

In CrossOver, edit the SWAT 4 launch command to include:
```
-nointro
```
This skips intro videos that can hang or crash on Wine.

For the mod specifically, the launch command should be:
```
Swat4.exe -ini=DueProcess/System/Swat4.ini -nointro
```
(Or however the mod's INI override is structured — may need a custom `.bat` or shortcut.)

---

## Step 6: Test and Troubleshoot

### Expected issues and fixes:

| Issue | Symptom | Fix |
|-------|---------|-----|
| No sound | Silence or crash on map load | Set `UseEAX=False`, switch audio driver in winecfg |
| Texture corruption | Missing/garbled textures | Set `CacheSizeMegs=128`, or apply VRAM hex edit (see below) |
| Optiwand crash | Game crashes when using mirror gun | Known WineD3D shader bug — avoid optiwand or accept occasional crash |
| Hang on startup | Black screen after launch | Add `-nointro` flag, wait 30+ seconds for Rosetta JIT compilation on first launch |
| Low FPS | Stuttering, ~20-30 FPS | Expected on first run (Rosetta JIT cache). Second launch should be ~60-70% of native Windows perf |
| VRAM misdetection | "Low video memory" warning, broken textures | Hex edit `Swat4.exe` to bypass VRAM check (see below) |

### VRAM Hex Edit (if needed)
Wine may misreport GPU VRAM on Apple Silicon's unified memory. If the game shows a low VRAM warning:
1. Open `Swat4.exe` in a hex editor
2. Search for the VRAM detection routine (byte pattern varies by game version)
3. Force it to report 128MB+ — specific offsets depend on the exact executable version
4. This is a last resort; most users won't need it

---

## Step 7: Performance Expectations

- **First launch**: Slow (60-90 seconds). Rosetta 2 is JIT-compiling x86 instructions and caching them.
- **Subsequent launches**: Faster (15-30 seconds). Cached translations persist.
- **In-game FPS**: Expect 30-60 FPS depending on map complexity. The triple translation layer (x86→ARM + Win→macOS + DX9→Metal) has overhead.
- **Audio latency**: Slightly higher than native (~20-50ms). Not noticeable for dialogue playback.

---

## Alternative: Remote Windows Instance (Fallback)

If Wine proves too unstable for testing/development, a Windows VM or cloud instance remains an option:
- **Parallels Desktop** ($100/year) — runs Windows 11 ARM with x86 emulation, can run SWAT 4
- **AWS EC2** — spin up a `g4dn.xlarge` Windows instance for ~$0.71/hr when needed for testing
- **Shadow PC** — cloud gaming PC subscription

These are fallbacks, not the primary plan. CrossOver should work.

---

## Status

- [ ] Install CrossOver
- [ ] Create bottle and install SWAT 4
- [ ] Copy mod files into bottle
- [ ] Apply INI tweaks (UseEAX, CacheSizeMegs)
- [ ] Test base game launch with -nointro
- [ ] Test mod loading
- [ ] Test voice line playback (Andriy Kovalenko lines in SP-ABomb)
- [ ] Document any additional fixes needed
