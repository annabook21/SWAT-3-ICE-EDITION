#!/usr/bin/env python3
"""Generate ICE dispatcher and TOC mission start audio via ElevenLabs TTS."""

import os
import sys
import time
import subprocess
import json
import urllib.request
import urllib.error

API_KEY = "sk_2c24941493baceab59e8d6a8c37c8790fa6e73ad717cefd1"
BASE_URL = "https://api.elevenlabs.io/v1/text-to-speech"

# Voice assignments
VOICE_DIS = "zWoalRDt5TZrmW4ROIA7"  # Brooklyn — Dispatch, African American New Yorker
VOICE_TOC = "JjqNMa6BEYmyQYRCdHCa"  # Jim — T.O.C. command, corporate/authoritative

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "Content", "Sounds")

# All lines to generate: (subdir, filename_no_ext, voice_id, text)
LINES = [
    # Dispatcher load audio (plays during loading screen)
    ("ScriptedVO", "AbombLoad_dis", VOICE_DIS,
     "All units, this is Operations. ERO enforcement team responding to 127 Adelaide Boulevard. Administrative warrants to be served. Secure perimeter on arrival."),

    ("ScriptedVO", "HospitalLoad_dis", VOICE_DIS,
     "All units, this is Operations. ERO team deploying to St. Michael's Medical Center. Administrative target identified in waiting area. Plainclothes and uniformed elements converging."),

    ("ScriptedVO", "RedLoad_dis", VOICE_DIS,
     "All units, this is Operations. ERO enforcement team en route to Gridley and Bromfield. Administrative warrants to be served at community center. Sensitive location protocols suspended per updated guidance."),

    ("ScriptedVO", "QwikLoad_dis", VOICE_DIS,
     "All units, this is Operations. ERO enforcement action at Pitkin and Daly intersection. Administrative detainers for multiple subjects. Collateral arrests authorized."),

    ("ScriptedVO", "TenementLoad_dis", VOICE_DIS,
     "All units, this is Operations. ERO team responding to 2189 Carrols Road. Expedited removal warrants for multiple subjects. Pre-dawn entry authorized."),

    # TOC mission start (plays when entering the map)
    ("TOC", "toc_RepliedMissionStart_1", VOICE_TOC,
     "Operations copies. Entry team, you are cleared for enforcement action. Execute on your go."),
    ("TOC", "toc_RepliedMissionStart_2", VOICE_TOC,
     "Operations copies. Enforcement team, you are green-lit. Initiate on your command."),
    ("TOC", "toc_RepliedMissionStart_3", VOICE_TOC,
     "Copy that. ERO element, you have authorization to proceed. Go when ready."),
    ("TOC", "toc_RepliedMissionStart_4", VOICE_TOC,
     "Operations has you on scope. Entry team, execute enforcement action at your discretion."),
    ("TOC", "toc_RepliedMissionStart_5", VOICE_TOC,
     "Acknowledged. All elements, warrants are confirmed. Begin enforcement operation."),
    ("TOC", "toc_RepliedMissionStart_6", VOICE_TOC,
     "Operations copies all. Entry team, you are cleared hot. Execute."),
    ("TOC", "toc_RepliedMissionStart_7", VOICE_TOC,
     "Roger. Enforcement team, perimeter is set. You are cleared for entry. Go."),
]


def generate_tts(voice_id, text, output_mp3):
    """Call ElevenLabs TTS API and save MP3."""
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    body = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8,
            "style": 0.15,
            "use_speaker_boost": True,
        },
    }).encode()

    url = f"{BASE_URL}/{voice_id}"
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(output_mp3, "wb") as f:
                f.write(resp.read())
        return True
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.read().decode()[:200]}")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def mp3_to_ogg(mp3_path, ogg_path):
    """Convert MP3 to OGG Vorbis (mono, 44100 Hz) via ffmpeg+oggenc."""
    # First decode MP3 to WAV with ffmpeg
    wav_path = mp3_path.replace(".mp3", ".wav")
    cmd_wav = [
        "ffmpeg", "-y", "-i", mp3_path,
        "-ac", "1", "-ar", "44100",
        "-c:a", "pcm_s16le", wav_path,
    ]
    result = subprocess.run(cmd_wav, capture_output=True, text=True)
    if result.returncode != 0:
        return False
    # Then encode WAV to OGG with oggenc
    cmd_ogg = ["oggenc", "-q", "4", "-o", ogg_path, wav_path]
    result = subprocess.run(cmd_ogg, capture_output=True, text=True)
    # Clean up WAV
    if os.path.exists(wav_path):
        os.remove(wav_path)
    return result.returncode == 0


def main():
    os.makedirs(os.path.join(SOUNDS_DIR, "ScriptedVO"), exist_ok=True)
    os.makedirs(os.path.join(SOUNDS_DIR, "TOC"), exist_ok=True)

    total = len(LINES)
    success = 0
    failed = 0

    for i, (subdir, filename, voice_id, text) in enumerate(LINES):
        ogg_path = os.path.join(SOUNDS_DIR, subdir, f"{filename}.ogg")
        mp3_path = ogg_path.replace(".ogg", ".mp3")

        print(f"[{i+1}/{total}] {subdir}/{filename}")
        print(f"  Text: {text[:80]}...")

        # Generate TTS
        if not generate_tts(voice_id, text, mp3_path):
            print(f"  FAILED TTS generation")
            failed += 1
            continue

        # Convert to OGG
        if not mp3_to_ogg(mp3_path, ogg_path):
            print(f"  FAILED OGG conversion")
            failed += 1
            continue

        # Clean up MP3
        os.remove(mp3_path)

        size = os.path.getsize(ogg_path)
        print(f"  OK ({size:,} bytes)")
        success += 1

        # Rate limit
        if i < total - 1:
            time.sleep(0.5)

    print(f"\nDone: {success} succeeded, {failed} failed out of {total}")


if __name__ == "__main__":
    main()
