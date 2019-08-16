class KaryHeap:
    def __init__(self, k, data=None):
        self.__k = k
        if data is None:
            self.__nodes = []
        else:
            self.__nodes = data[:]
            for i in range(len(self.__nodes) - 1, -1, -1):
                self.__sift_down(i)

    def  add(self, key):
        self.__nodes.append(key)
        self.__sift_up(len(self.__nodes) - 1)

    def get_min(self):
        if len(self.__nodes) == 0:
            raise RuntimeError("Couldn't get minimum! The heap is empty!")
        return self.__nodes[0]

    def extract_min(self):
        if len(self.__nodes) == 0:
            raise RuntimeError("Couldn't extract min! The heap is empty!")
        result = self.__nodes[0]
        self.__nodes[0] = self.__nodes[-1]
        self.__nodes.pop(-1)
        self.__sift_down(0)
        return result

    def __swap(self, pos1, pos2):
        temp = self.__nodes[pos1]
        self.__nodes[pos1] = self.__nodes[pos2]
        self.__nodes[pos2] = temp

    def __sift_up(self, position):
        while position > 0 and self.__nodes[position] < self.__nodes[(position - 1) // self.__k]:
            parent = (position - 1) // self.__k
            self.__swap(parent, position)
            position = parent

    def __sift_down(self, position):
        heap_size = len(self.__nodes)
        while position * self.__k + 1 < heap_size:
            min_child_index = position * self.__k + 1
            for i in range(2, min(self.__k + 1, heap_size - position * self.__k)):
                if self.__nodes[position * self.__k + i] < self.__nodes[min_child_index]:
                    min_child_index = position * self.__k + i
            if self.__nodes[min_child_index] < self.__nodes[position]:
                self.__swap(position, min_child_index)
                position = min_child_index
            else:
                break
