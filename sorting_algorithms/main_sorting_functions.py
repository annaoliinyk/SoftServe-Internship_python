import generate_list
import insertion_sort
import merge_sort

LIST_TO_SORT = generate_list.generate_list(length=8)


def main():
    print(f"List to sort: {LIST_TO_SORT}")
    print("\nMerge sort:")
    merge_sort.merge_sort(list_to_sort=LIST_TO_SORT)
    print(f"\n\nList to sort: {LIST_TO_SORT}")
    print("\nInsertion sort:")
    insertion_sort.insertion_sort(list_to_sort=LIST_TO_SORT)


if __name__ == "__main__":
    main()
