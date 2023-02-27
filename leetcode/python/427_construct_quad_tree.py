class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        return self._construct(grid, 0, 0, len(grid))
    
    def _construct(self, grid: list[list[int]], x: int, y: int, n: int) -> Node:
        if n == 1:
            return Node(grid[x][y] == 1, True, None, None, None, None)

        topLeft = self._construct(grid, x, y, n // 2)
        topRight = self._construct(grid, x, y + n // 2, n // 2)
        bottomLeft = self._construct(grid, x + n // 2, y, n // 2)
        bottomRight = self._construct(grid, x + n // 2, y + n // 2, n // 2)
        arr = [topLeft, topRight, bottomLeft, bottomRight]
        if all([x.isLeaf for x in arr]) and len(set([x.val for x in arr])) == 1:
            return Node(topLeft.val, True, None, None, None, None)
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
