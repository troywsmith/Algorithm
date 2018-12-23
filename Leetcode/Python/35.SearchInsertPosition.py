# Solution 1: Binary Search solution -> O(log n)
def searchInsert(nums, target, count=0):
  if len(nums) < 1:
    return count
  else:
    midIndex = len(nums) // 2
    if target == nums[midIndex]:
      return midIndex + count
    else:
      if target < nums[midIndex]:
        return searchInsert(nums[:midIndex], target, count)
      else:
        return searchInsert(nums[midIndex + 1:], target, midIndex + count + 1)

# Solution 2: Elegant solution but too slow -> O(n)
# def searchInsert(nums, target, count=0):
#   return [x for x in nums if x<target]
  

print(searchInsert([1,3,5,6], 6))
print(searchInsert([1,3,5,6], 2))