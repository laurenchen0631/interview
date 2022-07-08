from sys import maxsize


class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        dp = [[[maxsize] * n  for _ in range(target + 1)] for _ in range(m)]
        for k in range(1, n+1):
            if houses[0] == k:
                dp[0][1][k-1] = 0
            elif houses[0] == 0:
                dp[0][1][k-1] = cost[0][k-1]

        for i in range(1, m):
            for j in range(1, min(target+1, i+2)):
                for k in range(1, n+1):
                    if houses[i] != 0 and houses[i] != k:
                        continue
                    cur = maxsize
                    for color in range(1, n+1):
                        if color != k:
                            cur = min(cur, dp[i-1][j-1][color-1])
                        else:
                            cur = min(cur, dp[i-1][j][k-1])
                    dp[i][j][k-1] = cur + (cost[i][k-1] if houses[i] == 0 else 0)

        minCost = min([dp[m-1][target][k-1] for k in range(1, n+1)])

        return minCost if minCost < maxsize else -1

s = Solution()
print(s.minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
print(s.minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
print(s.minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3))