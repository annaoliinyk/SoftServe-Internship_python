# Task from https://exercism.org/tracks/python/exercises/sublist

SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif list_two in list_one:
        return SUPERLIST
    elif list_one in list_two:
        return SUBLIST
    else:
        return UNEQUAL
