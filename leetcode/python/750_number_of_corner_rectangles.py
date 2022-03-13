class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [[0] * n for _ in range(n)]
        count: int = 0
        for row in grid:
            for c1 in range(n):
                if row[c1] == 0:
                    continue
                for c2 in range(c1+1, n):
                    if row[c2]:
                        count += dp[c1][c2]
                        dp[c1][c2] += 1
        return count

s = Solution()
print(s.countCornerRectangles([[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]))
print(s.countCornerRectangles([[1,1,1],[1,1,1],[1,1,1]]))
print(s.countCornerRectangles([[1,1,1,1]]))