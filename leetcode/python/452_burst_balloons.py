class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if (n := len(points)) <= 1:
            return n
        
        points.sort(key=lambda p: p[1])
        arrows: int = 1
        currentEnd = points[0][1]
        for [start, end] in points[1:]:
            if currentEnd < start:
                arrows += 1
                currentEnd = end
        return arrows

s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))