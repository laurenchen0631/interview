class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return -1
            if visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            count = 1
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                c = dfs(i + di, j + dj)
                if c == -1:
                    count = -1
                elif count > 0:
                    count += c
            return count

        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    res += max(0, dfs(i, j))
        return res