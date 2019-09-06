from sort import Sort


class PairSort(Sort):
    def __call__(self, array, left_bound, right_bound):
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


class MergeSort(Sort):
    def __init__(self,
                 bottom_part_max_size=2,
                 bottom_part_sort=None,
                 merge_algorithm=simplest_merge,
                 merge_buffer=None):
        self.bottom_part_max_size = bottom_part_max_size
        if bottom_part_sort is None:
            if bottom_part_max_size > 2:
                raise RuntimeError("You specified bottom_part_max_size > 2 but didn't specify bottom_part_sort!")
            else:
                bottom_part_sort = PairSort()
        self.bottom_part_sort = bottom_part_sort
        self.merge_algorithm = merge_algorithm
        self.merge_buffer = merge_buffer

    def __call__(self, array, left_bound=None, right_bound=None):
        if left_bound is None:
            left_bound = 0
        if right_bound is None:
            right_bound = len(array) - 1
        array_size = right_bound - left_bound + 1
        part_size = self.bottom_part_max_size
        for i in range(left_bound, right_bound + 1, self.bottom_part_max_size):
            self.bottom_part_sort(array, i, min(i + self.bottom_part_max_size - 1, right_bound))
        while part_size < array_size:
            for first_part_begin in range(left_bound, right_bound + 1, 2 * part_size):
                second_part_begin = first_part_begin + part_size
                if second_part_begin <= right_bound:
                    second_part_end = min(second_part_begin + part_size - 1, right_bound)
                    self.merge_algorithm(array, first_part_begin, second_part_begin, second_part_end, self.merge_buffer)
            part_size *= 2
