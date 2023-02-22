class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * (numPeople//2 + 1)
        for i in range(2, len(dp)):
            dp[i] = sum([dp[j] * dp[i-j-1] for j in range(i)]) % MOD
        return dp[-1] 

s = Solution()
print(s.numberOfWays(4))
print(s.numberOfWays(6))
print(s.numberOfWays(8))
print(s.numberOfWays(10))
print(s.numberOfWays(140))