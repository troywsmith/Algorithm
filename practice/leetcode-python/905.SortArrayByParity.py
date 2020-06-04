def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    return [num for num in A if num % 2 == 0] + [num for num in A if num % 2 != 0]
    # ls = [] 
    # for num in A:
    #   ls.insert(0, num) if num % 2 == 0 else ls.append(num)
    # return ls 

print(sortArrayByParity([3, 1, 2, 4]))