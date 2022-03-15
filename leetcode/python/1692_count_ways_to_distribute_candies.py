class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MAX = 1_000_000_007
        dp = [[0] * n for _ in range(k)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, k):
            for j in range(i, n):
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] * (i+1)) % MAX
        return dp[k-1][n-1]
    
s = Solution()
print(s.waysToDistribute(n = 3, k = 2))
print(s.waysToDistribute(n = 4, k = 2))
print(s.waysToDistribute(n = 20, k = 5))