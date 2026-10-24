class Solution:
    def maxArea(self, height):
        n = len(height)
        max_w = 0
        left = 0
        right = n-1

        while(left<right):
            h = min(height[left], height[right])
            w = right - left 
            area = h*w
            max_w = max(max_w, area)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_w