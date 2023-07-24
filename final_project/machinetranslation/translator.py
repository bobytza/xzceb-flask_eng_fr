""" Translator English-French """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ Translate from English to French """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """ Translate from French to English """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
