class Solution:
    def findDerangement(self, n: int) -> int:
        if n < 2:
            return 0 
        MAX = 1_000_000_007
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = (i-1) * (dp[i-1] + dp[i-2]) % MAX
        return dp[n]