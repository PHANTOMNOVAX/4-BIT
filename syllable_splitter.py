import re


LONG_VOWELS = ["आ","ई","ऊ","ए","ऐ","ओ","औ","ॠ"]

SHORT_VOWELS = ["अ","इ","उ","ऋ","ऌ"]


def is_long(syllable):

    for v in LONG_VOWELS:

        if v in syllable:
            return True

    if syllable.endswith("ं") or syllable.endswith("ः"):
        return True

    return False


def split_syllables(text):

    pattern = r'[\u0900-\u097F][\u093E-\u094C\u0902\u0903]?'

    return re.findall(pattern, text)


def guru_laghu_pattern(text):

    syllables = split_syllables(text)

    pattern = []

    for s in syllables:

        if is_long(s):

            pattern.append("G")

        else:

            pattern.append("L")

    return syllables, pattern
