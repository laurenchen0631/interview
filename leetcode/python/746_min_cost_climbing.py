class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0, 0]
        for c in cost:
            minCost = min(dp) + c
            dp[0], dp[1] = dp[1], minCost
        return min(dp)

s = Solution()
print(s.minCostClimbingStairs([10]))
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))