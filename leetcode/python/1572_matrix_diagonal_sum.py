class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i] + mat[i][n - 1 - i]
        if n % 2 == 1:
            res -= mat[n // 2][n // 2]
        return res