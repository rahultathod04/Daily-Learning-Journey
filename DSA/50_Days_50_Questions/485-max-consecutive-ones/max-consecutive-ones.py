class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        curr = 0
        ans = 0

        for i in range(n):
            if(nums[i]==1):
                curr +=1

                if(curr>ans):
                    ans = curr
            else:
                    curr=0
        return ans