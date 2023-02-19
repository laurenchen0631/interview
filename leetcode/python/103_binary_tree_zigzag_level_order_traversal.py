# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        left_to_right = True
        while stack:
            values = list[int]()
            tmp: list[TreeNode] = []
            while stack:
                node = stack.pop()
                values.append(node.val)
                first, second = (node.left, node.right) if left_to_right else (node.right, node.left)
                if first:
                    tmp.append(first)
                if second:
                    tmp.append(second)
            res.append(values)
            stack = tmp
            left_to_right = not left_to_right
        return res
            
                      
            