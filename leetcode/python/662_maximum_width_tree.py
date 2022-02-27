# Definition for a binary tree node.
import collections
from this import d
from xml.dom.minidom import Element


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        res: int = 0
        leftmost: int = 0
        q = collections.deque([(0, root)])
        while q:
            element = q.popleft()
            if not element:
                if q:
                    leftmost = q[0][0]
                    print(leftmost)
                    q.append(None)
                continue
            (index, node) = element
            res = max(res, index-leftmost+1)
            if node.left:
                q.append((2*index, node.left))
            if node.right:
                q.append((2*index+1, node.right))
        return res