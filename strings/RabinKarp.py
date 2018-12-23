
d = 256
# RabinKarp Search
def search(txt, pat, q):
    N = len(txt)
    M = len(pat)
    h = (1 * 256) % q

    startIndex = 0
    endIndex = 0

    for x in range(N - M + 1):
        window = txt[x:x + M]
        print(window)


print(search('GEEKSFORGEEKS', 'GEEK'))
# print(search('ABDCBABDVDSF', 'DCB'))
