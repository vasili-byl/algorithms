import sort.qsort as qsort


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
            return array[0]

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

        return array[left_bound]
