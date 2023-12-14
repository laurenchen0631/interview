class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        n: int = len(grid)
        m: int = len(grid[0])
        row: list[int] = [0] * n
        col: list[int] = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
                    
                    
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] += row[i] + col[j]
                res[i][j] -= (n - row[i]) + (m - col[j])
        return res
                
        