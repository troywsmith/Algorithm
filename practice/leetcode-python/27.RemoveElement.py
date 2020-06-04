# Solution 1: O(n)
def removeElement(nums, val):
  nonValueCount = 0
  for x in range(len(nums)):
    if nums[x] != val:
      nums[nonValueCount] = nums[x]
      nonValueCount += 1
  return nonValueCount

# Solution 2: Could be O(n^2)
# def removeElement(nums, val):
#   while val in nums: nums.pop(nums.index(val))
#   return len(nums)

print(removeElement([3,2,2,3], 3))