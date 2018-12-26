def findComplement(num):
    bin = '{0:b}'.format(num)
    inversed = ''
    for digit in bin:
        inversed += '1' if digit == '0' else '0'
    return int(inversed, 2)

print(findComplement(5))
print(findComplement(1))
