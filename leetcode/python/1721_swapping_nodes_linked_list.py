# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def swapNodes(self, head: ListNode | None, k: int) -> ListNode | None:
        first = head
        for _ in range(k-1):
            first = first.next
        last = head
        t = first
        while t.next:
            t = t.next
            last = last.next
        first.val, last.val = last.val, first.val
        return head