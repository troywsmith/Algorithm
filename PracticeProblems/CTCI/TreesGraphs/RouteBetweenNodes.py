from collections import deque


def find_path(graph, start, end):
    """
    Find the shortest in an undirected 'graph' between 'start' and 'end'
    If no path exists, returns 'None'
    """
    if start == end:
        return [start]

    visited = {start}

    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == end:
                return path + [current, neighbor]

            if neighbor in visited:
                continue

            queue.append((neighbor, path + [current]))
            visited.add(neighbor)

    return None


if __name__ == '__main__':
    graph = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E']),
    }
    path = find_path(graph, 'A', 'F')
    if path:
        print(path)
    else:
        print('no path found')
