from collections import defaultdict


def main(n):
    memo = defaultdict()
    getCombos(n, memo)
    return memo[n]


def getCombos(n, memo):
    if n == 1:
        return ['()']
    else:
        # Get combos from n-1, add a paren to each combo and add all perms
        memo[n-1] = getCombos(n-1, memo)
        memo[n] = addAnotherParenToCombos(memo[n-1])
        return memo[n]


def addAnotherParenToCombos(last_combos):
    # Get combos from n-1, add a paren to each combo and add all perms
    new_combos = set()
    for combo in last_combos:
        x = 0
        y = len(combo)
        while y >= 0:
            openParen = '('
            left = combo[:y]
            closeParen = ')'
            right = combo[y:]
            new = openParen + left + closeParen + right
            if new not in new_combos:
                new_combos.add(new)
            y -= 1

        x = 0
        y = len(combo)
        while x <= len(combo):
            openParen = '('
            left = combo[:x]
            closeParen = ')'
            right = combo[x:]
            new = left + openParen + right + closeParen
            if new not in new_combos:
                new_combos.add(new)
            x += 1

    return new_combos


if __name__ == '__main__':
    n = 3
    combos = main(n)
    print('With 3 parentesis, we get the following combos')
    for i, combo in enumerate(combos):
        print(i+1, combo)

else:
    print('Importing: Parenthesis Combonations Algorithm')