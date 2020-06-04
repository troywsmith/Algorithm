"""
Write a function to swap a number in place
"""


def number_swapper(a, b):
    a, b = b, a
    return (a, b)


if __name__ == '__main__':
    a, b = 10, 5
    print(number_swapper(a, b))
