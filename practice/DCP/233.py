"""
This problem was asked by Apple.
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""


def fib(n):
    if n <= 1:
        return n

    last_last = 0
    last = 1
    x = 2
    while x <= n:
        curr = last_last + last
        last_last = last
        last = curr
        x += 1

    return last


if __name__ == '__main__':
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))