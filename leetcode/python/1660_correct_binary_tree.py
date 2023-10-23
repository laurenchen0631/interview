# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            tmp = []
            visited = set()
            for node in q:
                if node.right:
                    tmp.append(node.right)
                    visited.add(node.right)
                    if node.right.right and node.right.right in visited:
                        node.right = None
                        return root
                        
                if node.left:
                    tmp.append(node.left)
                    visited.add(node.left)
                    if node.left.right and node.left.right in visited:
                        node.left = None
                        return root
            q = tmp