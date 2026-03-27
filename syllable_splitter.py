def split_syllables(text):

    vowels = "अआइईउऊऋएऐओऔ"

    syllables = []

    current = ""

    for char in text:

        if char == " ":
            continue

        current += char

        if char in vowels:
            syllables.append(current)
            current = ""

    if current:
        syllables.append(current)

    return syllables
