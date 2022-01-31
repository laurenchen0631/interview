import sys

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [sys.maxsize] + matrix[0] + [sys.maxsize]
        for row in range(1, m):
            tmp = dp.copy()
            for col in range(1, n+1):
                dp[col] = matrix[row][col-1] + min(tmp[col-1], tmp[col], tmp[col+1])
        
        return min(dp[1:n+1])

s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(s.minFallingPathSum([[-19,57],[-40,-5]]))