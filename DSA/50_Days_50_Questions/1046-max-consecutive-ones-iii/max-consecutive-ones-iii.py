class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        left = 0
        ans = 0
        zeroes = 0

        for right in range(n):
            if(nums[right]==0):
                zeroes +=1
            while(zeroes>k):
                if(nums[left]==0):
                    zeroes-=1
                left+=1
            window = right - left + 1
            ans = max(window, ans)
        return ans        