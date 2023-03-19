class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random
        
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def __init__(self):
        # Hashmap to map old tree's nodes with new tree's nodes.
        self.seen: dict[Node | None, NodeCopy | None] = {None: None}
            
    def dfs(self, root: Node | None) -> NodeCopy | None:
        if not root:
            return None

        if self.seen.get(root) is not None:
            return self.seen.get(root)

        node = NodeCopy(root.val)
        # Mark old root as seen and store its respective new node.
        self.seen[root] = node
        
        # Traverse on all 3 edges of root and attach respective new node
        # to the newRoot.
        node.left = self.dfs(root.left)
        node.right = self.dfs(root.right)
        node.random = self.dfs(root.random)
        return node
    
    def copyRandomBinaryTree(self, root: Node | None) -> NodeCopy | None:
        return self.dfs(root)