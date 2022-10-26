def merge_sort(list_to_sort):
    # code assuming length of the list if 8
    counter = 1
    half_1, half_2 = list_to_sort[:4], list_to_sort[4:]
    print(f"Step {counter}: {half_1}, {half_2}")
    counter += 1
    quater_1, quater_2, quater_3, quater_4 = half_1[:2],  half_1[2:], half_2[:2],  half_2[2:]
    print(f"Step {counter}: {quater_1}, {quater_2}, {quater_3}, {quater_4}")
    counter += 1
    # Split into parts:
    p1 = quater_1[0]
    p2 = quater_1[1]
    p3 = quater_2[0]
    p4 = quater_2[1]
    p5 = quater_3[0]
    p6 = quater_3[1]
    p7 = quater_4[0]
    p8 = quater_4[1]
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
        return sorted(part1 + part2)
    return sorted([part1, part2])
