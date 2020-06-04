smalls = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
tens = [
    '',
    '',
    'twenty',
    'thirty',
    'fourty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]
bigs = [
    '',
    'thousand',
    'million',
    'billion',
]
hundred = 'hundred'
negative = 'negative'


def convertIntToPhrase(num):
    if num < 0:
        return negative + convertIntToPhrase(-1*num)
    elif num < 10:
        return smalls[num]

    phrase = []
    num = str(num)
    N = len(num)
    for i in range(N):
        place = N-1-i
        digitPhrase = smalls[int(num[i])]
        placePhrase = tens[place]

        current = " {} {}".format(digitPhrase, placePhrase)
        phrase.append(current)

    return ''.join(phrase)


if __name__ == '__main__':
    tests = [123, 0, -123, 100123456]
    for test in tests:
        ans = convertIntToPhrase(test)
        print('{} -> {}'.format(test, ans))
