from collections import deque


def decodeString(s):
    """
    :type s: str
    :rtype: str
    """

    stack = deque()
    curr_string = ''
    curr_num = 0

    for char in s:

        print(curr_string)

        if char == '[':
            stack.append(curr_string)
            stack.append(curr_num)
            curr_string = ''
            curr_num = 0

        elif char == ']':
            num = stack.pop()
            prev_string = stack.pop()
            curr_string = prev_string + curr_string * num

        elif char.isdigit():
            curr_num = curr_num * 10 + int(char)

        else:
            curr_string += char

    return curr_string


if __name__ == '__main__':

    s = "3[a]2[bc]"     # "aaabcbc".
    # s = "3[a2[c]]"      # "accaccacc".
    # s = "2[abc]3[cd]ef"  # "abcabccdcdcdef".
    decoded_string = decodeString(s)
    print(decoded_string)
