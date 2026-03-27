from gtts import gTTS
import os
import re


OUTPUT_FILE = "static/audio/output.mp3"


def preprocess_text(text):
    """
    Clean Sanskrit text for chanting
    """

    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_lines(text):
    """
    Split verse into chanting segments
    """

    parts = text.split(". ")

    return [p.strip() for p in parts if p.strip()]


def generate_audio(text, meter=""):

    cleaned = preprocess_text(text)

    lines = split_lines(cleaned)

    chant_text = ""

    for line in lines:
        chant_text += line + "... "

    # Restore original Hindi chanting voice
    tts = gTTS(
        text=chant_text,
        lang="hi",
        slow=False
    )

    if not os.path.exists("static/audio"):
        os.makedirs("static/audio")

    tts.save(OUTPUT_FILE)

    return "/" + OUTPUT_FILE
