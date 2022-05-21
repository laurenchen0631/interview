
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = math.ceil(n / 2)
        while l <= r:
            m = (l+r) // 2
            coins = (m+1) * m // 2
            if coins <= n and coins + m + 1 > n:
                return m
            elif coins + m + 1 <= n:
                l = m + 1
            else:
                r = m - 1

s = Solution()
# print(s.arrangeCoins(0))
print(s.arrangeCoins(1))
print(s.arrangeCoins(2))
print(s.arrangeCoins(3))
print(s.arrangeCoins(4))
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
        