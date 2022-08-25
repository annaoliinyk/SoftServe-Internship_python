# Task taken from https://exercism.org/tracks/python/exercises/acronym

def abbreviate(words):
    result = ""
    words_as_list = split_phrase_into_list_words(words)
    for word in words_as_list:
        result += word[0].upper()
    return result


def split_phrase_into_list_words(phrase):
    phrase = phrase.replace("-", " ")
    phrase = phrase.replace("_", " ")
    phrase = phrase.replace("   ", " ")
    phrase = phrase.replace("  ", " ")

    return phrase.split(" ")
