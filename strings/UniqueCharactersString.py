def uni_char(s):

  # Solution 1
  # return len(set(s)) == len(s)

  # Solution 2
  if len(s) < 2:
    return True
  
  map = {}
  for char in s:
    if char in map:
      map[char] += 1 
    else:
      map[char] = 1

  for val in map.values():
    if val > 1:
      return False
    
  return True

print(uni_char('abcde')) # True
print(uni_char('abcda')) # False