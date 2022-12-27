import heapq


class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        heap = [capacity[i] - rocks[i] for i in range(len(capacity))]
        heapq.heapify(heap)
        res = 0
        while heap and additionalRocks >= 0:
            v = heapq.heappop(heap)
            if additionalRocks >= v:
               res += 1
            additionalRocks -= v
        return res 