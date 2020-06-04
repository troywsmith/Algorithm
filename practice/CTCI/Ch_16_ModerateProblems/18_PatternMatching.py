from collections import Counter


def is_match(value, pattern):
    """
    Time Complexity = O(V * P)
    Space Complexity = O(V)
    """
    if len(pattern) == 0:
        return len(value) == 0

    # Assigning first/second to a/b
    first = pattern[0]
    second = 'a' if first == 'b' else 'a'

    # Other variables we will need
    second_start = pattern.index(second)
    char_counts = Counter(pattern)

    for i in range(1, len(value)):

        # Find possible length of a string and b strings
        first_length = len(value[:i])
        second_length = (len(value) - (first_length * char_counts[first])) / char_counts[second]   # 2

        # Build possible a and b strings based on calculated lengths
        first_string = value[0:first_length]
        temp = first_length * second_start
        second_string = value[temp:temp + second_length]

        # Building a possible string based on a and b strings
        possible = ''
        for char in pattern:
            if char == first:
                possible += first_string
            if char == second:
                possible += second_string

        # If the possible string is the real value, return true
        if possible == value:
            return True

    # If we havent seen any matches, return false
    return False


if __name__ == '__main__':
    value = 'catcatgocatgo'
    pattern = 'bbaba'
    print(is_match(value, pattern))
