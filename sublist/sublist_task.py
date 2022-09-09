# Task from https://exercism.org/tracks/python/exercises/sublist
import logging

logging.basicConfig(level=logging.INFO)


def sublist(list_a, list_b) -> str:
    # condition used to check for input correctness, try/except does not work here
    if type(list_a) == list and type(list_b) == list:
        list_a = sorted(list_a)
        list_b = sorted(list_b)
        if list_a == list_b:
            return "lists are equal"
        elif if_lista_contains_listb(list_a, list_b):
            return "A is a superlist of B"
        # swap lists for method input - check if list b contains list a
        elif if_lista_contains_listb(list_b, list_a):
            return "A is sublist of B"
        else:
            return "lists are unequal"
    else:
        logging.error("invalid input")


# method to check if list provided as 1st argument contains the list provided as 2nd argument
def if_lista_contains_listb(list_a, list_b):
    # iteration through a candidate sublist elements
    for el in list_b:
        # check if element in candidate superlist
        if el in list_a:
            list_a.remove(el)
        # if not - list a isn't a superlist and b isn't a sublist
        else:
            return False
    return True


def main():
    logging.info(sublist("", []))
    logging.info(sublist(["a", "d", "a", "s"], ["a", "a", "a"]))
    logging.info(sublist([1, 3, 5, 6], [3]))
    logging.info(sublist([1, 3, 5, 6], [3, 3]))
    logging.info(sublist([67, 62, 34], [67, 62, 34]))
    logging.info(sublist([67, 62, 34], [67, 62, 34, 1]))
    logging.info(sublist([1, 2, 4], [3, 3, 8, 6]))


if __name__ == "__main__":
    main()
