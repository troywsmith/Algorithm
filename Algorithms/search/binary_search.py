def binarySearch(arr, tar):

  # Base Case
  if len(arr) == 0:
    return False
  
  # Recursive Case
  else:
    mid = len(arr) // 2

    if arr[mid] == tar:
      return True

    else:
      if tar < arr[mid]:
        return binarySearch(arr[:mid], tar)
        
      else:
        return binarySearch(arr[mid + 1:], tar)

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 10))