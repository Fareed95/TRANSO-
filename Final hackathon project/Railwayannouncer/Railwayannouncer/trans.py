from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

# Example usage:
# input_text = input("enter what you want :")
# # # target_language_code = 'es'  # Change this to the language code you want

# translated_text = translate_text(input_text, "mr")
# # print(translate_text)
# if translated_text:
#     print(f"Original Text: {input_text}")
#     print(f"Translated Text: {translated_text}")
