class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        if(len(dist)-1>hour):
            return -1

        l = 1
        r = 10**7*100
        ans = -1

        def can_cover(speed):
            curr_h = 0
            for d in dist[:-1]:
                curr_h += math.ceil(float(d)/speed)
            curr_h += float(dist[-1])/speed
            return curr_h<=hour

        while l<=r:
            mid = l +(r-l)//2

            if(can_cover(mid)):
                ans = mid 
                r = mid-1
            else:
                l = mid+1
        return ans 
        