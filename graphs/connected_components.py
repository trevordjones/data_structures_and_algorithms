"""
Problem: Adding Exits to a Maze
Task: Given an undirected graph with n vertices and m edges,
      compute the number of connected components in it.
"""


def number_of_components(graph):
    """
    :param list[list[int]] graph: A graph represented as a matrix

    :rtype int
    :returns Number of connected components
    """

    visited = [[] for _ in range(len(graph))]
    visited = visit(graph, 0, visited)
    count = check_visited(graph, visited)
    return count

def visit(graph, vertex, visited):
    """
    :param list[list[int]] graph: A graph represented as a matrix
    :param int vertex: The vertex to visit
    :param list[list[boolean]] visited: Mimics graph to track if a vertex has been visited

    :rtype list[list[boolean]]
    :returns A graph where the nodes are boolean values
    """

    if not graph[vertex]:
        visited[vertex].append(True)
    for idx, connected_vertex in enumerate(graph[vertex]):
        try:
            visited[vertex][idx]
        except:
            visited[vertex].append(True)
            visited = visit(graph, connected_vertex, visited)

    return visited

def check_visited(graph, visited):
    """
    :param list[list[int]] graph: A graph represented as a matrix
    :param list[list[boolean]] visited: Mimics graph to track if a vertex has been visited

    :rtype int
    :reterns The number of vertices that are connected
    """

    count = 1
    for idx, visits in enumerate(visited):
        if not visits:
            visited = visit(graph, idx, visited)
            count += check_visited(graph, visited)

    return count

if __name__ == '__main__':
    """
    graph: The index of the inner array represents a vertex. The numbers in
           the inner array indicate which vertices they connect to. A graph
           the values [[1], [0,2], [1], []] means vertex 1 connects to vertex 2.
           Vertex 2 connects to vertices 1 and 3. Vertex 3 connects to vertex 2.
           Vertex 4 does not connect to any.
    """
    graph = [[1], [0, 2], [1], []]
    assert number_of_components(graph) == 2
