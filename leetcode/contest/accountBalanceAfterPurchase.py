from numpy import integer


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        integer_part = purchaseAmount // 10
        decimal_part = purchaseAmount % 10
        if decimal_part >= 5:
            integer_part += 1
        
        return 100 - (integer_part * 10)
    
s = Solution()
print(s.accountBalanceAfterPurchase(5))