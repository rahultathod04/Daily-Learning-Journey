class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        r = len(matrix)
        c = len(matrix[0])

        s = 0
        e = c*r-1

        while(s<=e):
            mid = s +(e-s)/2
            mid_val= matrix[mid//c][mid%c]
            if(mid_val<target):
                s = mid+1
            elif(mid_val>target):
                e = mid-1
            else:
                return True
        return False