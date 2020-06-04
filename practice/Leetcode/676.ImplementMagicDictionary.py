from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            n = len(word)
            self.words[n].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)

        if not n in self.words:
            return False

        for wd in self.words[n]:

            incorrect = 0
            for x, char in enumerate(wd):
                if word[x] != char:
                    incorrect += 1
                    if incorrect > 1:
                        break

            if incorrect == 1:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)