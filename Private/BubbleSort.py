def bubble_sort(arr):

  for x in range(len(arr) - 1):

    for y in range(len(arr) - 1):

      left = arr[y]
      right = arr[y + 1]

      if left > right:
        arr[y], arr[y + 1] = arr[y + 1], arr[y]
  
  return arr

print(bubble_sort([1,4,2,3,7,6,5]))