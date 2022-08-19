# Task from https://exercism.org/tracks/python/exercises/isbn-verifier

def is_valid(isbn):
    if '-' in isbn:
        if len(isbn) == 13 and isbn[1] == '-' and isbn[5] == '-' and isbn[11] == '-':
            isbn_digits_only = isbn.replace('-', '')
            return check_if_numberic_or_X(isbn_digits_only)
    else:
        if len(isbn) == 10:
            return check_if_numberic_or_X(isbn)
    return False


def check_if_numberic_or_X(isbn):
    for digit in isbn:
        if digit.isnumeric() or (digit == isbn[-1] and digit is "X"):
            continue
        else:
            return False
    return check_validity_by_formula(isbn)


def check_validity_by_formula(isbn):
    result = 0
    multiplier = 10
    for digit in isbn:
        if digit == 'X':
            digit = 10
        else:
            digit = int(digit)
        result += multiplier * digit
        multiplier -= 1
    return result % 11 == 0
