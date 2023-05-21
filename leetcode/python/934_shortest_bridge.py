from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        visited = self.find_first_island(grid)
        q = deque(visited)
        # bfs to find the shortest path
        step = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                        if grid[nr][nc] == 1:
                            return step
                        q.append((nr, nc))
            step += 1
        return -1
    
    def find_first_island(self, grid: list[list[int]]) -> set[tuple[int, int]]:
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
        
        # traverse the first island
        q = deque([start])
        visited = set()
        while q:
            r, c = q.popleft()
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    q.append((nr, nc))
        return visited