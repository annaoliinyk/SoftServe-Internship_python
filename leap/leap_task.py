# Task from https://exercism.org/tracks/python/exercises/leap
import logging

logging.basicConfig(level=logging.INFO)


def leap_year(year):
    try:
        return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)
    except:
        logging.error("Invalid input")


def main():
    logging.info(leap_year(1996))
    logging.info(leap_year(2000))
    logging.info(leap_year(1997))
    logging.info(leap_year("1430"))


if __name__ == "__main__":
    main()
