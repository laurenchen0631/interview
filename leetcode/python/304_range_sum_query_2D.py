import collections


class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.dp = collections.defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i, j] = self.dp[i-1, j] + self.dp[i, j-1] - self.dp[i-1, j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2, col2] - self.dp[row1-1, col2] - self.dp[row2, col1-1] + self.dp[row1-1, col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(m.sumRegion(2, 1, 4, 3))
print(m.sumRegion(1, 1, 2, 2))
print(m.sumRegion(1, 2, 2, 4))