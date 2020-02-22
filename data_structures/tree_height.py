import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, value):
        """
        :param int value: Index of the node
        """

        self.children = []
        self.parent = None
        self.value = value
        self.root = False

    def add_child(self, child):
        self.children.append(child)

class TreeHeight:
    def __init__(self, parents):
        """
        :param list[int] parents: Parent of a Node based on index
        """

        self.parent = parents
        self.nodes = []

    def create_nodes(self, node_size):
        """
        :param int node_size: The number of Nodes in the tree
        """

        for i in range(node_size):
            self.nodes.append(Node(i))

        for ci in range(node_size):
            pi = self.parent[ci]
            if pi != -1:
                self.nodes[ci].parent = self.nodes[pi]
                self.nodes[pi].add_child(self.nodes[ci])
            else:
                self.root_index = ci

    def compute_height(self):
        if not self.nodes:
            return 0

        root = self.nodes[self.root_index]
        return self.recursive_height(root)

    def recursive_height(self, node):
        if not node.children:
            return 1

        heights = []
        for n in node.children:
            heights.append(self.recursive_height(n))
        return max(heights) + 1

def main():
    tree = TreeHeight(parents=[4, -1, 4, 1, 1])
    tree.create_nodes(node_size=5)
    assert(tree.compute_height()) == 3

    tree = TreeHeight(parents=[-1, 0, 4, 0, 3])
    tree.create_nodes(node_size=5)
    assert(tree.compute_height()) == 4

threading.Thread(target=main).start()
