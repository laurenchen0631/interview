class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        def findNode(node: TreeNode):
            nonlocal ancestor
            if node == None:
                return False
            left = findNode(node.left)
            right = findNode(node.right)
            mid = (node == p) or (node == q)
            if mid + left + right >= 2: # find p and q
                ancestor = node
            return mid or left or right
        findNode(root)
        return ancestor
    
    def lowestCommonAncestor2(self, root, p, q):
        if root is None:
            return None
        
        l = self.lowestCommonAncestor2(root.left, p, q)
        r = self.lowestCommonAncestor2(root.right, p, q)
        
        if (l and r) or (root in [p, q]):
            return root
        else:
            return l or r