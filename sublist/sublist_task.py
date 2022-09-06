# Task from https://exercism.org/tracks/python/exercises/sublist

def sublist(list_a, list_b) -> str:
    if type(list_a) == list and type(list_b) == list:
        list_a = sorted(list_a)
        list_b = sorted(list_b)

        if list_a == list_b:
            return "lists are equal"
        elif set(list_a) >= set(list_b):
            return "A is a superlist of B"
        elif set(list_a) <= set(list_b):
            return "A is sublist of B"
        else:
            return "lists are unequal"

    else:
        return "invalid input"


def main():
    print(sublist("", []))
    print(sublist([1, 3, 5, 6], [3]))
    print(sublist([67, 62, 34], [67, 62, 34]))
    print(sublist([67, 62, 34], [67, 62, 34, 1]))
    print(sublist([1, 2, 4], [3, 3, 8, 6]))


if __name__ == "__main__":
    main()
