class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            d = 1
            cur = 0
            for w in weights:
                if cur + w > m:
                    d += 1
                    cur = 0
                cur += w
            if d > days:
                l = m + 1
            else:
                r = m
        return l