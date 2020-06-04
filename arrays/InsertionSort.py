def insertion_sort(arr):

  for x in range(1, len(arr)):

    position, currentValue = x, arr[x]

    while position > 0 and arr[position - 1] > currentValue:
      
      arr[position] = arr[position - 1]
      position -= 1

    arr[position] = currentValue

  return arr

print(insertion_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))