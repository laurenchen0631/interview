# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = tail = ListNode()
        cur = head
        while cur:
            n = cur.val
            if not cur.next or cur.next.val != n:
                tail.next, tail = cur, cur

            cur = cur.next
            while cur.val == n:
                cur = cur.next
        tail.next = None
        return dummy.next