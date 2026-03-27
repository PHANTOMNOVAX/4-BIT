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
    lines = None

    if request.method == "POST":

        verse = request.form.get("verse", "").strip()

        if verse:

            lines = verse.split("\n")

            meter = detect_meter(verse)

            translation = translate_text(verse)

            audio = generate_audio(verse, meter)

    return render_template(
        "index.html",
        meter=meter,
        translation=translation,
        audio=audio,
        lines=lines
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
