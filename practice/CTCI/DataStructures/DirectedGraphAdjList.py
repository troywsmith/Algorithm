from collections import defaultdict

class Graph():
    """
    Directed graph using adjacency list representation
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, cost=0):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True