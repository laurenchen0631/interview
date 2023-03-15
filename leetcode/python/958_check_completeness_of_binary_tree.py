class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        q: list[TreeNode] = [root]
        hasEmpty = False
        while q:
            tmp: list[TreeNode] = []
            for node in q:
                if node.left:
                    if hasEmpty:
                        return False
                    tmp.append(node.left)
                else:
                    hasEmpty = True
                
                if node.right:
                    if hasEmpty:
                        return False
                    tmp.append(node.right)
                else:
                    hasEmpty = True
            q = tmp
        return True