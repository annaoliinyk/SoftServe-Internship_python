# Task from https://exercism.org/tracks/python/exercises/sublist

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return 3
    elif check_if_sublist(list_two, list_one):
        return 1
    elif check_if_sublist(list_one, list_two):
        return 2
    else:
        return 4


def check_if_sublist(full_list, sub_list):
    sub_list_as_str = convert_int_list_to_str(sub_list)
    full_list_as_str = convert_int_list_to_str(full_list)

    return sub_list_as_str in full_list_as_str and check_if_all_items_in_full_list(full_list, sub_list)


def convert_int_list_to_str(integers_list):
    result = ''
    for integer in integers_list:
        result += str(integer) + " "
    return result


def check_if_all_items_in_full_list(full_list, sub_list):
    for item in sub_list:
        if item not in full_list:
            return False
    return True
