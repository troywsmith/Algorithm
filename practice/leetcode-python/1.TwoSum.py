def twoSum(nums, target):

    # # Brute Force
    # for x in range(len(nums)):
    #   for y in range(x + 1, len(nums)):
    #     if nums[x] + nums[y] == target:
    #       return [x, y]

    # for x in range(len(nums)):
    #     slow, fast = x, x + 1
    #     while fast < len(nums):
    #         if nums[slow] + nums[fast] == target: return [slow, fast]
    #         else: fast += 1

    # Moving Window Solution
    sortedArr = sorted(nums)
    print(sortedArr)

    # Base Case
    if len(sortedArr) == 1:
        return False

    # Recursive Case
    else:
        mid = len(nums) // 2

        try:
            sums = sortedArr[mid] + sortedArr[mid + 1]
        except:
            sums = sortedArr[mid] + sortedArr[mid - 1]

        print(sums, target)
        if sums == target:
            return True

        else:
            if sums > target:
                return twoSum(sortedArr[:mid], target)
            else:
                return twoSum(sortedArr[mid:], target)


print(twoSum([2, 7, 11, 15], 9))
