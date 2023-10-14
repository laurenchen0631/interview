from functools import lru_cache
import sys


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def dp(i: int, remain: int) -> int:
            if remain <= 0:
                return 0
            if i == n:
                return sys.maxsize

            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            skip = dp(i + 1, remain)
            return min(paint, skip)

        return dp(0, n)
    
# cost = [1,2,3,2], time = [1,2,3,2]
# cost = [2,3,4,2], time = [1,1,1,1]