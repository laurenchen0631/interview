# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' | None = None, right: 'Node' | None = None, next: 'Node' | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return
        
        q = [root]
        while len(q) > 0:
            tmp: list[Node] = []
            for i in range(len(q) - 1):
                q[i].next = q[i+1] if i+1 < len(q) else None
                if q[i].left:
                    tmp.append(q[i].left)
                    tmp.append(q[i].right)
            q = tmp
        return root

    def connectOpt(self, root: Node) -> Node | None:
        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 
        