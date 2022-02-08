import math

class Solution:
    def numSquares(self, n: int) -> int:
        root = n ** 0.5
        if root % 1 == 0:
            return 1
        root = math.floor(root)
        dp = [n] * (n+1)
        dp[0] = 0
        for r in range(1, root+1):
            sq = r ** 2
            for i in range(sq, n+1):
                dp[i] = min(dp[i], 1 + dp[i-sq])
        return dp[-1]

s = Solution()
print(s.numSquares(2))
print(s.numSquares(3))
print(s.numSquares(4))
print(s.numSquares(5))
print(s.numSquares(6))
print(s.numSquares(7))
print(s.numSquares(8))
print(s.numSquares(12))
print(s.numSquares(13))
