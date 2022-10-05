class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        if depth == 1:
            return TreeNode(val, root)
        if not root:
            return None

        level = [root]
        while level:
            depth -= 1
            if depth == 1:
                for node in level:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
            else:
                level = [child for node in level for child in (node.left, node.right) if child]
        return root