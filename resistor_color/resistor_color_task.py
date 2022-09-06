# Task from https://exercism.org/tracks/python/exercises/resistor-color

switch = {
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

colors_list = list(switch.keys())


def color_code(color):
    return switch.get(color)


def colors():
    return colors_list


def main():
    print(color_code("black"))
    print(color_code("white"))
    print(color_code("orange"))
    print(colors())


if __name__ == "__main__":
    main()
