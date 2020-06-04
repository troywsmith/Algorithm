def strStr(haystack, needle):
  if len(needle) == 0:
    return 0
    
  if needle not in haystack:
    return -1
  else:
    return haystack.index(needle)
  

print(strStr('hello', 'll'))