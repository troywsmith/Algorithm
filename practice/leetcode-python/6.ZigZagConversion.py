def convert(string, numRows):
    index = {}
    m = 1
    n = numRows-1
    if len(string) == numRows or len(string) <= numRows or numRows == 1:
        return string
    else:
        for i in string:
            if m > numRows and n != 0:
                index[n] += i
                n -= 1
            elif m > numRows and n == 0:
                m = 2
                n = numRows-1
                index[m] += i
                m += 1
            else:
                if m not in index.keys():
                    index[m] = i
                else:
                    index[m] += i
                m += 1
    converted_string = ""
    for i in range(1, numRows+1):
        converted_string += index[i]
    return converted_string


print(convert('PAYPALISHIRING', 3))
# print(convert('PAYPALISHIRING', 4))
