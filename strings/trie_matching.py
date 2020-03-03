"""
Problem: Multiple Pattern Matching
Task: Find all occurrences of a collection of patterns in a text.
"""

def find_patterns(text, patterns):
    """
    :param  str text: The text to search
    :param  str patterns: The patterns to search for in text

    :rtype  list[int]
    :return All starting position in text where the string pattern was found
    """

    result = []
    count = 0
    trie = build_trie(patterns)
    result = []
    while text:
        pattern = prefix_trie_matching(text, trie)
        if pattern in patterns:
            result.append(count)
        count += 1
        text = text[1:]

    return result

def prefix_trie_matching(text, trie):
    """
    :param  str text: The text to search
    :param  dict[int, dict[str, int]] trie: The trie to use to match the pattern

    :rtype  str
    :return The pattern that was found
    """

    count = 0
    symbol = text[count]
    text_length = len(text)
    node = 0
    nodes = []
    while True:
        if not trie[node]:
            pattern = ""
            new_node = 0
            for n in nodes:
                for key, value in trie[new_node].items():
                    if value == n:
                        pattern += key
                        new_node = value

            return pattern
        elif symbol in trie[node]:
            count += 1
            node = trie[node][symbol]
            if count < text_length:
                nodes.append(node)
                symbol = text[count]
            elif not trie[node]:
                nodes.append(node)
        else:
            return "pattern not found"

def build_trie(patterns):
    """
    :param  list[str] patterns: A list of patterns to search for

    :rtype  dict[int, dict[str, int]]
    :return tree created from patterns
    """

    tree = {0: {}}
    node = 0
    new_node = 0
    for pattern in patterns:
        current_node = node
        for _, p in enumerate(pattern):
            current_symbol = p
            if current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                new_node += 1
                tree[current_node][current_symbol] = new_node
                current_node = new_node
                tree[new_node] = {}

    return tree

if __name__ == '__main__':
    text = 'AAA'
    patterns = ['AA']
    assert find_patterns(text, patterns) == [0, 1]

    text = 'AATCGGGTTCAATCGGGGT'
    patterns = ['ATCG', 'GGGT']
    assert find_patterns(text, patterns) == [1, 4, 11, 15]

