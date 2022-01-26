# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode|None, root2: TreeNode|None) -> list[int]:
        a: list[int] = []
        self.sortBST(root1, a)
        b: list[int] = []
        self.sortBST(root2, b)
        return self.mergeSorted(a, b)
    
    def sortBST(self, root: TreeNode|None, res: list[int]) -> None:
        if not root:
            return
        self.sortBST(root.left, res)
        res.append(root.val)
        self.sortBST(root.right, res)

    def mergeSorted(self, a: list[int], b: list[int]) -> list[int]:
        c1 = c2 = 0
        res: list[int] = []
        while c1 < len(a) or c2 < len(b):
            if c1 == len(a):
                res.append(b[c2])
                c2 += 1
            elif c2 == len(b):
                res.append(a[c1])
                c1 += 1
            elif a[c1] <= b[c2]:
                res.append(a[c1])
                c1 += 1
            else:
                res.append(b[c2])
                c2 += 1
        return res