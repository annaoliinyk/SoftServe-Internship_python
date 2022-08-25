# Task from https://exercism.org/tracks/python/exercises/binary-search

def find(search_list, value):
    try:
        return search_list.index(value)
    except ValueError:
        raise ValueError("value not in array")
