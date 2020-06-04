def compress(s):
  if len(s) == 0:
    return ''
  if len(s) == 1:
    return s + '1'

  map = {}
  for letter in s:
    if letter in map:
      map[letter] += 1
    else: 
      map[letter] = 1
    
  result = ''
  for k, v in map.items():
    result += k + str(v)

  return result

print(compress('AAABBBCCCaaabbbccc'))
print(compress('AAB'))
print(compress('AAB'))