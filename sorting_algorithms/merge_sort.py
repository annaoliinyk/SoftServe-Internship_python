import math

def merge_sort(list_to_sort):
    # code assuming length of the list if 8
    counter = 1
    for i in range(int(math.log(len(list_to_sort), 2))):
        half_1, half_2 = slice_list(list_to_sort)
        print(f"Step {counter}: {half_1}, {half_2}")
        counter += 1
        quater_1, quater_2 = slice_list(half_1)
        quater_3, quater_4 = slice_list(half_2)
        print(f"Step {counter}: {quater_1}, {quater_2}, {quater_3}, {quater_4}")
        counter += 1
        # Split into parts:
        p1, p2 = slice_list(quater_1)
        p3, p4 = slice_list(quater_2)
        p5, p6 = slice_list(quater_3)
        p7, p8 = slice_list(quater_4)
        print(f"Step {counter}: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}, {p7}, {p8}")
        counter += 1
    sorted_quater_1, sorted_quater_2 = connect_parts(p1, p2), connect_parts(p3, p4)
    sorted_quater_3, sorted_quater_4 = connect_parts(p5, p6), connect_parts(p7, p8)
    print(f"Step {counter}: {sorted_quater_1}, {sorted_quater_2}, {sorted_quater_3}, {sorted_quater_4}")
    counter += 1
    sorted_half_1, sorted_half_2 = connect_parts(sorted_quater_1, sorted_quater_2), connect_parts(sorted_quater_3,
                                                                                                  sorted_quater_4)
    print(f"Step {counter}: {sorted_half_1}, {sorted_half_2}")
    counter += 1
    sorted_list = connect_parts(sorted_half_1, sorted_half_2)
    print(f"Step {counter}: {sorted_list}")


def connect_parts(part1, part2):
    if type(part1) == list and type(part2) == list:
        return merge_lists_sorted(part1, part2)
    elif part1 < part2:
        return [part1, part2]
    else:
        return [part2, part1]


def merge_lists_sorted(list1, list2):
    result = []
    for item1, item2 in map(list1, list2):
        if item1 < item2:
            result += [item1, item2]
        else:
            result += [item2, item1]
    return result


def slice_list(list_to_slice):
    slice_obj = slice(0, len(list_to_slice) // 2)
    part_1 = list_to_slice[slice_obj]
    part_2 = list_to_slice - part_1
    return part_1, part_2
