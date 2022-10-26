def insertion_sort(list_to_sort):
    counter = 1
    was_changed = True
    tmp_result = list_to_sort
    while was_changed:
        tmp_result, counter, was_changed = iterate_list_once(list_to_sort, tmp_result, counter)
    return tmp_result


def iterate_list_once(list_to_sort, tmp_result, counter):
    was_changed = False
    for i in range(1, len(list_to_sort)):
        if tmp_result[i] < tmp_result[i-1]:
            tmp_value = tmp_result[i]
            tmp_result[i] = tmp_result[i-1]
            tmp_result[i-1] = tmp_value
            was_changed = True
        print(f"Step {counter}: {tmp_result}")
        counter += 1
    return tmp_result, counter, was_changed
