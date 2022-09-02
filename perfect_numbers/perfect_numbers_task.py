# Task from https://exercism.org/tracks/python/exercises/perfect-numbers

def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    elif number == 1:
        return "deficient"
    else:
        sum = 1
        for n in range(2, number):
            if number % n == 0:
                sum += n

        if sum == number:
            return "perfect"
        elif sum > number:
            return "abundant"
        else:
            return "deficient"
