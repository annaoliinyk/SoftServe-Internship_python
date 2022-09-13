# Task from https://exercism.org/tracks/python/exercises/resistor-color
import logging

logging.basicConfig(level=logging.INFO)

SWITCH = {
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


def color_code(color: str):
    try:
        return SWITCH.get(color)
    except:
        logging.error("Invalid input")


# method to list all the existing colors
def get_colors():
    return list(SWITCH.keys())


def main():
    logging.info(color_code("black"))
    logging.info(color_code("white"))
    logging.info(color_code("orange"))
    logging.info(color_code("ivory"))  # error expected
    logging.info(get_colors())


if __name__ == "__main__":
    main()
