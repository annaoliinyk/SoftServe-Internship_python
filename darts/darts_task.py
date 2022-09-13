# Task from https://exercism.org/tracks/python/exercises/darts

def score(x, y):
    if (abs(x) <= 0.75 or abs(y) <= 0.75) and (abs(x) <= 1 and abs(y) <= 1):
        return 10
    elif (abs(x) <= 3.5 or abs(y) <= 3.5) and (abs(x) <= 6 and abs(y) <= 6):
        return 5
    elif (abs(x) <= 7 or abs(y) <= 7) and (abs(x) <= 16 and abs(y) <= 16):
        return 1
    else:
        return 0
