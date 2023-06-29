class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode) -> tuple[int, bool]:
            if not node.left and not node.right:
                return 1, True
            
            left_count, left_uni = dfs(node.left) if node.left else (0, True)
            right_count, right_uni = dfs(node.right) if node.right else (0, True)
            is_uni = left_uni and right_uni and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val)
            
            return left_count + right_count + (1 if is_uni else 0), is_uni

        return dfs(root)[0]
            