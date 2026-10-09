class Solution(object):
    def fib(self, n):
        def rec(n, a=0 , b=1):
            if n==1:
                return b
            if n==0:
                return a
            else:
                return rec(n-1, b , a+b)
        return rec(n)