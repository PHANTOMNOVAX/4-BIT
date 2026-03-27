from googletrans import Translator

translator = Translator()

def translate_text(text):
    try:
        result = translator.translate(text, src='auto', dest='en')
        return result.text
    except:
        return "Translation unavailable (check internet connection)"
