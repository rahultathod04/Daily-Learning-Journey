class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
    # right_max[i] = max suffix sum starting at index >= i
        right_max = [0] * n
        suffix = nums[-1]
        right_max[-1] = suffix
        for i in range(n - 2, -1, -1):
            suffix += nums[i]
            right_max[i] = max(right_max[i + 1], suffix)

        best = kadane_best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            kadane_best = max(kadane_best, cur)

        prefix = 0
        for i in range(n - 2):          # leave room so suffix starts at i+2 or later
            prefix += nums[i]
            best = max(best, prefix + right_max[i + 2])

        return max(kadane_best, best)    
        