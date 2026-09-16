class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        ans = float('inf')
        l = 0
        sum = 0

        for r in range(n):
            sum += nums[r]

            while (sum>=target):
                win_len = r - l + 1
                ans = min (ans, win_len)

                sum -=nums[l]
                l +=1
        if(ans == float('inf')):
            return 0
        else:
            return ans 
