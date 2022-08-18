import heapq
from math import ceil
from typing import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counter = Counter(arr)
        heap = [-v for v in counter.values()]
        heapq.heapify(heap)
        res, reduced, target = 0, 0, ceil(len(arr) / 2)
        while reduced < target:
            reduced += -heapq.heappop(heap)
            res += 1
        return res

s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
        