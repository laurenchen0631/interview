class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, nSquare = self.analyzeGrid(grid, m, n)
        visited = set[tuple[int,int]]()
        res = 0
        def dfs(i: int, j: int) -> None:
            if grid[i][j] == 2:
                nonlocal res
                res += 1 if len(visited) == nSquare-1 else 0
                return

            visited.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii, jj = di+i, dj+j
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != -1 and (ii, jj) not in visited:
                    dfs(ii, jj)
            visited.remove((i, j))
        dfs(start[0], start[1])
        return res
        
    def analyzeGrid(self, grid: list[list[int]], m: int, n: int) -> tuple[tuple[int,int], int]:
        start: tuple[int, int] = (0, 0)
        nSquare = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    nSquare += 1
        return start, nSquare
    
s = Solution()
print(s.uniquePaths([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(s.uniquePaths([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(s.uniquePaths([[0,1],[2,0]]))