from googletrans import Translator

def translate_text_eng_api(text, target_language='en'):
    translator = Translator()
    
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None


def translate_text_hi_api(text, target_language='hi'):
    translator = Translator()
    
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None


def translate_text_mr_api(text, target_language='mr'):
    translator = Translator()
    
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None
    


