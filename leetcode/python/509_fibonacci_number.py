class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * max(n+1, 2)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

s = Solution()
print(s.fib(0))
print(s.fib(1))
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))