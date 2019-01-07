def buildPowerSet(arr):
    """
    Time Complexity: O(n2^n)
    Space Complexity: O(n2^n)
    """
    powerset = [[]]
    for i in range(len(arr)):
        num = arr[i]
        curr_combos = powerset[:]
        for combo in powerset:
            new = combo[:]
            new.append(num)
            curr_combos.append(new)
        powerset = curr_combos
    return powerset


if __name__ == '__main__':
    arr = [2, 4, 5, 10]
    powersets = buildPowerSet(arr)
    print(powersets)
    print('RESULT # of sets in powerset: {} - {}'.format(len(powersets),
                                                         len(powersets) == 2**len(arr)))

else:
    print('Importing: Powerset Algorithm')
