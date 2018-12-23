def solution(A):

    lights = []
    # sorted_arr = sorted(arr)

    # Loop through array
    for x in range(0, len(A) - 1):
        if A[x] > A[x + 1]:
          lights.append('False')
    
    return len(lights)


    # Push values to a separate data structure which you keep sorted.

    # check the sorted array to see if the lights should shine or not


A = [2, 1, 3, 5, 4]
print(solution(A))