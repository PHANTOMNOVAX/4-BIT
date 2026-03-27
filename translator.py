from googletrans import Translator

translator = Translator()

def translate_text(text):
    try:
        translated = translator.translate(text, src='sa', dest='en')
        return translated.text
    except:
        return "Translation temporarily unavailable"
