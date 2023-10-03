from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = Counter(nums)
        res = 0
        for v in counter.values():
            if v < 2:
                continue
            
            res += v * (v-1) // 2
        return res

        