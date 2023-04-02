from bisect import bisect_left
import math


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res: list[int] = []
        for s in spells:
            t = math.ceil(success/s)
            i = bisect_left(potions, t)
            res.append(len(potions) - i)
        return res