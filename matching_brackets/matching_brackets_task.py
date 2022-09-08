# Task from https://exercism.org/tracks/python/exercises/matching-brackets
import logging

logging.basicConfig(level=logging.INFO)

BEGINNING_BRACKETS = ["(", "[", "{"]
ENDING_BRACKETS = [")", "]", "}"]


def is_paired_and_nested(input_string: str) -> bool:
    try:
        return are_paired(input_string) and are_nested(input_string)
    except:
        logging.error("Invalid input")


# the method is used to check if number of beginning and ending brackets is same (counter == 0 if yes)
def are_paired(input_string) -> bool:
    # declare counters for [], {} and () accordingly;
    # count number of begin brackets and subtract number of ending brackets
    brackets_counter = input_string.count("[") - input_string.count("]")
    braces_counter = input_string.count("{") - input_string.count("}")
    parentheses_counter = input_string.count("(") - input_string.count(")")
    return brackets_counter == 0 and braces_counter == 0 and parentheses_counter == 0


# method checking if nested correctly - if order is correct
def are_nested(input_string) -> bool:
    # idea is to give each type of brackets a value 1-3 depending on their position in a BEGINNING_BRACKETS
    # those values will be stored here:
    tmp_result_list = []
    try:
        for el in input_string:
            # case 1: element is {, ( or [
            if el in BEGINNING_BRACKETS:
                # el_value for value of an element as explained above
                el_value = BEGINNING_BRACKETS.index(el) + 1
                tmp_result_list.append(el_value)
            # case 2: element isn't a bracket, so will ignore it
            elif el not in BEGINNING_BRACKETS and el not in ENDING_BRACKETS:
                continue
            # case 3: element is }, ) or ] and its value is the same as the last element in list with values -
            # previous element was a beginning bracket from the pair
            elif el in ENDING_BRACKETS and tmp_result_list[-1] == ENDING_BRACKETS.index(el) + 1:
                tmp_result_list.pop()
            # in other cases brackets are not nested
            else:
                return False
        return tmp_result_list == []
    except:
        # return False instead of error in case input_string starts with ending bracket ), } or ]
        return False


def main():
    logging.info(is_paired_and_nested(8))  # expecting an error
    logging.info(is_paired_and_nested("[]"))  # True
    logging.info(is_paired_and_nested("[](())"))  # True
    logging.info(is_paired_and_nested("[]("))  # False
    logging.info(is_paired_and_nested("[}{]"))  # False
    logging.info(is_paired_and_nested("[({]})"))  # False
    logging.info(is_paired_and_nested("}[({]{})"))  # False


if __name__ == "__main__":
    main()
