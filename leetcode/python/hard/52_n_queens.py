class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(row: int, diagonal: set[int], antiDiagonal: set[int], cols: set[int]) -> int:
            if row == n:
                return 1
            
            res = 0
            for col in range(n):
                d = row - col
                a = row + col

                if col in cols or d in diagonal or a in antiDiagonal:
                    continue
                cols.add(col)
                diagonal.add(d)
                antiDiagonal.add(a)
                res += helper(row+1, diagonal, antiDiagonal, cols)
                cols.remove(col)
                diagonal.remove(d)
                antiDiagonal.remove(a)
            return res

        return helper(0, set(), set(), set())

s = Solution()
print(s.totalNQueens(4))