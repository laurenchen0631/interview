class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        if n >= 3:
            dp[3] = 2
        for i in range(4, n+1):
            dp[i] = max([j * max(dp[i-j], i-j) for j in range(2, i//2 + 1)])
        return dp[-1]

s = Solution()
print(s.integerBreak(2))
print(s.integerBreak(11))