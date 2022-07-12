from functools import lru_cache


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        n = len(matchsticks)
        k, rem = divmod(sum(matchsticks), 4)
        if rem != 0 or max(matchsticks) > k:
            return False

        @lru_cache(None)
        def dfs(unused) -> int:
            if unused == 0:
                return 0
            for i in range(n):
                if unused & (1 << i):
                    comb = dfs(unused ^ (1 << i))
                    if comb >= 0 and comb + matchsticks[i] <= k:
                        return (comb + matchsticks[i]) % k
            return -1
        return dfs((1 << n) - 1) == 0

s = Solution()
print(s.makesquare([1,1,2,2,2]))