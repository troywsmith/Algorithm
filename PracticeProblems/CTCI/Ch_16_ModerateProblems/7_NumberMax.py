"""
Write a method that finds the maximum of two numbers. You should not use if-else or any other comparator operator
"""


def find_max(a, b):
    
    x = float(a) * 3.0
    y = float(b) * 3.0
    print(x, y)

    return abs((y / x)) * b

if __name__ == '__main__':
    a = 1234
    b = 2134
    print(find_max(a, b))
