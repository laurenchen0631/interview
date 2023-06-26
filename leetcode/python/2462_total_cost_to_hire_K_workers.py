import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        l, r = 0, len(costs) - 1
        heap = []
        for _ in range(candidates):
            heap.append((costs[l], l))
            l += 1
            if l > r:
                break
            heap.append((costs[r], r))
            r -= 1
            if l > r:
                break
        
        heapq.heapify(heap)
        res = 0
        for _ in range(k):
            if not heap:
                break
            cost, i = heapq.heappop(heap)
            res += cost
            if l > r:
                continue
            elif i < l:
                heapq.heappush(heap, (costs[l], l))
                l += 1
            else:
                heapq.heappush(heap, (costs[r], r))
                r -= 1
        return res
        