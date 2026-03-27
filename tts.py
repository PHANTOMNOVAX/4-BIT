from gtts import gTTS
from syllable_splitter import split_syllables
import re


def apply_sanskrit_pronunciation(text):

    # normalize anusvara and visarga spacing
    text = re.sub("ं", "म्", text)
    text = re.sub("ः", "ह्", text)

    return text


def create_chant_pattern(syllables):

    chant_sequence = []

    for index, syllable in enumerate(syllables):

        # simulate udātta emphasis
        if index % 4 == 0:
            chant_sequence.append(syllable.upper())

        # simulate svarita rise
        elif index % 3 == 0:
            chant_sequence.append(syllable + "—")

        else:
            chant_sequence.append(syllable)

    return chant_sequence


def generate_audio(text, meter="Unknown"):

    text = apply_sanskrit_pronunciation(text)

    syllables = split_syllables(text)

    chant_pattern = create_chant_pattern(syllables)

    if "Anushtubh" in meter:
        pause = " ... "

    elif "Trishtubh" in meter:
        pause = " .. "

    elif "Jagati" in meter:
        pause = " .... "

    else:
        pause = " ... "

    chanting_text = pause.join(chant_pattern)

    filename = "static/audio/output.mp3"

    try:

        tts = gTTS(
            text=chanting_text,
            lang="hi",
            slow=True
        )

        tts.save(filename)

    except:
        with open(filename, "wb") as f:
            f.write(b"")

    return filename
