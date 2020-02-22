"""
Task: Convert array of integers into a heap
"""


class HeapBuilder:
    def __init__(self, data):
        """
        :param list[int] data: list of integers to convert to a heap

        parent(i) = [i / 2]
        left_child(i) = 2i
        right_child(i) = 2i + 1
        """

        self.swaps = []
        self.data = data

    def build_heap(self):
        size = len(self.data)
        for i in range(size // 2, -1, -1):
            self._sift_up(i)

    def _sift_up(self, pi):
        size = len(self.data)
        min_index = pi
        left_child, right_child = 2 * pi + 1, 2 * pi + 2
        if left_child < size and self.data[left_child] < self.data[min_index]:
            min_index = left_child
        if right_child < size and self.data[right_child] < self.data[min_index]:
            min_index = right_child

        if self.data[pi] > self.data[min_index]:
            ai, bi = pi, min_index
            self.swaps.append((ai, bi))
            self.data[bi], self.data[ai] = self.data[ai], self.data[bi]
            self._sift_up(min_index)

if __name__ == '__main__':
    heap = HeapBuilder([5, 4, 3, 2, 1])
    heap.build_heap()
    assert heap.data == [1, 2, 3, 5, 4]

    heap = HeapBuilder([1, 2, 3, 4, 5])
    heap.build_heap()
    assert heap.data == 0
