def merge_sort(arr):

  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  return merge_arrays(merge_sort(left), merge_sort(right))

def merge_arrays(a, b):

  merged = []
  while len(a) > 0 and len(b) > 0:
    
    if a[0] < b[0]:
      merged.append(a[0])
      a.pop(0)
    else: 
      merged.append(b[0])
      b.pop(0)
  
  merged += a + b
  return merged



print(merge_sort([1,4,2,3,7,6,5]))