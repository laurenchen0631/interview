from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        l = 1
        r = 10**7
        res = -1
        while l <= r:
            m = (l + r) // 2
            if self.canFinish(dist, hour, m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
                
    def canFinish(self, dist: list[int], hour: float, speed: int):
        total = 0
        for i in range(len(dist) - 1):
            total += ceil(dist[i] / speed)
        total += dist[-1] / speed
        return total <= hour