class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        size = m * n
        k %= size
        if k == 0:
            return grid
        
        res = [[0] * n for _ in range(m)]
        for index in range(size):
            (x, y) = divmod(index, n)
            index = (index + k) % size
            (i, j) = divmod(index, n)
            res[i][j] = grid[x][y]
        return res

s = Solution()
print(s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(s.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
