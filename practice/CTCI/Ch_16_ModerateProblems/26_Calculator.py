import re

def calculate(equation):

    # Store answer
    result = 0

    # operator_order = ['*', '/', '+', '-']
    operator_order = ['*']

    # Split the string on operations (*,/,+,-)
    e = equation.split('*')
    e = equation.split('/')
    e = equation.split('+')
    e = equation.split('-')

    print(e)

    for operator in operator_order:

        # Iterate through string
        x = 0
        y = 1
        z = 2
        while z < len(e):

            # look for operator
            if e[y] == '*':
                ans = int(e[x]) * int(e[z])
                e[x] = '_'
                e[y] = '_'
                e[z] = float(ans)

    return e


if __name__ == '__main__':
    e = '2*3+5/6*3+15'
    print(calculate(e))
