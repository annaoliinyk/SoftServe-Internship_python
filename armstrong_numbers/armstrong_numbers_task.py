# Task from https://exercism.org/tracks/python/exercises/armstrong-numbers

def is_armstrong_number(number):
    power = len(str(number))
    result = 0
    list_of_digits = convert_number_to_list_digits(number)
    for digit in list_of_digits:
        result += pow(digit, power)
    return result == number


def convert_number_to_list_digits(number):
    str_number = str(number)
    result_list = []
    for symbol in str_number:
        result_list.append(int(symbol))
    return result_list
