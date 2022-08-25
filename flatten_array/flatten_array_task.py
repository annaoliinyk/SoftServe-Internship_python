# Task from https://exercism.org/tracks/python/exercises/flatten-array

def flatten(iterable):
    result = []
    convert_list(iterable, result)
    return result


def convert_list(iterable, result=[]):
    for item in iterable:
        if not item:
            continue
        elif type(item) == list:
            convert_list(item, result)
        else:
            result.append(item)
    return result
