class Solution:
    # Greedy
    def minDistance(self, height: int, width: int, tree: list[int], squirrel: list[int], nuts: list[list[int]]) -> int:
        res = most_saved = 0
        for nut in nuts:
            res += 2 * self.distance(nut, tree)
            most_saved = max(most_saved, self.distance(nut, tree) - self.distance(nut, squirrel))
        return res - most_saved
        
    def distance(self, p1: list[int], p2: list[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])