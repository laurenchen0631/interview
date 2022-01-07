class Solution:
    def __init__(self):
        self.dirs = [(0,1), (1,0), (0,-1), (-1, 0)]

    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = set[tuple[int,int]]()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' or (i, j) in visited:
                    continue
                surrounded: bool = True
                q: list[tuple[int,int]] = [(i,j)]
                tmp: list[tuple[int,int]] = [(i,j)]

                while q:
                    p = q.pop()
                    if p in visited:
                        continue
                    
                    visited.add(p)
                    tmp.append(p)
                    for d in self.dirs:
                        y = p[0] + d[0]
                        x = p[1] + d[1]
                        if x < 0 or x >= n or y < 0 or y >= m:
                            surrounded = False
                        elif board[y][x] == 'O':
                            q.append((y, x))

                if surrounded:
                    for (y,x) in tmp:
                        board[y][x] = 'X'
        return board

if __name__ == '__main__':
    s = Solution()

    b = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    s.solve(b)
    print(b)

    b = [['O']]
    s.solve(b)
    print(b)