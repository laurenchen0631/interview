class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if s[j-1] == t[i-1] else 0)
        return dp[-1][-1]

s = Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit"))
print(s.numDistinct(s = "babgbag", t = "bag"))