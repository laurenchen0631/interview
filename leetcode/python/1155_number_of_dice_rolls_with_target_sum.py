class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MAX = 10 ** 9 + 7
        dp = [0] * (target + 1)
        for j in range(1, min(k+1, target+1)):
            dp[j] = 1

        for _ in range(1, n):
            for j in range(target, 0, -1):
                dp[j] = sum(dp[max(j-k, 0):j]) % MAX
        return dp[-1]

s = Solution()
print(s.numRollsToTarget(n = 1, k = 6, target = 3))
print(s.numRollsToTarget(n = 2, k = 6, target = 7))
print(s.numRollsToTarget(n = 30, k = 30, target = 500))