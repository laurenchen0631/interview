import collections

class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        dp = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                dp[i, j] = dp[i-1, j] + dp[i, j-1] - dp[i-1, j-1] + mat[i][j]
        print(dp)
        
        res: list[list[int]] = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = min(j+k, n-1), min(i+k, m-1)
                x0, y0 = max(j-k, 0), max(i-k, 0)
                res[i][j] = dp[y1,x1] - dp[y1, x0-1] - dp[y0-1, x1] + dp[y0-1, x0-1]
        return res

s = Solution()
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2))