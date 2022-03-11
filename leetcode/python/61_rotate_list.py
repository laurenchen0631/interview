# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        val: list[str] = []
        node = self
        while node != None:
            val.append(str(node.val))
            node = node.next
        return ' -> '.join(val)


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None
        l, r = head, self.advance(head, k)
        if l == r:
            return head
        while r.next:
            l, r = l.next, r.next
        t = l.next
        r.next = head
        l.next = None
        return t

    def advance(self, head: ListNode, k: int) -> ListNode:
        node = head
        n = 0
        while n < k:
            node = node.next
            n += 1
            if not node:
                k %= n
                n = 0
                node = head
        return node

s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next  = ListNode(4)
h.next.next.next.next  = ListNode(5)

print(s.rotateRight(h, 5))