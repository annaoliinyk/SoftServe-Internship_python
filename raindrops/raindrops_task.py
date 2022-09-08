# Task from https://exercism.org/tracks/python/exercises/raindrops

import logging

logging.basicConfig(level=logging.INFO)


def convert(number: int):
    # check the provided input type
    try:
        result = ""
        if number % 3 == 0:
            result += "Pling"
        if number % 5 == 0:
            result += "Plang"
        if number % 7 == 0:
            result += "Plong"
        if not result:
            return str(number)
        return result
    except:
        return logging.error("Invalid input")


def main():
    logging.info(convert(67))
    logging.info(convert(7 * 15))
    logging.info(convert(33))
    logging.info(convert("87"))
    logging.info(convert(-21))


if __name__ == "__main__":
    main()
