from gtts import gTTS
import os
import uuid
import re


AUDIO_FOLDER="static/audio"


def preprocess_text(text):

    text=text.replace("॥",". ")
    text=text.replace("।",". ")

    text=re.sub(r"\s+"," ",text)

    return text.strip()


def generate_audio(text,meter=""):

    filename=f"chant_{uuid.uuid4().hex}.mp3"

    filepath=os.path.join(AUDIO_FOLDER,filename)

    os.makedirs(AUDIO_FOLDER,exist_ok=True)

    tts=gTTS(text=text,lang="hi",slow=False)

    tts.save(filepath)

    return filename
