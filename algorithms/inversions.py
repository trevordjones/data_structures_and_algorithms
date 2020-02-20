"""
Problem: Number of Inversions
Task: Count the number of inversions of a given sequence. Shows how close a sequence is
      to being sorted.
"""

def get_number_of_inversions(sequence, lower_bound, upper_bound):
    """
    @type   sequence: list[int]
    @param  sequence: A sequence of integers to be inverted

    @type   lower_bound: int
    @param  lower_bound: Index of the lower bound of the sequence

    @type   upper_bound: int
    @param  upper_bound: Index of the upper bound of the sequence

    @rtype  int
    @return The number of inversions for the sequence
    """

    number_of_inversions = 0
    if upper_bound - lower_bound <= 1:
        return number_of_inversions
    middle = (lower_bound + upper_bound) // 2
    number_of_inversions += get_number_of_inversions(sequence, lower_bound, middle)
    number_of_inversions += get_number_of_inversions(sequence, middle, upper_bound)

    merged_sequence, merge_sequence_inversions = merge(
        sequence[lower_bound : middle],
        sequence[middle : upper_bound],
        sequence[lower_bound : upper_bound]
        )
    sequence[lower_bound : upper_bound] = merged_sequence
    return number_of_inversions + merge_sequence_inversions

def merge(lower_bound_sequence, upper_bound_sequence, sequence):
    """
    @type   lower_bound_sequence: list[int]
    @param  lower_bound_sequence: A sequence taken from the lower half of a sequence

    @type   upper_bound_sequence: list[ing]
    @param  upper_bound_sequence: A sequence taken from the upper half of a sequence

    @type   sequence: list[int]
    @param  sequence: A sequence of integers

    @rtype  list[int], int
    @return Inverted sequence and the number of inversions for the sequence
    """

    number_of_inversions = 0
    a, b, c = 0, 0, 0
    while a < len(lower_bound_sequence) and b < len(upper_bound_sequence):
        if lower_bound_sequence[a] <= upper_bound_sequence[b]:
            sequence[c], a, c = lower_bound_sequence[a], a + 1, c + 1
        else:
            sequence[c], b, c = upper_bound_sequence[b], b + 1, c + 1
            number_of_inversions += (len(lower_bound_sequence) - a)
    while a < len(lower_bound_sequence):
        sequence[c], a, c = lower_bound_sequence[a], a + 1, c + 1
    while b < len(upper_bound_sequence):
        sequence[c], b, c = upper_bound_sequence[b], b + 1, c + 1
    return sequence, number_of_inversions

if __name__ == '__main__':
    sequence = [2, 3, 9, 2, 9]
    assert get_number_of_inversions(sequence, 0, len(sequence)) == 2

    sequence = [1,2,3,4,5]
    assert get_number_of_inversions(sequence, 0, len(sequence)) == 0

    sequence = [5, 4, 3, 2, 1]
    assert get_number_of_inversions(sequence, 0, len(sequence)) == 10
