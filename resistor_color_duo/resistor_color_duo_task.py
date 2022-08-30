# Task from https://exercism.org/tracks/python/exercises/resistor-color-duo

def value(colors):
    if not colors:
        return None
    elif len(colors) == 1:
        result = color_value(colors[0].lower())
    else:
        result = color_value(colors[0].lower())
        result *= 10
        result += color_value(colors[1].lower())
    return result


def color_value(color):
    switcher = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return switcher.get(color)
