class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)

        if hour <= n-1:
            return -1
        def check(v):
            total_nice = 0
            for num in dist[:-1]:
                total_nice += ((num + v -1)//v)
            
            total_nice  += dist[-1] / float(v)
            return total_nice <= hour
        
        left = 1
        right = 10**7
        ans = -1 
        while left <= right:
            mid = (left + right )//2
            if check(mid):
                ans = mid 
                right = mid -1
            else:
                left = mid + 1 
        return ans