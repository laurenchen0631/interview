class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        dp = [0] * 3
        for cost in costs:
            dp[0], dp[1], dp[2] = cost[0] + min(dp[1], dp[2]), cost[1] + min(dp[0], dp[2]), cost[2] + min(dp[0], dp[1])
        return min(dp)

s = Solution()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(s.minCost([[7,6,2]]))