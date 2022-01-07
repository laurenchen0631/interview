from collections import deque

class Solution:
    def __init__(self):
        self.dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        self.layer = (-1,-1)

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        q = deque([self.layer, (0,0)])
        visited = set[tuple[int,int]]()
        n = len(grid)
        steps: int = 1

        while q:
            p = q.pop()
            if p == self.layer:
                steps += 1
                if len(q) > 0:
                    q.appendleft(self.layer)
                continue
            elif p == (n-1, n-1):
                return steps
            elif p in visited:
                continue

            visited.add(p)
            for d in self.dirs:
                x = p[1] + d[1]
                y = p[0] + d[0]
                if 0 <= x < n and 0 <= y < n and grid[y][x] == 0:
                    q.appendleft((y, x))
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([
        [0,1],
        [1,0]
    ]))

    print(s.shortestPathBinaryMatrix([
        [0,0,0],
        [1,1,0],
        [1,1,0]
    ]))

    print(s.shortestPathBinaryMatrix([
        [1,0,0],
        [1,1,0],
        [1,1,0]
    ]))

    print(s.shortestPathBinaryMatrix([
        [0,0,0],
        [1,1,0],
        [1,1,1]
    ]))