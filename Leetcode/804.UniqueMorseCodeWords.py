
def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    results = set()

    for word in words:
      encoded_word = ''

      for letter in word:
        encoded_word += codes[(ord(letter) - 97)]
      results.add(encoded_word)
      
    return(len(results))


words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))