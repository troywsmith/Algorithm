def ReverseSentence(str):
  return ' '.join(str.split()[::-1])

print(ReverseSentence('This is the best'))
print(ReverseSentence('Hi John,     are you ready to go'))