# Task from https://exercism.org/tracks/python/exercises/anagram

def find_anagrams(word, candidates):
    result_list = []
    for candidate in candidates:
        if check_if_sublist(word, candidate):
            result_list.append(candidate)
    return result_list


def check_if_sublist(word, candidate):
    if len(candidate) > len(word) or word.lower() == candidate.lower():
        return False
    else:
        candidate_as_letters_list = list(candidate.lower())
        for letter in word.lower():
            if letter in candidate_as_letters_list:
                candidate_as_letters_list.remove(letter)
            else:
                return False
        return True
