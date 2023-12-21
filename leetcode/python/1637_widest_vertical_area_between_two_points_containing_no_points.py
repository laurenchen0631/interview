class Solution:
    # [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    # [1,0], [1,4], [3,1], [5,3], [8,8], [9,0]
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i-1][0])
        return res
        