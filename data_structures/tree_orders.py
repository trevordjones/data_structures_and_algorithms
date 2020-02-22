"""
Problem: Binary Tree Traversals
Task: When given a rooted binary tree, build and output its in-order,
      pre-order and post-order traversals.
"""

import sys, threading


sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def __init__(self, vertices):
        """
        :param list[list[int]] vertices: Vertices in a binary tree
        """

        vertex_size = len(vertices)
        self.key = [0 for i in range(vertex_size)]
        self.left = [0 for i in range(vertex_size)]
        self.right = [0 for i in range(vertex_size)]
        for i in range(vertex_size):
            [key, left, right] = vertices[i]
            self.key[i] = key
            self.left[i] = left
            self.right[i] = right

    def in_order(self):
        self.result = []
        self.in_order_traversal(0)

        return self.result

    def in_order_traversal(self, parent):
        if parent == -1:
            return

        self.in_order_traversal(self.left[parent])
        self.result.append(self.key[parent])
        self.in_order_traversal(self.right[parent])

    def pre_order(self):
        self.result = []
        self.pre_order_traversal(0)

        return self.result

    def pre_order_traversal(self, parent):
        if parent == -1:
            return

        self.result.append(self.key[parent])
        self.pre_order_traversal(self.left[parent])
        self.pre_order_traversal(self.right[parent])

    def post_order(self):
        self.result = []
        self.post_order_traversal(0)

        return self.result

    def post_order_traversal(self, parent):
        if parent == -1:
            return

        self.post_order_traversal(self.left[parent])
        self.post_order_traversal(self.right[parent])
        self.result.append(self.key[parent])

def main():
    vertices = [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1],
    ]
    tree = TreeOrders(vertices)
    assert tree.in_order() == [1, 2, 3, 4, 5]
    assert tree.pre_order() == [4, 2, 1, 3, 5]
    assert tree.post_order() == [1, 3, 2, 5, 4]

    vertices = [
        [0, 7, 2],
        [10, -1, -1],
        [20, -1, 6],
        [30, 8, 9],
        [40, 3, -1],
        [50, -1, -1],
        [60, 1, -1],
        [70, 5, 4],
        [80, -1, -1],
        [90, -1, -1],
    ]
    tree = TreeOrders(vertices)
    assert tree.in_order() == [50, 70, 80, 30, 90, 40, 0, 20, 10, 60]
    assert tree.pre_order() == [0, 70, 50, 40, 30, 80, 90, 20, 60, 10]
    assert tree.post_order() == [50, 80, 90, 30, 40, 70, 10, 60, 20, 0]

threading.Thread(target=main).start()
