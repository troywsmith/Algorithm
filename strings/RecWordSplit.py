def split(phrase, list_of_words, output = None):
  if output is None:
    output = []

  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)
      return split(phrase[len(word):], list_of_words, output)
  
  return output

print(split('i am a phrase', ['am', 'phrasee', 'hi', 'how', 'a', 'i']))