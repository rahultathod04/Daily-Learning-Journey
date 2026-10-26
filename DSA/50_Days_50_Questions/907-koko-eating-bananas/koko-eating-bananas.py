class Solution:
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles) 
        ans = r


        def can_eat(eat):
            cur_h = 0
            for p in piles:
                cur_h += (p + eat - 1) // eat
            return cur_h <= h

        while l<=r:
            mid = l + (r-l)//2

            if(can_eat(mid)):
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans