# Question 1.3

# def URLify(s, n):
#   return s.replace(' ', '%20')


def URLify(s, trueLength):
    arr = list(s)

    index = len(s) - 1

    for i in range(trueLength-1, -1, -1):
        print(i)
        print(s[i])

        if s[i] == ' ':
            arr[index] = '0'
            arr[index-1] = '2'
            arr[index-2] = '%'
            index -= 3

        else:
            arr[index] = s[i]
            index -= 1

    return ''.join(arr)


print(URLify('Mr John Smith    ', 13))
