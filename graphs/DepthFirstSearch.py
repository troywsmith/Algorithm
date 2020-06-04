

# Recursive Version
parent = {s: None}
def DFS_visit(Adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_visit(Adj, v)


# To visit all nodes
def DFS(V, Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(Adj, s)