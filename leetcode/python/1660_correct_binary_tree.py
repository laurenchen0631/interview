# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = [(root, None)]
        while q:
            visited = set()
            tmp = []
            for node, parent in q:
                if node.right in visited:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                visited.add(node)
                
                if node.right:
                    tmp.append((node.right, node))
                if node.left:
                    tmp.append((node.left, node))
            q = tmp