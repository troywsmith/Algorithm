# 
# min length = 
# max length = 
# maxUnique 

def count_unique_chars(s):
  return len(list(set(s)))

def getMaxOccurences(s, min, max, maxUnique):

  arr = []

  for index in range(0, len(s)):
    
    index_2 = index + 1

    substring = s[index:index_2]

    # str_length = index_2

    while str_length <= max:

      if len(substring) >= min:
        substring = s[index:index_2]

        if count_unique_chars(substring) <= maxUnique:
          arr.append(substring)

        index_2 += 1
        str_length = index_2 - index

  return arr 

print(getMaxOccurences('abcde', 2, 4, 26))