"""
given an unsorted array and a number k
we need to find the kth smallest element in the array
"""

def partition(arr, left, right):
    x = arr[right]
    i = left

    for j in range(left, right-1):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def kthSmallest(arr, left, right, k):

    if k > 0 and k <= right - left + 1:

        pos = partition(arr, left, right)

        if pos-left == k-1:
            return arr[pos]

        if pos-left > k-1:
            return kthSmallest(arr, left, pos-1, k)
        
        return kthSmallest(arr, pos+1, right, k-pos+left-1)
    
    return 'K is larger than the length of the array'

arr = [12, 3, 5, 7, 4, 19, 26]
print(kthSmallest(arr, 0, len(arr)-1, 3))
