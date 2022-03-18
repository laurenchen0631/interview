class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for k in range(len(group)):
            for i in range(n, group[k]-1, -1):
                for p in range(minProfit+1):
                    j = min(minProfit, p+profit[k])
                    dp[i][j] += dp[i-group[k]][p]
        return dp[-1][-1] % (10**9 + 7)

s = Solution()
print(s.profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3]))
print(s.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]))