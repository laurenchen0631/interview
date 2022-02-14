class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        dp = [0] * (len(prob) + 1)
        dp[0] = 1
        for i, p in enumerate(prob):
            maxToss = min(i+1, target)
            for j in range(maxToss, 0, -1):
                dp[j] = dp[j-1] * p + dp[j] * (1-p)
            dp[0] *= (1-p)
        return dp[target]

s = Solution()
print(s.probabilityOfHeads([0.5,0.5,0.5,0.5,0.5], target = 2))
print(s.probabilityOfHeads([0.4], target = 1))
        