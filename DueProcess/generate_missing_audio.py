#!/usr/bin/env python3
"""Generate all missing audio files referenced in SoundEffects.ini via ElevenLabs TTS."""

import os
import re
import json
import time
import subprocess
import urllib.request
import urllib.error

API_KEY = "sk_2c24941493baceab59e8d6a8c37c8790fa6e73ad717cefd1"
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "Content", "Sounds")
INI_FILE = os.path.join(BASE_DIR, "System", "SoundEffects.ini")

# Voice assignments by speaker ID — DISTINCT voice per character
# NYC setting: accents and ethnic backgrounds considered
VOICE_MAP = {
    # --- Training characters (locked in from previous generation) ---
    "u1":  "zfpxqh60b0TrMkJHDLsR",  # Peter — DAD Stokes (Instructor), NY accent
    "vaz": "zwDSHuqO0tEVwNUuHmR1",  # Ivan — Agt. Vasquez, Puerto Rican accent
    "daw": "0JRpJnrcyEVIabsZ4U5I",  # Jean-Paul Niko — Agt. Dawson, calm American

    # --- Four officers: each gets a DISTINCT voice ---
    "b1":  "OBLxU3DhFiBOh33EeRvi",  # Pauly — Agent Fields, Brooklyn Italian-American
    "b2":  "aOZ9Pl8uWUTet0DS7PYP",  # Scott — Agent Jackson, deep NY accent
    "r1":  "ICwKbPHDHAM3eal5tHEZ",  # Tony — Agent Reynolds, tough/confident
    "r2":  "iP95p4xoKVk53GoZ742B",  # Chris — Agent Girard, charming/down-to-earth

    # --- Player / Command ---
    "ld":  "CwhRBWXzGAHq8TQ4Fs17",  # Roger — Player/squad leader, laid-back
    "toc": "JjqNMa6BEYmyQYRCdHCa",  # Jim — T.O.C. command, corporate/authoritative

    # --- Female roles: each gets a DISTINCT voice ---
    "dis": "zWoalRDt5TZrmW4ROIA7",  # Brooklyn — Dispatch, African American New Yorker
    "tv1": "oWjuL7HSoaEJRMDMP3HD",  # Lina — News Reporter, confident/dynamic
    "wk":  "cgSgspJ2msm6clMCkdW9",  # Jessica — Woman on Radio, bright/warm

    # --- Tactical (snipers/overwatch): each distinct ---
    "hg":  "cjVigY5qzO86Huf0OWal",  # Eric — Highground, smooth/trustworthy
    "s1":  "nPczCjzI2devNBz1zQrb",  # Brian — Sierra 1, deep/resonant
    "s2":  "pNInz6obpgDQGcFmaJgB",  # Adam — Sierra 2, dominant/firm

    # --- Named characters ---
    "cj":  "jXkeB46JcPXXUSxzn3MD",  # Edward — Carl Jennings (arms dealer), reserved/old
    "cr":  "0q9TlrIoQJIdxZP9oZh7",  # Hazel — Carmen Reyes, Spanish accent female
}

# Fallback: any unknown speaker gets a generic male voice
DEFAULT_VOICE = "CwhRBWXzGAHq8TQ4Fs17"  # Roger

# Directories we care about (our mod content)
MOD_DIRS = [
    "CivilianHospital/",
    "CivilianSchool/",
    "CivilianTaco/",
    "CivilianNightclub/",
    "CivilianTenement/",
    "ScriptedVO/",
    "OfficerDueProcess/",
]


def parse_specs(ini_path):
    """Parse SoundEffects.ini and return dict of {spec_name: {streams, caption, speaker}}."""
    specs = {}
    current_spec = None

    with open(ini_path, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            stripped = line.strip()

            # Section header
            if stripped.startswith('[') and stripped.endswith(']'):
                name = stripped[1:-1]
                # Skip non-spec sections (preloaders, etc.)
                if 'PlayerController' not in name and 'Speakers' not in name and 'SwatGame' not in name:
                    current_spec = name
                    specs[current_spec] = {"streams": [], "caption": "", "speaker": ""}
                else:
                    current_spec = None
                continue

            if current_spec and '=' in stripped:
                key, val = stripped.split('=', 1)
                key = key.strip()
                val = val.strip()
                if key == "Streams":
                    specs[current_spec]["streams"].append(val)
                elif key == "Caption":
                    specs[current_spec]["caption"] = val
                elif key == "Speaker":
                    specs[current_spec]["speaker"] = val

    return specs


def find_missing_files(specs):
    """Find specs whose audio files don't exist in our mod directories."""
    missing = []
    for name, spec in specs.items():
        for stream in spec["streams"]:
            # Only check files in our mod directories
            if any(stream.startswith(d) for d in MOD_DIRS):
                full_path = os.path.join(SOUNDS_DIR, stream)
                if not os.path.exists(full_path):
                    caption = spec["caption"]
                    speaker = spec["speaker"]
                    if caption and caption != "None":  # Skip specs with no caption
                        missing.append({
                            "spec": name,
                            "stream": stream,
                            "caption": caption,
                            "speaker": speaker,
                            "full_path": full_path,
                        })
    return missing


def generate_tts(text, voice_id, output_mp3):
    """Call ElevenLabs TTS API and save MP3."""
    url = f"{BASE_URL}/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    data = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        }
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            with open(output_mp3, "wb") as f:
                while True:
                    chunk = resp.read(4096)
                    if not chunk:
                        break
                    f.write(chunk)
        return True
    except urllib.error.HTTPError as e:
        body = e.read()[:200]
        print(f"  ERROR {e.code}: {body}")
        return False


def convert_mp3_to_ogg(mp3_path, ogg_path):
    """Convert MP3 to mono 44100Hz OGG Vorbis."""
    wav_path = mp3_path.replace(".mp3", "_temp.wav")
    r1 = subprocess.run(
        ["ffmpeg", "-y", "-i", mp3_path, "-ac", "1", "-ar", "44100", wav_path],
        capture_output=True
    )
    if r1.returncode != 0:
        print(f"\n  ffmpeg error: {r1.stderr[-200:]}")
        return False
    r2 = subprocess.run(
        ["oggenc", "-q", "4", wav_path, "-o", ogg_path, "--quiet"],
        capture_output=True
    )
    if os.path.exists(wav_path):
        os.remove(wav_path)
    if r2.returncode != 0:
        print(f"\n  oggenc error: {r2.stderr[-200:]}")
        return False
    return True


def main():
    print("Parsing SoundEffects.ini...")
    specs = parse_specs(INI_FILE)
    print(f"Found {len(specs)} total specs")

    print("Checking for missing audio files...")
    missing = find_missing_files(specs)
    print(f"Found {len(missing)} missing files with captions")

    if not missing:
        print("Nothing to generate!")
        return

    # Deduplicate by stream path (same file might be referenced by multiple specs)
    seen = set()
    unique_missing = []
    for m in missing:
        if m["stream"] not in seen:
            seen.add(m["stream"])
            unique_missing.append(m)

    print(f"Unique files to generate: {len(unique_missing)}")
    print()

    # Show breakdown by speaker
    by_speaker = {}
    for m in unique_missing:
        sp = m["speaker"] or "unknown"
        by_speaker.setdefault(sp, []).append(m)
    for sp, items in sorted(by_speaker.items()):
        voice = VOICE_MAP.get(sp, DEFAULT_VOICE)
        mapped = "MAPPED" if sp in VOICE_MAP else "DEFAULT"
        print(f"  {sp}: {len(items)} files ({mapped})")
    print()

    total = len(unique_missing)
    done = 0
    skipped = 0
    failed = 0

    for i, m in enumerate(unique_missing, 1):
        ogg_path = m["full_path"]
        mp3_path = ogg_path.replace(".ogg", ".mp3")

        # Create directory if needed
        os.makedirs(os.path.dirname(ogg_path), exist_ok=True)

        # Skip if already exists (resume support)
        if os.path.exists(ogg_path):
            print(f"[{i:3d}/{total}] SKIP (exists): {m['stream']}")
            skipped += 1
            continue

        speaker = m["speaker"] or "ld"
        voice_id = VOICE_MAP.get(speaker, DEFAULT_VOICE)
        caption = m["caption"]

        print(f"[{i:3d}/{total}] Generating: {m['stream']} ({speaker})...", end=" ", flush=True)

        if not generate_tts(caption, voice_id, mp3_path):
            failed += 1
            print("FAILED")
            continue

        if not convert_mp3_to_ogg(mp3_path, ogg_path):
            failed += 1
            print("CONVERT FAILED")
            continue

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

        if os.path.exists(ogg_path):
            size_kb = os.path.getsize(ogg_path) / 1024
            print(f"OK ({size_kb:.0f} KB)")
            done += 1
        else:
            print("MISSING OGG")
            failed += 1

        time.sleep(0.3)

    print(f"\n{'='*50}")
    print(f"Done! Generated: {done}, Skipped: {skipped}, Failed: {failed}")


if __name__ == "__main__":
    main()
