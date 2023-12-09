from transformers import MarianMTModel, MarianTokenizer
import re

def translate_with_curly_brackets(input_text, source_lang, target_lang):
    # Initialize the MarianMT model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate translation
    translation = model.generate(**inputs)

    # Decode the translated tokens
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]

    # Preserve words within curly brackets
    curly_words = re.findall(r'\{([^}]*)\}', input_text)

    # Format only the words that exist in the translated text
    formatted_words = {k: f'{{{k}}}' for k in curly_words if k in translated_text}
    translated_text = translated_text.format(**formatted_words)

    # Print a message for unmatched words
    unmatched_words = set(curly_words) - set(formatted_words)
    if unmatched_words:
        print(f"Warning: Some words within curly brackets were not found in the translation: {unmatched_words}")

    return translated_text

if __name__ == "__main__":
    # Example usage
    source_language = "en"  # Source language code (English)
    target_language = "hi"  # Target language code (Hindi)
    input_text = "Hello, {world}! This is a test."

    translated_text = translate_with_curly_brackets(input_text, source_language, target_language)

    print(f"Input text: {input_text}")
    print(f"Translated text: {translated_text}")
