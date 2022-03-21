from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        for i in range(len(piles)-2, -1, -1):
            piles[i] += piles[i+1]
        
        @lru_cache(None)
        def dp(first: int, m: int) -> int:
            if first + 2*m >= len(piles):
                return piles[first]
            return piles[first] - min(dp(first+x, max(m,x)) for x in range(1, 2*m+1))

        return dp(0, 1)

s = Solution()
print(s.stoneGameII([2,7,9,4,4]))
print(s.stoneGameII([1,2,3,4,5,100]))