"""
Problem: Majority Element
Task: Check whether an input sequence contains a majority element
"""


def get_majority_element(sequence, lower_bound, upper_bound):
    """
    @type   sequence: list[int]
    @param  sequence: A sequence of integers

    @type   lower_bound: int
    @param  lower_bound: Index of the lower bound of the sequence

    @type   upper_bound: int
    @param  upper_bound: Index of the upper bound of the sequence

    @rtype  int
    @return The integer that makes up the majority of the sequence.
            If no majority, return -1
    """
    if lower_bound == upper_bound:
        return -1
    if lower_bound + 1 == upper_bound:
        return sequence[lower_bound]
    middle = round(upper_bound / 2)
    lower_majority = get_majority_element(sequence[lower_bound : middle], lower_bound, len(sequence[lower_bound : middle]))
    upper_majority = get_majority_element(sequence[middle : upper_bound], lower_bound, len(sequence[middle : upper_bound]))

    lower_count = 0
    for i in range(lower_bound, upper_bound):
        if sequence[i] == lower_majority:
            lower_count += 1
    if lower_count > (upper_bound)//2:
        return lower_majority

    upper_count = 0
    for i in range(lower_bound, upper_bound):
        if sequence[i] == upper_majority:
            upper_count += 1
    if upper_count > (upper_bound)//2:
        return upper_majority
    return -1

if __name__ == '__main__':
    sequence = [2, 3, 9, 2, 2]
    assert get_majority_element(sequence, 0, len(sequence)) == 2

    sequence = [1, 2, 3, 4]
    assert get_majority_element(sequence, 0, len(sequence)) == -1

    sequence = [1, 2, 3, 1]
    assert get_majority_element(sequence, 0, len(sequence)) == -1
