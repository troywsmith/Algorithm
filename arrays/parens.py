def parens(n):
    openParen = '('
    closeParen = ')'

    combos = {
        0: [],
        1: ['()'],
        2: ['()()', '(())']
    }
    for x in range(3, n+1):

        last = combos[x-1]
        current = []
        for combo in last:
            temp = '(' + combo + ')'
            current.append(temp)
            # current.append()
        current.append(last[0] + '()')
        combos[x] = current
    
    return combos


if __name__ == "__main__":
    print(parens(4))
