# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = list1
        for _ in range(a - 1):
            p = p.next
        q = p
        for _ in range(b - a + 2):
            q = q.next
        p.next = list2
        while p.next:
            p = p.next
        p.next = q
        return list1
        