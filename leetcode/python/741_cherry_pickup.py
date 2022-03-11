from functools import lru_cache
from math import inf


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        @lru_cache(None)
        def dp(r1, c1, r2, c2):
            if r1 >= n or r2 >= n or c1 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -(n**2)
            
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            pick = grid[r1][c1] if r1 == r2 or c1 == c2 else grid[r1][c1] + grid[r2][c2]
            
            return pick + max(
                dp(r1 + 1, c1, r2 + 1, c2), 
                dp(r1 + 1, c1, r2, c2 + 1), 
                dp(r1, c1 + 1, r2 + 1, c2), 
                dp(r1, c1 + 1, r2, c2 + 1)
            )
        
        return max(dp(0, 0, 0, 0), 0)


s = Solution()
print(s.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))
print(s.cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]))
print(s.cherryPickup([
    [1,1,1,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,1,1,1]
]))
print(s.cherryPickup([
    [1,-1, 1],
    [-1, 1, 1],
    [1, 1, 1],
]))
print(s.cherryPickup([
    [1,-1,1,-1,1,1,1,1,1,-1],
    [-1,1,1,-1,-1,1,1,1,1,1],
    [1,1,1,-1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [-1,1,1,1,1,1,1,1,1,1],
    [1,-1,1,1,1,1,-1,1,1,1],
    [1,1,1,-1,1,1,-1,1,1,1],
    [1,-1,1,-1,-1,1,1,1,1,1],
    [1,1,-1,-1,1,1,1,-1,1,-1],
    [1,1,-1,1,1,1,1,1,1,1]
]))