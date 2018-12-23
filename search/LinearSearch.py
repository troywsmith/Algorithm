def linearSearch(arr, target):

    for x in range(len(arr)):
      
      if arr[x] == target:
        return True
    
    return False

print(linearSearch([1,3,5,2,6,2,67,46,534,545], 4))