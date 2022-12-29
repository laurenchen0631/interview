import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        heap = [-n for n in piles]
        heapq.heapify(heap)
        for _ in range(k):
            if heap[0] == -1: 
                break
            n = -heapq.heappop(heap)
            heapq.heappush(heap, -(n - n // 2))
        return -sum(heap)