import math


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if 2 * k > n:
            return self.maxProfitUnlimited(prices)
        
        dp = [[[-math.inf] * 2 for _ in range(k+1)] for _ in range(n)] 
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for d in range(1, n):
            for j in range(k+1):
                dp[d][j][0] = max(dp[d-1][j][0], dp[d-1][j][1] + prices[d])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[d][j][1] = max(dp[d-1][j][1], dp[d-1][j-1][0] - prices[d])
        return max(dp[n-1][j][0] for j in range(k+1))

    def maxProfitUnlimited(self, prices: list[int]) -> int:
        profit: int = 0
        for i in range(1, len(prices)):
            if (p := prices[i] - prices[i-1]) > 0:
                profit += p
        return profit

s = Solution()
# print(s.maxProfit(k = 2, prices = [2,4,1]))
# print(s.maxProfit(k = 2, prices = [3,2,6,5,0,3]))
print(s.maxProfit(k = 1, prices = [2,1]))