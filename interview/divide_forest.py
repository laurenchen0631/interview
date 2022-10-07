
#
# Complete the 'dividing_forest' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY forest
#  2. INTEGER number
#
from functools import lru_cache


def dividing_forest(forest: list[list[int]], number: int):
    m, n = len(forest), len(forest[0])
    numPoplar: int = 0
    rowPopular: list[int] = [[0] * m for _ in range(n+1)]
    colPopular: list[int] = [[0] * n for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            cur = forest[i][j] == 2
            numPoplar += cur
            rowPopular[j][i] = rowPopular[j+1][i] + cur
            colPopular[i][j] = colPopular[i+1][j] + cur

    @lru_cache(None)
    def divide(row: int, col: int, total: int, num: int) -> int:
        res = 0
        if num == 1:
            return 1

        num -= 1
        curPoplar: int = 0
        for r in range(row, m):
            curPoplar += rowPopular[col][r]
            if curPoplar > 0 and total - curPoplar >= num:
                res += divide(r + 1, col, total - curPoplar, num)
        
        curPoplar = 0
        for c in range(col, n):
            curPoplar += colPopular[row][c]
            if curPoplar > 0 and total - curPoplar >= num:
                res += divide(row, c + 1, total - curPoplar, num)
        
        return res % 1000000007
    

    return divide(0, 0, numPoplar, number)

print(dividing_forest([[2,2,2], [2,2,2], [2,2,2]], 3))
print(dividing_forest([[1,2,3], [2,1,2], [2,2,2]], 3))
print(dividing_forest([[1,2,3], [2,1,2]], 3))
print(dividing_forest([[1,2,3], [2,1,2], [3,1,1]], 3))
