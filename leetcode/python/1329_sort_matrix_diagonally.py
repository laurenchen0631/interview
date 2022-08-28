class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        for j in range(n-1):
            arr = [mat[i][i+j] for i in range(min(m, n-j))]
            arr.sort()
            for i in range(min(m, n-j)):
                mat[i][i+j] = arr[i]
        
        for i in range(1, m-1):
            arr = [mat[i+j][j] for j in range(min(n, m-i))]
            arr.sort()
            for j in range(min(n, m-i)):
                mat[i+j][j] = arr[j]
        return mat

s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(s.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))