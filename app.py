from flask import Flask, render_template, request, redirect, url_for, session

from meter import detect_meter
from translator import translate_text
from tts import generate_audio

app = Flask(__name__)

app.secret_key = "chant_engine_secret"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/translate", methods=["GET", "POST"])
def translate():

    if request.method == "POST":

        verse = request.form.get("verse", "").strip()

        if verse:

            session["verse"] = verse

            session["meter"] = detect_meter(verse)

            session["translation"] = translate_text(verse)

            session["audio"] = generate_audio(
                verse,
                session["meter"]
            )

            return redirect(url_for("chant"))

    return render_template("translate.html")


@app.route("/chant")
def chant():

    verse = session.get("verse", "")

    meter = session.get("meter", "")

    translation = session.get("translation", "")

    audio = session.get("audio", "")

    lines = verse.split("\n") if verse else []

    return render_template(
        "chant.html",
        lines=lines,
        meter=meter,
        translation=translation,
        audio=audio
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
