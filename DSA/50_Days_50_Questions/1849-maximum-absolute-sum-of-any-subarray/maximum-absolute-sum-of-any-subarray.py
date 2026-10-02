class Solution(object):
    def maxAbsoluteSum(self, nums):
        cur_max = cur_min = 0
        best_max = best_min = 0

        for x in nums:
            cur_max = max(0, cur_max + x)
            cur_min = min(0, cur_min + x)
            best_max = max(best_max, cur_max)
            best_min = min(best_min, cur_min)

        return max(best_max, -best_min)