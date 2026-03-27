from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-sa-en"
)

def translate_text(text):

    result = translator(text)

    return result[0]['translation_text']
