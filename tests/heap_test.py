import random
import time
from data_structures.heap.kary_heap import KaryHeap
from data_structures.heap.binomial_heap import BinomialHeap
from data_structures.heap.leftist_heap import LeftistHeap


def create_kary_heap_add(k, keys):
    heap = KaryHeap(k)
    for i in keys:
        heap.add(i)
    return heap


def create_kary_heap_make(k, keys):
    return KaryHeap(k, keys)


def create_binomial_heap(keys):
    return BinomialHeap(keys)


def create_leftist_heap(keys):
    heap = LeftistHeap()
    for i in keys:
        heap.add(i)
    return heap


def create_skew_heap(keys):
    heap = LeftistHeap(skew_heap=True)
    for i in keys:
        heap.add(i)
    return heap


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
        keys_size = random.randint(n // 2, n)
        print("Test number {} n = {}".format(k, keys_size))
        keys = list(range(1, keys_size + 1))
        random.shuffle(keys)

        start_time = time.time()
        heap = create_binomial_heap(keys)
        test_heap_and_write_result(heap, time.time() - start_time, keys_size)


def test_leftist_heap(n=10000):
    print("=====Test leftist heap=====")
    for k in range(1, 11):
        keys_size = random.randint(n // 2, n)
        print("Test number {} n = {}".format(k, keys_size))
        keys = list(range(1, keys_size + 1))
        random.shuffle(keys)

        start_time = time.time()
        heap = create_leftist_heap(keys)
        test_heap_and_write_result(heap, time.time() - start_time, keys_size)


def test_skew_heap(n=10000):
    print("=====Test skew heap=====")
    for k in range(1, 11):
        keys_size = random.randint(n // 2, n)
        print("Test number {} n = {}".format(k, keys_size))
        keys = list(range(1, keys_size + 1))
        random.shuffle(keys)

        start_time = time.time()
        heap = create_skew_heap(keys)
        test_heap_and_write_result(heap, time.time() - start_time, keys_size)


if __name__ == "__main__":
    test_kary_heap(100000)
    test_binomial_heap(10000)
    test_leftist_heap(100000)
    test_skew_heap(100000)