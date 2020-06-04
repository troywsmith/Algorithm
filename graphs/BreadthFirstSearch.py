def BFS(s, Adj):
    """
    s: the node we are starting from
    Adj: the adjacency list that shows all edges
    """
    level = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for node in frontier:
            for v in Adj[node]:
                if v not in level:
                    level[v] = i
                    next.append(node)

        frontier = next
        i += 1
