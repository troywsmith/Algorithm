"""
This problem was asked by Bloomberg.
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.
Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
"""


def find_last_prisoner(n, k):

    # Will be used to store the order of executions
    execution_order = []

    # Initialize prisoners array
    prisoners = [x+1 for x in range(n)]

    # Rotate array so the kth prisoner is in the front
    prisoners = prisoners[k-1:] + prisoners[:k-1]

    # Execute prisoners
    for _ in range(n):

        # Add executed prisoner
        execution_order.append(prisoners[0])

        # Rotate array and remove executed prisoner
        prisoners = prisoners[k:] + prisoners[1:k]

    # Return the last executed prisoner
    return execution_order[len(execution_order)-1]


if __name__ == '__main__':
    n = 5
    k = 2
    last_prisoner = find_last_prisoner(n, k)
    print('Last Prisoner: {}'.format(last_prisoner))
