import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[r][0], r, 0) for r in range(n)]
        heapq.heapify(heap)
        for _ in range(k-1):
            _, r, i = heapq.heappop(heap)
            if i+1 < n:
                heapq.heappush(heap, (matrix[r][i+1], r, i+1))
        return heap[0][0]


s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))