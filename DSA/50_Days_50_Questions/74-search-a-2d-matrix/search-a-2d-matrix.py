class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row*col-1

        while l<=r:
            mid = l+(r-l)//2
            mid_val = matrix[mid/col][mid%col]

            if(mid_val==target):
                return True
            elif(mid_val<target):
                l = mid+1
            else:
                r = mid-1
        return False