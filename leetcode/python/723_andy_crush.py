class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        crushed = self.find(board)
        while crushed:
            self.crush(board, crushed)
            self.drop(board)
            crushed = self.find(board)
        return board
    
    def find(self, board: list[list[int]]) -> set[tuple[int, int]]:
        crushed = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    continue
                if i > 1 and board[i][j] == board[i-1][j] == board[i-2][j]:
                    crushed |= {(i, j), (i-1, j), (i-2, j)}
                if j > 1 and board[i][j] == board[i][j-1] == board[i][j-2]:
                    crushed |= {(i, j), (i, j-1), (i, j-2)}
        return crushed
    
    def crush(self, board: list[list[int]], crushed: set[tuple[int, int]]) -> None:
        for i, j in crushed:
            board[i][j] = 0
    
    def drop(self, board: list[list[int]]) -> None:
        for j in range(len(board[0])):
            zero = -1
            for i in range(len(board)-1, -1, -1):
                if board[i][j] == 0:
                    zero = max(zero, i)
                elif zero > -1:
                    board[i][j], board[zero][j] = board[zero][j], board[i][j]
                    zero -= 1
                
                