from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            prev.next = ListNode(gcd(prev.val, cur.val))
            prev.next.next = cur
            prev, cur = cur, cur.next
        return head
        