# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        mid = self.getMid(head)
        mid = self.reverse(mid)
        self.merge(head, mid)

    def getMid(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev: ListNode | None = None
        cur: ListNode | None = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def merge(self, l: ListNode, r: ListNode) -> None:
        while r.next:
            l.next, l = r, l.next
            r.next, r = l, r.next