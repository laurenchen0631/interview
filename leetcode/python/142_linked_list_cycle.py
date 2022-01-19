# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow == fast:
                break
        
        if not fast:
            return None

        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next
        return cur