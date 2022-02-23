
class Solution:
    def __init__(self) -> None:
        self.dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        cache = [[0] * n for _ in range(m)]
        res: int = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        return res

    def dfs(self, mat: list[list[int]], i: int, j: int, cache: list[list[int]]) -> int:
        if cache[i][j] > 0:
            return cache[i][j]
        for dy, dx in self.dirs:
            y, x = dy+i, dx+j
            if x >= 0 and x < len(mat[0]) and y >= 0 and y < len(mat) and mat[y][x] > mat[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(mat, y, x, cache))
        cache[i][j] += 1
        return cache[i][j]

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(s.longestIncreasingPath([[3,4,5],[2,1,6],[9,8,7]]))