from syllable_splitter import split_syllables


def detect_meter(text):

    lines = text.replace("॥", "\n").replace("।", "\n").split("\n")

    lines = [l.strip() for l in lines if l.strip()]

    if len(lines) < 2:
        return "Prose (not a metrical verse)"

    counts = []

    for line in lines:

        syllables = split_syllables(line)

        counts.append(len(syllables))

    if all(7 <= c <= 9 for c in counts):

        return f"Anushtubh Meter (pattern: {counts})"

    elif all(10 <= c <= 12 for c in counts):

        return f"Trishtubh Meter (pattern: {counts})"

    elif all(12 <= c <= 14 for c in counts):

        return f"Jagati Meter (pattern: {counts})"

    return f"Unknown Meter (pattern: {counts})"
