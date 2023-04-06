class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i: int, j: int) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if visited[i][j] or grid[i][j] == 1:
                return True
            visited[i][j] = True
            isClosed = True
            for di, dj in dirs:
                isClosed &= dfs(i + di, j + dj)
            return isClosed
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    res += dfs(i, j)
        return res