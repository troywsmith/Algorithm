from collections import defaultdict, Counter

# def group_anagrams(words):
# """
# Description: Method storing words into buckets based on char counts
# """
#     # Hash Table for words. key=freqString, value=words with that freq string
#     freqMap = defaultdict(list)

#     # Iterate through words
#     for word in words:
#         freqString = ''
#         freqCount = Counter()
#         for char in word:
#             freqCount[char] += 1

#         # Make freqString with freqMap
#         for char, freq in freqCount.items():
#             freqString += char + str(freq)

#         # Store word in hash table above
#         freqMap[freqString].append(word)

#     print(freqMap)

#     # For each bucket of words in hash table
#     left = 0
#     right = len(words) - 1
#     for freqString, bucket in freqMap.items():

#         # Not anagrams
#         if len(bucket) == 1:
#             words[right] = bucket[0]
#             right -= 1

#         # Anagrams
#         elif len(bucket) > 1:
#             for wd in bucket:
#                 words[left] = wd
#                 left += 1

#     return words


def group_anagrams(words):
    """
    Description: Method storing words into buckets based on their sorted version
    """

    # Hash Table for words. key=freqString, value=words with that freq string
    sorted_words_buckets = defaultdict(list)

    # Iterate through words
    for word in words:

        # Sort word
        sorted_word = ''.join(sorted(word))

        # Place sorted word into sorted words buckets
        sorted_words_buckets[sorted_word].append(word)

    # For each bucket of words in hash table
    left = 0
    right = len(words) - 1
    for sorted_word, bucket in sorted_words_buckets.items():

        # Not anagrams
        if len(bucket) == 1:
            words[right] = bucket[0]
            right -= 1

        # Anagrams
        elif len(bucket) > 1:
            for wd in bucket:
                words[left] = wd
                left += 1

    return words


words = ['race', 'dsgg', '342', 'acre', 'rice', 'ecar', 'ggsd']
new_words = group_anagrams(words)
print(new_words)
