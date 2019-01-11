"""
Given an integer, print an english phrase that describes the integer
"""

def print_int_phrase(n):

    lookup = {
        '0': ' zero ',
        '1': ' one ',
        '2': ' two',
        '3': ' three ',
        '4': ' four ',
        '5': ' five ',
        '6': ' six ',
        '7': ' seven ',
        '8': ' eight ',
        '9': ' nine '
    }

    loop_2 = {
        '0': ' ty ',
        '1': ' ten ',
        '2': ' twenty',
        '3': ' thirty ',
        '4': ' forty ',
        '5': ' five ',
        '6': ' six ',
        '7': ' seven ',
        '8': ' eight ',
        '9': ' nine '
    }

    n_str = str(n)

    phrase = []

    place = len(n_str) - 1

    i = 0
    while i < len(n_str):

        digit = n_str[i]
        print(i, digit, place)

        phrase.append(lookup[digit])

        if place == 2:
            phrase.append('hundred')

        if i == 1:
            phrase += 'ty'

        i += 1

    return ''.join(phrase)


n = 234
print(print_int_phrase(n))
