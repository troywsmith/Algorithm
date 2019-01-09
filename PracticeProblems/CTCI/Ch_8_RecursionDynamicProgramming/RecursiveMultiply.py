# def Multiply(a, b):
#     """
#     Solution: Iterative addition
#     Operations: min(a, b) / 2
#     """
#     ops = 0
#     smaller, bigger = (a, b) if a <= b else (b, a)
#     # Variable we will increment by bigger, smaller times
#     product = 0
#     while smaller > 0:
#         ops += 1
#         product += bigger
#         smaller -= 2
#     if smaller % 2 == 1:
#         return product + product - bigger
#     else:
#         return product + product


def Multiply(a, b, product=0):
    """
    Solution: Recursive addition
    Time Complexity: log s
    """
    smaller, bigger = (a, b) if a < b else (b, a)
    return recurseHelper(smaller, bigger)


def recurseHelper(smaller, bigger):

    # Base cases
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    # Divide smaller by 2
    s = smaller >> 1

    # Get half product
    halfProd = recurseHelper(s, bigger)

    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


if __name__ == '__main__':
    a = 4
    b = 5
    ans = Multiply(a, b)
    print('Product: {}'.format(ans))
    print('Correct: {}'.format(ans == a*b))

else:
    print('Importing: Recursive Multiplication Algorithm')