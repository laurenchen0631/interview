class Solution:
    def maxA(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(4, n+1):
            for k in range(3, i+1):
                dp[i] = max(dp[i], dp[i-k] * (k-1))
        return dp[n]

s = Solution()
print(s.maxA(10))