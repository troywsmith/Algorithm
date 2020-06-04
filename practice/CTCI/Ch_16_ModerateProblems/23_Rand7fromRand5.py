import random


def rand5():
    return random.randint(0, 4)


def rand7():

    # Get a random number from from 0-3
    n = float(rand5())
    print(n)

    # Multiply that so its in the range 0-1 (reduce range from 0-4 to 0-1)
    n /= 4
    print(n)

    # Multiply that num by 7
    n *= 6

    return int(n)


if __name__ == '__main__':

    print(rand7())
