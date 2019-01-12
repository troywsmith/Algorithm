class Calculator:
    def multiply(self, a, b):

        # Find smaller and bigger
        smaller, bigger = (a, b) if a <= b else (b, a)

        # Store result in a variable, product
        product = 0

        # Add the bigger to product, the smaller amount of times
        while smaller > 0:
            product += bigger
            smaller -= 1

        # Return the product
        return product

    def negate(self, n):
        neg = 0
        new_sign = 1 if n < 0 else -1
        while n != 0:
            neg += new_sign
            n += new_sign
        return neg

    def subtract(self, a, b):

        # Add negative b to a
        return a + self.negate(b)

    def divide(self, a, b):

        # Store original b in temp variable
        c = b

        # Add b to itself until it equals a
        count = 1
        while a > b:

            b += c
            count += 1

        # Return count
        return count


if __name__ == '__main__':
    calc = Calculator()
    a = 12
    b = 4
    print(calc.multiply(a, b))
    print(calc.subtract(a, b))
    print(calc.divide(a, b))
