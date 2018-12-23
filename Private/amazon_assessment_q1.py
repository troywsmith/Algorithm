import math

# Comparator to find location closer to origin
def getDistanceBetweenCoords(loc1, loc2):
    x1, y1 = loc1[0], loc1[1]
    x2, y2 = loc2[0], loc2[1]
    distance1 = math.sqrt(x1**2 + y1**2)
    distance2 = math.sqrt(x2**2 + y2**2)
    
    if distance1 > distance2:
        return 1 
    elif distance2 > distance1:
        return -1
    else:
        return 0

def nearestXsteakHouses(totalSteakhouses, allLocations, numSteakhouses):
    
    # Sort locations by distance from
    allLocations.sort(cmp = getDistanceBetweenCoords)
    
    # Since locations are ordered, return first locations up to amount required
    return allLocations[:numSteakhouses]


totalSteakhouses = 3
locations = [[1,-3], [1,2], [3,4]]
numSteakhouses = 1

nearestXsteakHouses(totalSteakhouses, locations, numSteakhouses)