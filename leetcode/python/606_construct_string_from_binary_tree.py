class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        def postorder(root):
            if not root:
                return ''
            if not root.left and not root.right:
                return str(root.val)
            if not root.right:
                return str(root.val) + '(' + postorder(root.left) + ')'
            return str(root.val) + '(' + postorder(root.left) + ')(' + postorder(root.right) + ')'

        return postorder(root)
        