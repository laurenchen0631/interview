class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sold = -prices[0]
        reset: int = 0
        held: int = 0
        for n in prices[1:]:
            sold, held, reset = held + n, max(held, reset - n), max(reset, sold)
        return max(reset, sold)

s = Solution()
print(s.maxProfit([1,2,3,0,2]))