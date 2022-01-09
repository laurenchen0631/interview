class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if word == '':
            return True
        elif len(board) == 0:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and self.helper(board, (i, j), word, 0, set()):
                    return True
        return False

    def helper(self, board: list[list[str]], p: tuple[int,int], word: str, index: int, visited: set[tuple[int,int]]) -> bool:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        if word[index] != board[p[0]][p[1]]:
            return False
        elif index == len(word) - 1:
            return True
        
        visited.add(p)
        res: bool = False
        for d in dirs:
            x = p[1] + d[1]
            y = p[0] + d[0]
            if 0 <= x < len(board[0]) and 0 <= y < len(board) and (t := (y,x)) not in visited:
                res = res or self.helper(board, t, word, index+1, visited)
            
            if res:
                return True
        visited.remove(p)
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))