import random


def randomizeInPlace(arr):
    print(arr)

    n = len(arr)
    for i in range(n):
        j = random.randint(i, n-1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


print(randomizeInPlace([1, 2, 3]))