class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = {}
        def f(ind,prev):
            if ind<0:
                return []
            if (ind,prev) in dp:
                return dp[(ind,prev)]

            res = f(ind-1,prev)
            if prev == 1 or prev % nums[ind] == 0:
                pick = [nums[ind]] + f(ind-1,nums[ind])
                if len(pick) > len(res):
                    res = pick
            
            dp[(ind,prev)] = res
            return res
           
        return f(len(nums)-1,1)
        