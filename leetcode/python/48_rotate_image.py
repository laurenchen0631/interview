class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n-1-i):
                prev = matrix[n-1-j][i]
                prev, matrix[i][j] = matrix[i][j], prev
                prev, matrix[j][n-1-i] = matrix[j][n-1-i], prev
                prev, matrix[n-1-i][n-1-j] = matrix[n-1-i][n-1-j], prev
                matrix[n-1-j][i] = prev

s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)