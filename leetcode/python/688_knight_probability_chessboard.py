class Solution:
    def __init__(self):
        self.dirs = [(-2,1), (-1,2), (1,2), (2,1),
                    (-2, -1), (-1,-2), (1,-2), (2,-1)]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp =[[0] * n for _ in range(n)]
        dp[row][column] = count = 1
        for _ in range(k):
            if count == 0:
                break
            count = 0
            tmp =[[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for (di, dj) in self.dirs:
                        y = i + di
                        x = j + dj
                        if 0 <= y < n and 0 <= x < n:
                            tmp[i][j] += dp[y][x]
                    count += tmp[i][j]
            dp = tmp
        return count / (len(self.dirs) ** k)

s = Solution()
print(s.knightProbability(n = 3, k = 2, row = 0, column = 0))
print(s.knightProbability(n = 1, k = 0, row = 0, column = 0))
        