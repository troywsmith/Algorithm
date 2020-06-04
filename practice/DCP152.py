# This problem was asked by Triplebyte.
# You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.
# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
# You can generate random numbers between 0 and 1 uniformly.

import random

def Generator(numbs, probs):
  
  ls = []
  counter = 0
  for x in range(len(numbs)):
    counter += probs[x]
    ls.append( (counter, numbs[x]) )

  ran = random.uniform(0, 1)
  print(ls)
  print(ran)

  count = 0
  for item in ls:
    if ran < ls[count][0]:
      return(ls[count][1])
    
    count += 1

print(Generator([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2]))