"""
Name: Floyd-Warshall Algorithm
Description: find shortest path between all pairs of vertices on a directed graph. negative edges allowed
Input: directed graph (n x n matrix)
Output: matrix of shortest paths between all pairs of vertices
Time Complexity: O(V^3)
Space Complexity: O(V)
Algorithm Technique: Dynamic Programming
"""

INF = float('inf')

def floydWarshall(graph):

    # initializing the solution matrix same as input graph matrix
    dist = graph
    V = len(dist)

    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the above picked source
            for j in range(V):

                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
    V = len(dist)
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF")),
            else:
                print("%7d\t" % (dist[i][j])),
            if j == V-1:
                print("")


# Driver program to test the above program
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

# Print the solution
floydWarshall(graph)
