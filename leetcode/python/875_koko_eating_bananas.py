from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            print(f'l={l}, r={r}, m={m}')
            hours = sum([ceil(p / m) for p in piles])
            if hours <= h:
                r = m
            else:
                l = m + 1
                
        return l

s = Solution()
# print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([312884470], 968709470))