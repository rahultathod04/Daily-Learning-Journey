class Solution(object):
    def shipWithinDays(self, weights, days):
        l = max(weights)
        r = sum(weights)

        ans = r

        def can_ship(capacity):
            curr_day = 1
            curr_w = 0
            for w in weights:
                if(curr_w + w > capacity):
                    curr_day+=1
                    curr_w = w
                else:
                    curr_w+=w
            return curr_day<=days

        while l<=r:
            mid = l+(r-l)//2

            if(can_ship(mid)):
                ans = mid
                r = mid-1
            else:
                l= mid+1
        return ans