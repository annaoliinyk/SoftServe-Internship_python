# Task from https://exercism.org/tracks/python/exercises/grains

def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    result = 1
    for n in range(1, number):
        result *= 2
    return result


def total():
    total_number = 0
    for n in range(1, 65):
        total_number += square(n)
    return total_number
