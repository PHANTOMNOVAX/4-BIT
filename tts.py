from gtts import gTTS
from syllable_splitter import split_syllables
import time

def generate_audio(text):

    syllables = split_syllables(text)

    rhythmic_text = " ".join(syllables)

    filename = "static/audio/output.mp3"

    try:
        tts = gTTS(text=rhythmic_text, lang="hi", slow=True)
        tts.save(filename)

    except:
        with open(filename, "wb") as f:
            f.write(b"")

    return filename
