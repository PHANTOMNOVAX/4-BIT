from syllable_splitter import split_syllables


def detect_meter(text):

    # split stanza into lines automatically
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if len(lines) == 1:
        # try splitting by danda punctuation
        lines = text.replace("।", "\n").replace("॥", "\n").split("\n")

    syllable_pattern = []

    for line in lines:

        syllables = split_syllables(line)

        syllable_pattern.append(len(syllables))

    if not syllable_pattern:
        return "Unknown Meter"

    avg = sum(syllable_pattern) / len(syllable_pattern)

    if 7 <= avg <= 9:
        return "Anushtubh (8 syllables per line)"

    elif 10 <= avg <= 12:
        return "Trishtubh (11 syllables per line)"

    elif 12 <= avg <= 14:
        return "Jagati (12 syllables per line)"

    else:
        return f"Unknown Meter (pattern: {syllable_pattern})"
