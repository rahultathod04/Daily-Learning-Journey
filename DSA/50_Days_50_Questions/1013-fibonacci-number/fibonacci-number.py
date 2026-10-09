class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
            
        prev2, prev1 = 0, 1
        
        for _ in range(2, n + 1):
            # Tuple unpacking: shifts both values forward simultaneously
            prev2, prev1 = prev1, prev1 + prev2
            
        return prev1

        # def rec(n, a=0 , b=1):
        #     if n==1:
        #         return b
        #     if n==0:
        #         return a
        #     else:
        #         return rec(n-1, b , a+b)
        # return rec(n)