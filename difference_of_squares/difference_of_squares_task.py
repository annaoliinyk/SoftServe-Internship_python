# Task from https://exercism.org/tracks/python/exercises/difference-of-squares

def square_of_sum(number):
    sum = 0
    for n in range(1, number + 1):
        sum += n
    return pow(sum, 2)


def sum_of_squares(number):
    sum_of_squares = 0
    for n in range(1, number + 1):
        sum_of_squares += n * n
    return sum_of_squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
