class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(n):
                dp[j] = dp[j] + (dp[j-1] if j > 0 else 0)
        return dp[-1]

s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(4, 4))