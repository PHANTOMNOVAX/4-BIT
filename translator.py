from googletrans import Translator

translator = Translator()

def translate_text(text):
    translated = translator.translate(text, src='sa', dest='en')
    return translated.text
