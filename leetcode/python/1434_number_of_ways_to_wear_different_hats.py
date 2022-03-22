from collections import defaultdict
from functools import lru_cache


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        waiting = defaultdict(list[int])
        n = len(hats) # n people
        for i in range(n):
            for h in hats[i]:
                waiting[h].append(i)
        @lru_cache(None)
        def dp(hat: int, mask: int) -> int:
            if mask == (1 << n) - 1: # every one has a hat
                return 1
            if hat >= 40:
                return 0
            res = dp(hat+1, mask)
            for p in waiting[hat+1]:
                if mask & (1 << p) == 0:
                    res += dp(hat+1, mask | (1 << p))
            return res
        return dp(0, 0) % (10**9 + 7)

s = Solution()
print(s.numberWays([[3,4],[4,5],[5]]))
print(s.numberWays([[3,2,1],[3,2]]))
print(s.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))