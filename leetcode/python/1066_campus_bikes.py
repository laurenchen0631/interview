from math import inf

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        cache: list[int] = [-1] * (1 << len(bikes))
        def dp(w: int, mask: int) -> int:
            if w >= len(workers):
                return 0
            if cache[mask] != -1:
                return cache[mask]
            res: int = inf
            for b in range(len(bikes)):
                if mask & (1 << b) > 0:
                    continue
                res = min(res, dp(w+1, mask | 1 << b) + self.getDistance(workers[w], bikes[b]))
            cache[mask] = res
            return res
        return dp(0, 0)

    
    def getDistance(self, p1: list[int], p2: list[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

s = Solution()
print(s.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))
print(s.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))
print(s.assignBikes(workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]))
