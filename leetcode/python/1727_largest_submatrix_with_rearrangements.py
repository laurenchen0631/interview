class Solution:
    # 1111000000
    # 0011111111
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] = matrix[i-1][j] + 1
            
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                res = max(res, row[j] * (j+1))
        return res
