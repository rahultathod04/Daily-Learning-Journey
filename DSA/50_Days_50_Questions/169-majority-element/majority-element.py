class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        ans = nums[0]
        frq = 0 

        for i in range(n):
            if(frq == 0):
                ans = nums[i]
            if(ans == nums[i]):
                frq+=1
            else:
                frq-=1
        return ans