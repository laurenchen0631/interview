# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        head = dummy
        for _ in range(count // k):
            prev, cur = None, head.next
            for _ in range(k):
                cur.next, cur, prev = prev, cur.next, cur
            head.next.next, head.next, head = cur, prev, head.next
        
        return dummy.next