from syllable_splitter import split_syllables

def detect_meter(text):

    lines = text.split("\n")

    syllable_counts = []

    for line in lines:
        syllables = split_syllables(line)
        syllable_counts.append(len(syllables))

    avg = sum(syllable_counts) / len(syllable_counts)

    if avg <= 8:
        return "Anushtubh (8 syllables per line)"

    elif avg <= 11:
        return "Trishtubh (11 syllables per line)"

    elif avg <= 12:
        return "Jagati (12 syllables per line)"

    else:
        return "Unknown Meter"
