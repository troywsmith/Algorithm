class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph():
    """
    Directed, Weighted Graph
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertList.values())

    def getVertices(self):
        return self.vertList.keys()

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, vertA, vertB, cost=0):
        if vertA not in self.vertList:
            self.addVertex(vertA)
        if vertB not in self.vertList:
            self.addVertex(vertB)
        self.vertList[vertA].addNeighbor(self.vertList[vertB], cost)


def dfs(root):
    if not root:
        return
    print(root)
    root.visited = True
    visited = {}
    for v in g:
        for w in v.getConnections():
            if w not in visited:
                dfs(w)

    # for  in root.adjacent:
    #     if n.visited == False:
    #         dfs(n)


# def bfs(root):
#     if not root:
#         return
#     print(root)
#     q = Queue()
#     for n in root.adjacent:
#         q.enqueue(n)
#     while not q.isEmpty():
#         bfs(q.dequeue())


# Graph represented as an adjacency list
{'A': {'B'},
 'B': {'D', 'C'},
 'C': {'D'},
 'E': {'F'},
 'F': {'C'}}

# Graph represented as an adjacency matrix




if __name__ == "__main__":

    g = Graph()
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
