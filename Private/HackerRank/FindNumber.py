# def findNum(arr, k):
#   if k in arr:
#     return 'YES'
#   else:
#     return 'NO'
  
# print(findNum([1,2,5,3,5,2,5,245,2], 3))

def oddNumbers(l, r):

  odds = []
  for i in range(l, r + 1):
    if i % 2 != 0:
      odds.append(i)
  return odds

print(oddNumbers(34, 223))