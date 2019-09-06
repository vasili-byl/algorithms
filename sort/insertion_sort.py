from sort.abstract_sort import Sort


class InsertionSort(Sort):
    def __call__(self, array, left_bound=None, right_bound=None):
        if left_bound is None:
            left_bound = 0
        if right_bound is None:
            right_bound = len(array) - 1
        for i in range(left_bound + 1, right_bound + 1):
            pos = left_bound
            for j in range(i - 1, left_bound - 1, -1):
                if array[j] <= array[i]:
                    pos = j + 1
                    break
            current = array[i]
            for j in range(i - 1, pos - 1, -1):
                array[j + 1] = array[j]
            array[pos] = current
