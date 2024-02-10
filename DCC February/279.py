class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        def f(n):
            if n==0:                                                    
                return 0  
            if dp[n] != -1:
                return dp[n]
            mini = n                                                     
            i = 1
            while i*i<=n:                                               
                mini = min(mini, f(n-(i*i)))
                i+=1
            dp[n] =  mini+1                                              
            return dp[n]
        return f(n)