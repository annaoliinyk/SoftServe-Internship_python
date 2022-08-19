# Task from https://exercism.org/tracks/python/exercises/isogram

def is_isogram(string):
    string = string.lower()
    letters_in_string_list = []
    for letter in string:
        if letter not in letters_in_string_list and letter not in [' ', '-']:
            letters_in_string_list += letter
        elif letter not in [' ', '-']:
            return False
    return True
