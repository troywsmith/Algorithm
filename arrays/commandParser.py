"""
Implement a function to parse commands and take appropriate actions on a string.
"""


def getCommand():

    inputString = input('Please enter a string: ')

    commands = {
        1: 'split string',
        2: 'capitalize',
        3: 'lowercase',
        4: 'uppercase'
    }

    for num, command in commands.items():
        print("{}: {}".format(num, command))

    commandNumber = int(input('Please enter one of the listed commands: '))
    return commandNumber, inputString


def parseCommand():

    commandNumber, string = getCommand()

    commandFunctions = {
        1: (lambda: string, string.split(' ')),
        2: (lambda: string, string.capitalize()),
        3: (lambda: string, string.lower()),
        4: (lambda: string, string.upper()),
    }

    command, result = commandFunctions[commandNumber]
    return result


if __name__ == '__main__':
    ans = parseCommand()
    print(ans)
