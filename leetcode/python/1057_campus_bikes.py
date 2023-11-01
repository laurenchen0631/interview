import heapq


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        heap = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                heap.append((dist, i, j))
        heapq.heapify(heap)
        
        res = [-1] * len(workers)
        used_bikes = set()
        while len(used_bikes) < len(workers):
            dist, worker, bike = heapq.heappop(heap)
            if res[worker] == - 1 and bike not in used_bikes:
                res[worker] = bike
                used_bikes.add(bike)
        return res