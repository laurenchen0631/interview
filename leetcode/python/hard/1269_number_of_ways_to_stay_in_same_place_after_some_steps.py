from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(i: int, remain: int) -> int:
            if i == 0 and remain == 0:
                return 1
            elif remain == 0:
                return 0
            
            res = dp(i, remain-1) # stay
            if i > 0: # left
                res += dp(i-1, remain-1)
            if i < arrLen-1: # right
                res += dp(i+1, remain-1)
            return res
            
        return dp(0, steps) % (10**9 + 7)