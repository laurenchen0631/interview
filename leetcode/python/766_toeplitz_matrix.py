class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        diagonals = dict[int, int]()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i - j not in diagonals:
                    diagonals[i - j] = matrix[i][j]
                elif diagonals[i - j] != matrix[i][j]:
                    return False
        return True

s = Solution()
print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))