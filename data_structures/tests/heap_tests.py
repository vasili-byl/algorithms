import random
import time
from data_structures.heap.kary_heap import KaryHeap

HEAP_SIZE = 10000000


def create_kary_heap_add(k, keys):
    heap = KaryHeap(k)
    for i in keys:
        heap.add(i)
    return heap


def create_kary_heap_make(k, keys):
    return KaryHeap(k, keys)


def test_heap(heap, n=50000):
    for i in range(1, n + 1):
        if i != heap.get_min() or i != heap.extract_min():
            return False
    return True


def test_heap_and_write_result(heap, create_heap_time):
    start_time = time.time()
    if test_heap(heap):
        print("Result: OK")
    else:
        print("Result: Fail!")
    test_time = time.time() - start_time
    print("Creating heap took {}. Extracting min took {}".format(create_heap_time, test_time))


def test_kary_heap():
    keys = list(range(1, HEAP_SIZE + 1))
    random.shuffle(keys)
    for k in range(2, 11):
        print("=====Test=====")
        print("k={} heap created throw sequence of add operations".format(k))
        start_time = time.time()
        heap = create_kary_heap_add(k, keys)
        test_heap_and_write_result(heap, time.time() - start_time)

        print("k={} heap created with time complexity O(n)".format(k))
        start_time = time.time()
        heap = create_kary_heap_make(k, keys)
        test_heap_and_write_result(heap, time.time() - start_time)


if __name__ == "__main__":
    test_kary_heap()