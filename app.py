from flask import Flask, render_template, request, redirect, url_for, session
from meter import detect_meter
from translator import translate_text
from tts import generate_audio


app = Flask(__name__)

app.secret_key = "vakya_vani_secret_key"


# HOME PAGE

@app.route("/")
def home():
    return render_template("home.html")


# TRANSLATE PAGE

@app.route("/translate", methods=["GET", "POST"])
def translate():

    if request.method == "POST":

        verse = request.form.get("verse", "").strip()

        if verse:

            session["verse"] = verse

            meter = detect_meter(verse)
            session["meter"] = meter

            translation = translate_text(verse)
            session["translation"] = translation

            audio_path = generate_audio(verse, meter)
            session["audio"] = audio_path

            return redirect(url_for("chant"))

    return render_template("translate.html")


# CHANT PAGE

@app.route("/chant")
def chant():

    verse = session.get("verse", "")
    meter = session.get("meter", "")
    translation = session.get("translation", "")
    audio = session.get("audio", "")

    if verse == "":
        return redirect(url_for("translate"))

    return render_template(
        "chant.html",
        verse=verse,
        meter=meter,
        translation=translation,
        audio=audio
    )


# ABOUT PAGE

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)