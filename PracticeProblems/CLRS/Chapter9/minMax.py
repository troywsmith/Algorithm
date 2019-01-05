def findMinMax(arr):

    n = len(arr)

    smallest, largest = arr[0], arr[0]
    
    # if n is odd, start from first element
    if n % 2 != 0:
      start = 1
    else:
      start = 0

    for x in range(start, n, 2):

        # compare left and right
        small = min(arr[x], arr[x+1])
        big = max(arr[x], arr[x+1])

        if small < smallest:
            smallest = small

        if big > largest:
            largest = big

    return (smallest, largest)

print(findMinMax([251, 234, 765, 234, 76, 34, 764, 243, 5434]))

# time complexity: O(n) => O(3n/2 )