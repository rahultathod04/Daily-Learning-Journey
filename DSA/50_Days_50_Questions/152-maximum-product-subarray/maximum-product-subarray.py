class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        r = 1
        l = 1
        ans = float('-inf')

        for i in range(n):
            if(r == 0):
                r = 1
            if(l == 0):
                l = 1
            
            l *= nums[i]
            r *= nums[n-1-i]

            ans = max(ans ,r, l )
        return ans 