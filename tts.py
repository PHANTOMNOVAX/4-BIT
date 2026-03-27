from gtts import gTTS
import os
import re


AUDIO_PATH = "static/audio/output.mp3"


def clean_text(text):
    """
    Prepare Sanskrit text for better chanting rhythm
    """

    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_for_chanting(text):
    """
    Split verse into chantable segments
    """

    lines = re.split(r"[।॥]", text)

    return [line.strip() for line in lines if line.strip()]


def generate_audio(text, meter=""):

    text = clean_text(text)

    chant_lines = split_for_chanting(text)

    chant_text = ""

    for line in chant_lines:
        chant_text += line + "... "

    # Hindi voice gives best Sanskrit phonetics in gTTS
    tts = gTTS(
        text=chant_text,
        lang="hi",
        slow=False
    )

    if not os.path.exists("static/audio"):
        os.makedirs("static/audio")

    tts.save(AUDIO_PATH)

    return "/" + AUDIO_PATH
