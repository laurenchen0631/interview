class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q: list[tuple[int,int]] = []
        oranges: int = 0
        m = len(grid)
        n = len(grid[0]) if m else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    oranges += 1

        if not q:
            return 0 if oranges == 0 else -1

        elapse: int = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        tmp: list[tuple[int,int]] = []
        while q:
            r, c = q.pop()
            for x, y in directions:
                i = r + x
                j = c + y
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        tmp.append((i,j))
                        oranges -= 1
            if not q:
                elapse += 1
                q = tmp
                tmp = []
        return elapse if oranges == 0 else -1


if __name__ == '__main__':
  s = Solution()
  print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))