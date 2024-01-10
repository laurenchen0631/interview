# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.max_time = 0
    
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        self.traverse(root, start)
        return self.max_time

    def traverse(self, root: TreeNode | None, start: int) -> int:
        if root is None:
            return 0

        left_time = self.traverse(root.left, start)
        right_time = self.traverse(root.right, start)
        if root.val == start:
            self.max_time = max(left_time, right_time)
            return -1
        elif left_time >= 0 and right_time >= 0:
            return max(left_time, right_time) + 1
        else:
            self.max_time = max(self.max_time, abs(left_time) + abs(right_time))
            return min(left_time, right_time) - 1

        
        