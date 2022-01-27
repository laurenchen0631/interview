class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        sold = 0
        held = -prices[0]
        for n in prices:
            sold = max(sold, held + n - fee) # sell stock
            held = max(held, sold - n) # buy stock
        return sold

s = Solution()
print(s.maxProfit([1,3,2,8,4,9], fee = 2))
print(s.maxProfit([1,3,7,5,10,3], fee = 3))