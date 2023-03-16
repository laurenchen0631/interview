class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inIndex = {val: i for i, val in enumerate(inorder)}
        def traverse(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = inIndex[val]
            root.right = traverse(index + 1, right)
            root.left = traverse(left, index - 1)
            return root
        return traverse(0, len(inorder) - 1)