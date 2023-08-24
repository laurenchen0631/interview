# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        node_set = set(nodes)
        res: TreeNode | None = None
        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            v = dfs(node.left) + dfs(node.right)
            v += node in node_set
            
            nonlocal res
            if v == len(node_set) and not res:
                res = node
        
        dfs(root)
        return res