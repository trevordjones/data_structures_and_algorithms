"""
Problem: Checking whether a Graph is Bipartite
Task: Given an undirected graph with n vertices and m edges,
      check whether it is bipartite.
"""

def bipartite(graph):
    """
    :param list[list[int]] graph: A graph represented as a matrix

    :rtype boolean
    :returns True if graph is bipartite. False otherwise.
    """

    """
    A graph is bipartite if it can be colored with two colors such
    that the endpoints of each have different colors.
    """
    colors = [None] * len(graph)
    colors[0] = 1

    queue = [0]
    is_bipartite = True

    while queue:
        node = queue.pop(0)
        for connected_node in graph[node]:
            if colors[connected_node] is None:
                colors[connected_node] = colors[node] + 1
                queue.append(connected_node)
            elif colors[connected_node] == colors[node]:
                is_bipartite = False
                break

    return is_bipartite

if __name__ == '__main__':
    """
    graph: The index of the inner array represents a vertex. The numbers in
           the inner array indicate which vertices they connect to. A graph
           the values [[1], [0,2], [1], []] means vertex 1 connects to vertex 2.
           Vertex 2 connects to vertices 1 and 3. Vertex 3 connects to vertex 2.
           Vertex 4 does not connect to any.
    """

    graph = [[1, 3, 2], [0, 2], [1, 0], [0]]
    assert bipartite(graph) == False

    graph = [[3], [4, 3], [3], [1, 2, 0], [1]]
    assert bipartite(graph) == True
