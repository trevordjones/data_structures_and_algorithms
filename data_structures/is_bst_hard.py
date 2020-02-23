"""
Problem: Is it a Binary Search Tree (hard)
Task: Check whether a binary tree is a binary search tree, with the caveat
      that keys may be of equal value.
"""

import sys, threading, pdb

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
        return check_if_binary(tree, tree[0], False, False, float("-inf"), float("inf"))

def check_if_binary(tree, nodes, is_left, is_right, min, max):
    """
    :param list[list[int]] tree: Binary tree
    :param list[int] nodes: Nodes that make up a tree
    :param boolean is_left: If the child is left it must
                            be strictly less than parent
    :param boolean is_right: If the child is right it must
                             be less than or equal to parent
    :param float min_node: Min node in a list of nodes
    :param float max_node: Max node in a list of nodes

    :rtype boolean
    :returns Whether the tree is a binary search tree
    """

    parent = 0
    left = 1
    right = 2
    if is_left:
        if nodes[parent] >= max or nodes[parent] < min:
            return False

    if is_right:
        if nodes[parent] == min:
            pass
        elif nodes[parent] < min or nodes[parent] >= max:
            return False

    if nodes[left] == -1:
        left_is_bst = True
    else:
        left_is_bst = check_if_binary(tree, tree[nodes[left]], True, False, min, nodes[parent])

    if nodes[right] == -1:
        right_is_bst = True
    else:
        right_is_bst = check_if_binary(tree, tree[nodes[right]], False, True, nodes[parent], max)

    return left_is_bst and right_is_bst

def main():
    tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
    assert is_binary_search_tree(tree) == True

    tree = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
    assert is_binary_search_tree(tree) == False

    tree = [[2, 1, 2], [2, -1, -1], [3, -1, -1]]
    assert is_binary_search_tree(tree) == False

    tree = [[2147483647, -1, -1]]
    assert is_binary_search_tree(tree) == True

threading.Thread(target=main).start()
