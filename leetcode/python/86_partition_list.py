class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        p1, p2 = ListNode(), ListNode()
        l, r = p1, p2
        while head:
            if head.val < x:
                l.next, l = head, head
            else:
                r.next, r = head, head
            head = head.next
        r.next, l.next = None, p2.next
        return p1.next
                