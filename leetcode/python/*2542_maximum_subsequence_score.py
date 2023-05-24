import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        heap = [x[0] for x in pairs[:k]]
        total = sum(heap)
        heapq.heapify(heap)
        res = total * pairs[k-1][1]
        for i in range(k, len(pairs)):
            total = total - heapq.heappop(heap) + pairs[i][0]
            heapq.heappush(heap, pairs[i][0])
            res = max(res, total * pairs[i][1])
        return res