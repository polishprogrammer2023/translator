import requests

print("This translator was made using the MyMemory API")
word = input("Input sentence to translate> ")
lang_from = input("Input input language(ISO 639-1)> ")
lang_to = input("Input output language(ISO 639-1)> ")
translation = requests.get(f"https://api.mymemory.translated.net/get?q={word}&langpair={lang_from}|{lang_to}").json()

print(translation["responseData"]["translatedText"])