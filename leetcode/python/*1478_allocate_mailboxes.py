import math


class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                mid = (i+j) // 2
                costs[i][j] = sum([abs(houses[mid] - houses[l]) for l in range(i, j+1)])
        
        dp = [[math.inf] * n for _ in range(k)]
        dp[0] = costs[0]
        for t in range(1, k):
            for i in range(n):
                for j in range(i):
                    dp[t][i] = min(dp[t][i], costs[j+1][i] + dp[t-1][j])
        return dp[-1][-1]

s = Solution()
print(s.minDistance(houses = [1,4,8,10,20], k = 3))
print(s.minDistance(houses = [2,3,5,12,18], k = 2))