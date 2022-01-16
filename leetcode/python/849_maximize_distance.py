import enum


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        left: int = -1
        maxDist: int = 1
        for i, n in enumerate(seats):
            if n == 0:
                continue
            if left == -1:
                maxDist = max(i, maxDist)
            elif left+1 < i:
                maxDist = max((i-left)//2, maxDist)
            left = i
        return max(maxDist, len(seats)-1-left)

s = Solution()
print(s.maxDistToClosest([1,0,0,0,1,0,1]))
print(s.maxDistToClosest([0,1]))
print(s.maxDistToClosest([1,0,0,0]))