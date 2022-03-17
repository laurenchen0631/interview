class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = days[-1]
        dp = [0] * (n+1)
        passes = [1, 7, 30]
        daysSet = set(days)
        for i in range(1, n+1):
            if i not in daysSet:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(i-passes[j], 0)] + costs[j] for j in range(3))
        return dp[n]

s = Solution()
print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))