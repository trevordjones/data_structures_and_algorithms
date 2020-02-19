"""
Problem: Binary Search
Task: Implement the binary search algorithm

Binary search algorithm: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
"""


def binary_search(sorted_list, integer):
    """
    @type   sorted_list: list[int]
    @param  sorted_list: sorted list of distinct integers

    @type   integer: int
    @param  integer: integer to search for in the sorted_list

    @rtype  int
    @return The index where the integer appears in the sorted_list
            Return -1 if the integer does not appear in the list
    """

    lower_bound = 0
    upper_bound = len(sorted_list) - 1
    while True:
        if lower_bound > upper_bound:
            answer = -1
            break

        middle = (lower_bound + upper_bound) // 2
        if sorted_list[middle] == integer:
            answer = middle
            break
        elif sorted_list[middle] < integer:
            lower_bound = middle + 1
        else:
            upper_bound = middle - 1
    return answer


def binary_search_recursion(sorted_list, integer, lower_bound, upper_bound):
    """
    Recursive implementation of binary search algorithm

    @type   sorted_list: list[int]
    @param  sorted_list: sorted list of distinct integers
    @type   integer: int
    @param  integer: integer to search for in the above list
    @type   lower_bound: int
    @param  lower_bound: lower bound to begin the search
    @type   upper_bound: int
    @param  upper_bound: upper bound to begin the search

    @rtype  int
    @return The index where the integer appears in the list
            Return -1 if the integer does not appear in the list
    """

    if lower_bound > upper_bound:
        return -1

    middle = (lower_bound + upper_bound) // 2
    if sorted_list[middle] == integer:
        return middle
    elif sorted_list[middle] < integer:
        return binary_search_recursion(sorted_list, integer, middle + 1, upper_bound)
    else:
        return binary_search_recursion(sorted_list, integer, lower_bound, middle - 1)


if __name__ == '__main__':
    sorted_list = [3, 4, 6, 10, 12, 14, 20, 25]

    assert binary_search(sorted_list, 5) == -1
    assert binary_search(sorted_list, 14) == 5

    assert binary_search_recursion(sorted_list, 20, 0, len(sorted_list) - 1) == 6
    assert binary_search_recursion(sorted_list, 15, 0, len(sorted_list) - 1) == -1
