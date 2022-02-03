import sys


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        dp = [sys.maxsize] * (n+1)
        dp[1] = 0
        for i in range(m):
            for j in range(1, n+1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j-1]
        return dp[-1]

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))