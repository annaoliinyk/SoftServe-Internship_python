# Task from https://exercism.org/tracks/python/exercises/pig-latin
import logging

logging.basicConfig(level=logging.INFO)

VOWEL = ("xr", "yt", "a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")


def translate(text: str):
    try:
        text = text.lower()
        result = ""
        for word in text.split(" "):
            result += translate_single_word(word) + " "
        # return result without extra space
        return result[:-1]
    except:
        logging.error("Invalid input")


def translate_single_word(word):
    # for rule 1
    if word.startswith(VOWEL):
        return word + "ay"
    # for rules 2, 3, 4
    elif word.startswith(CONSONANTS):
        # need to check if there's just one consonant or more; and if it's followed by qu; or followed by y
        return starts_with_consonants(word)
    return word


def starts_with_consonants(word: str):
    result = word
    for letter in word:
        if result.startswith("qu"):
            result = result[2:] + result[:2]
        elif result.startswith(CONSONANTS) or letter is word[0]:
            result = result[1:] + result[0]
    return result + "ay"


def main():
    for word in ["xray", "yttria", "chair", "square", "rhythm", "my", "xray my xray"]:
        logging.info(translate(word))


if __name__ == "__main__":
    main()
