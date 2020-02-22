"""
Problem: Is it a Binary Search Tree?
Task: Check whether a binary tree is a binary search tree
"""

import sys, threading


sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def is_binary_search_tree(tree):
    """
    :param list[list[int]] tree: Binary tree

    :rtype boolean
    :returns Uses a recursive method to check whether the tree is a
             binary search tree or not
    """

    if not tree:
        return True
    else:
        return check_if_binary(tree, tree[0], float("-inf"), float("inf"))

def check_if_binary(tree, nodes, min_node, max_node):
    """
    :param list[list[int]] tree: Binary tree
    :param list[int] nodes: Nodes that make up a tree
    :param float min_node: Min node in a list of nodes
    :param float max_node: Max node in a list of nodes

    :rtype boolean
    :returns Whether the tree is a binary search tree
    """

    parent = 0
    left = 1
    right = 2
    if nodes[parent] < min_node or nodes[parent] > max_node:
        return False

    if nodes[left] == -1:
        left_is_bst = True
    else:
        left_is_bst = check_if_binary(tree, tree[nodes[left]], min_node, nodes[parent])

    if nodes[right] == -1:
        right_is_bst = True
    else:
        right_is_bst = check_if_binary(tree, tree[nodes[right]], nodes[parent], max_node)

    return left_is_bst and right_is_bst

def main():
    tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
    assert is_binary_search_tree(tree) == True

    tree = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
    assert is_binary_search_tree(tree) == False

    tree = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
    assert is_binary_search_tree(tree) == True

    tree = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
    assert is_binary_search_tree(tree) == False

threading.Thread(target=main).start()
