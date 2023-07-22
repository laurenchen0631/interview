class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
    
        # Create a table to store the number of ways for each sum value from 0 to n.
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, round(n ** (1 / x)) + 1):
            power_i = i ** x
            for j in range(n, power_i - 1, -1):
                dp[j] += dp[j - power_i]
                dp[j] %= mod
        
        return dp[n]

s = Solution()
print(s.numberOfWays(10, 2))
# print(s.numberOfWays(100, 2))
print(s.numberOfWays(4, 1))
print(s.numberOfWays(64, 3))
print(s.numberOfWays(200, 1))