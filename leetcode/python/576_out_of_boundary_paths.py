class Solution:
    def __init__(self) -> None:
        self.MAX = 10**9 + 7

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count: int = 0
        for _ in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        count = (count + dp[i][j]) % self.MAX
                    if i == m - 1:
                        count = (count + dp[i][j]) % self.MAX
                    if j == 0:
                        count = (count + dp[i][j]) % self.MAX
                    if j == n - 1:
                        count = (count + dp[i][j]) % self.MAX

                    temp[i][j] = (dp[i-1][j] if i > 0 else 0) + \
                        (dp[i+1][j] if i < m-1 else 0) + \
                        (dp[i][j-1] if j > 0 else 0) + \
                        (dp[i][j+1] if j < n-1 else 0)
            dp = temp
        return count
                    
s = Solution()
print(s.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))