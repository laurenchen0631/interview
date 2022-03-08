# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if fast and slow == fast:
                return True
        return False