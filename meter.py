from syllable_splitter import split_syllables


def clean_lines(text):

    text = text.replace("॥", "\n")
    text = text.replace("।", "\n")

    return [line.strip() for line in text.split("\n") if line.strip()]


def detect_meter(text):

    lines = clean_lines(text)

    if len(lines) < 2:
        return "Not a metrical verse (looks like paragraph text)"

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

    else:
        return f"Unknown Meter (pattern: {syllable_counts})"
