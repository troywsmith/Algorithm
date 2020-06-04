# def contiguousSequenceBF(nums):

#     maxSum = float('-inf')
#     maxSequence = None
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             currentSum = sum(nums[i:j])
#             if currentSum > maxSum:
#                 maxSum = currentSum
#                 maxSequence = nums[i:j]

#     return maxSum, maxSequence


def contiguousSequenceOptimized(nums):
    maxSum = float('-inf')
    currentSum = float('-inf')
    for num in nums:
        currentSum += num
        if currentSum < 0:
            currentSum = 0
        else:
            maxSum = max(currentSum, maxSum)

    return maxSum


if __name__ == '__main__':
    nums = [2, -8, 3, -2, 4, -10]
    ans = contiguousSequenceOptimized(nums)
    print(ans)
    # print('The max sequence is {} with a sum of {}'.format(ans[1], ans[0]))
