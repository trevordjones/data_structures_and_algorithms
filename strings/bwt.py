"""
The Burrows–Wheeler transform of a string permutes the symbols
so that it becomes more easily compressible. This is particularly
helpful with compressing genomes which have repeats. BWT can take
repeats (abcabcabc) and convert them to strings with more runs
(aaabbbccc) which can then be compressed (3a3b3c).

Problem: BWT
Task: Construct the Burrows-Wheeler transform of a string
"""

def bwt(text):
    """
    :param  str text: The text to permute

    :rtype  str
    :return The Burrows-Wheeler transform of a string
    """
    matrix = []
    length = len(text)
    for i in range(1, length + 1):
        matrix.append(text[length-i:length] + text[0:length-i])
    matrix.sort()
    string = ""
    for m in matrix:
        string += m[-1]
    return string

if __name__ == '__main__':
    text = 'ACACACAC$'
    assert (bwt(text)) == 'CCCC$AAAA'

    text = 'AGACATA$'
    assert (bwt(text)) == 'ATG$CAAA'
