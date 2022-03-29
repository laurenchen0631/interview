class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        validDigits = set([str(i) for i in range(1, 10)])
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        for r in range(9):
            row = set[str]()
            for c in range(9):
                d = board[r][c]
                if d == '.':
                    continue
                if d not in validDigits:
                    return False
                gridIndex = (r // 3) * 3 + (c // 3)
                if d in row or d in cols[c] or d in grids[gridIndex]:
                    return False
                row.add(d)
                cols[c].add(d)
                grids[gridIndex].add(d)
        return True

s = Solution()
print(s.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))

print(s.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))