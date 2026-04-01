from flask import Flask, render_template, request, redirect, url_for, session
import os

from meter import detect_meter
from translator import translate_text
from tts import generate_audio


app = Flask(__name__)

# Secret key for session storage
app.secret_key = "vakya_vani_secret_key"


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("home.html")


# =========================
# TRANSLATION PAGE
# =========================
@app.route("/translate", methods=["GET", "POST"])
def translate():

    if request.method == "POST":

        verse = request.form.get("verse", "").strip()

        if verse:

            # Store verse
            session["verse"] = verse

            # Detect meter
            meter = detect_meter(verse)
            session["meter"] = meter

            # Translate verse
            translation = translate_text(verse)
            session["translation"] = translation

            # Generate chant audio
            audio_file = generate_audio(verse, meter)
            session["audio"] = audio_file

            return redirect(url_for("chant"))

    return render_template("translate.html")


# =========================
# CHANT PAGE
# =========================
@app.route("/chant")
def chant():

    verse = session.get("verse", "")
    meter = session.get("meter", "")
    translation = session.get("translation", "")
    audio = session.get("audio", "")

    # Split verse lines
    lines = verse.split("\n") if verse else []

    return render_template(
        "chant.html",
        lines=lines,
        meter=meter,
        translation=translation,
        audio=audio
    )


# =========================
# ABOUT PAGE
# =========================
@app.route("/about")
def about():
    return render_template("about.html")


# =========================
# SERVER START (Render compatible)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
