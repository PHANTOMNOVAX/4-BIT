from gtts import gTTS
import os
import uuid
import re


AUDIO_FOLDER = "static/audio"


def preprocess_text(text):
    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_lines(text):
    return [p.strip() for p in text.split(". ") if p.strip()]


def generate_audio(text, meter=""):

    cleaned = preprocess_text(text)
    lines = split_lines(cleaned)

    chant_text = " ... ".join(lines)

    filename = f"chant_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    tts = gTTS(
        text=chant_text,
        lang="hi",
        slow=False
    )

    tts.save(filepath)

    return filename
