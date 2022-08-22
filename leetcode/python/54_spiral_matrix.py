class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []
        xl, xr, yl, yr = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while xl <= xr and yl <= yr:
            res.extend(matrix[yl][xl:xr + 1])
            yl += 1

            if yl > yr:
                break
            res.extend([matrix[i][xr] for i in range(yl, yr + 1)])
            xr -= 1

            if xl > xr:
                break
            res.extend(matrix[yr][xl:xr+1][::-1])
            yr -= 1

            if yl > yr:
                break
            res.extend([matrix[i][xl] for i in range(yr, yl-1, -1)])
            xl += 1
        return res

s = Solution()
print(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
