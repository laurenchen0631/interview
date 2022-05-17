class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        visited = set[tuple[int,int]]()
        distinctIslands = set[set[tuple[int,int]]]()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                stack = [(r,c)]
                blocks = set[tuple[int,int]]()
                while stack:
                    p = stack.pop()
                    visited.add(p)
                    blocks.add((p[0]-r, p[1]-c))
                    for dy, dx in dirs:
                        x = p[1] + dx
                        y = p[0] + dy
                        if 0 <= x < n and 0 <= y < m and grid[y][x] == 1 and (y,x) not in visited:
                            stack.append((y,x))
                distinctIslands.add(frozenset(blocks))
        return len(distinctIslands)

s = Solution()
print(s.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(s.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))