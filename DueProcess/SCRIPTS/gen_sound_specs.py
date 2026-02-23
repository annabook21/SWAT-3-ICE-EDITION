#!/usr/bin/env python3
"""Generate SoundEffectSpecification entries for Due Process voice lines."""
import re

LINES = [
    # David Whitehorse (dw) - CivilianHospital
    ("dw_01", "CivilianHospital", "dw", "I'm sorry, you want to see MY papers? On THIS land?"),
    ("dw_02", "CivilianHospital", "dw", "Let me get this straight. You're asking me to prove I belong here. You."),
    ("dw_03", "CivilianHospital", "dw", "I'm Lakota. My family has been here for about twelve thousand years. How long has yours been here?"),
    ("dw_04", "CivilianHospital", "dw", "You want my tribal ID? Fine. Here. It's federal. Issued by your government. Recognizing that I exist. On my land."),
    ("dw_05", "CivilianHospital", "dw", "No, I don't have a passport. I've never left the country. I've never left the continent. My ancestors didn't either."),
    ("dw_06", "CivilianHospital", "dw", "This is... this is really happening right now. Okay."),
    ("dw_07", "CivilianHospital", "dw", "You know what's funny? My grandmother went to one of your boarding schools. \"Kill the Indian, save the man.\" And now you want my papers."),
    ("dw_08", "CivilianHospital", "dw", "I'm not going anywhere. I'm waiting for my mother. She has diabetes. Thanks to government commodity food, by the way."),
    ("dw_09", "CivilianHospital", "dw", "Do I have documentation? Do YOU have documentation? The Treaty of Fort Laramie, 1868. You're standing on stolen land."),
    ("dw_10", "CivilianHospital", "dw", "Sure, detain me. Add it to the list. Wounded Knee, Sand Creek, now this hospital waiting room."),
    ("dw_11", "CivilianHospital", "dw", "I'm not being difficult. I'm being Native American in America. It's always been difficult."),
    # Marcus Williams (mw) - CivilianHospital
    ("mw_01", "CivilianHospital", "mw", "Wait, you're offering to send me to another country? For free?"),
    ("mw_02", "CivilianHospital", "mw", "Hold on, hold on. Let me hear you out. Where we talking?"),
    ("mw_03", "CivilianHospital", "mw", "Canada? I could do Canada. Universal healthcare. They're polite. It snows, but I can adjust."),
    ("mw_04", "CivilianHospital", "mw", "What about Portugal? I heard they decriminalized everything. Very progressive. Good food."),
    ("mw_05", "CivilianHospital", "mw", "Ghana has that Right of Return program for Black Americans. You could send me to Ghana. I'd be welcomed."),
    ("mw_06", "CivilianHospital", "mw", "Actually, what about Norway? Highest quality of life in the world. Free college. They pay you to go to school."),
    ("mw_07", "CivilianHospital", "mw", "I'm not being difficult, officer. I'm cooperating. I'm enthusiastically cooperating. Pick a country."),
    ("mw_08", "CivilianHospital", "mw", "Germany? Strong economy. They actually dealt with their history. They have museums about it. Very healthy."),
    ("mw_09", "CivilianHospital", "mw", "New Zealand? Jacinda Ardern's not there anymore, but still. Hobbits. Mountains. No mass shootings."),
    ("mw_10", "CivilianHospital", "mw", "You're saying I have to PROVE I'm American to stay? And you're ALSO saying you could send me somewhere else if I can't?"),
    ("mw_11", "CivilianHospital", "mw", "My man, my ancestors have been here since 1619. Involuntarily. You sure you want me to stay?"),
    ("mw_12", "CivilianHospital", "mw", "No no no, don't put the paper away. Let's keep this conversation going. What about Barbados? Rihanna's from there."),
    ("mw_13", "CivilianHospital", "mw", "France? They got problems too but at least the cops don't— actually never mind, skip France."),
    ("mw_14", "CivilianHospital", "mw", "I'm just saying, if you're OFFERING, I'm LISTENING. This feels like an opportunity."),
    ("mw_15", "CivilianHospital", "mw", "Wait, you're telling me I can't be deported because I'm a citizen? That's... that's disappointing, actually."),
    ("mw_16", "CivilianHospital", "mw", "So let me understand: the one time the government wants to give a Black man a free trip somewhere, I don't qualify?"),
    ("mw_17", "CivilianHospital", "mw", "Alright. Alright. I'll stay. But I want it on the record that I was willing to go. Enthusiastically."),
    # Kevin Chen (kc) - CivilianSchool
    ("kc_01", "CivilianSchool", "kc", "What? No, I speak English. I was born here. Queens. Flushing Hospital. 1997."),
    ("kc_02", "CivilianSchool", "kc", "I don't— what are you saying? Is that supposed to be Chinese?"),
    ("kc_03", "CivilianSchool", "kc", "Bro, I literally don't understand you. I went to Stuyvesant. I took AP English."),
    ("kc_04", "CivilianSchool", "kc", "That's not— okay, that's Mandarin. I think. I speak Cantonese. My parents speak Cantonese. We're from Hong Kong."),
    ("kc_05", "CivilianSchool", "kc", "No, I don't \"understand you when you try.\" You're saying random words. That's not how languages work."),
    ("kc_06", "CivilianSchool", "kc", "My parents LEFT China because of the Communist Party. In 1989. You know what happened in 1989?"),
    ("kc_07", "CivilianSchool", "kc", "They're political refugees. THEY have papers. I was BORN here. I don't NEED papers. I'm a citizen."),
    ("kc_08", "CivilianSchool", "kc", "Are you seriously— okay, \"ni hao\" is literally the only thing you've said that made sense, and it's \"hello.\" We're past hello."),
    ("kc_09", "CivilianSchool", "kc", "I'm not \"pretending.\" I'm telling you, in perfect English, that I don't speak Mandarin. My family doesn't speak Mandarin. Because we're Cantonese. From Hong Kong. Different language."),
    ("kc_10", "CivilianSchool", "kc", "Can you just— can you get your supervisor? Someone who understands that Asia isn't one country?"),
    ("kc_11", "CivilianSchool", "kc", "This is insane. My niece is on that stage. She's Tinkerbell. She's eight. She was born in Jersey City. Can I please just watch her fly?"),
    ("kc_12", "CivilianSchool", "kc", "You want to call my parents? Sure. Call them. They'll tell you about Tiananmen Square. They'll tell you about democracy. They'll tell you what actual government overreach looks like."),
    ("kc_13", "CivilianSchool", "kc", "I went to Columbia. I have a law degree. I work at Sullivan & Cromwell. I make more money than you. And you're asking me for papers at my niece's school play."),
    ("kc_14", "CivilianSchool", "kc", "No, I will NOT \"calm down.\" You just spent five minutes speaking gibberish at me because you assumed I don't speak English. I'm from QUEENS."),
    # Officer Mandarin (om) - OfficerDueProcess
    ("om_01", "OfficerDueProcess", "om", "Okay, ni hao. Ni hao. Can you understand me? Wo shi... ICE officer."),
    ("om_02", "OfficerDueProcess", "om", "Qing... uh... show me... gei wo kan... your papers? Ni de... paperwork?"),
    ("om_03", "OfficerDueProcess", "om", "I know you understand me. I took two years of Mandarin at UVA. Just cooperate, okay? Wo... wo yao... help you."),
    ("om_04", "OfficerDueProcess", "om", "Look, I'm trying to be culturally sensitive here. Most guys would just yell at you. I'm meeting you halfway."),
    ("om_05", "OfficerDueProcess", "om", "Ni shi... illegal? Ni you... green card? Wei shen me... you don't talk?"),
    ("om_06", "OfficerDueProcess", "om", "Why are you being difficult? I'm speaking YOUR language."),
    ("om_07", "OfficerDueProcess", "om", "Fine. Fine. You want to play it that way. I'll get the translator. But I KNOW you understand me."),
    ("om_08", "OfficerDueProcess", "om", "Dui bu qi, but I don't believe you. You people always pretend not to understand."),
    ("om_09", "OfficerDueProcess", "om", "I spent $200,000 on my education. I took Chinese. I know what I'm saying."),
    # Carmen Reyes (cr) - CivilianTaco
    ("cr_01", "CivilianTaco", "cr", "Excuse me? EXCUSE ME? You want to see MY papers?"),
    ("cr_02", "CivilianTaco", "cr", "I'm Puerto Rican, pendejo! PUERTO RICAN! You know what that means?"),
    ("cr_03", "CivilianTaco", "cr", "It means I'm American! Born American! My GRANDMOTHER was born American! In 1917!"),
    ("cr_04", "CivilianTaco", "cr", "You want my papers? Here's my papers! It's called the Jones Act! Google it!"),
    ("cr_05", "CivilianTaco", "cr", "Puerto Rico is part of the United States! Did they not teach you geography?!"),
    ("cr_06", "CivilianTaco", "cr", "I don't need a passport! I don't need a green card! I don't need NOTHING from you!"),
    ("cr_07", "CivilianTaco", "cr", "You know what I need? I need my LUNCH! Which you are INTERRUPTING!"),
    ("cr_08", "CivilianTaco", "cr", "This is what happens when you elect a puto! A PUTO! You know what that means?!"),
    ("cr_09", "CivilianTaco", "cr", "My brother served in Iraq! My father served in Vietnam! For THIS country! And you're asking ME for papers?!"),
    ("cr_10", "CivilianTaco", "cr", "We've been citizens since 1917! NINETEEN SEVENTEEN! Before your grandfather was BORN!"),
    ("cr_11", "CivilianTaco", "cr", "You threw paper towels at us after Maria! Paper towels! And now you want ME to show YOU papers?!"),
    ("cr_12", "CivilianTaco", "cr", "You don't even know where Puerto Rico IS, do you? DO YOU?!"),
    ("cr_13", "CivilianTaco", "cr", "It's not Mexico! It's not Cuba! It's AMERICA! With no voting rights! Which is ANOTHER conversation!"),
    ("cr_13b", "CivilianTaco", "cr", "You know what's funny? Your President doesn't even know he's MY President too! He has NO IDEA he's President of Puerto Rico!"),
    ("cr_14", "CivilianTaco", "cr", "Call your supervisor! Call the President! Call whoever you want! I'm not going ANYWHERE!"),
    ("cr_15", "CivilianTaco", "cr", "Actually, you know what? Deport me to Puerto Rico! DO IT! See what happens! I'LL STILL BE IN AMERICA!"),
    ("cr_16", "CivilianTaco", "cr", "Mira, I pay federal taxes! I can't vote for President, but I pay taxes! And THIS is what I get?!"),
    ("cr_17", "CivilianTaco", "cr", "Un puto. Un puto in the White House. And now his pendejos are asking ME for papers. Increíble."),
    ("cr_18", "CivilianTaco", "cr", "You want my Social Security card? HERE! You want my birth certificate? It says SAN JUAN! Which is in AMERICA!"),
    ("cr_19", "CivilianTaco", "cr", "I'm done. I'm DONE. Give me my tacos. I'm going back to work. Some of us have JOBS."),
]

TEMPLATE = """[{obj}]
ClassName=Class'IGSoundEffectsSubsystem.StreamSoundEffectSpecification'
Precache=false
Streams={folder}/{obj}.ogg
Volume=100
AISoundRadius=0
SoundCategory=
Caption={caption}
Speaker={speaker}
OuterRadius=1500
InnerRadius=0
Delay=0
Monoloop=(Min=-1,Max=-1)
PolyLoop=(PolyLoopRange=(Min=-1,Max=-1),LoopSoundLimit=0)
LoopCount=0
Local=False
NoRepeat=False
NeverRepeat=False
PlayOnce=False
Killable=False
MonoPhonic=1
MonoPhonicPriority=2
MonophonicToClass=False
Priority=1
PitchRange=(Min=0,Max=0)
PanRange=(Min=0,Max=0)
FadeInTime=0
FadeOutTime=0
Retriggerable=True
VolumeCategory=VOL_Voice

"""

def main():
    out = []
    out.append("; === DUE PROCESS: Custom character voice lines ===\n")
    for obj, folder, speaker, caption in LINES:
        out.append(TEMPLATE.format(obj=obj, folder=folder, speaker=speaker, caption=caption))
    print("".join(out))

if __name__ == "__main__":
    main()
