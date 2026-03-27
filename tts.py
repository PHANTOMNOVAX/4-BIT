from gtts import gTTS

def generate_audio(text):

    filename = "static/audio/output.mp3"

    # fallback pronunciation engine (Hindi supports Sanskrit phonetics well)
    tts = gTTS(text=text, lang="hi")

    tts.save(filename)

    return filename
