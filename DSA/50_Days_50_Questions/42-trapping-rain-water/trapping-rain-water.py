class Solution(object):
    def trap(self, height):
        
        n = len(height)
        lmax = [0]*n
        rmax = [0]*n
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        ans = 0

        for i in range(n):
            lmax[i] = max(lmax[i-1], height[i])
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])
        for i in range(n):
            ans += min(lmax[i], rmax[i]) - height[i]
        
        return ans