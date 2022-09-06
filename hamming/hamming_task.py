# Task from https://exercism.org/tracks/python/exercises/hamming

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        count_differences = 0
        for letter_a, letter_b in zip(strand_a, strand_b):
            if letter_a != letter_b:
                count_differences += 1
        return count_differences
