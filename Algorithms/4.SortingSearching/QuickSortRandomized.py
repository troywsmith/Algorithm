import random

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def randomizedPartition(arr, low, high):
  i = random.randint(low, high)
  arr[high], arr[i] = arr[i], arr[high]
  print(arr)
  return partition(arr, low, high)


def quicksort(arr, low, high):
    if low < high:
        pivot = randomizedPartition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


arr = [2, 8, 7, 1, 3, 5, 6, 4]
print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)