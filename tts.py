from gtts import gTTS
import os
import re


OUTPUT = "static/audio/output.mp3"


def improve_pronunciation(text):
    """
    Adjust Sanskrit phonetics for clearer Indian-style chanting
    """

    replacements = {

        "ः": "aha",
        "ं": "am",
        "ण": "na",
        "ञ": "nya",
        "त्र": "tra",
        "ज्ञ": "gya",
        "श्र": "shra",

        "क": "ka",
        "ख": "kha",
        "ग": "ga",
        "घ": "gha",

        "च": "cha",
        "ज": "ja",

        "ट": "ta",
        "ठ": "tha",
        "ड": "da",
        "ढ": "dha",

        "त": "ta",
        "थ": "tha",
        "द": "da",
        "ध": "dha",

        "प": "pa",
        "फ": "pha",
        "ब": "ba",
        "भ": "bha",

        "श": "sha",
        "ष": "sha",
        "स": "sa",

        "अ": "a",
        "आ": "aa",
        "इ": "i",
        "ई": "ee",
        "उ": "u",
        "ऊ": "oo",
        "ए": "e",
        "ऐ": "ai",
        "ओ": "o",
        "औ": "au"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


def split_for_rhythm(text):

    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")

    return text


def generate_audio(text, meter=""):

    text = split_for_rhythm(text)

    phonetic_text = improve_pronunciation(text)

    tts = gTTS(
        phonetic_text,
        lang="en", tld="co.in",
        slow=False
    )

    if not os.path.exists("static/audio"):
        os.makedirs("static/audio")

    tts.save(OUTPUT)

    return "/" + OUTPUT
