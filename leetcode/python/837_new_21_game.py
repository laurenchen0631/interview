class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1
        dp: list[float] = [0] * (n + 1)
        dp[0] = 1
        window: float = 1
        res = 0
        
        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                res += dp[i]
            if i >= maxPts:
                window -= dp[i - maxPts]
        return res
        
            
            