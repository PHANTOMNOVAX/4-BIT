def split_syllables(text):

    vowels = "अआइईउऊएऐओऔ"

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
