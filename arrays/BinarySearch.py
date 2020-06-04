"""
Binary Search:
- Sort List
- Start by examining middle item
- If that item is the target, we are done
- If the middle item is greater than the target, search the lower half
- If the middle item is less than the target, search the higher half
"""

# Iterative Implementation
def BinarySearch(arr, tar):

    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:

        mid = int((first + last) / 2)

        if tar == arr[mid]:
            found = True
        else:
            if tar < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


## Recursive Implementation
def BinarySearch(arr, tar):

  # Base Case
  if len(arr) == 0:
    return False

  # Recursive Case
  else:
    mid = int(len(arr) / 2)

    if arr[mid] == tar:
      return True

    else:
      if tar < arr[mid]:
        return BinarySearch(arr[:mid], tar)
      else:
        return BinarySearch(arr[mid + 1:], tar)
      
  
  

print(BinarySearch([17, 20, 26, 31, 44, 54, 55, 65, 77, 93], 53))
