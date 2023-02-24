import heapq
import sys


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        heap = []
        res = curMin = sys.maxsize
        for n in nums:
            n = n * 2 if n & 1 == 1 else n
            heap.append(-n)
            curMin = min(curMin, n)
        heapq.heapify(heap)
        while heap[0] & 1 == 0:
            n = -heapq.heappop(heap)
            res = min(res, n - curMin)
            curMin = min(curMin, n // 2)
            heapq.heappush(heap, -n // 2)
        return min(res, -heap[0] - curMin)
    
s = Solution()
print(s.minimumDeviation([1,2,3,4]))