class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dpH = [[0] * (n+1) for _ in range(m+1)]
        dpV = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] != 'W':
                    dpH[i][j] = dpH[i][j-1] + (1 if grid[i-1][j-1] == 'E' else 0)
                    dpV[i][j] = dpV[i-1][j] + (1 if grid[i-1][j-1] == 'E' else 0)

        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if grid[i-1][j-1] == 'W':
                    continue
                
                if j < n:
                    dpH[i][j] = dpH[i][j+1] if grid[i-1][j] != 'W' else dpH[i][j]
                if i < m:
                    dpV[i][j] = dpV[i+1][j] if grid[i][j-1] != 'W' else dpV[i][j]

        res: int = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == '0':
                    res = max(res, dpH[i][j] + dpV[i][j])
        return res

s = Solution()
# print(s.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
# print(s.maxKilledEnemies([["W","W","W"],["0","0","0"],["E","E","E"]]))
print(s.maxKilledEnemies([["E","E","E","E","E","E","E","E","E","E"],["0","0","0","0","0","0","0","0","0","0"],["E","E","E","E","E","E","E","E","E","E"]]))