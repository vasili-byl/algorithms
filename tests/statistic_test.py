import random
import search.kthstatistic as kthstatistic


def test_statistic_different_size(algorithm, size_from=100, size_to=200, n_experiments=10):
    for i in range(1, n_experiments + 1):
        size = random.randint(size_from, size_to)
        k = random.randint(0, size - 1)
        print("Test {}: size is {} and k is {}".format(i, size, k))
        array = list(range(size))
        random.shuffle(array)
        result = algorithm(array, k)
        if array[result] == k:
            print("Result: OK")
        else:
            print("Result: Fail!")


def test_statistic_all_statistics(algorithm, size=100):
    array = list(range(size))
    random.shuffle(array)
    for i in range(size):
        result = algorithm(array, i)
        if array[result] != i:
            print("Result: Fail!")
            return None
    print("Result: OK")


if __name__ == "__main__":
    print("=====Test k-th statistic algorithm with random pivot=====")
    size = 1000
    print("Test all statistics for {}".format(size))
    test_statistic_all_statistics(kthstatistic.KthStatistic(), size)
    print("Test with different sizes")
    test_statistic_different_size(kthstatistic.KthStatistic(), 30000, 100000, n_experiments=10)
    print("=====Test k-th statistic algorithm with median of five pivot=====")
    pivot_selector = kthstatistic.MedianOfFive()
    statistic_algorithm = kthstatistic.KthStatistic(pivot_selector=pivot_selector)
    pivot_selector.set_statistic_algorithm(statistic_algorithm)
    size = 1000
    print("Test all statistics for {}".format(size))
    test_statistic_all_statistics(statistic_algorithm, size)
    print("Test with different sizes")
    test_statistic_different_size(statistic_algorithm, 30000, 100000, n_experiments=10)
    for i in range(7, 12, 2):
        print("Median of {} test all statistics for {}".format(i, size))
        pivot_selector = kthstatistic.MedianOfFive(column_size=i)
        statistic_algorithm = kthstatistic.KthStatistic(pivot_selector=pivot_selector)
        pivot_selector.set_statistic_algorithm(statistic_algorithm)
        test_statistic_all_statistics(statistic_algorithm, size)
