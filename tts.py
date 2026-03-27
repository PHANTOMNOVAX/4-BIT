from gtts import gTTS

def generate_audio(text):

    filename = "static/audio/output.mp3"

    tts = gTTS(text=text, lang="sa")

    tts.save(filename)

    return filename
