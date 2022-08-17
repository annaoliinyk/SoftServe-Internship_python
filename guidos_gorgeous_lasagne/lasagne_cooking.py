"""Functions used in preparing Guido's gorgeous lasagna.

Task taken from: https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
"""

# defining constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(already_elapsed):
    """Calculate the bake time remaining.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - already_elapsed


def preparation_time_in_minutes(number_of_layers):
    """
    Function to calculate time for each layer preparation.
    provided number of layers, return total time for layers preparation.
    It takes 2 minutes to prepare each layer, so PREPARATION_TIME mean time needed to prepare a single layer
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, already_elapsed):
    """
    Provided number of layers and time lasagne is already cooking for,
    return the total time the lasagne is already cooked for
    """
    return (number_of_layers * PREPARATION_TIME) + already_elapsed

