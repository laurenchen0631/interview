class Solution:
    
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        "matrix multiplication"
        res = []
        for i in range(len(mat1)):
            res.append([])
            for j in range(len(mat2[0])):
                res[i].append(0)
                for k in range(len(mat1[0])):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res