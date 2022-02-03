class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        maxWidth: int = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxWidth = max(maxWidth, dp[i][j])
        return maxWidth ** 2

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquare([["0","1"],["1","0"]]))