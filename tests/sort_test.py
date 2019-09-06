import random
import sort.insertion_sort as insertion_sort
import sort.merge_sort as merge_sort
import sort.qsort as qsort


def test_sort(sort_algorithm, n_experiments=1000, max_size=None):
    test_failed = False
    for i in range(n_experiments):
        size = random.randint(0, 200) * 1000 + random.randint(1, 1000)
        if max_size is not None:
            size = min(size, max_size)
        array = [random.randint(0, 10 ^ 8) for i in range(size)]
        print("Test {}: size is {}".format(i + 1, len(array)))
        sorted_array = sorted(array)
        random.shuffle(array)
        sort_algorithm(array)
        if array != sorted_array:
            print("Test failed!")
            test_failed = True
            break
    if not test_failed:
        print("Tests passed!")


def test_bottom_part_size(sort_algorithm, additional_sort, n_experiments):
    for i in range(n_experiments):
        bottom_part_size = 2#random.randint(2, 50)
        print("Bottom part size is {}".format(bottom_part_size))
        sort = sort_algorithm(bottom_part_max_size=bottom_part_size, bottom_part_sort=additional_sort)
        test_sort(sort, n_experiments=1)


def buffered(func):
    def inner(*args, **kwargs):
        buffer = [0] * len(args[0])
        kwargs["merge_buffer"] = buffer
        func(*args, **kwargs)
    return inner


def with_bottom_sort(func, sort_algorithm, bottom_part_size):
    def inner(*args, **kwargs):
        kwargs["bottom_part_sort"] = sort_algorithm
        kwargs["bottom_part_max_size"] = bottom_part_size
        func(*args, **kwargs)
    return inner


def add_pivot(func, pivot_selector):
    def inner(*args, **kwargs):
        kwargs["pivot_selector"] = pivot_selector
        func(*args, **kwargs)
    return inner


def add_partition(func, partition):
    def inner(*args, **kwargs):
        kwargs["partition_algorithm"] = partition
        func(*args, **kwargs)
    return inner


if __name__ == "__main__":
    print("=====Insertion sort=====")
    test_sort(insertion_sort.InsertionSort(), n_experiments=5, max_size=12345)

    print("=====Merge sort=====")
    test_sort(merge_sort.MergeSort(), n_experiments=10)

    print("=====Merge sort with insertion sort for the small parts=====")
    test_bottom_part_size(merge_sort.MergeSort, insertion_sort.InsertionSort(), n_experiments=10)

    print("=====Qsort(median of three, standard partition, divide while chunk > 2)=====")
    test_sort(qsort.Qsort(), n_experiments=10)

    print("=====Qsort(median of three, standard partition)=====")
    test_bottom_part_size(qsort.Qsort, insertion_sort.InsertionSort(), n_experiments=10)

    print("=====Qsort(random pivot, divide while chunk size > 16)=====")
    sort = qsort.Qsort(bottom_part_max_size=16,
                       bottom_part_sort=insertion_sort.InsertionSort(),
                       pivot_selector=qsort.random_pivot_selector)
    test_sort(sort, n_experiments=10)

    print("=====Qsort(random pivot, lomoto partition, divide while chunk size > 16)=====")
    sort = qsort.Qsort(bottom_part_max_size=16,
                       bottom_part_sort=insertion_sort.InsertionSort(),
                       pivot_selector=qsort.random_pivot_selector,
                       partition_algorithm=qsort.lomoto_partition)
    test_sort(sort, n_experiments=10)
