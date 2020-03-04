"""
Problem: Inverse of Burrows-Wheeler Transform
Task: Convert a string that has been transformed by BWT back to its original version.
"""

def inverse_bwt(bwt):
    """
    :param  str bwt: The Burrows-Wheeler transform of a string

    :rtype  str
    :return The original string before it was transformed
    """
    sorted_bwt = sorted(bwt)
    length = len(bwt)
    bwt_tracker = {}
    sorted_tracker = {}
    tracker = {}
    for i in range(length):
        b = bwt[i]
        s = sorted_bwt[i]
        if b in bwt_tracker:
            bwt_tracker[b] += 1
        else:
            bwt_tracker[b] = 0
        if sorted_bwt[i] in sorted_tracker:
            sorted_tracker[s] += 1
        else:
            sorted_tracker[s] = 0

        tracker[s + str(sorted_tracker[s])] = b + str(bwt_tracker[b])

    inverse = ""
    key = '$0'
    for i in range(length):
        inverse += tracker[key][0]
        key = tracker[key]

    return inverse[::-1][1:] + '$'


if __name__ == '__main__':
    assert inverse_bwt('AGGGAA$') == 'GAGAGA$'
    assert inverse_bwt('annb$aa') == 'banana$'
    assert inverse_bwt('smnpbnnaaaaa$a') == 'panamabananas$'
