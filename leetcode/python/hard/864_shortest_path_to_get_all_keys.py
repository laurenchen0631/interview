from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        goal = 0
        start = (0, 0)
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '@':
                    start = (i, j)
                elif c.islower():
                    goal |= 1 << (ord(c) - ord('a'))
        
        q = deque[tuple[int,int,int,int]]([(start[0], start[1], 0, 0)]) # (x, y, keys, steps)
        visited = set[tuple[int, int, int]]([(start[0], start[1], 0)])
        while q:
            i, j, state, steps = q.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = i + di, j + dj
                if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#':
                    continue
                
                if grid[r][c].isupper() and not (state & (1 << (ord(grid[r][c]) - ord('A')))):
                    continue
                elif grid[r][c].islower() and not (state & (1 << (ord(grid[r][c]) - ord('a')))):
                    s = state | (1 << (ord(grid[r][c]) - ord('a')))
                    if s == goal:
                        return steps + 1
                    visited.add((r, c, s))
                    q.append((r, c, s, steps + 1))
                elif (r, c, state) not in visited:
                    visited.add((r, c, state))
                    q.append((r, c, state, steps + 1))
            
        return -1
        