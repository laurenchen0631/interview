from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        visited: dict[int, int] = {1: 0}
        q = deque([1])
        n = len(board)
        end = n * n
        while q:
            i = q.popleft()
            if i == end:
                return visited[i]
            for j in range(i + 1, min(i + 6, end) + 1):
                r, c = self.getLoc(j, n)
                if board[r][c] != -1:
                    j = board[r][c]
                if j not in visited:
                    visited[j] = visited[i] + 1
                    q.append(j)
        return -1
    
    def getLoc(self, i: int, n: int) -> tuple[int, int]:
        r, d = divmod(i - 1, n)
        return (n - 1 - r, d) if r % 2 == 0 else (n - 1 - r, n - 1 - d)
        
s = Solution()
print(s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(s.snakesAndLadders([[-1,-1],[-1,3]]))