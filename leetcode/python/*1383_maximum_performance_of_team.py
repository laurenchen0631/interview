import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        team = list(range(n))
        team.sort(key=lambda x: efficiency[x], reverse=True)
        speedHeap: list[int] = []
        curSum = res = 0
        for i in team:
            curMin = efficiency[i]
            curSum += speed[i]
            heapq.heappush(speedHeap, speed[i])
            if len(speedHeap) > k:
                curSum -= heapq.heappop(speedHeap)
            res = max(res, curSum *curMin)
        return res % (10**9 + 7)