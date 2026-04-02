import re


def split_syllables(text):

    vowels = "अआइईउऊऋॠऌएऐओऔ"

    syllables = []

    current = ""

    for char in text:

        current += char

        if char in vowels:

            syllables.append(current)

            current = ""

    if current:
        syllables.append(current)

    return syllables
