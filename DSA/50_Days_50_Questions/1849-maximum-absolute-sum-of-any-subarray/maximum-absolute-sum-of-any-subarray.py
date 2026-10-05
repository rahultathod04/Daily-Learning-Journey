class Solution(object):
    def kmax(self, nums, n):
        sum = nums[0]
        max_sum = nums[0]

        for i in range(1,n):
            sum = max(sum+nums[i], nums[i])
            max_sum = max(max_sum, sum)
        return max_sum

    def kmin(self, nums, n):
        sum = nums[0]
        min_sum = nums[0]

        for i in range(1,n):
            sum = min(sum+nums[i], nums[i])
            min_sum = min(min_sum, sum)
        return min_sum

    def maxAbsoluteSum(self, nums):
        n = len(nums)
        max_sum = self.kmax(nums, n)
        min_sum = self.kmin(nums, n)

        return max(abs(max_sum), abs(min_sum))