def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current = 0
    sm = 0
    while current < len(nums) - 1:
        print(current, nums[current])

        x = 0

        if nums[current] < nums[current + 1]:
            x = 1

        sm += nums[current + x]

        current += 2 + x


# print(rob([1,2,3,1]))
print(rob([2, 7, 9, 3, 1]))
