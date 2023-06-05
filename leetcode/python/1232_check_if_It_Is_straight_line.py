class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        [x1, y1] = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]]
        for x, y in coordinates[2:]:
            [x2, y2] = [x - coordinates[0][0], y - coordinates[0][1]]
            if y1 * x2 != y2 * x1:
                return False
        return True