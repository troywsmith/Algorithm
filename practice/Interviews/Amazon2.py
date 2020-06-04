from collections import deque

def removeObstacle(numRows, numColumns, lot):
    """BFS to find the obstacle"""
    
    # Define the objects on the grid
    flat = 1
    trench = 0
    obstacle = 9
    
    # The robots starting point
    start = (0, 0)
    
    d = deque([[start]])
    seen = set([start])
    
    # While there are still possible paths to search
    while d:
        path = d.popleft()
        x, y = path[-1]
        
        # If the current element is a 9, we have found the obstacle
        if lot[y][x] == obstacle:
            return len(path) - 1
            
        # Check all possible directions
        for x2, y2 in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if 0 <= x2 < numColumns and 0 <= y2 < numRows and lot[y2][x2] != trench and (x2, y2) not in seen:
                d.append(path + [(x2, y2)])
                seen.add((x2, y2))
    
    # The robot cannot possibly find the obstacle
    return -1