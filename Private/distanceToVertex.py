import math

def getDistanceBetweenCoords(loc1, loc2):
    x1, y1 = loc1[0], loc1[1]
    x2, y2 = loc2[0], loc2[1]
    distance1 = math.sqrt((2 - x1)**2 + (2 - y1)**2)
    distance2 = math.sqrt((2 - x2)**2 + (2 - y2)**2)
    print(distance1, distance2)
    if distance1 > distance2:
        return 1 
    elif distance2 > distance1:
        return -1
    else:
        return 0

def kClosest(points, k):
    
    # Sort locations by distance from
    sortedPoints = sorted(points, key = getDistanceBetweenCoords)
    
    # Since locations are ordered, return first locations up to amount required
    print(sortedPoints)
    # return sortedPoints[k]


pts = [[1, 2], [3, -1], [2, 1], [2, 3]]
vtx = [2, 2]
print(kClosest(pts, 2))
