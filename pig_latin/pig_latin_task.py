consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]


def translate(text):
    if type(text) == str and " " not in text:
        return translate_single_word(text)
    else:
        translated_phrase = ""
        for word in text.split(" "):
            translated_phrase += translate_single_word(word) + " "
        return translated_phrase[:-1]


def translate_single_word(text):
    if text.startswith("xr") or text.startswith("yt"):
        return text + "ay"
    elif text.startswith("qu"):
        return text[2:] + "quay"
    elif text.startswith(tuple(consonants)):
        return translate_starting_with_consonants(text)
    else:
        if not translate_starting_with_consonants(text):
            return text + "ay"
        else:
            return translate_starting_with_consonants(text)


def translate_starting_with_consonants(text):
    translated_text = text
    for letter in text:
        if translated_text.startswith("qu"):
            return translated_text[2:] + "quay"
        elif translated_text[0] in consonants or (text[0] is "y" and translated_text[0] == text[0]):
            translated_text = translated_text[1:] + letter
        else:
            return translated_text + "ay"
