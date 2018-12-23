A = [8, 24, 3, 20, 1, 17]

def solution(A):
    # Sort the array so we can compare elements next to each other
    # Using built-in sort to conserve time and have more efficient solution that one with O(n^2)
    sortedA = sorted(A)

    # Initialize the difference by the greatest possible difference 
    diff = 1000000 - 0

    # Iterate over sorted array, comparing each element
    for x in range(len(sortedA) - 1):

        # If the difference is less than the current diff, this is the new diff
        if sortedA[x + 1] - sortedA[x] < diff:
            diff = sortedA[x + 1] - sortedA[x]

    return diff

print(solution(A))