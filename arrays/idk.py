"""
Given an array of sorted integers, 
return a string array that contains the ranges of consecutive integers
"""


def create_range(lower, upper):
    s = str(lower) + '-' + str(upper)
    return s


def hi(arr):

    rangeString = ''
    isRange = False

    for i in range(0, len(arr)):

        while (i < len(arr) - 1 and arr[i] + 1 == arr[i + 1]):

            if not isRange:
                rangeString += str(arr[i])
                isRange = True
                i += 1

        if isRange:
            rangeString += '-'
            isRange = False
        
        rangeString += str(arr[i])

    return rangeString


if __name__ == "__main__":
    arr = [-2, 0, 1, 2, 3, 4, 5, 8, 9, 11, 13, 15, 18, 22, 25, 28, 29, 30]
    print(hi(arr))
