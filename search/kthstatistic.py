import sort.qsort as qsort
import sort.insertion_sort as insertion_sort


class MedianOfFive(object):
    def __init__(self, column_size=5, colums_sort=insertion_sort.InsertionSort()):
        self.statistic_algorithm = None
        self.column_size = column_size
        self.columns_sort = colums_sort

    def __call__(self, array, left_bound, right_bound):
        if self.statistic_algorithm is None:
            raise RuntimeError("Could not select pivot! You should set up finding statistic algorithm.")
        if left_bound == right_bound:
            return left_bound
        if right_bound - left_bound + 1 <= self.column_size:
            self.columns_sort(array, left_bound, right_bound)
            return (left_bound + right_bound) // 2

        for i in range(left_bound, right_bound, self.column_size):
            column_end = min(i + self.column_size - 1, right_bound)
            self.columns_sort(array, i, column_end)

        result_index = self.statistic_algorithm([array[i] for i in range(self.column_size // 2, right_bound + 1, self.column_size)],
                                                (left_bound + right_bound) // (2 * self.column_size))
        return result_index * self.column_size + self.column_size // 2

    def set_statistic_algorithm(self, algorithm):
        self.statistic_algorithm = algorithm


class KthStatistic(object):
    def __init__(self,
                 pivot_selector=qsort.random_pivot_selector,
                 partition_algorithm=qsort.lomoto_partition):
        self.pivot_selector = pivot_selector
        self.partition_algorithm = partition_algorithm

    def __call__(self, array, k):
        left_bound = 0
        right_bound = len(array) - 1
        if k > right_bound:
            raise RuntimeError("You are trying to find {} order statistic "
                               "in the array of size {}.".format(k, len(array)))
        if len(array) == 0:
            raise RuntimeError("Array is empty")
        if len(array) == 1:
            return left_bound

        while left_bound < right_bound:
            pivot_index = self.pivot_selector(array, left_bound, right_bound)
            smaller_part_end, bigger_part_begin = self.partition_algorithm(array, left_bound, right_bound, pivot_index)
            if smaller_part_end < left_bound + k < bigger_part_begin:
                left_bound = right_bound = left_bound + k
            elif left_bound + k <= smaller_part_end:
                right_bound = smaller_part_end
            elif left_bound + k >= bigger_part_begin:
                k -= bigger_part_begin - left_bound
                left_bound = bigger_part_begin

        return left_bound
