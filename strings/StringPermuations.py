def permute(s):

  result = []
  if len(s) == 1:
    result = [s]
  else:
    for i, char in enumerate(s):
      for perm in permute(s[:i] + s[i+1:]):
        result += [char + perm]
  
  return result

print(permute('abc'))
# should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']