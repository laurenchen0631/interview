class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        def helper(row: int, diagonal: set[int], antiDiagonal: set[int], cols: set[int], board: list[list[str]]) -> None:
            if row == n:
                res.append([''.join(board[i]) for i in range(n)])
                return
            
            for col in range(n):
                d = row - col
                a = row + col

                if col in cols or d in diagonal or a in antiDiagonal:
                    continue
                cols.add(col)
                diagonal.add(d)
                antiDiagonal.add(a)
                board[row][col] = 'Q'
                helper(row+1, diagonal, antiDiagonal, cols, board)
                cols.remove(col)
                diagonal.remove(d)
                antiDiagonal.remove(a)
                board[row][col] = '.'

        helper(0, set(), set(), set(), [['.'] * n for _ in range(n)])
        return res
    
s = Solution()
print(s.solveNQueens(4))