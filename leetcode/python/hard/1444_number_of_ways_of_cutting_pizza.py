from functools import lru_cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        MOD = (10 ** 9) + 7
        appleSum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                appleSum[i][j] = appleSum[i+1][j] + appleSum[i][j+1] - appleSum[i+1][j+1] + (1 if pizza[i][j] == 'A' else 0)
        
        @lru_cache(None)
        def dp(i: int, j: int, k: int):
            if appleSum[i][j] == 0:
                return 0
            if k == 1:
                return 1
            res = 0
            for ni in range(i+1, m):
                if appleSum[i][j] - appleSum[ni][j] > 0:
                    res += dp(ni, j, k-1) % MOD
            for nj in range(j+1, n):
                if appleSum[i][j] - appleSum[i][nj] > 0:
                    res += dp(i, nj, k-1) % MOD
            return res
        return dp(0, 0, k) % MOD
        
        