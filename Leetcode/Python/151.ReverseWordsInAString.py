# x = "the sky is blue"
x = "   a   b "

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join(reversed(s.split()))

print(reverseWords(x))