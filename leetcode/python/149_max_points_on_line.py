import math


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return len(points)
        return max([self.getLinePoints(points, i) for i in range(len(points) - 1)])
    
    def getLinePoints(self, points: list[list[int]], i: int) -> int:
        lines: dict[tuple[int,int], int] = {}
        count: int = 1
        duplicates: int = 0
        for j in range(i+1, len(points)):
            [x1,y1], [x2,y2] = points[i], points[j]
            if x1 == x2 and y1 == y2:
                duplicates += 1
            else:
                slope = self.getSlope(x1,y1,x2,y2)
                lines[slope]  = lines.get(slope, 1) + 1
                count = max(count, lines[slope])

        return count + duplicates

    def getSlope(self, x1: int, y1: int, x2: int, y2: int) -> tuple[int,int]:
        dx, dy = x2-x1, y2-y1
        if dx == 0:
            return (0, 1)
        elif dy == 0:
            return (1, 0)
        
        if dx < 0:
            dx, dy = -dx, -dy
        gcd = math.gcd(dx, dy)
        return (dx/gcd, dy/gcd)

s = Solution()
print(s.maxPoints([[1,1],[2,2],[3,3]]))
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))