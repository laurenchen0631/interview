from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dp(row: int, col1: int, col2: int) -> int:
            if not 0 <= col1 < n or not 0 <= col2 < n:
                return -1
            total = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            if row < m - 1:
                total += max(
                    dp(row+1, c1, c2)
                    for c1 in [col1-1, col1, col1+1]
                    for c2 in [col2-1, col2, col2+1]
                )
            return total
        
        return dp(0, 0, n - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
    print(s.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
