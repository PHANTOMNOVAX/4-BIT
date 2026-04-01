from deep_translator import GoogleTranslator
import re


def normalize(text):

    text = text.replace("।", "")
    text = text.replace("॥", "")
    return text.strip()


def split_words(text):

    return re.findall(r'[\u0900-\u097F]+', text)


def translate_text(text):

    text = normalize(text)

    words = split_words(text)

    translated = []

    translator = GoogleTranslator(source="auto", target="en")

    for word in words:

        try:

            result = translator.translate(word)

            translated.append(result)

        except:

            translated.append(word)

    return " ".join(translated)
