"""
Task: Find all occurrences of a pattern in a string
"""

def find_pattern(pattern, text):
    """
    :param  str pattern: Pattern to search for in the text
    :param  str text: The text to use to search for the pattern

    :rtype  list[int]
    :return All the starting positions of the pattern in the text
    """
    result = []
    s = pattern + "$" + text
    prefix = compute_prefix_function(s)
    plength = len(pattern)
    slength = len(s)
    for i in range(plength + 1, slength):
        if prefix[i] == plength:
            result.append(i - 2 * plength)
    return result

def compute_prefix_function(text):
    """
    :param  str text: The text to use to search for the pattern

    :rtype  list[int]
    :return All the starting positions that match the prefix of the given text
    """
    length = len(text)
    s = [0] * length
    border = 0
    for i in range(1, length):
        while border > 0 and text[i] != text[border]:
            border = s[border - 1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        s[i] = border

    return s


if __name__ == '__main__':
    assert find_pattern("ab", "abababcaab") == [0, 2, 4, 8]
    assert find_pattern("abra", "abracadabra") == [0, 7]
    assert find_pattern("TACG", "GT") == []
    assert find_pattern("ATA", "ATATA") == [0, 2]
    assert find_pattern("ATAT", "GATATATGCATATACTT") == [1, 3, 9]
