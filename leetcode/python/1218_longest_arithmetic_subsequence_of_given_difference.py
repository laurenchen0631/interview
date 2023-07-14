
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        res = 0
        count = defaultdict(int)
        for n in arr:
            count[n] = count[n - difference] + 1
            res = max(res, count[n])
        return res