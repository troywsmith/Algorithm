romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def convert(stringString):
    result = 0
    string = list(stringString)
    while (len(string)):
        current = romans[string[0]]
        try:
            next = romans[string[1]]
        except:
            next = 0

        if current < next:
            result += next - current
            string.pop(0)
            string.pop(0)
        else:
            result += current
            string.pop(0)

    return result


print(convert('III'))
print(convert('IV'))
print(convert('IX'))
print(convert('LVIII'))
print(convert('MCMXCIV'))
