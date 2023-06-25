from functools import lru_cache


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(i: int, fuel: int) -> int:
            if fuel < 0:
                return 0

            count = 0 if i != finish else 1
            for j in range(n):
                if i == j:
                    continue
                dist = abs(locations[i] - locations[j])
                count += dp(j, fuel - dist)
            return count % MOD
        return dp(start, fuel)
        