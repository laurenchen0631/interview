class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        step: int = 0
        m, n = len(grid), len(grid[0])
        q: list[tuple[int, int, int]] = [(0, 0, k)]
        visited: set[tuple[int, int, int]] = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            tmp = []
            for p in q:
                if p in visited:
                    continue
                visited.add(p)
                i, j, r = p
                if i == m-1 and j == n-1:
                    return step
                if grid[i][j] == 1:
                    if r == 0:
                        continue
                    r -= 1
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n:
                        tmp.append((ni, nj, r))
            q = tmp
            step += 1
        return -1

s = Solution()
print(s.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[1,1,1],[0,0,0]], k = 2))