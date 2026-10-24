class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        count = {0:-1}
        pref = 0

        for i in range(n):
            pref += nums[i]
            remain = pref % k

            if remain in count:
                last_ind = count[remain]
                if(i - last_ind >= 2):
                    return True
            else:
                count[remain] = i
        return False
