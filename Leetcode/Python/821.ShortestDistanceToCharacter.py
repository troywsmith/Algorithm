def shortestDistance(word, char):

  distances = []

  char_indexes = []
  for x in range(len(word)):
    if word[x] == char:
      char_indexes.append(x)

  for x in range(len(word)):
    minimum = 10000
    for idx in char_indexes:
      val = abs(idx - x)
      if val < minimum:
        minimum = val

    distances.append(minimum)
  
  return distances


print(shortestDistance('loveleetcode', 'e'))