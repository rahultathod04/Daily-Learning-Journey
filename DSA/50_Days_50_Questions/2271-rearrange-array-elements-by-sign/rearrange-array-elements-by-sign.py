class Solution(object):
    def rearrangeArray(self, nums):
        l = len(nums)
        neg = []
        pos = []
        n = 0
        p = 0

        for i in range(l):
            if(nums[i]>=0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(l/2):
             nums[i*2] = pos[i]
             nums[(i*2)+1] = neg[i]


        return nums