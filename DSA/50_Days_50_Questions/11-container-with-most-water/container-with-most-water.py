class Solution:
    def maxArea(self, height):
       n = len(height)
       l = 0
       r = n-1
       ans = 0

       for i in range(n):
        w = r-l
        h = min(height[l], height[r])
        area = w*h
        ans = max(area, ans)

        if(height[l]<height[r]):
            l+=1
        else:
            r-=1
       return ans