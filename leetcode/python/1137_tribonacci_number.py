class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            t = dp[0] + dp[1] + dp[2]
            dp[0], dp[1], dp[2] = dp[1], dp[2], t
        return dp[-1]

s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(25))
