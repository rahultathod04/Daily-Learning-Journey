class Solution(object):
    def Left(self, nums, target, n):
        left_most = -1
        l=0
        r=n-1
        while l<=r:
            mid = l+(r-l)//2
            if(nums[mid]==target):
                left_most = mid
                r = mid-1
            elif(nums[mid]<target):
                l = mid+1
            else:
                r =mid-1
        return left_most
    def Right(self, nums, target, n):
        right_most = -1
        l=0
        r=n-1
        while l<=r:
            mid = l+(r-l)//2
            if(nums[mid]==target):
                right_most = mid
                l = mid+1
            elif(nums[mid]<target):
                l = mid+1
            else:
                r =mid-1
        return right_most

    def searchRange(self, nums, target):
        n = len(nums)

        left_most = self.Left(nums, target, n)
        right_most = self.Right(nums, target, n)

        return [left_most, right_most]     