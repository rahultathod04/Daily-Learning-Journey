class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1

        while l<=r:
            mid = l+(r-l)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                r = mid-1
        return l
        