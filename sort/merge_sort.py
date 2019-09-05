
def pair_sort(array, left_bound, right_bound):
    if right_bound - left_bound > 1:
        raise RuntimeError("Error! You are trying to use pair_sort for array with size not equal 2.")
    if array[left_bound] > array[right_bound]:
        temp = array[left_bound]
        array[left_bound] = array[right_bound]
        array[right_bound] = temp


def simplest_merge(array, first_part_begin, second_part_begin, second_part_end, buffer=None):
    if buffer is None:
        buffer = [0] * (second_part_begin - first_part_begin)
    elif len(buffer) < second_part_begin - first_part_begin:
        raise RuntimeError("Error! Buffer for merge too small!")
    for i in range(first_part_begin, second_part_begin):
        buffer[i - first_part_begin] = array[i]

    current = first_part_begin
    first = 0
    first_end = second_part_begin - first_part_begin - 1
    second = second_part_begin
    while first <= first_end and second <= second_part_end:
        if buffer[first] < array[second]:
            array[current] = buffer[first]
            first += 1
        else:
            array[current] = array[second]
            second += 1
        current += 1
    if first <= first_end:
        for i in range(first, first_end + 1):
            array[current] = buffer[i]
            current += 1
    else:
        for i in range(second, second_part_end + 1):
            array[current] = array[i]
            current += 1


def merge_sort(array,
               bottom_part_max_size=2,
               bottom_part_sort=pair_sort,
               merge_algorithm=simplest_merge,
               merge_buffer=None):
    array_size = len(array)
    part_size = bottom_part_max_size
    for i in range(0, array_size, bottom_part_max_size):
        bottom_part_sort(array, i, min(i + bottom_part_max_size, array_size) - 1)
    while part_size < array_size:
        for first_part_begin in range(0, array_size, 2 * part_size):
            second_part_begin = first_part_begin + part_size
            if second_part_begin < array_size:
                second_part_end = min(second_part_begin + part_size, array_size) - 1
                merge_algorithm(array, first_part_begin, second_part_begin, second_part_end, merge_buffer)
        part_size *= 2
