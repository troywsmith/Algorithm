class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        
        quads = []
        
        # Sort the array: O(nlogn)
        nums.sort()        
        
        # For each item in array from 0 to last - 3
        for i in range(len(nums)-3):
        
            # For each of those items, iterate over the remaining items in array from item to last - 2
            for j in range(i+1, len(nums)-2):
                                
                # For the remaining elements, find a pair that equal the diff of target and current items
                x = j + 1
                y = len(nums)-1
                while x < y:
                    
                    q_sum = nums[i] + nums[j] + nums[x] + nums[y]
                                        
                    # If sum is less than target, move left pointer right to increase value
                    if q_sum < target:
                        x += 1
                    
                    # If sum is greater than target, move right pointer left to decrease value
                    elif q_sum > target:
                        y -= 1
                    
                    # If both of those fail, the sum must be equal to the target
                    else:
                        quad = [nums[i], nums[j], nums[x], nums[y]]
                        if quad not in quads:
                            quads.append(quad)
                            
                        x += 1
                        y -= 1
        
        # Return quads array
        return quads