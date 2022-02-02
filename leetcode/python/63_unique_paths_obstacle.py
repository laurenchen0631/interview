class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m > 0 else 0
        if n == 0 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(m):
            for j in range(1, n+1):
                if obstacleGrid[i][j-1] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j-1] + dp[j]
        return dp[-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))