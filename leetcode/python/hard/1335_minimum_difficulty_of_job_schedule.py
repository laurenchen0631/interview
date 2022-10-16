from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        base = [jobDifficulty[-1]] * len(jobDifficulty)
        for i in range(n-2, -1, -1):
            base[i] = max(base[i+1], jobDifficulty[i])
        @lru_cache(None)
        def dp(i: int, d: int) -> int:
            if d == 1:
                return base[i]
            res = float('inf')
            curMax = jobDifficulty[i]
            for j in range(i, n-d+1):
                curMax = max(curMax, jobDifficulty[j])
                res = min(res, curMax + dp(j+1, d-1))
            return res
        return dp(0, d)

s = Solution()
print(s.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
print(s.minDifficulty(jobDifficulty = [9,9,9], d = 4))
print(s.minDifficulty(jobDifficulty = [1,1,1], d = 3))