from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        flood = dict[tuple[int,int], int]()
        for i, [r, c] in enumerate(cells):
            flood[(r-1, c-1)] = i + 1
        
        l, r = 1, len(cells)
        while l < r:
            m = (l + r) // 2
            if self.canCross(row, col, flood, m):
                l = m + 1
            else:
                r = m
        return l - 1
    
    def canCross(self, row: int, col: int, flood: dict[tuple[int,int], int], m: int) -> bool:
        q = deque()
        visited = set()
        for j in range(col):
            if flood[(0, j)] > m:
                q.append((0, j))
                visited.add((0, j))
        
        while q:
            i, j = q.popleft()
            if i == row - 1:
                return True
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  
                r, c = i + di, j + dj
                if 0 <= r < row and 0 <= c < col and (r, c) not in visited and flood[(r,c)] > m:
                    q.append((r, c))
                    visited.add((r, c))
        return False
        