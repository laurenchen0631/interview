from concurrent.futures import process


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curMin = prices[0]
        profit: int = 0
        for i in range(1, len(prices)):
            if prices[i-1] >= prices[i]:
                curMin = prices[i]
            else:
                profit += prices[i] - curMin
                curMin = prices[i]
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))