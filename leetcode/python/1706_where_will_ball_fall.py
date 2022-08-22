class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        def canFallthrough(x: int) -> int:
            for y in range(n):
                dx = grid[y][x] + x
                if dx < 0 or dx >= m or grid[y][dx] != grid[y][x]:
                    return -1
                x = dx
            return x
        return [canFallthrough(x) for x in range(m)]

s = Solution()
print(s.findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(s.findBall(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))