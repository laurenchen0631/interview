class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (query_row+2) for _ in range(query_row+2)]
        tower[0][0] = poured
        for row in range(query_row+1):
            for col in range(row+1):
                unit = (tower[row][col]-1)/2
                if unit > 0:
                    print(row+1, col)
                    tower[row+1][col] += unit
                    tower[row+1][col+1] += unit
        return min(tower[query_row][query_glass], 1.0)

s = Solution()
print(s.champagneTower(poured = 1, query_row = 1, query_glass = 1))
print(s.champagneTower(poured = 2, query_row = 1, query_glass = 1))
print(s.champagneTower(poured = 100000009, query_row = 33, query_glass = 17))