"""
Problem: Computing the Minimum Number of Flight Segments
Task: Given an undirected graph with n vertices and m edges and two vertices u and v,
      compute the length of a shortest path between u and v (that is, the minimum
      number of edges in a path from u to v).
"""

def distance(graph, source, sink):
    """
    :param list[list[int]] graph: A graph represented as a matrix
    :param int source: Where to start in bfs
    :param int sink: Where to end in bfs

    :rtype int
    :returns Minimum distance between the source and the sink. Return -1 if
             there is no path
    """
    if source > sink:
        tmp = sink
        sink = source
        source = tmp
    dist = [None] * len(graph)
    prev = [None] * len(graph)

    dist[source] = 0
    queue = [source]

    while queue:
        nodes_index = queue.pop(0)
        for node in graph[nodes_index]:
            if dist[node] is None:
                queue.append(node)
                dist[node] = dist[nodes_index] + 1
                prev[node] = nodes_index

    if prev[sink] is None:
        return -1

    count = 0
    while sink != source:
        sink = prev[sink]
        count += 1

    return count

if __name__ == '__main__':
    graph = [[1, 3, 2], [0, 2], [1, 0], [0]]
    assert distance(graph, 1, 3) == 2

    graph = [[2, 3], [4], [0, 3], [2, 0], [1]]
    assert distance(graph, 2, 4) == -1
