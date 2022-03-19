from math import inf


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [-inf] * (n+1)
        dp[-1] = 0
        for i in range(n-1, -1, -1):
            acc: int = 0
            for j in range(i, min(i+3, n)):
                acc += stoneValue[j]
                dp[i] = max(dp[i], acc - dp[j+1])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] == 0:
            return 'Tie'
        else:
            return 'Bob'

s = Solution()
print(s.stoneGameIII([1,2,3,7]))
print(s.stoneGameIII([1,2,3,-9]))
print(s.stoneGameIII([1,2,3,6]))