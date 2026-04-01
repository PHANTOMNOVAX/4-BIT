from gtts import gTTS
import os
import re

OUTPUT_FILE = "audio/output.mp3"


def preprocess_text(text):

    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_lines(text):

    parts = text.split(". ")

    return [p.strip() for p in parts if p.strip()]


def generate_audio(text, meter=""):

    cleaned = preprocess_text(text)

    lines = split_lines(cleaned)

    chant_text = ""

    for line in lines:
        chant_text += line + "... "

    tts = gTTS(
        text=chant_text,
        lang="hi",
        slow=False
    )

    audio_path = os.path.join("static", "audio")

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    full_file = os.path.join(audio_path, "output.mp3")

    tts.save(full_file)

    return "audio/output.mp3"
