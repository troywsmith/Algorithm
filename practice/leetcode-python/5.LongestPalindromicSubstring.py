def longestPalindrome(s):
    rs = s[::-1]
    if s == rs:
        return s
    if len(s) == 2:
        return s[0]

    longest = ''
    for x in range(len(s)):
        if s[x] == rs[x]:
            # print(s[x:])
            # print(rs[x:])

            curr = ''

            for y in range(x, len(s)):
                if s[y] == rs[y]:
                    curr += s[y]

            if len(curr) > len(longest):
                longest = curr

    return longest


# print(longestPalindrome('babad'))
print(longestPalindrome('abb'))
