def print_list_elements(list1):
    print("List elements are:")
    for el in list1:
        print(el)
    print()


def convert_list_to_set(list1):
    return set(list1)


def concatenate_two_lists(list1, list2):
    return list1 + list2


def main():
    list1 = [1, 2, 3]
    list2 = [5, 2, 1, 6, 1, "i"]
    convert_list_to_set(list1)
    print(convert_list_to_set(list2))
    print(concatenate_two_lists(list1, list2))


if __name__ == "__main__":
    main()
