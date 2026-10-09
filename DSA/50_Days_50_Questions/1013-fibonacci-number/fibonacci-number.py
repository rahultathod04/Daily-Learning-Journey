class Solution(object):
    def fib(self, n):
        n0 = 0
        n1 = 1
        nth = None
        if(n==0):
            return 0
        else:
            count = 1
            nth = 1
            while count < n:
                nth = n0 + n1
                n0 = n1
                n1 = nth
                count+=1
            return nth 
