def isValid(string):
    if len(string) == 0:
        return True

    matches = { ")": "(", "}": "{", "]": "[" }
    stack = []

    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            top_char = stack.pop() if stack else '#'
            if matches[char] != top_char:
                return False
    
    if stack: return False
    else: return True


print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))