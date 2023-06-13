
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        n = len(grid)
        for i in range(n):
            rows[tuple(grid[i])] += 1
            col = []
            for j in range(n):
                col.append(grid[j][i])
            cols[tuple(col)] += 1
        res = 0
        for k, v in rows.items():
            if k in cols:
                res += v * cols[k]
        return res
        