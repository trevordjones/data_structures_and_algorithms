"""
Task: Construct a trie from a collection of patterns

 Return the trie built from patterns
 in the form of a dictionary of dictionaries,
 e.g. {0:{'A':1,'T':2},1:{'C':3}}
 where the key of the external dictionary is
 the node ID (integer), and the internal dictionary
 contains all the trie edges outgoing from the corresponding
 node, and the keys are the letters on those edges, and the
 values are the node IDs to which these edges lead.
"""

def build_trie(patterns):
    """
    :param  list[str] patterns: A list of patterns

    :rtype  dict[int, dict[str, int]]
    :return A trie
    """
    trie = {0: {}}
    new_node = 0
    for pattern in patterns:
        current_node = 0
        for _, current_symbol in enumerate(pattern):
            if current_symbol in trie[current_node]:
                current_node = trie[current_node][current_symbol]
            else:
                new_node += 1
                trie[current_node][current_symbol] = new_node
                current_node = new_node
                trie[new_node] = {}

    return trie


if __name__ == '__main__':
    patterns = ['AT', 'AG', 'AC']
    assert build_trie(patterns) == {0: {'A': 1}, 1: {'T': 2, 'G': 3, 'C': 4}, 2: {}, 3: {}, 4: {}}

    patterns = ['ATAGA', 'ATC', 'GAT']
    assert build_trie(patterns) == {0: {'A': 1, 'G': 7}, 1: {'T': 2}, 2: {'A': 3, 'C': 6}, 3: {'G': 4}, 4: {'A': 5}, 5: {}, 6: {}, 7: {'A': 8}, 8: {'T': 9}, 9: {}}
