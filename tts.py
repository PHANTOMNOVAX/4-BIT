from gtts import gTTS
import os
import re


OUTPUT_PATH = "static/audio/output.mp3"


def preprocess_text(text):
    """
    Prepare Sanskrit verse for chanting clarity
    """

    text = text.replace("॥", "।")
    text = text.replace("\n", "।")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_padas(text):
    """
    Split verse into chantable padas (metrical segments)
    """

    segments = re.split(r"[।]", text)

    return [seg.strip() for seg in segments if seg.strip()]


def meter_pause(meter):
    """
    Adjust pause timing based on detected meter
    """

    if "Anushtubh" in meter:
        return "... "

    elif "Trishtubh" in meter:
        return ".... "

    elif "Jagati" in meter:
        return "..... "

    else:
        return "... "


def generate_audio(text, meter=""):

    cleaned = preprocess_text(text)

    segments = split_padas(cleaned)

    pause = meter_pause(meter)

    chant_text = ""

    for seg in segments:
        chant_text += seg + pause

    # Hindi phonetics produce best Sanskrit clarity
    tts = gTTS(
        text=chant_text,
        lang="hi",
        slow=True 
    )

    if not os.path.exists("static/audio"):
        os.makedirs("static/audio")

    tts.save(OUTPUT_PATH)

    return "/" + OUTPUT_PATH
