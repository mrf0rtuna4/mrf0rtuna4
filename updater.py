from googletrans import Translator
import os

def read_readme():
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()

def update_localizations():
    readme_content = read_readme()
    translator = Translator()

    src_lang = translator.detect(readme_content).lang

    languages = ['ru', 'fr', 'es']  
    for lang in languages:
        if lang != src_lang:
            translated_content = translator.translate(readme_content, src=src_lang, dest=lang).text
            with open(f"locales/{lang}.md", "w", encoding="utf-8") as file:
                file.write(translated_content)
            print(f"Localization for {lang} updated.")

update_localizations()
