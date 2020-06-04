"""
Write a program to swap off and even bits in an integer with as few instructions as possible.
"""


def swap(x):
    even_mask = 0b10101010101010101010101010101010
    odd_mask = 0b01010101010101010101010101010101
    return (x & even_mask) >> 1 | (x & odd_mask) << 1


if __name__ == '__main__':
    x = 13
    print(swap(x))