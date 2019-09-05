class LeftistNode:
    rank = None
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value
        self.rank = 0

    def update_rank(self):
        if self.right is None:
            self.rank = 0
        else:
            self.rank = self.right.rank + 1


def right_descent(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node2.value < node1.value:
        temp = node1
        node1 = node2
        node2 = temp
    node1.right = right_descent(node1.right, node2)
    left_rank = node1.left.rank if node1.left is not None else 0
    right_rank = node1.right.rank if node1.right is not None else 0
    if left_rank < right_rank:
        temp = node1.left
        node1.left = node1.right
        node1.right = temp
    node1.update_rank()
    return node1


class LeftistHeap(object):
    head = None

    def __init__(self, head=None):
        self.head = head

    def add(self, key):
        heap = LeftistHeap(LeftistNode(key))
        self.__meld(heap)

    def get_min(self):
        if self.head is None:
            raise RuntimeError("Can not get minimum! Heap is empty!")
        return self.head.value

    def extract_min(self):
        if self.head is None:
            raise RuntimeError("Could not extract min! Heap is empty!")
        result = self.head.value
        left_subtree = LeftistHeap(self.head.left)
        self.head = self.head.right
        self.__meld(left_subtree)
        return result

    def __meld(self, other):
        if self.head is None and other.head is None:
            self.head = None
        else:
            root = right_descent(self.head, other.head)
            self.head = root
