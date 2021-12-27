# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev: ListNode | None = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev