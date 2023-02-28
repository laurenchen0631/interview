
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:
        res: list[TreeNode] = []
        cnt = defaultdict(int)
        def traverse(node: TreeNode | None) -> tuple:
            if not node:
                return ()
            id = (traverse(node.left), node.val, traverse(node.right))
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id
        traverse(root)
        return res
            
            
            