class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        res: list[int] = []
        def preorder(root: TreeNode | None) -> None:
            if not root:
                return
            res.append(str(root.val))
            if root.left:
                res.append('(')
                preorder(root.left)
                res.append(')')
            if root.right:
                if not root.left:
                    res.append('()')
                res.append('(')
                preorder(root.right)
                res.append(')')
        preorder(root)
        return ''.join(res)