# translib-o.1
A text translation library designed to rewrite text files with translations, powered by Lingva API, requests, and pathlib.
# 

A lightweight and efficient Python library for text and file translation powered by the **Lingva API**, built using `requests` and `pathlib`.

## 📦 Installation

```bash
pip install git+https://github.com/Spandersss/translib-o.1
```

## 🚀 Functions Overview

### 🔹 `translate(text, to_lang, from_lang='auto')`
Translates a text string and returns the result.
* **`from_lang`**: If not specified, the source language is **automatically detected**.
* **Returns**: `str` (the translated text).

### 🔹 `help()`
Displays a list of **all available languages** and their short codes supported by the API.

### 🔹 `trach(way, lang)`
Translates the content of a file and **overwrites the original file** with the translation.
* **`way`**: Absolute path to the file.
* **`lang`**: Target language code.

### 🔹 `trf(way, lang)`
Translates the content of a file and **returns the result** as a string, leaving the original file untouched.
* **`way`**: Absolute path to the file.
* **`lang`**: Target language code.
* **Returns**: `str` (the translated content).

### 🔹 `mkd(nameofdict, lang, *keys)`
Translates a list of words or phrases (`keys`) and adds them to a specified dictionary where the **key is the original text** and the **value is the translation**.
* **`nameofdict`**: The dictionary variable to update.
* **`lang`**: Target language code.
* **`*keys`**: One or more strings to translate.

---

## 💡 Code Examples

```python
from translib0.1 import translate, help, trach, trf, mkd

# 1. Basic Translation (Auto-detects source language)
text = translate("Привет, как дела?", to_lang="en")
print(text)  # Output: Hello, how are you?

# 2. Show Available Languages
help()

# 3. Translate and Overwrite a File
trach("/absolute/path/to/document.txt", lang="es")

# 4. Translate File and Get the Output String
translated_content = trf("/absolute/path/to/document.txt", lang="fr")
print(translated_content)

# 5. Build a Translation Dictionary
my_dict = {}
mkd(my_dict, "en", "привет", "пока", "яблоко")
print(my_dict)  
# Output: {'привет': 'hello', 'пока': 'goodbye', 'яблоко': 'apple'}
```

## 📄 License
This project is licensed under the MIT License.
