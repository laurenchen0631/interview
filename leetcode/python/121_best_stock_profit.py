class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curMin = prices[0]
        profit: int = 0
        for n in prices[1:]:
            profit = max(profit, n - curMin)
            curMin = min(n, curMin)
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
        