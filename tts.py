from gtts import gTTS
import os
import uuid
import re


def preprocess_text(text):

    text = text.replace("॥", ". ")
    text = text.replace("।", ". ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def generate_audio(text, meter=""):

    cleaned = preprocess_text(text)

    filename = f"chant_{uuid.uuid4().hex}.mp3"

    audio_folder = "static/audio"

    os.makedirs(audio_folder, exist_ok=True)

    filepath = os.path.join(audio_folder, filename)

    tts = gTTS(text=cleaned, lang="hi")

    tts.save(filepath)

    return "audio/" + filename
