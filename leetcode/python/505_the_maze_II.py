import heapq


class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        # dijkstra variation
        m, n = len(maze), len(maze[0])
        q: list[tuple[int,int,int]] = [(0, start[0], start[1])]
        visited = {(start[0], start[1]): 0}
        while q:
            d, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return d
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i, j, distance = x, y, d
                while 0 <= i + dx < m and 0 <= j + dy < n and maze[i + dx][j + dy] == 0:
                    i += dx
                    j += dy
                    distance += 1
                if (i, j) not in visited or distance < visited[(i, j)]:
                    visited[(i, j)] = distance
                    heapq.heappush(q, (distance, i, j))
        return -1
        
        