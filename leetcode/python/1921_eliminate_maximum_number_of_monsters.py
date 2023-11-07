import heapq
import math

class Solution:
    # [2, 1, 4], [1, 0, 4]
    # taken time (min) = dist / speed
    # sorted by increasing taken time
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        heap = [math.ceil(dist[i] / speed[i]) for i in range(n)]
        heapq.heapify(heap)
        i = 0
        while heap:
            arrival = heapq.heappop(heap)
            if arrival > i:
                i += 1
            else:
                return i
        return n
                
        