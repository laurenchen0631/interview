class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(row: int, col: int, suffix: str) -> bool:
            # bottom case: we find match for each letter in the word
            if len(suffix) == 0:
                return True

            # Check the current status, before jumping into backtracking
            if row < 0 or row == m or col < 0 or col == n or board[row][col] != suffix[0]:
                return False

            ret = False
            # mark the choice before exploring further.
            board[row][col] = '#'
            # explore the 4 neighbor directions
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(row + rowOffset, col + colOffset, suffix[1:])
                # break instead of return directly to do some cleanup afterwards
                if ret: break

            # revert the change, a clean slate and no side-effect
            board[row][col] = suffix[0]

            # Tried all directions, and did not find any match
            return ret

        for row in range(m):
            for col in range(n ):
                if backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))