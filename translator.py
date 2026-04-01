from googletrans import Translator

translator = Translator()


def translate_text(text):

    try:

        translation = translator.translate(text, src="sa", dest="en")

        return translation.text

    except:

        return "Translation unavailable"
