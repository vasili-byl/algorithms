import random
import insertion_sort
import merge_sort


def random_pivot_selector(array, left_bound, right_bound):
    return random.randint(left_bound, right_bound)


def median_of_three_pivot_selector(array, left_bound, right_bound):
    first = array[left_bound]
    middle_index = (left_bound + right_bound) // 2
    middle = array[middle_index]
    last = array[right_bound]

    if first <= middle:
        if middle <= last:
            return middle_index
        elif last <= first:
            return left_bound
        else:
            return right_bound
    else:
        if middle >= last:
            return middle_index
        elif last >= first:
            return left_bound
        else:
            return right_bound


def standard_partition(array, left_bound, right_bound, pivot_index):
    left = left_bound
    right = right_bound
    pivot = array[pivot_index]

    while left <= right:
        while left <= right_bound and array[left] < pivot:
            left += 1
        while right >= left_bound and array[right] > pivot:
            right -= 1
        if left <= right:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1

    return right, left


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def lomoto_partition(array, left_bound, right_bound, pivot_index):
    if right_bound - left_bound == 0:
        return left_bound - 1, right_bound + 1

    pivot = array[pivot_index]
    swap(array, pivot_index, left_bound)
    smaller_end = left_bound - 1
    equal_end = left_bound
    for i in range(left_bound + 1, right_bound + 1):
        if array[i] == pivot:
            swap(array, i, equal_end + 1)
            equal_end += 1
        if array[i] < pivot:
            swap(array, smaller_end + 1, i)
            smaller_end += 1
            swap(array, equal_end + 1, i)
            equal_end += 1
    return smaller_end, equal_end + 1


def qsort_internal(array,
                   left_bound,
                   right_bound,
                   pivot_selector,
                   partition_algorithm,
                   bottom_part_max_size,
                   bottom_part_sort):
    while left_bound < right_bound:
        pivot_index = pivot_selector(array, left_bound, right_bound)
        first_part_end, second_part_begin = partition_algorithm(array, left_bound, right_bound, pivot_index)
        segments = []
        if first_part_end - left_bound > 0:
            if first_part_end - left_bound < bottom_part_max_size:
                bottom_part_sort(array, left_bound, first_part_end)
            else:
                segments.append((left_bound, first_part_end))

        if right_bound - second_part_begin > 0:
            if right_bound - second_part_begin < bottom_part_max_size:
                bottom_part_sort(array, second_part_begin, right_bound)
            else:
                segments.append((second_part_begin, right_bound))

        if len(segments) == 2:
            s1 = segments[0]
            s2 = segments[1]
            max = s2
            min = s1
            if s1[1] - s1[0] > s2[1] - s2[0]:
                max = s1
                min = s2
            qsort_internal(array,
                           min[0],
                           min[1],
                           pivot_selector,
                           partition_algorithm,
                           bottom_part_max_size,
                           bottom_part_sort)
            left_bound, right_bound = max
        elif len(segments) == 1:
            left_bound, right_bound = segments[0]
        else:
            break


def qsort(array,
          pivot_selector=median_of_three_pivot_selector,
          partition_algorithm=standard_partition,
          bottom_part_max_size=2,
          bottom_part_sort=merge_sort.pair_sort):
    left_bound = 0
    right_bound = len(array) - 1
    if left_bound < right_bound:
        qsort_internal(array,
                       left_bound,
                       right_bound,
                       pivot_selector,
                       partition_algorithm,
                       bottom_part_max_size,
                       bottom_part_sort)


if __name__ == "__main__":
    N = 10
    a = list(range(N))
    random.shuffle(a)
    qsort(a, partition_algorithm=lomoto_partition)
    if a == list(range(N)):
        print("Success")
    else:
        print("Fail")