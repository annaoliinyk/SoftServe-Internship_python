# Task from https://exercism.org/tracks/python/exercises/matching-brackets

def is_paired(input_string):
    number_of_braces_dict = {"[": input_string.count("["),
                             "]": input_string.count("]"),
                             "{": input_string.count("{"),
                             "}": input_string.count("}"),
                             "(": input_string.count("("),
                             ")": input_string.count(")"),
                             }
    return check_number_of_brackets(number_of_braces_dict) and check_the_order(input_string)


def check_number_of_brackets(number_of_braces_dict):
    number_of_brackets_is_equal = number_of_braces_dict["["] == number_of_braces_dict["]"]
    number_of_braces_is_equal = number_of_braces_dict["{"] == number_of_braces_dict["}"]
    number_of_parentheses_is_equal = number_of_braces_dict["("] == number_of_braces_dict[")"]
    return number_of_brackets_is_equal and number_of_braces_is_equal and number_of_parentheses_is_equal


def check_the_order(input_string):
    input_string = input_string.replace(" ", "")
    input_string_as_list = list(input_string)
    check_brackets_order, check_braces_order, check_parentheses_order = True, True, True
    begin_brackets, begin_braces, begin_parentheses = 0, 0, 0
    end_brackets, end_braces, end_parentheses = len(input_string), len(input_string), len(input_string)
    # check if indexes of begin brackets match the indexes of end brackets for all pairs: [], {}, ()

    if "[" in input_string_as_list:
        begin_brackets = input_string_as_list.index("[")
        end_brackets = input_string_as_list.index("]")
        check_brackets_order = begin_brackets < end_brackets

    if "{" in input_string_as_list:
        begin_braces = input_string_as_list.index("{")
        end_braces = input_string_as_list.index("}")
        check_braces_order = begin_braces < end_braces

    if "(" in input_string_as_list:
        begin_parentheses = input_string_as_list.index("(")
        end_parentheses = input_string_as_list.index(")")
        check_parentheses_order = begin_parentheses < end_parentheses
    # check if the order of brackets is correct:
    if input_string.startswith("["):
        if begin_braces != 0:
            if end_brackets < end_braces and begin_brackets < begin_braces:
                return False
        if begin_parentheses != 0:
            if end_brackets < end_parentheses and begin_brackets > begin_parentheses:
                return False
    elif input_string.startswith("{"):
        if begin_brackets != 0:
            if end_braces < end_brackets and begin_braces > begin_brackets:
                return False
        if begin_parentheses != 0:
            if end_braces < end_parentheses and begin_braces < begin_parentheses:
                return False

    elif input_string.startswith("("):
        if begin_braces != 0:
            if end_parentheses < end_braces and begin_parentheses > begin_braces:
                return False
        if begin_brackets != 0:
            if end_parentheses < end_brackets and begin_parentheses > begin_brackets:
                return False
    # return the result of both the indexes and order correctness
    return check_brackets_order and check_braces_order and check_parentheses_order
