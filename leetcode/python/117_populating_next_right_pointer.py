class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    
    def processChild(self, childNode: Node | None, prev: Node | None, leftmost: Node | None):
        if childNode:
            if prev:
                prev.next = childNode
            else:    
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
    
    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # so, we keep going until we do find the last level.
        while leftmost:
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
                
        return root 