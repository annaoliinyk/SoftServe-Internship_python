# Task from https://exercism.org/tracks/python/exercises/resistor-color-duo

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


def value(colors):
    if type(colors) == list:
        if not colors:
            return None
        first_color = colors[0].lower()
        try:
            if len(colors) == 1:
                result = SWITCH.get(first_color)
            else:
                second_color = colors[1].lower()
                # to get two digits result, multiplying first digit by 10:
                result = SWITCH.get(first_color) * 10 + SWITCH.get(second_color)
            return result
        except:
            logging.error("Invalid color provided")
    else:
        logging.error("Invalid input - should be a list")


def main():
    logging.info(value(["red"]))
    logging.info(value("blue"))
    logging.info(value(["green", "white"]))
    logging.info(value(["green", "while"]))
    logging.info(value(["green", "white", "red"]))


if __name__ == "__main__":
    main()
