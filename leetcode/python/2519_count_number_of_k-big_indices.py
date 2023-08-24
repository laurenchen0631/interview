import heapq


class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:
        prefix = [False] * len(nums)
        pq = [] # to keep the most smallest k element (always pop max)
        for i, n in enumerate(nums):
            if len(pq) == k and -pq[0] < n:
                prefix[i] = True
            heapq.heappush(pq, -n)
            if len(pq) > k:
                heapq.heappop(pq)
        res = 0
        pq = []
        for i, n in list(enumerate(nums))[::-1]:
            if len(pq) == k and -pq[0] < n and prefix[i]:
                res += 1
            heapq.heappush(pq, -n)
            if len(pq) > k:
                heapq.heappop(pq)
        return res