# Task from https://exercism.org/tracks/python/exercises/list-ops

def append(list1, list2):
    result = list1
    for element in list2:
        result.append(element)
    return result


def concat(lists):
    result = []
    for list in lists:
        for element in list:
            result.append(element)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    length = 0
    for item in list:
        length += 1
    return length


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    result = initial
    for item in list:
        result += function(item, 0)
    return result


def foldr(function, list, initial):
    result = initial
    if list:
        if type(list[0]) == int:
            temporary_result = 0
        else:
            temporary_result = ""
        for item in list:
            temporary_result = function(temporary_result, item)
        result = temporary_result + initial
    return result


def reverse(list):
    result = []
    for item in list:
        result.insert(0, item)
    return result
