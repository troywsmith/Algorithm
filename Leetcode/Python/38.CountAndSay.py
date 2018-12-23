def count_say(current):
    c = current[0]
    count = 0
    result = ""
    for s in current:
        if s != c:
            result += str(count)
            result += c
            flag = True
            count = 1
            c = s
        else:
            count += 1
    if count:
        result += str(count)
        result += c
    return result

def countAndSay(n):
    c_s = {1: "1", 2: "11"}
    for i in range(3, n+1):
        c_s[i] = count_say(c_s[i-1])
    return c_s[n]


print(countAndSay(4))
