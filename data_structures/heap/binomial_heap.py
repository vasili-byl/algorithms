

class BinomialNode(object):
    children = None
    value = None

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class BinomialTree(object):
    head = None
    size = None

    def __init__(self, tree_head, tree_size):
        self.head = tree_head
        self.size = tree_size

    def drop(self):
        self.head = None
        self.size = None

    def get_top(self):
        if self.head is None:
            raise RuntimeError("Can not get value in the root! Binomial tree is not initialized!")
        return self.head.value


def meld_similar_trees(tree1, tree2):
    if tree1.size != tree2.size:
        raise RuntimeError("Error! You tried to meld binomial trees with different sizes {} and {}.".format(tree1.size, tree2.size))
    if tree1.get_top() < tree2.get_top():
        parent_tree = tree1
        child_tree = tree2
    else:
        parent_tree = tree2
        child_tree = tree1
    tree = BinomialTree(parent_tree.head, parent_tree.size * 2)
    tree.head.add_child(child_tree.head)

    child_tree.drop()
    parent_tree.drop()
    return tree


class BinomialHeap(object):
    min_tree_index = None
    trees = None

    def __init__(self, data=None):
        self.trees = []
        if data is not None and len(data) > 0:
            self.min_tree_index = 0
            temporary_trees = [BinomialTree(BinomialNode(element), 1) for element in data]
            while len(temporary_trees) > 0:
                new_trees = []
                for i in range(0, len(temporary_trees) - 1, 2):
                    new_trees.append(meld_similar_trees(temporary_trees[i], temporary_trees[i + 1]))
                if len(temporary_trees) % 2 == 1:
                    self.trees.append(temporary_trees[-1])
                    if temporary_trees[-1].get_top() < self.trees[self.min_tree_index].get_top():
                        self.min_tree_index = len(self.trees) - 1
                temporary_trees = new_trees

    def add(self, key):
        heap = BinomialHeap([key])
        self.__meld(heap)

    def get_min(self):
        if self.trees is None or self.min_tree_index is None:
            raise RuntimeError("Couldn't get minimum! The heap is empty!")
        return self.trees[self.min_tree_index].get_top()

    def extract_min(self):
        if self.trees is None or self.min_tree_index is None:
            raise RuntimeError("Couldn't extract min! The heap is empty!")
        tree = self.trees.pop(self.min_tree_index)
        self.min_tree_index = None
        heap = BinomialHeap()
        size = 1
        for node in tree.head.children:
            heap.trees.append(BinomialTree(node, size))
            size *= 2
        self.__meld(heap)
        result = tree.get_top()
        tree.drop()
        return result

    def drop(self):
        self.trees = None
        self.min_tree_index = None

    def __meld(self, other):
        result_trees = []
        self_index = 0
        other_index = 0
        while self_index < len(self.trees) and other_index < len(other.trees):
            self_next_tree = self.trees[self_index]
            other_next_tree = other.trees[other_index]
            if self_next_tree.size == other_next_tree.size:
                tree = meld_similar_trees(self_next_tree, other_next_tree)
                result_trees.append(tree)
                self_index += 1
                other_index += 1
            else:
                if self_next_tree.size < other_next_tree.size:
                    smallest_tree = self_next_tree
                    self_index += 1
                else:
                    smallest_tree = other_next_tree
                    other_index += 1
                if len(result_trees) > 0 and result_trees[-1].size == smallest_tree:
                    tree = meld_similar_trees(result_trees[-1], smallest_tree)
                    result_trees[-1] = tree
                else:
                    result_trees.append(smallest_tree)

        if self_index < len(self.trees):
            for index in range(self_index, len(self.trees)):
                if len(result_trees) > 0 and self.trees[index].size == result_trees[-1].size:
                    tree = meld_similar_trees(result_trees[-1], self.trees[index])
                    result_trees[-1] = tree
                else:
                    result_trees.append(self.trees[index])
        elif other_index < len(other.trees):
            for index in range(other_index, len(other.trees)):
                if len(result_trees) > 0 and other.trees[index].size == result_trees[-1].size:
                    tree = meld_similar_trees(result_trees[-1], other.trees[index])
                    result_trees[-1] = tree
                else:
                    result_trees.append(other.trees[index])
        self.trees = result_trees
        if len(result_trees) > 0:
            self.min_tree_index = 0
        else:
            self.min_tree_index = None
        for index, t in enumerate(self.trees):
            if t.get_top() < self.trees[self.min_tree_index].get_top():
                self.min_tree_index = index
        other.drop()
