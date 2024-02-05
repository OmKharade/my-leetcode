class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # front partition
        n = len(arr)
        dp = [-1 for _ in range(n)]
        def f(ind):
            if ind == n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            res = 0
            len, maxi = 0, float("-infinity")
            for j in range(ind, min(n,ind+k)):
                len += 1
                maxi = max(maxi,arr[j])
                sum = len*maxi + f(j+1)
                res = max(res,sum)

            dp[ind] = res
            return dp[ind]

        return f(0)