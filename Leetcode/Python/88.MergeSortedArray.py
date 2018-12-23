def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    # Iteratre through numbers backwards
    while m > 0 and n > 0:

        # If last item in nums1 is bigger, make it last item in nums1
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1

        # Otherwise, make last item in nums2 the new last item in nums1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    # If after that, nums2 still has items, append them in place to nums1
    if n > 0:
        nums1[:n] = nums2[:n]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))
