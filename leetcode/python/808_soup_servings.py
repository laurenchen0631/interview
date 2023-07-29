import dis
from functools import lru_cache
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        n = ceil(n / 25)
        dp = {}
        
        def distribute(a: int, b: int) -> float:
            return (
                dp[max(0, a-4)][b] +
                dp[max(0, a-3)][max(0, b-1)] +
                dp[max(0, a-2)][max(0, b-2)] +
                dp[max(0, a-1)][max(0, b-3)]
            ) / 4
        
        dp[0] = {0: 0.5}
        for k in range(1, n + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k+1):
                dp[j][k] = distribute(j, k)
                dp[k][j] = distribute(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1
        return dp[n][n]
    
    def serving2(self, n: int) -> float:
        @lru_cache(None)
        def distribute(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0
            
            return (
                distribute(a-100, b) +
                distribute(a-75, b-25) +
                distribute(a-50, b-50) +
                distribute(a-25, b-75)
            ) / 4.0
        
        return distribute(n, n)

        
s = Solution()
print(s.serving2(100))