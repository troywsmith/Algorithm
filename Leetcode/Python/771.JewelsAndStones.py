def numJewelsInStones(J, S):
    count = 0
    for letter in S:
        if letter in J:
            count += 1
    return count

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))
