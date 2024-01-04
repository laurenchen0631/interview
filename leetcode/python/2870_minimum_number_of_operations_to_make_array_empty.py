from collections import Counter
from math import ceil


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = Counter(nums)
        
        res = 0
        for _, v in count.items():
            if v == 1:
                return -1
            res += ceil(v / 3)
        return res
        
        