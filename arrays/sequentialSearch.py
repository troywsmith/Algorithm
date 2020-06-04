# Sequential Search

# Ordered Implementation
def search(arr, tar):
  """
  Input array must be sorted
  """
  pos = 0
  found = False
  stopped = False

  while pos < len(arr) and not found and not stopped:

    if arr[pos] == tar:
      found = True
    else:
      if arr[pos] > tar:
        stopped = True
      else:
        pos += 1

  return found


# # Unordered Implementation
# def search(arr, tar):
#   for i in range(len(arr)):
#     print(i, arr[i])

#     if arr[i] == tar:
#       return True
#   return False

print(search([1, 2, 3, 4, 5, 6, 7, 8], 4))