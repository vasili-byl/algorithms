import random
import time
from data_structures.heap.kary_heap import KaryHeap
from data_structures.heap.binomial_heap import BinomialHeap


def create_kary_heap_add(k, keys):
    heap = KaryHeap(k)
    for i in keys:
        heap.add(i)
    return heap


def create_kary_heap_make(k, keys):
    return KaryHeap(k, keys)


def create_binomial_heap(keys):
    return BinomialHeap(keys)


def test_heap(heap, n=50000):
    for i in range(1, n + 1):
        if i != heap.get_min() or i != heap.extract_min():
            return False
    return True


def test_heap_and_write_result(heap, create_heap_time, n):
    start_time = time.time()
    if test_heap(heap, n):
        print("Result: OK")
    else:
        print("Result: Fail!")
    test_time = time.time() - start_time
    print("Creating heap took {}. Extracting min took {}".format(create_heap_time, test_time))


def test_kary_heap(n=100000):
    keys = list(range(1, n + 1))
    random.shuffle(keys)
    print("=====Test K-ary heap=====")
    for k in range(2, 11):
        print("k={} heap created throw sequence of add operations".format(k))
        start_time = time.time()
        heap = create_kary_heap_add(k, keys)
        test_heap_and_write_result(heap, time.time() - start_time, n)

        print("k={} heap created with time complexity O(n)".format(k))
        start_time = time.time()
        heap = create_kary_heap_make(k, keys)
        test_heap_and_write_result(heap, time.time() - start_time, n)


def test_binomial_heap(n=10000):
    print("=====Test binomial heap=====")
    for k in range(1, 11):
        print("Test number {}".format(k))
        keys = list(range(1, n + 1))
        random.shuffle(keys)

        start_time = time.time()
        heap = create_binomial_heap(keys)
        test_heap_and_write_result(heap, time.time() - start_time, n)


if __name__ == "__main__":
    test_kary_heap(100000)
    test_binomial_heap(10000)