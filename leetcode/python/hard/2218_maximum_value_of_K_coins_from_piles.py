class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for coins in range(1, k+1):
                dp[i][coins] = dp[i-1][coins]
                total = 0
                for j in range(1, min(len(piles[i-1]), coins) + 1):
                    total += piles[i-1][j-1]
                    dp[i][coins] = max(dp[i][coins], dp[i-1][coins-j] + total)
        return dp[n][k]