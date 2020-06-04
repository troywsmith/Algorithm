class Dictionary(object):
    def __init__(self):
        self.words = {}

    def AddWord(self, word):
        key = len(word)
        if key in self.words:
            self.words[key].add(word)
        else:
            self.words[key] = set()
            self.words[key].add(word)

    def SearchWord(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        key = len(word)

        if key not in self.words:
            return False

        words = self.words[key]

        if word in words:
            return True

        for i in range(key):
            if word[i] == '.':
                continue

            words = {wd for wd in words if wd[i] == word[i]}
            if not words:
                return False

        return True


s = Dictionary()
s.AddWord('tokyo')
s.AddWord('hello')
s.AddWord('helo')
print(s.words)

print(s.SearchWord('tokyo'))
print(s.SearchWord('h.llo'))
print(s.SearchWord('hill.'))
