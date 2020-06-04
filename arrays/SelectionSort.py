def selection_sort(arr):

    for x in range(len(arr) - 1):

      minimumIndex = x

      for y in range(x, len(arr)):

        if arr[y] < arr[minimumIndex]:

          minimumIndex = y

      temp = arr[x]
      arr[x] = arr[minimumIndex]
      arr[minimumIndex] = temp

    return arr

print(selection_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))