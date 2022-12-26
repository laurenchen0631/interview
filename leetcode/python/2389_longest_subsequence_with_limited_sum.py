import heapq


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        heap = nums.copy()
        heapq.heapify(heap)
        ans = dict[int,int]()
        cur = curTotal = 0
        for q in sorted(queries):
            while heap and curTotal + heap[0] <= q:
                curTotal += heapq.heappop(heap)
                cur += 1
            ans[q] = cur
        return [ans[q] for q in queries]