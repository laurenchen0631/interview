class Solution:
    def longestLine(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        dp = [[[0,0,0,0] for _ in range(n)] for _ in range(m)]
        res: int = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                dp[i][j][0] = (dp[i][j-1][0] + 1) if j > 0 else 1
                dp[i][j][1] = (dp[i-1][j][1] + 1)  if i > 0 else 1
                dp[i][j][2] = (dp[i-1][j-1][2] + 1) if i > 0 and j > 0 else 1
                dp[i][j][3] = (dp[i-1][j+1][3] + 1) if i > 0 and j < n-1 else 1
                res = max(res, max(dp[i][j]))
        return res

s = Solution()
print(s.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))
print(s.longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]))