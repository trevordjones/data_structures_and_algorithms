"""
Problem: Acyclicity
Task: Check whether a given directed graph with n vertices and m edges contains a cycle.
"""

def is_acyclic(graph):
    """
    :param list[list[int]] graph: A graph represented as a matrix.

    :rtype boolean
    :returns true if graph is acyclic. False otherwise.
    """
    visited = [False] * len(graph)
    stack = [False] * len(graph)

    for node in range(len(graph)):
        if visited[node] is False:
            if is_cyclic(graph, node, stack, visited) is True:
                return True

    return False

def is_cyclic(graph, node, stack, visited):
    """
    :param list[list[int]] graph: A graph represented as a matrix.
    :param int node: The node to check if there is a cycle.
    :param list[boolean] stack: Track if any of the nodes connected to node are cyclic.
    :param list[boolean] visited: Track if node has been visited.
    """
    visited[node] = True
    stack[node] = True

    for connected_node in graph[node]:
        if visited[connected_node] is False:
            if is_cyclic(graph, connected_node, stack, visited) is True:
                return True
        elif stack[connected_node] is True:
            return True

    stack[node] = False
    return False

if __name__ == '__main__':
    """
    graph: The index of the inner array represents a vertex. The numbers in
           the inner array indicate which vertices they connect to. A graph
           the values [[1], [0,2], [1], []] means vertex 1 connects to vertex 2.
           Vertex 2 connects to vertices 1 and 3. Vertex 3 connects to vertex 2.
           Vertex 4 does not connect to any.
    """
    graph = [[1], [2], [0], [0]]
    assert is_acyclic(graph) == True

    graph = [[1, 2, 3], [2, 4], [3, 4], [], []]
    assert is_acyclic(graph) == False
