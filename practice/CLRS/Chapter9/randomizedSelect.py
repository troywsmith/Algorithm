from random import randrange

def partition(arr, pivot_index=0):
    i = 0
    if pivot_index != 0:
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]

    for j in range(len(arr)-1):
        if arr[j+1] < arr[0]:
            arr[i+1], arr[j+1] = arr[j+1], arr[i+1]
            i += 1

    arr[0], arr[i] = arr[i], arr[0]
    return arr, i

def quickSelect(arr, k):

    if len(arr) == 1:
        return arr[0]

    else:
        part = partition(arr, randrange(len(arr)))
        arr = part[0]
        j = part[1]

        if j == k:
            return arr[j]

        elif j > k:
            return quickSelect(arr[:j], k)

        else:
            k = k - j - 1
            return quickSelect(arr[j+1:], k)


A = [1, 34, 234, 634, 235, 25, 523, 5, 25, 235, 25]
i = 4

sortedA = [quickSelect(A, x) for x in range(len(A))]

print(sorted(A))
print(sortedA)

# expected time complexity: O(n)
# worst case time complexity: O(n^2)