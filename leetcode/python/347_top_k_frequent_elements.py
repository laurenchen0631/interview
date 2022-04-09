import heapq
from typing import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = [(f, n) for n, f in counter.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [e[1] for e in heap]

s = Solution()
print(s.topKFrequent([1,2,3,1,2,1], 2))
print(s.topKFrequent([-1,-1], 1))
        