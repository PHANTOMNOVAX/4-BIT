import re


VOWELS = "अआइईउऊऋॠऌएऐओऔ"


def split_syllables(text):

    text = re.sub(r"[^\u0900-\u097F]", "", text)

    syllables = []

    current = ""

    for char in text:

        current += char

        if char in VOWELS:

            syllables.append(current)

            current = ""

    if current:
        syllables.append(current)

    return syllables
