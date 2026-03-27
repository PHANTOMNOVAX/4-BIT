from flask import Flask, render_template, request

from meter import detect_meter
from translator import translate_text
from tts import generate_audio

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():

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
        "translate.html",
        meter=meter,
        translation=translation,
        audio=audio,
        lines=lines
    )


@app.route("/chant")
def chant():
    return render_template("chant.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
