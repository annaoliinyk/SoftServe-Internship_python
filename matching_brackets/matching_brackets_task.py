# Task from https://exercism.org/tracks/python/exercises/matching-brackets
import logging

logging.basicConfig(level=logging.INFO)


def is_paired(input_string):
    brackets_counter, braces_counter, parentheses_counter = get_brackets_counters(input_string)
    return brackets_counter == 0 and braces_counter == 0 and parentheses_counter == 0


# the method is used to check if number of beginning and ending brackets is same (counter == 0 if yes)
def get_brackets_counters(input_string):
    # declare counters for [], {} and () accordingly;
    # count number of begin brackets and subtract number of ending brackets
    brackets_counter = input_string.count("[") - input_string.count("]")
    braces_counter = input_string.count("{") - input_string.count("}")
    parentheses_counter = input_string.count("(") - input_string.count(")")
    return brackets_counter, braces_counter, parentheses_counter


# TODO: add method checking if nested correctly - if order is correct

def main():
    logging.info(8)
    logging.info(is_paired("[](())"))  # True
    logging.info(is_paired("[]("))  # False
    logging.info(is_paired("[}{]"))  # False
    logging.info(is_paired("[({]})"))  # False


if __name__ == "__main__":
    main()
