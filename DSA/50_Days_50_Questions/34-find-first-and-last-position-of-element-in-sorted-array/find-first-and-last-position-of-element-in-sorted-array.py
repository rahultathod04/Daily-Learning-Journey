class Solution(object):
    def LEFT(self, nums, t, n):
        l_m = -1
        l = 0
        r = n-1
        while l<=r:
            m = l+(r-l)/2
            if(nums[m]==t):
                l_m = m
                r = m-1
            elif(nums[m]<t):
                l=m+1
            else:
                r=m-1
        return l_m
    
    def RIGHT(self, nums, t, n):
        r_m = -1
        l = 0
        r = n-1
        while l<=r:
            m = l+(r-l)/2
            if(nums[m]==t):
                r_m = m
                l = m+1
            elif(nums[m]<t):
                l=m+1
            else:
                r=m-1
        return r_m
    def searchRange(self, nums, target):
        n = len(nums)
        l = self.LEFT(nums, target, n)
        r = self.RIGHT(nums, target, n)
        return [l,r]