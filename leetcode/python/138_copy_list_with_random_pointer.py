class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None
        nodes: dict[Node, int] = {}
        copyNodes: dict[int, Node] = {}
        cur = head
        i = 0
        while cur:
            print(i)
            nodes[cur] = i
            copyNodes[i] = Node(cur.val)
            if i > 0:
                copyNodes[i-1].next = copyNodes[i]
            cur, i = cur.next, i+1
        print('b')
        i = 0
        cur = head
        while cur:
            if cur.random:
                copyNodes[i].random = copyNodes[nodes[cur.random]]
            cur, i = cur.next, i+1
        return copyNodes[0]

a = Node(3)
a.next = Node(3)
a.next.random = a
a.next.next = Node(3)
s = Solution()
print(s.copyRandomList(a))