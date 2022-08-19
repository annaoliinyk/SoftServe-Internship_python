# Task from https://exercism.org/tracks/python/exercises/pangram

def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
