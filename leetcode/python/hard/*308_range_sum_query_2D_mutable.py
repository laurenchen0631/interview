class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self._rows, self._cols = len(matrix), len(matrix[0])
        self._bits = [[0] * (self._cols+1) for _ in range(self._rows+1)]
        self._buildBIT(matrix)

    def lsb(self, x: int) -> int: # least significant bit
        return x & -x

    def _buildBIT(self, matrix: list[list[int]]) -> None:
        for row in range(1, self._rows+1):
            for col in range(1, self._cols+1):
                self._updateBIT(row, col, matrix[row-1][col-1])
    
    def _updateBIT(self, row: int, col: int, val: int) -> None:
        while row <= self._rows:
            c = col
            while c <= self._cols:
                self._bits[row][c] += val
                c += self.lsb(c)
            row += self.lsb(row)
    
    def _queryBIT(self, row: int, col: int) -> int:
        res = 0
        while row > 0:
            c = col
            while c > 0:
                res += self._bits[row][c]
                c -= self.lsb(c)
            row -= self.lsb(row)
        return res

    def update(self, row: int, col: int, val: int) -> None:
        oldVal = self.sumRegion(row, col, row, col)
        diff = val - oldVal
        self._updateBIT(row+1, col+1, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        return (self._queryBIT(r2, c2)
            - self._queryBIT(r1-1, c2)
            - self._queryBIT(r2, c1-1)
            + self._queryBIT(r1-1, c1-1))
        


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))