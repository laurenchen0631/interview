import sys

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k == 0:
            return 0
        profit = [0] * (k+1)
        cost = [sys.maxsize] * (k+1)

        for price in prices:
            for i in range(1, k+1):
                cost[i] = min(cost[i], price - profit[i-1])
                profit[i] = max(profit[i], price - cost[i])
            
        return profit[-1]
        