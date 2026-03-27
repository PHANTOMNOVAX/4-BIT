from syllable_splitter import split_syllables


def detect_meter(text):

    lines = text.replace("॥", "\n").split("\n")

    lines = [l.strip() for l in lines if l.strip()]

    if len(lines) < 2:
        return "Prose (not a metrical verse)"

    syllable_counts = []

    for line in lines:
        syllables = split_syllables(line)
        syllable_counts.append(len(syllables))

    avg = sum(syllable_counts) / len(syllable_counts)

    if 7 <= avg <= 9:
        return f"Anushtubh Meter (pattern: {syllable_counts})"

    elif 10 <= avg <= 12:
        return f"Trishtubh Meter (pattern: {syllable_counts})"

    elif 12 <= avg <= 14:
        return f"Jagati Meter (pattern: {syllable_counts})"

    return f"Unknown Meter (pattern: {syllable_counts})"
