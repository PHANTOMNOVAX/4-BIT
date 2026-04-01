from deep_translator import GoogleTranslator


def translate_text(text):
    try:
        translation = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        return translation

    except Exception:
        return "Translation unavailable right now."
