import sys


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = sorted(cuts + [0, n])
        dp = [[0] * len(cuts) for _ in range(len(cuts))]
        for l in range(2, len(cuts)):
            for i in range(len(cuts) - l):
                j = i + l
                cost = sys.maxsize
                for k in range(i + 1, j):
                    cost = min(cost, cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
                dp[i][j] = cost
        return dp[0][-1]