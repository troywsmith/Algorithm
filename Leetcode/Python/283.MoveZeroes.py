def moveZeroes(nums):

    last_zero = 0
    curr = 0
    while curr < len(nums) and last_zero < len(nums):
        if nums[curr] != 0:
            nums[last_zero], nums[curr] = nums[curr], nums[last_zero]
            last_zero += 1
        curr += 1
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
print(moveZeroes([0, 0, 1]))
