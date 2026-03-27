from gtts import gTTS

def generate_audio(text):

    filename = "static/audio/output.mp3"

    try:
        tts = gTTS(text=text, lang="hi")
        tts.save(filename)
    except:
        # fallback if no internet
        with open(filename, "wb") as f:
            f.write(b"")

    return filename
