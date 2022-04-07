import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x - y > 0:
                heapq.heappush(heap, y-x)
        return -heap[0] if heap else 0

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([1]))