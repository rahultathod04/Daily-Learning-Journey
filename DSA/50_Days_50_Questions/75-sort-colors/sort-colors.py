class Solution:
    def sortColors(self, nums):
        n = len(nums)
        l = 0
        m = 0
        h = n-1
        while m<=h:
            if(nums[m]==0):
                nums[m] = nums[l]
                nums[l] = 0
                l+=1
                m+=1

            elif(nums[m]==1):
                m+=1

            elif(nums[m]==2):
                nums[m], nums[h] = nums[h], nums[m]
                h-=1
