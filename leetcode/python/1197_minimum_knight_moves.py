from collections import deque
from functools import lru_cache


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.dfs(abs(x), abs(y))
    
    @lru_cache(None)
    def dfs(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        elif x + y == 2:
            return 2
        else:
            return min(self.dfs(abs(x-2),abs(y-1)), self.dfs(abs(x-1), abs(y-2))) + 1


s = Solution()
print(s.minKnightMoves(x = 2, y = 112))
print(s.minKnightMoves(x = 5, y = 3))
print(s.minKnightMoves(x = 2, y = 1))
print(s.minKnightMoves(x = 5, y = 5))