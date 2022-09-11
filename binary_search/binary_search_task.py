# Task from https://exercism.org/tracks/python/exercises/binary-search
import logging

logging.basicConfig(level=logging.INFO)


def find(search_list: list, value):
    try:
        return search_list.index(value)
    except ValueError:
        # the task says to raise an error:
        # raise ValueError("value not in array")
        # will show logging error instead:
        logging.error("value not in array")
    except:
        logging.error("Incorrect input")


def main():
    logging.info(find([6], 6))
    logging.info(find([1, 3, 4, 6, 8, 9, 11], 1))
    logging.info(find([1, 2], 0))
    logging.info(find(1, [1, 2]))


if __name__ == "__main__":
    main()
