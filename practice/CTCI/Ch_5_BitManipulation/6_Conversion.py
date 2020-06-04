"""
Write a function to determine the number of bits you would need to flip to convert interger A to interger B
"""


def bit_swaps_required(a, b):

    # Use XOR to find out which bits are different
    c = a ^ b
    bits_to_shift = 0
    while c != 0:
        bits_to_shift += 1
        c = c & (c-1)

    return bits_to_shift


if __name__ == '__main__':
    a = 124
    b = 125
    print(bit_swaps_required(a, b))
