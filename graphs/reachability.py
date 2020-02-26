"""
Problem: Finding an Exit from a Maze
Task: Given an undirected graph and two distinct vertices u and v,
      check if there is a path between u and v.
"""


def is_reachable(graph, u, v):
    """
    param: list[list[int]] graph: A graph represented as a matrix
    param: int u: Starting from vertex in the graph
    param: int v: Ending vertex in the graph

    :rtype boolean
    :returns Whether the two vertices are connected
    """

    visited = [[] for _ in range(len(graph))]
    return explore(graph, u, v, visited)

def explore(graph, u, v, visited):
    """
    param: list[list[int]] graph: A graph represented as a matrix
    param: int u: Starting from vertex in the graph
    param: int v: Ending vertex in the graph
    :param list[list[boolean]] visited: Mimics graph to track if a vertex has been visited

    :rtype boolean
    :returns Whether the two vertices are connected
    """

    if not graph[u] or not graph[v]:
        reachable = False
    else:
        for idx, vertex in enumerate(graph[u]):
            if vertex in graph[v]:
                visited[vertex].append(True)
                reachable = True
                break
            else:
                reachable = False
            try:
                visited[u][idx]
                continue
            except:
                visited[u].append(True)
                reachable = explore(graph, vertex, v, visited)
                if reachable:
                    break

    return reachable

if __name__ == '__main__':
    graph = [[1, 3], [0, 2], [1, 3], [2, 0]]
    assert is_reachable(graph, 0, 3) == True

    graph = [[1], [0, 2], [1], []]
    assert is_reachable(graph, 0, 3) == False
