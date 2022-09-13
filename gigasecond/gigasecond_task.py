# Task from https://exercism.org/tracks/python/exercises/gigasecond
from datetime import datetime, timedelta


def add(moment):
    return moment + timedelta(seconds=1000000000)
