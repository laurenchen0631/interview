class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0]) if m else 0
        if m * n != r * c:
            return mat
        
        res: list[list[int]] = [[]]
        for row in mat:
            for n in row:
                if len(res[-1]) == c:
                    res.append([n])
                else:
                    res[-1].append(n)
        return res

s = Solution()
print(s.matrixReshape([[1,2],[3,4]], r = 1, c = 4))
print(s.matrixReshape([[1,2],[3,4],[5,6]], r = 2, c = 3))
