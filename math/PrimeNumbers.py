"""
Write a method to return all prime numbers less than a number, N
"""


def primeNumbers(N):

    primes = []
    for x in range(2, N):

        prime = True
        factor = 2
        while factor < x and prime:
            if x % factor == 0:
                prime = False

            factor += 1

        if prime:
            primes.append(x)

    return primes


if __name__ == '__main__':
    N = 50
    print(primeNumbers(N))
