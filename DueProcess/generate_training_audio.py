#!/usr/bin/env python3
"""Generate all 121 SP-Training voice lines via ElevenLabs TTS, convert to OGG."""

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
VOICES = {
    "u1":  "zfpxqh60b0TrMkJHDLsR",  # Peter (Stokes)
    "vaz": "zwDSHuqO0tEVwNUuHmR1",  # Ivan (Vasquez)
    "daw": "0JRpJnrcyEVIabsZ4U5I",  # Jean-Paul Niko (Dawson)
    "b1":  "OBLxU3DhFiBOh33EeRvi",  # Pauly (Fields)
    "b2":  "OBLxU3DhFiBOh33EeRvi",  # Pauly (Jackson)
    "r1":  "OBLxU3DhFiBOh33EeRvi",  # Pauly (Reynolds)
    "r2":  "OBLxU3DhFiBOh33EeRvi",  # Pauly (Girard)
}

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "Content", "Sounds", "ScriptedVO")

# All lines: (filename_without_ext, speaker, text)
LINES = [
    # ACT I: ORIENTATION
    ("icetr_01_01_u1", "u1", "Welcome to the Federal Law Enforcement Training Center. I'm Deputy Assistant Director Garrett Stokes, twenty-three years with Immigration and Customs Enforcement. I'll be observing your qualification run from the catwalks and walking you through our updated operational procedures."),
    ("icetr_01_02_u1", "u1", "As of January, the Academy has been restructured. Director Homan reduced the program from seventy-two days to forty-two. He called it cutting redundancy. I call it excellence through efficiency. When you're ready, proceed through the door on the right."),

    # ACT II: FIRING RANGE
    ("icetr_02_01_u1", "u1", "This is the firing range. We've updated the scenario targets to reflect current enforcement priorities. You'll notice the silhouettes are wearing civilian clothing. That's by design."),
    ("icetr_02_02_u1", "u1", "Our subjects don't wear uniforms. They look like your neighbor. Your landscaper. The woman at the grocery store. Engagement distances have been adjusted to reflect residential hallway widths. Because that's where you'll be working."),
    ("icetr_02_03_u1", "u1", "A good drill to practice is the failure-to-comply sequence. Two to the center mass, one to the head. In enforcement scenarios, you'll encounter subjects who don't respond to verbal commands. Language barriers, hearing impairment, or simple noncompliance. The response is the same regardless of cause."),
    ("icetr_02_04_u1", "u1", "When you're finished, continue to the next station."),
    ("icetr_03_01_u1", "u1", "Not bad. The button on the left will reel in the target for inspection. Note the grouping. In a residential entry scenario, every round that misses the subject enters a wall. And behind that wall might be a family. This matters for your after-action report. Not for your authorization to engage."),
    ("icetr_04_01_u1", "u1", "That one was wide. In the old program, you'd get three days on marksmanship fundamentals for a grouping like that. Now you get a passing note and a deployment date. Adjust accordingly."),
    ("icetr_05_01_u1", "u1", "Your sidearm is your backup weapon, but in tight spaces -- apartments, kitchens, bathrooms -- it becomes your primary. The Todd Lyons memo on residential enforcement specifically addresses this."),
    ("icetr_05_02_u1", "u1", "If you haven't read the Lyons memo... well. You won't read it. It's a read-and-return document. You go to the supervisor's office, you read it, and you hand it back. Nothing leaves the room. Nothing gets photocopied."),
    ("icetr_05_03_u1", "u1", "When you're done, move on to the next station."),
    ("icetr_06_01_u1", "u1", "At this distance, accuracy becomes imperative. But I'll be honest with you -- most of your engagements will be at fifteen feet or less. Hallways. Doorframes. The space between a bed and a wall where someone is hiding their child."),
    ("icetr_06_02_u1", "u1", "When you're finished on the range, head to the grenade training area."),
    ("icetr_07_01_u1", "u1", "Now you can see how hard it is to maintain accuracy at range. The Director says there are no more sensitive locations. Schools, churches, hospitals -- they're all standard enforcement environments now. Tom Homan's exact words: 'There are no sanctuaries.' So you need to be accurate everywhere."),
    ("icetr_08_01_u1", "u1", "Not bad. Remember, you are most accurate when you have a stable firing position. But you won't always have one."),
    ("icetr_08_02_u1", "u1", "Five AM entries. Dark hallways. Subjects in bedclothes. Children in the next room. You need to make correct decisions in two-tenths of a second with adrenaline and a flashlight."),
    ("icetr_08_03_u1", "u1", "In the old program, they gave you two hundred and fifty hours of scenario training for this. Now it's handled in the field. What the whistleblower called 'deficient, defective, and broken' training. What we call 'streamlined.'"),
    ("icetr_08_04_u1", "u1", "Head through the door to the grenade range."),

    # ACT III: GRENADE RANGE
    ("icetr_09_01_u1", "u1", "Welcome to the grenade range. Under updated guidelines, these are classified as 'compliance tools.' Flashbangs, CS gas, and stinger grenades are all authorized for residential enforcement operations."),
    ("icetr_09_02_u1", "u1", "Agent Vasquez, you're our most recent Academy graduate. How much time did they give you on compliance tools?"),
    ("icetr_09_03_vaz", "vaz", "Half a day, sir. We did flashbangs in the morning and they said we'd cover gas in the field."),
    ("icetr_09_04_u1", "u1", "Half a day. Well. The field is the best teacher. Let's see what you retained."),
    ("icetr_10_01_u1", "u1", "Flashbangs are designed to disorient subjects with a concussive blast and a blinding flash. For five AM entries, they serve a dual purpose -- they establish that you are federal officers. Even when you're not wearing identification. Even when you haven't announced yourself. The bang announces you."),
    ("icetr_11_01_u1", "u1", "CS gas. Causes eyes to water, disrupts breathing. Extremely effective in enclosed spaces. If the residence contains infants, elderly, or individuals with respiratory conditions, you note that on form ICE-37B after the operation. Not before. Before, it's a tactical decision. After, it's paperwork."),
    ("icetr_12_01_u1", "u1", "Stinger grenades. Rubber pellets at high velocity. Noncompliant subjects drop. Compliant subjects also drop, if they're in the blast radius. The grenades don't distinguish. That's why you fill out the form afterward."),

    # ACT IV: DOOR BREACHING
    ("icetr_13_01_u1", "u1", "Go ahead and try this door. This is the section that matters most. Expedited entry procedures."),
    ("icetr_14_01_u1", "u1", "I locked it before you got here. We have multiple entry tools available -- the breaching shotgun and the C2 charge. Under the updated guidelines from the Todd Lyons memorandum, an administrative warrant -- the I-200 -- provides sufficient authority for entry."),
    ("icetr_14_02_u1", "u1", "You don't need a judge. You don't need a signature from a magistrate. The I-200 is signed by your supervisor. That's the authority. A locked door is a logistical obstacle, not a legal one."),
    ("icetr_14_03_u1", "u1", "Nice work. Move on to the next door. We'll use a C2 charge."),
    ("icetr_15_01_u1", "u1", "OK, we're going all out on this one. Place the C2 on the door. In the field, this is your five AM wake-up call. The family on the other side has no idea you're federal agents. They hear an explosion, their door is gone, and there are men with guns in their hallway."),
    ("icetr_15_02_u1", "u1", "The whistleblower who testified in February called this training 'deficient, defective and broken.' Congress held a hearing. Nothing changed. Set the charge."),
    ("icetr_16_01_u1", "u1", "Now step back and blow it."),
    ("icetr_17_01_u1", "u1", "Nice. I never get tired of that."),
    ("icetr_17_02_u1", "u1", "You just breached a door on the authority of an administrative warrant signed by your field supervisor. No judge involved. The Lyons memo says that's sufficient. The ACLU says it's unconstitutional. The courts haven't decided yet. But you're already through the door."),
    ("icetr_18_01_u1", "u1", "You'll have to learn about C2 in the field. Like everything else in the new program. Let's move on."),

    # ACT V: KILL HOUSE
    ("icetr_19_01_u1", "u1", "We are a processing organization. Every encounter is a potential administrative action. Every subject is a potential detainee. Your job is not to determine guilt or innocence. Your job is to process."),
    ("icetr_20_01_u1", "u1", "You are authorized to detain anyone at the scene of an enforcement action. The Director's criteria for collateral arrest are broad. His words: 'location, occupation, physical appearance, and actions -- such as the person walks away.'"),
    ("icetr_20_02_u1", "u1", "Walking away. That's sufficient basis. If someone turns and leaves when they see you, that's reasonable suspicion. If someone reaches for a phone, that's a potential threat. Comply, or be processed. Now engage the targets."),
    ("icetr_20_03_u1", "u1", "Now that Agent Dawson has demonstrated the incorrect response, let's continue. Dawson, you all right?"),

    # ACT VI: AGENT BANTER
    ("icetr_21_01_b2", "b2", "You see the DHS Instagram post? The one with the Pine Tree Riots song?"),
    ("icetr_21_02_r1", "r1", "'We'll Have Our Home Again.' Yeah. Someone in communications thought a neo-Nazi recruitment anthem was a good look for the agency."),
    ("icetr_21_03_b1", "b1", "They took it down after three hours. But the iFunny guys already screenshotted it."),
    ("icetr_21_04_r1", "r1", "The Agartha stuff? Jesus."),
    ("icetr_21_05_r2", "r2", "So what? It's a good song. I don't see the problem."),
    ("icetr_21_06_u1", "u1", "That's enough. Lessons were learned. Process improvement was implemented. Let's move on."),
    ("icetr_21_07_u1", "u1", "We're hiring ten thousand new agents this fiscal year. Background checks have been expedited. Some things slip through. The system self-corrects."),

    # ACT VII: TEAM COMMANDS
    ("icetr_22_01_u1", "u1", "If you're going to lead a tactical element, you'll need to command your team effectively. These are your officers. Give them orders and they'll respond. Just like the subjects in the field -- only these ones actually listen."),
    ("icetr_23_01_b1", "b1", "Nice to meet you, sir. I had a question -- are we still doing school drop-off operations? I heard they suspended those."),
    ("icetr_23_02_u1", "u1", "I don't think I quite heard you, Fields. What did you say?"),
    ("icetr_23_03_b1", "b1", "The school operations, sir. Drop-off lines, bus stops. I heard they--"),
    ("icetr_23_04_u1", "u1", "The updated sensitive locations guidance specifically authorizes enforcement in proximity to educational facilities. The old policy created an enforcement gap. Fields, we don't have gaps anymore."),
    ("icetr_23_05_u1", "u1", "Now, let's focus on the exercise. Tell Blue Team to fall in behind you."),
    ("icetr_24_01_u1", "u1", "Not that one. Focus. Your team is watching."),
    ("icetr_25_01_u1", "u1", "Are we speaking the same language here? I said fall in behind me."),
    ("icetr_26_01_u1", "u1", "Don't make me come down there. Fields would be happy to take over."),
    ("icetr_26_02_u1", "u1", "Equip your flashlight. In a five AM entry, you cut the power to the residence first. The subject wakes up to darkness, then a flashlight in their face. They're disoriented before you give the first command."),
    ("icetr_26_03_u1", "u1", "Try it now."),
    ("icetr_27_01_u1", "u1", "Beware of doorways. Most fatalities in enforcement operations occur at the threshold. But here's the thing -- in a residential entry, the door frame is also where the family photos are. You'll see them as you stack up. Try not to look."),
    ("icetr_27_03_u1", "u1", "Use your optiwand to check the next room before entering."),
    ("icetr_28_01_u1", "u1", "Alright. Behind these barriers there's an open doorway. Use the optiwand to scout the room before your team enters. Through the camera, you might see a family eating breakfast. Or a child doing homework. None of this changes your operational mandate."),
    ("icetr_28_02_u1", "u1", "If the subject is in the room, you enter and process. If the subject is not in the room, you enter and search. Bystanders are secured until identification is verified."),
    ("icetr_29_02_u1", "u1", "That's the collateral arrest procedure. Anyone at the scene is subject to processing. Director Homan calls it 'operational efficiency.' The Minneapolis operation processed over two thousand people in a single day."),
    ("icetr_30_01_u1", "u1", "When the team discovers a hallway during clearing, you'll need to make quick decisions about direction. In residential structures, hallways lead to bedrooms. Bedrooms are where subjects are at five AM."),
    ("icetr_30_02_u1", "u1", "Tell your team where to go."),
    ("icetr_31_01_u1", "u1", "You now have two possible directions. Standard procedure is to clear left to right, but in an enforcement operation, you go to the sound. Crying children indicate occupied rooms. Follow the noise."),
    ("icetr_31_02_u1", "u1", "Send a team to cover each direction."),
    ("icetr_32_01_u1", "u1", "Good. Now tell Red Team to fall in. You'll need both elements for the next exercise."),
    ("icetr_33_01_u1", "u1", "That's not what I asked. Try again. And remember -- if you can't follow my commands in training, how are you going to give them in a subject's living room?"),
    ("icetr_34_01_u1", "u1", "No, that's not right. One more time."),
    ("icetr_35_01_u1", "u1", "Don't you listen? Tell Blue to stack up on the door."),
    ("icetr_36_01_u1", "u1", "Maybe you didn't hear me. Tell Blue to stack up on the door. This isn't complicated."),
    ("icetr_37_01_u1", "u1", "When you're ready to stop screwing around, let me know. The ten thousand new hires can't get here fast enough."),
    ("icetr_37_02_u1", "u1", "Fine. Figure it out yourself. Excellence through compliance. Or not. Your call."),
    ("icetr_38_01_u1", "u1", "No, no. The other door. The one that's closed. In the field, closed doors are where the subjects are."),
    ("icetr_39_01_u1", "u1", "No, you're going back where you came from. Try going left at the intersection. Body camera footage should be recording, by the way. Not for oversight -- for recruitment content."),
    ("icetr_40_01_u1", "u1", "OK. You can keep tabs on your officers when you're separated using the command interface. In the Minneapolis operation, teams cleared forty residences simultaneously. Coordination is everything."),
    ("icetr_41_01_u1", "u1", "Since you can essentially see through their eyes, it's not hard to command them from a distance. Use the interface to order an entry. Think of it as... managing a process. Because that's what this is. A process."),
    ("icetr_42_01_u1", "u1", "Great. Let's continue."),
    ("icetr_42_02_u1", "u1", "Head out of this room and stop about halfway up the stairs. We have one more section."),

    # ACT VIII: SNIPER OVERVIEW
    ("icetr_43_01_u1", "u1", "One of the most valuable members of your team is the sniper. Sierra team provides overwatch during enforcement operations."),
    ("icetr_43_02_u1", "u1", "In January, an agent discharged his weapon at a vehicle moving away from him. Three rounds through the rear windshield. The subject -- a United States citizen -- was fatally wounded."),
    ("icetr_43_03_u1", "u1", "Her name was Renee Good. She was not a target. She was not a suspect. She was driving away."),
    ("icetr_43_04_u1", "u1", "The agent -- Jonathan Ross -- said he feared for his safety. The administration classified the shooting as justified. Self-defense."),
    # icetr_43_04a_ld is a silent beat — generate a short silence file instead
    ("icetr_43_05_u1", "u1", "The Director stood behind the agent. The agency stood behind the Director. That's the chain. You shoot, you're covered. As long as you followed procedure."),
    ("icetr_43_06_u1", "u1", "As long as you followed procedure."),
    ("icetr_43_07_u1", "u1", "When you're finished, continue up and go into the room to conclude your qualification."),

    # ACT IX: WRAP-UP
    ("icetr_44_01_u1", "u1", "Well, that's it for the qualification run. One last thing. Kilmar Abrego Garcia. Man had legal withholding-of-removal status. Court-ordered. Still got deported to El Salvador. To CECOT prison. Supreme Court ordered the administration to bring him back. They said no. Called it an 'administrative error.' Errors happen. The important thing is that the system keeps moving. Excellence through compliance."),

    # ACT X: MISBEHAVIOR - Stokes
    ("icetr_45_01_u1", "u1", "What the HELL was that?! Stand DOWN!"),
    ("icetr_46_01_u1", "u1", "You just discharged your weapon at a federal instructor! Every round has a congressional inquiry attached!"),
    ("icetr_47_01_u1", "u1", "Are you a plant? Did the ACLU send you? Because this is EXACTLY what they want on camera!"),
    ("icetr_48_01_u1", "u1", "This isn't Minneapolis! You can't just -- ! STAND DOWN!"),
    ("icetr_50_01_u1", "u1", "That is a CAREER-ENDING discharge! The Office of Professional Responsibility will have your badge by MONDAY!"),
    ("icetr_51_01_u1", "u1", "I have been with this agency twenty-three years! TWENTY-THREE YEARS! And I have NEVER -- !"),
    ("icetr_52_01_u1", "u1", "Do you have any idea how much paperwork you just created? Do you?!"),
    ("icetr_53_01_u1", "u1", "The Director will hear about this! You want to explain this to Tom Homan personally?!"),
    ("icetr_54_01_u1", "u1", "I'm done. I'm DONE. Somebody get this agent out of my facility before they shoot me AGAIN!"),

    # ACT X: MISBEHAVIOR - Vasquez
    ("icetr_55_01_vaz", "vaz", "OW! What the -- I just graduated! I've been an agent for TWO WEEKS!"),
    ("icetr_56_01_vaz", "vaz", "STOP SHOOTING ME! I haven't even finished my field training!"),
    ("icetr_57_01_vaz", "vaz", "Is this NORMAL?! They didn't cover this in the forty-two day program!"),
    ("icetr_58_01_vaz", "vaz", "Sir! SIR! I'm requesting a transfer! RIGHT NOW!"),

    # ACT X: MISBEHAVIOR - Dawson
    ("icetr_59_01_daw", "daw", "ARGH! Son of a -- I transferred from CBP to get AWAY from this!"),
    ("icetr_60_01_daw", "daw", "That's a federal agent you're shooting! I have fifteen years in! FIFTEEN!"),
    ("icetr_61_01_daw", "daw", "I didn't leave Border Patrol to get shot in TRAINING!"),
    ("icetr_62_01_daw", "daw", "You know what? I'm going back to CBP. At least the DESERT doesn't shoot at you."),

    # ACT X: MORE MISBEHAVIOR - Stokes
    ("icetr_63_01_u1", "u1", "HOLSTER YOUR WEAPON! That is an ORDER!"),
    ("icetr_64_01_u1", "u1", "I am filing an incident report that will follow you to EVERY field office in the COUNTRY!"),
    ("icetr_65_01_u1", "u1", "The Inspector General will review this! The SECRETARY will review this!"),
    ("icetr_66_01_u1", "u1", "You think you're funny? You think this is a JOKE? People DIED in the field last month!"),
    ("icetr_67_01_u1", "u1", "This is why the whistleblower testified! THIS! Right HERE!"),
    ("icetr_68_01_u1", "u1", "SECURITY! I need security in the training facility! We have an active -- YOU KNOW WHAT I MEAN!"),
    ("icetr_69_01_u1", "u1", "Twenty-three years. Twenty-three years of excellence through compliance and THIS is what they send me."),
    ("icetr_70_01_u1", "u1", "You're done. You're DONE. Hand me your badge and your I-200 pad. NOW."),
    ("icetr_71_01_u1", "u1", "I'm calling the Deputy Director. I'm calling the ACTING Deputy Director. I'm calling whoever is in charge THIS WEEK."),
    ("icetr_72_01_u1", "u1", "That's it. Training is suspended. Everybody out. EVERYBODY OUT. Not you. You STAY."),

    # ACT XI: BREAK ROOM
    ("icetr_73_01_r2", "r2", "Sweet! Donuts! Nobody told me there'd be donuts! And what are these -- recruitment flyers?"),
    ("icetr_73_02_b2", "b2", "The ones with the Pine Tree Riots song? Or the other ones?"),
    ("icetr_73_03_b1", "b1", "Different batch. These just say 'Protect the Homeland' with a stock photo of agents in ski masks."),
    ("icetr_73_04_b2", "b2", "For safety. Because threats are up 'over eight thousand percent.' According to the Director."),

    # ACT XII: ALTERNATE PATH
    ("icetr_74_01_u1", "u1", "Guess you're not a fan of standard entry procedures. You can try the C2 charge. In the field, a locked door is not a legal barrier."),
    ("icetr_75_01_u1", "u1", "It's a logistical one."),
]


def generate_silence_ogg(filepath, duration=2.0):
    """Generate a short silence OGG file for the player's silent beat."""
    wav_path = filepath.replace(".ogg", "_temp.wav")
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
        "-t", str(duration), "-ac", "1", "-ar", "44100", wav_path
    ], capture_output=True)
    subprocess.run(["oggenc", "-q", "4", wav_path, "-o", filepath, "--quiet"], capture_output=True)
    if os.path.exists(wav_path):
        os.remove(wav_path)


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
        print(f"  ERROR {e.code}: {e.read()[:200]}")
        return False


def convert_mp3_to_ogg(mp3_path, ogg_path):
    """Convert MP3 to mono 44100Hz OGG Vorbis (two-step: ffmpeg→WAV, oggenc→OGG)."""
    wav_path = mp3_path.replace(".mp3", "_temp.wav")
    # Step 1: MP3 → WAV (mono, 44100 Hz)
    r1 = subprocess.run(
        ["ffmpeg", "-y", "-i", mp3_path, "-ac", "1", "-ar", "44100", wav_path],
        capture_output=True
    )
    if r1.returncode != 0:
        print(f"\n  ffmpeg error: {r1.stderr[-200:]}")
        return False
    # Step 2: WAV → OGG
    r2 = subprocess.run(
        ["oggenc", "-q", "4", wav_path, "-o", ogg_path, "--quiet"],
        capture_output=True
    )
    # Clean up WAV
    if os.path.exists(wav_path):
        os.remove(wav_path)
    if r2.returncode != 0:
        print(f"\n  oggenc error: {r2.stderr[-200:]}")
        return False
    return True


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate the silent beat file first
    silence_ogg = os.path.join(OUTPUT_DIR, "icetr_43_04a_ld.ogg")
    if not os.path.exists(silence_ogg):
        print("[  0/121] Generating silence: icetr_43_04a_ld.ogg")
        generate_silence_ogg(silence_ogg, duration=2.0)

    total = len(LINES)
    done = 0
    skipped = 0
    failed = 0

    for i, (filename, speaker, text) in enumerate(LINES, 1):
        ogg_path = os.path.join(OUTPUT_DIR, f"{filename}.ogg")
        mp3_path = os.path.join(OUTPUT_DIR, f"{filename}.mp3")

        # Skip if OGG already exists (resume support)
        if os.path.exists(ogg_path):
            print(f"[{i:3d}/{total}] SKIP (exists): {filename}.ogg")
            skipped += 1
            continue

        voice_id = VOICES[speaker]
        print(f"[{i:3d}/{total}] Generating: {filename}.ogg ({speaker})...", end=" ", flush=True)

        if not generate_tts(text, voice_id, mp3_path):
            failed += 1
            print("FAILED")
            continue

        if not convert_mp3_to_ogg(mp3_path, ogg_path):
            failed += 1
            print("CONVERT FAILED")
            continue

        # Clean up MP3
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

        if os.path.exists(ogg_path):
            size_kb = os.path.getsize(ogg_path) / 1024
            print(f"OK ({size_kb:.0f} KB)")
            done += 1
        else:
            print("MISSING OGG")
            failed += 1

        # Small delay to respect rate limits
        time.sleep(0.3)

    print(f"\n{'='*50}")
    print(f"Done! Generated: {done}, Skipped: {skipped}, Failed: {failed}")
    print(f"Total files in {OUTPUT_DIR}: {len([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.ogg')])}")


if __name__ == "__main__":
    main()
