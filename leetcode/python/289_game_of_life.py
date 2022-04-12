class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                neighbor: int = 0
                for (di, dj) in dirs:
                    y = i + di
                    x = j + dj
                    if -1 < y < m and -1 < x < n and abs(board[y][x]) == 1:
                        neighbor += 1
                if board[i][j] == 1 and (neighbor < 2 or neighbor > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and neighbor == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s = Solution()
s.gameOfLife(board)
print(board)