from flask import Flask, render_template, request
from meter import detect_meter
from translator import translate_text
from tts import generate_audio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    meter = None
    translation = None
    audio = None

    if request.method == "POST":

        verse = request.form["verse"]

        meter = detect_meter(verse)

        translation = translate_text(verse)

        audio = generate_audio(verse)

    return render_template(
        "index.html",
        meter=meter,
        translation=translation,
        audio=audio
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
