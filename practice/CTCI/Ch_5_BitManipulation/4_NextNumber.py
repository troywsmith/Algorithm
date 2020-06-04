# def next_number(n):
#     n = list(str(bin(n))[2:])
#     print(n)

#     # SMALLER
#     smaller = n[:]
#     smaller[0] = '0'
#     smaller[len(smaller)-1] = '0'
#     i = 1
#     while i < len(smaller):

#         # Flip first 0 to one
#         if smaller[i] == '0':
#             smaller[i] = '1'

#             # Iterate to right and make first 0 1
#             z = i + 1
#             while z < len(smaller):

#                 if smaller[z] == '0':
#                     smaller[z] = '1'
#                     break
#                 else:
#                     z += 1
#             break

#         else:
#             i += 1

#     # BIGGER
#     bigger = n[:]
#     j = len(bigger) - 1
#     while j > -1:

#         # Flip rightmost 0
#         if bigger[j] == '0':
#             bigger[j] = '1'

#             z = j + 1
#             while z < len(bigger):
#                 if bigger[z] == '1':
#                     bigger[z] = '0'
#                     break
#                 else:
#                     z += 1
#             break

#         else:
#             j -= 1

#     smaller = int(''.join(smaller))
#     bigger = int(''.join(bigger))
#     return (smaller, bigger)


def next(n, ones, direction):

    if direction == 'bigger':
        n += 1
    elif direction == 'smaller':
        n -= 1

    found = False
    while not found:

        binary = bin(n)
        count = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                count += 1

        if count == ones:
            return binary

        else:
            if direction == 'bigger':
                n += 1
            elif direction == 'smaller':
                n -= 1

    return -1


def next_number(n):

    binary = bin(n)
    print(binary)
    print(binary[6])

    ones = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            ones += 1

    next_bigger = next(n, ones, 'bigger')
    next_smaller = next(n, ones, 'smaller')
    return (next_bigger, next_smaller)


if __name__ == '__main__':
    n = 100
    result = next_number(n)
    print('Next smaller: {} ({})'.format(result[0], int(result[0], 2)))
    print('Next bigger: {} ({})'.format(result[1], int(result[1], 2)))
