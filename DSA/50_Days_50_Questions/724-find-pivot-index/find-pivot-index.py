class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)

        total = 0
        for i in range(n):
            total += nums[i]

        left = 0
        for i in range(n):
            right = total - left - nums[i]

            if(left == right ):
                return i
            
            left+=nums[i]
        
        return -1
        