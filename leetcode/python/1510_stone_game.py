import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1, n+1):
            for k in range(1, int(i**0.5) + 1):
                dp[i] = not dp[i - k*k]
                if dp[i]:
                    break
        return dp[n]
        # root = n ** 0.5
        # if root % 1 == 0:
        #     return True
        # root = math.floor(root)
        # dp = [False] * (n+1)
        # for i in range(n+1):
        #     if dp[i]: # If alice win dp[i], she will never win d[i+n^2]
        #         continue
        #     for j in range(1, root+1):
        #         k = i + j**2
        #         if k <= n:
        #             dp[k] = True
        #         else:
        #             break
        # return dp[n]


s = Solution()
print(s.winnerSquareGame(1))
print(s.winnerSquareGame(2))
print(s.winnerSquareGame(3))
print(s.winnerSquareGame(4))
print(s.winnerSquareGame(5))
print(s.winnerSquareGame(6))
print(s.winnerSquareGame(7))
print(s.winnerSquareGame(8))
print(s.winnerSquareGame(9))
print(s.winnerSquareGame(10))