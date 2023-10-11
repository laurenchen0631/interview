from bisect import bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = sorted([f[0] for f in flowers])
        ends = sorted([f[1] for f in flowers])
        res = []
        
        for t in people:
            i = bisect_right(starts, t)
            j = bisect_right(ends, t)
            res.append(i - j)
            print(i, j)
        
        return res
            
            
        