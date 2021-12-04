class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        h1: Node = head
        h2: Node | None = h1.next if h1 else None
        node = Node(insertVal)

        if not h2:
            self._insert(node, node, node)
            return node

        if h1 == h2:
            self._insert(h1, h2, node)
            return head

        while True:
            if h1.val > h2.val and (insertVal > h1.val or insertVal < h2.val):
                self._insert(h1, h2, node)
                return head
            if h1.val <= insertVal <= h2.val:
                self._insert(h1, h2, node)
                return head
            h1 = h2
            h2 = h2.next
            
            if h1 == head:
                break
        
        self._insert(h1, h2, node)
            
        return head

            
        
        
    def _insert(self, h1: Node, h2: Node, node: Node) -> None:
        h1.next = node
        h1.next.next = h2
        