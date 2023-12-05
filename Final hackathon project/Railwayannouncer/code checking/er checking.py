from transy import translate_text

input_text = input("enter what you want :")
# # target_language_code = 'es'  # Change this to the language code you want

translated_texth = translate_text(input_text, "hi")
translated_textm = translate_text(input_text, "mr")
# print(translate_text)
if translated_texth:
    print(f"Original Text: {input_text}")
    print(f"hindi : {translated_texth}")
if translated_textm:
    print(f'Marathi : {translated_textm}')