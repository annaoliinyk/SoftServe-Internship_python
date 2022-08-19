# Task from https://exercism.org/tracks/python/exercises/bob

import re


def response(hey_bob):
    if hey_bob.strip() == "":
        return 'Fine. Be that way!'

    elif hey_bob.rstrip()[-1] is '?':
        if hey_bob != hey_bob.upper():
            return 'Sure.'
        elif hey_bob != hey_bob.lower():
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Sure.'

    elif hey_bob != hey_bob.lower() and hey_bob == hey_bob.upper():
        return 'Whoa, chill out!'

    else:
        return 'Whatever.'
