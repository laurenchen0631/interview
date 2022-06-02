class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        mat: list[list[int]] = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat[j][i] = matrix[i][j]
        return mat
        
s = Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(s.transpose([[1,2,3],[4,5,6]]))