from syllable_splitter import split_syllables

def detect_meter(text):

    syllables = split_syllables(text)

    count = len(syllables)

    if count == 8:
        return "Anushtubh"

    elif count == 11:
        return "Trishtubh"

    elif count == 12:
        return "Jagati"

    else:
        return "Unknown Meter"   
