def find_array_quadruplet(arr, s):
  
  if arr == []:
    return []
  
  arr.sort()
  print(arr)
  
  # for i in range(len(arr)-3):
  #   for j in range(i+1, len(arr)-2):
  #     diff = s - arr[i] - arr[j]
      
  #     x = j+1
  #     y = len(arr) - 1
      
  #     while x < y:
        
  #       curr_sum = arr[x] + arr[y]
        
  #       if curr_sum == diff:
  #         return [arr[i],arr[j],arr[x],arr[y]]
        
  #       elif curr_sum > diff:
  #         y -= 1
          
  #       else:
  #         x += 1
      
  # return []
      