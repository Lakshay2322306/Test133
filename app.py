import asyncio
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Async function to translate text
async def translate_text(text, src_lang='auto', dest_lang='en'):
    try:
        # Translate the text (await the coroutine)
        translation = await translator.translate(text, src=src_lang, dest=dest_lang)
        return {
            'original': text,
            'translated': translation.text,
            'source_language': translation.src,
            'destination_language': translation.dest
        }
    except Exception as e:
        return f"Error: {str(e)}"

# Async function to handle multiple translations
async def run_translations(text, dest_langs):
    results = []
    for dest_lang in dest_langs:
        result = await translate_text(text, dest_lang=dest_lang)
        results.append((dest_lang, result))
    return results

# Main function to execute translations
def main():
    # Sample text to translate
    text = "Bonjour, comment vas-tu?"
    
    # List of destination languages
    dest_langs = ['en', 'es']
    
    # Run all translations in a single event loop
    results = asyncio.run(run_translations(text, dest_langs))
    
    # Process results
    for dest_lang, result in results:
        print(f"\nTranslation to {LANGUAGES[dest_lang].capitalize()}:")
        if isinstance(result, str):
            print(f"Translation failed: {result}")
        else:
            print(f"Original: {result['original']}")
            print(f"Translated: {result['translated']}")
            print(f"Source Language: {result['source_language']}")
            print(f"Destination Language: {result['destination_language']}")

    # Display all supported languages
    print("\nSupported Languages:")
    for lang_code, lang_name in sorted(LANGUAGES.items()):
        print(f"{lang_code}: {lang_name}")

# Example usage
if __name__ == "__main__":
    main()
