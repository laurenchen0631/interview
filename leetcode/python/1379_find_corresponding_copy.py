class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s1 = [original]
        s2 = [cloned]
        while s1:
            p1 = s1.pop()
            p2 = s2.pop()
            if target == p1:
                return p2
            
            if p1.left:
                s1.append(p1.left)
                s2.append(p2.left)
            if p1.right:
                s1.append(p1.right)
                s2.append(p2.right)