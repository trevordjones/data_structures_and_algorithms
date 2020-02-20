"""
Problem: Partitioning
Task: Partition sequence of integers into 3 subsets of equal sums
"""

import itertools


def partition3(sequence):
    """
    :param list[int] sequence: sequence of integers to partition

    :rtype boolean
    :returns Whether sequence can be partitioned into 3 subsets of equal sums
    """

    for indices in itertools.product(range(3), repeat=len(sequence)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(sequence[k] for k in range(len(sequence)) if indices[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return True

    return False

if __name__ == '__main__':
    assert partition3([3, 3, 3, 3]) == False
    assert partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == True
    assert partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == True

